#!/usr/bin/env python3
"""Build the data behind the homepage's quarter-hour grid.

    python scripts/build_quarter_hours.py

The grid shows, for an example community, how much solar energy is shared in
each of the 96 quarter-hours of a day, over the 28 days that end today. It is
an example, labelled as such on the page, and every number comes from here:

  Production  PVGIS hourly output (JRC, api v5.3, SARAH-3) for a 24 kWc
              installation facing due south at 35°, in Namur, 14 % system
              losses, with the weather of WEATHER_YEAR. Hourly values are
              interpolated to the middle of each quarter-hour.
  Consumption twelve households of 3 500 kWh a year each, with a synthetic
              daily profile (morning and evening peaks, more at the weekend
              during the day, more in winter). Documented below; it is not
              a Synergrid profile.
  Shared      min(production, consumption) in each quarter-hour: the roof
              produces for the twelve members; what they do not use goes to
              the grid.

Writes
  _data/quarter_hours.json               one string of 96 base-36 digits per
                                         day of the year (shared energy in
                                         STEP_WH steps), plus the parameters
  assets/images/quarter-hours-poster.svg the grid for the 28 days that end on
                                         21 June, shown when JavaScript is off

The page maps the visitor's date to the same calendar day of WEATHER_YEAR.
"""
import json
import math
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
DATA_OUT = ROOT / "_data" / "quarter_hours.json"
POSTER_OUT = ROOT / "assets" / "images" / "quarter-hours-poster.svg"

LAT, LON, PLACE = 50.4674, 4.8720, "Namur"
PEAK_KWC = 24
TILT, AZIMUTH, LOSS = 35, 0, 14
WEATHER_YEAR = 2023
MEMBERS = 12
ANNUAL_KWH_PER_MEMBER = 3500
STEP_WH = 60            # one base-36 digit = 60 Wh, 35 steps = 2.1 kWh per quarter-hour
LEVELS = (0.25, 0.5, 0.75)  # colour levels, as shares of the year's largest quarter-hour

BRUSSELS = ZoneInfo("Europe/Brussels")
PVGIS = (
    "https://re.jrc.ec.europa.eu/api/v5_3/seriescalc?"
    f"lat={LAT}&lon={LON}&peakpower={PEAK_KWC}&loss={LOSS}&angle={TILT}&aspect={AZIMUTH}"
    f"&pvcalculation=1&startyear={WEATHER_YEAR}&endyear={WEATHER_YEAR}"
    "&raddatabase=PVGIS-SARAH3&usehorizon=1&outputformat=json"
)


def fetch_pvgis():
    with urllib.request.urlopen(PVGIS, timeout=180) as r:
        payload = json.load(r)
    points = []
    for row in payload["outputs"]["hourly"]:
        # "20230101:0010": the satellite instant, in UTC.
        t = datetime.strptime(row["time"], "%Y%m%d:%H%M").replace(tzinfo=timezone.utc)
        points.append((t.timestamp(), float(row["P"])))
    points.sort()
    return points


def interpolator(points):
    times = [p[0] for p in points]
    values = [p[1] for p in points]

    def at(ts):
        if ts <= times[0]:
            return values[0]
        if ts >= times[-1]:
            return values[-1]
        lo, hi = 0, len(times) - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if times[mid] <= ts:
                lo = mid
            else:
                hi = mid
        f = (ts - times[lo]) / (times[hi] - times[lo])
        return values[lo] + f * (values[hi] - values[lo])

    return at


def gauss(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2)


def household_shape(hour, day):
    """Relative household demand at a local hour (float) of a date.

    A base load, a morning peak around 7:30 and a larger evening peak around
    19:00; at the weekend the morning peak moves later and the day is fuller.
    Winter demand is about 20 % above the yearly mean, summer about 20 % below.
    """
    weekend = day.weekday() >= 5
    shape = 0.55 + 0.85 * gauss(hour, 19.0, 1.8) + 0.25 * gauss(hour, 12.5, 1.6)
    shape += 0.30 * gauss(hour, 9.0, 1.4) if weekend else 0.35 * gauss(hour, 7.4, 1.1)
    if weekend:
        shape += 0.20 * gauss(hour, 14.0, 2.5)
    doy = day.timetuple().tm_yday
    season = 1 + 0.2 * math.cos(2 * math.pi * (doy - 15) / 365)
    return shape * season


def main():
    power = interpolator(fetch_pvgis())
    days = [date(WEATHER_YEAR, 1, 1) + timedelta(d) for d in range(365)]

    # Raw consumption shape, then scaled to the yearly total.
    shapes = {}
    total_shape = 0.0
    for day in days:
        row = [household_shape(q / 4 + 0.125, day) for q in range(96)]
        shapes[day] = row
        total_shape += sum(row)
    kwh_per_unit = MEMBERS * ANNUAL_KWH_PER_MEMBER / total_shape

    shared_wh = []
    produced_kwh = consumed_kwh = 0.0
    for day in days:
        row = []
        for q in range(96):
            local = datetime(day.year, day.month, day.day, tzinfo=BRUSSELS) + timedelta(minutes=15 * q + 7.5)
            prod_wh = power(local.timestamp()) * 0.25          # W over 15 minutes
            cons_wh = shapes[day][q] * kwh_per_unit * 1000
            produced_kwh += prod_wh / 1000
            consumed_kwh += cons_wh / 1000
            row.append(min(prod_wh, cons_wh))
        shared_wh.append(row)

    peak = max(max(r) for r in shared_wh)
    if peak / STEP_WH > 35:
        sys.exit(f"largest quarter-hour {peak:.0f} Wh does not fit in 35 steps of {STEP_WH} Wh")
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    encoded = ["".join(digits[round(v / STEP_WH)] for v in row) for row in shared_wh]
    shared_kwh = sum(sum(r) for r in shared_wh) / 1000

    data = {
        "about": "Example community for the homepage grid; built by scripts/build_quarter_hours.py",
        "place": PLACE,
        "members": MEMBERS,
        "peak_kwc": PEAK_KWC,
        "annual_kwh_per_member": ANNUAL_KWH_PER_MEMBER,
        "weather_year": WEATHER_YEAR,
        "source": "PVGIS v5.3, PVGIS-SARAH3",
        "step_wh": STEP_WH,
        "levels_wh": [round(peak * f) for f in LEVELS],
        "totals_kwh": {
            "produced": round(produced_kwh),
            "consumed": round(consumed_kwh),
            "shared": round(shared_kwh),
        },
        "days": encoded,
    }
    DATA_OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"wrote {DATA_OUT.relative_to(ROOT)}: {DATA_OUT.stat().st_size / 1024:.1f} KB")
    print(f"produced {produced_kwh:,.0f} kWh, consumed {consumed_kwh:,.0f} kWh, shared {shared_kwh:,.0f} kWh "
          f"({shared_kwh / produced_kwh:.0%} of production); largest quarter-hour {peak:.0f} Wh")

    write_poster(shared_wh, data["levels_wh"])


def write_poster(shared_wh, levels):
    """Static grid for visitors without JavaScript: the 28 days that end on 21 June."""
    ramp = ["#ECEFF1", "#81C784", "#43A047", "#2E7D32", "#1B5E20"]
    end = date(WEATHER_YEAR, 6, 21).timetuple().tm_yday - 1
    rows = shared_wh[end - 27:end + 1]
    pitch, cell = 10, 8
    width, height = 96 * pitch, 28 * pitch
    # One path per colour level (square cells), a fraction of the size of
    # 2 688 separate <rect> elements.
    paths = {level: [] for level in range(len(ramp))}
    for d, row in enumerate(rows):
        for q, wh in enumerate(row):
            if wh < STEP_WH / 2:
                level = 0
            else:
                level = 1 + sum(1 for lv in levels if wh >= lv)
            paths[level].append(f"M{q * pitch} {d * pitch}h{cell}v{cell}h-{cell}z")
    rects = [f'<path fill="{ramp[level]}" d="{"".join(cmds)}"/>' for level, cmds in paths.items() if cmds]
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img">'
        "<title>Énergie partagée par quart d'heure</title>"
        "<desc>Exemple : 28 jours jusqu'au 21 juin, 96 quarts d'heure par jour, "
        "une toiture de 24 kWc et douze foyers à Namur (PVGIS, météo 2023).</desc>"
        + "".join(rects) + "</svg>\n"
    )
    POSTER_OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {POSTER_OUT.relative_to(ROOT)}: {POSTER_OUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
