#!/usr/bin/env python3
"""Compare what the five Walloon DSOs charge for the same household.

    python scripts/compare_distribution_tariffs.py                # 2026: tables, CSV, 4 SVG
    python scripts/compare_distribution_tariffs.py --lang en      # tables in one language
    python scripts/compare_distribution_tariffs.py --year 2027 --dry-run

Every number of the guide "Tarif de distribution en Wallonie : 5 GRD comparés"
(ref distribution-tariffs-dso-wallonia, four languages) comes from here. Nothing
is fetched: the tariffs are transcribed from the documents below, and a check
fails the run if they no longer give the CWaPE's own summary to the fifth
decimal.

  Tariffs     the periodic low-voltage offtake tariffs of each DSO approved by
              the CWaPE (GRIDS), excluding VAT, one dict per DSO and per year,
              with the URL and approval date of the grid they come from.
  Summary     the CWaPE's VAT-inclusive summary of 3 February 2026 (SUMMARY),
              used only as the check: fixed part, then c€/kWh.
  Transport   the re-invoiced transmission tariff, the same for all Walloon
              DSOs (TRANSPORT), excluding VAT.
  Profiles    the CWaPE's reference low-voltage profiles (annex 9 of decision
              CD-25f26-CWaPE-1119, 26 June 2025), base and shifted versions,
              plus the site's own reference case: 3 500 kWh on a single-rate
              meter (CREG) and a 4 kWc PV installation for the prosumer tariff.

Rules applied (from the grids)
  - distribution = fixed part + kWh x (network use + public service
    obligations + surcharges + regulatory balances), then 6 % VAT;
  - the Impact tariff has no fixed part; its capacity term is 0 €/kW for
    2026-2029, so it is left out;
  - AIEG writes "V" (no amount) on the "other local, provincial or regional
    taxes" line: like the CWaPE summary, it counts as zero;
  - transmission is added separately, the same per kWh at every DSO.

Writes (unless --dry-run)
  assets/data/distribution-tariffs-wallonia-<year>.csv   one row per DSO x
        profile x formula x variant (CC BY 4.0, described in the guide)
  assets/images/diagrams/distribution-tariffs-dso-<lang>.svg   the guide's
        chart, in fr, en, de and nl; the <desc> is printed so that the
        article's alt text can be pasted from it

Yearly update
  1. Transcribe the new grids into GRIDS[<year>] (PDF or xlsx of each DSO on
     https://www.cwape.be/publications/document, type "Tarifs") and the new
     transmission tariff into TRANSPORT[<year>].
  2. Transcribe the new CWaPE summary into SUMMARY[<year>]; run the script
     until the check passes.
  3. Paste the printed tables into the four articles, update their text and
     sources, and set YEAR below.
"""
import argparse
import csv
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
YEAR = 2026
VAT = 1.06
CWAPE = "https://www.cwape.be/sites/default/files/cwape-documents/"

# ---------------------------------------------------------------- tariffs
# Keys, all excluding VAT: fixed (EUR/year), single, peak, offpeak, pic,
# medium, eco (EUR/kWh, network use, section I.D of the grid), osp (II),
# roads, corp_tax, other_tax (III, surcharges), balances (IV), prosumer
# (EUR/kWe, section I.B). Exclusive night is billed at the off-peak rate by
# all five DSOs, so it has no key of its own.
GRIDS = {
    2026: {
        "AIEG": dict(
            fixed=18.39, single=0.0843334, peak=0.0954951, offpeak=0.0446471,
            pic=0.1240197, medium=0.0744118, eco=0.0248039,
            osp=0.0064001, roads=0.0035565, corp_tax=0.0038043, other_tax=0.0,  # "V"
            balances=0.0044496, prosumer=76.4453194,
            url=CWAPE + "AIEG%20-%20Tarifs%20p%C3%A9riodiques%20de%20pr%C3%A9l%C3%A8vement%202026_1.pdf",
            approved="2026-03-26",  # grid _1, decision CD-26c26-CWaPE-1247: corrects the capacity terms
                                    # of BT > 56 kVA only; the residential lines below are unchanged
        ),
        "AIESH": dict(
            fixed=16.91, single=0.1087865, peak=0.1231847, offpeak=0.0575929,
            pic=0.1599802, medium=0.0959881, eco=0.0319960,
            osp=0.0104013, roads=0.0025149, corp_tax=0.0069728, other_tax=0.0000004,
            balances=0.0, prosumer=93.6721568,
            url=CWAPE + "AIESH%20-%20Tarifs%20p%C3%A9riodiques%20de%20pr%C3%A9l%C3%A8vement%202026.pdf",
            approved="2025-06-26",  # decision CD-25f26-CWaPE-1120
        ),
        "ORES": dict(
            fixed=13.30, single=0.0920974, peak=0.1042868, offpeak=0.0487574,
            pic=0.1354374, medium=0.0812624, eco=0.0270875,
            osp=0.0051022, roads=0.0034092, corp_tax=0.0047818, other_tax=0.0000387,
            balances=0.0075962, prosumer=80.9813336,
            url=CWAPE + "ORES%20-%20Tarifs%20p%C3%A9riodiques%20de%20pr%C3%A9l%C3%A8vement%202026_0.pdf",
            approved="2025-12-18",  # grid version 20251126, "Approuvé le 18/12/2025"
        ),
        "RESA": dict(
            fixed=25.00, single=0.0811993, peak=0.0919463, offpeak=0.0429879,
            pic=0.1194108, medium=0.0716465, eco=0.0238822,
            osp=0.0095475, roads=0.0032333, corp_tax=0.0038831, other_tax=0.0,
            balances=0.0065060, prosumer=79.45,
            url=CWAPE + "RESA%20-%20Tarifs%20p%C3%A9riodiques%20de%20pr%C3%A9l%C3%A8vement%202026.pdf",
            approved="2025-06-26",  # decision CD-25f26-CWaPE-1122
        ),
        "REW": dict(
            fixed=24.94, single=0.0930044, peak=0.1053139, offpeak=0.0492377,
            pic=0.1367713, medium=0.0820628, eco=0.0273543,
            osp=0.0110392, roads=0.0032727, corp_tax=0.0089790, other_tax=0.0003563,
            balances=0.0010384, prosumer=87.74,
            url=CWAPE + "REW%20-%20Tarifs%20p%C3%A9riodiques%20de%20pr%C3%A9l%C3%A8vement%202026.pdf",
            approved="2025-09-04",  # decision CD-25i04-CWaPE-1133
        ),
    },
    # 2027 grids as published on 17 November 2026. ORES is missing on purpose:
    # its 2027 grid (version 20251126) is being replaced after the revision of
    # its allowed revenues (decision CD-26i15-CWaPE-1318, 15 October 2026; new
    # tariff proposal due on 5 November 2026, not approved yet).
    2027: {
        "AIEG": dict(
            fixed=19.27, single=0.0868830, peak=0.0983822, offpeak=0.0459969,
            pic=0.1277691, medium=0.0766615, eco=0.0255538,
            osp=0.0061397, roads=0.0035270, corp_tax=0.0037961, other_tax=0.0,  # "V"
            balances=0.0043347, prosumer=77.7635250,
            url=CWAPE + "AIEG%20-%20Tarifs%20p%C3%A9riodiques%20de%20pr%C3%A9l%C3%A8vement%202027_1.pdf",
            approved="2025-11-27",
        ),
        "AIESH": dict(
            fixed=17.12, single=0.1118899, peak=0.1266989, offpeak=0.0592358,
            pic=0.1645440, medium=0.0987264, eco=0.0329088,
            osp=0.0101465, roads=0.0024218, corp_tax=0.0066499, other_tax=0.0000004,
            balances=0.0032379, prosumer=97.0596921,
            url=CWAPE + "AIESH%20-%20Tarifs%20p%C3%A9riodiques%20de%20pr%C3%A9l%C3%A8vement%202027_0.pdf",
            approved="2025-06-26",
        ),
        "RESA": dict(
            fixed=25.00, single=0.0855249, peak=0.0968444, offpeak=0.0452779,
            pic=0.1257719, medium=0.0754632, eco=0.0251544,
            osp=0.0092515, roads=0.0032438, corp_tax=0.0035864, other_tax=0.0,
            balances=0.0061658, prosumer=81.79,
            url=CWAPE + "RESA%20-%20Tarifs%20p%C3%A9riodiques%20de%20pr%C3%A9l%C3%A8vement%202027_0.pdf",
            approved="2025-06-26",
        ),
        "REW": dict(
            fixed=21.62, single=0.0958515, peak=0.1085378, offpeak=0.0507449,
            pic=0.1409581, medium=0.0845748, eco=0.0281916,
            osp=0.0110210, roads=0.0033246, corp_tax=0.0088383, other_tax=0.0003619,
            balances=0.0010299, prosumer=91.11,
            url=CWAPE + "REW%20-%20Tarifs%20p%C3%A9riodiques%20de%20pr%C3%A9l%C3%A8vement%202027.pdf",
            approved="2025-09-04",
        ),
    },
}

# CWaPE, "Tarifs de distribution électricité applicables en Région wallonne du
# 1er janvier 2026 au 31 décembre 2026 - TVAC", update of 3 February 2026:
# fixed part (EUR/year), then c€/kWh single, off-peak, peak, ECO, MEDIUM, PIC.
SUMMARY_URL = CWAPE + "SYNTHESE%20DES%20TARIFS%20DE%20DISTRIBUTION%20ELEC%202026%20(FR)-m%C3%A0j%203.02.2026.pdf"
SUMMARY = {
    2026: {
        "AIEG": (19.50, 10.86965, 6.66291, 12.05279, 4.55953, 9.81796, 15.07640),
        "AIESH": (17.93, 13.63965, 8.21312, 15.16586, 5.49986, 12.28302, 19.06618),
        "ORES": (14.10, 11.98070, 7.38666, 13.27278, 5.08965, 10.83219, 16.57474),
        "RESA": (26.50, 11.06315, 7.01273, 12.20232, 4.98753, 10.05054, 15.11356),
        "REW": (26.44, 12.47514, 7.83587, 13.77995, 5.51623, 11.31533, 17.11443),
    },
}

# Re-invoiced transmission, "Tous les GRD de Wallonie", low voltage, EUR/kWh
# excluding VAT: network infrastructure (I.B) + renewable support levy (II.1)
# + public domain surcharge (II.2) + transmission balances (III).
# CWaPE decision no. 1172 of 15 December 2025.
TRANSPORT_URL = CWAPE + "GRD%27s-Tarifs%20de%20refacturation%20du%20transport%202026.pdf"
TRANSPORT = {2026: dict(infrastructure=0.0243981, levies=0.0007764 + 0.0003310, balances=0.0003673)}

# ---------------------------------------------------------------- profiles
# CWaPE annex 9 (2026-2029 columns). Single-rate volume = total kWh. Bands:
# dual = (peak, offpeak); impact = (eco, medium, pic). The shifted EV volumes
# add up to 7 391 kWh (dual) and 7 364 kWh (Impact), not 7 380: used as
# published.
ANNEX9_URL = (CWAPE + "2025.06.26-GRD%27s-%20Tarifs%20distrib.%20%C3%A9lec.%202026-2029-"
              "Annexe%209%20-%20Profils%20conso%20BT-annexe%20IX.pdf")
PROFILES = {
    "ref3500": dict(kwh=3500, source="corpus"),
    "P_Db": dict(kwh=2077, impact=(893, 527, 656), source="cwape"),
    "P_Dc": dict(kwh=3408, dual=(1613, 1795), dual_shifted=(1427, 1981),
                 impact=(1410, 1022, 976), impact_shifted=(1796, 790, 822), source="cwape"),
    "P_DcVE1": dict(kwh=7380, dual=(3445, 3935), dual_shifted=(1787, 5604),
                    impact=(3147, 2079, 2154), impact_shifted=(5282, 1032, 1050), source="cwape"),
    "P_DcPAC": dict(kwh=7502, dual=(3462, 4040), dual_shifted=(2721, 4781),
                    impact=(3345, 2228, 1929), impact_shifted=(4285, 1727, 1490), source="cwape"),
}
PV_KWC = 4                 # the site's PV reference case: 4 kWc, 3 800 kWh a year
SHARED_KWH = 500           # the site's shared-energy case: 500 kWh a year
SAME_BUILDING_CUT = 0.80   # reduction of the proportional terms, same building

# CWaPE, avis CD-25k27-CWaPE-0967 on the 2026-2030 adaptation plans, table 32
# (overhead lines at the end of 2024, km): (low voltage, medium voltage).
# Municipalities: OptimCE "Quel est mon GRD ?" data, release 2026.10.0.
OVERHEAD_KM = {"AIEG": (513, 111), "AIESH": (781, 385), "ORES": (19347, 2955),
               "RESA": (5170, 684), "REW": (160, 0)}
MUNICIPALITIES = {"AIEG": 6, "AIESH": 6, "ORES": 194, "RESA": 54, "REW": 1}


# ---------------------------------------------------------------- maths
def adders(g):
    """Everything billed per kWh on top of network use, excluding VAT."""
    return g["osp"] + g["roads"] + g["corp_tax"] + g["other_tax"] + g["balances"]


def rate(g, band):
    """All-in distribution rate of a band, EUR/kWh excluding VAT."""
    return g[band] + adders(g)


def transport_rate(year):
    t = TRANSPORT.get(year)
    return None if t is None else sum(t.values())


def cost(g, formula, volumes):
    """Annual distribution cost excluding VAT."""
    if formula == "single":
        (kwh,) = volumes
        return g["fixed"] + kwh * rate(g, "single")
    if formula == "dual":
        peak, off = volumes
        return g["fixed"] + peak * rate(g, "peak") + off * rate(g, "offpeak")
    eco, med, pic = volumes
    return eco * rate(g, "eco") + med * rate(g, "medium") + pic * rate(g, "pic")


def cases():
    """(profile, formula, variant, volumes) for every row of the comparison."""
    out = []
    for name, p in PROFILES.items():
        out.append((name, "single", "base", (p["kwh"],)))
        if "dual" in p:
            out.append((name, "dual", "base", p["dual"]))
            out.append((name, "dual", "shifted", p["dual_shifted"]))
        if "impact" in p:
            out.append((name, "impact", "base", p["impact"]))
            if "impact_shifted" in p:
                out.append((name, "impact", "shifted", p["impact_shifted"]))
    return out


def check_summary(year):
    """The grids must give the CWaPE summary back, or nothing is written."""
    summary = SUMMARY.get(year)
    if summary is None:
        print(f"note: no CWaPE summary transcribed for {year}, check skipped", file=sys.stderr)
        return
    errors = []
    for dso, (fixed, single, off, peak, eco, med, pic) in summary.items():
        g = GRIDS[year][dso]
        if abs(g["fixed"] * VAT - fixed) > 0.015:
            errors.append(f"{dso} fixed part {g['fixed'] * VAT:.4f} vs {fixed}")
        for band, want in (("single", single), ("offpeak", off), ("peak", peak),
                           ("eco", eco), ("medium", med), ("pic", pic)):
            got = round(rate(g, band) * VAT * 100, 5)
            if abs(got - want) > 0.000011:
                errors.append(f"{dso} {band} {got} vs {want}")
    if year in TRANSPORT and abs(round(transport_rate(year) * VAT * 100, 5) - 2.74252) > 0.000011:
        errors.append(f"transport {transport_rate(year) * VAT * 100:.5f} vs 2.74252")
    if errors:
        sys.exit("grids do not match the CWaPE summary:\n  " + "\n  ".join(errors))
    print(f"check: {year} grids give the CWaPE summary back (5 DSOs, 7 values each)", file=sys.stderr)


# ---------------------------------------------------------------- output text
def num(x, lang, dec=0):
    """French, German and Dutch: 1 234,5; English: 1,234.5."""
    s = f"{x:,.{dec}f}"
    if lang == "en":
        return s
    return s.replace(",", " ").replace(".", ",")


def eur(x, lang):
    return f"{num(x, lang)} €"


def pct(x, lang):
    return f"{num(x * 100, lang)} %" if lang != "en" else f"{num(x * 100, lang)}%"


L = {
    "fr": dict(
        dso="GRD", fixed="Part fixe (€/an)", rate="Distribution (c€/kWh)", total="Distribution par an",
        gap="Écart avec le moins cher", single="Compteur simple", dual="Bihoraire",
        dual_s="Bihoraire, consommation déplacée", impact="Tarif Impact", impact_s="Impact, consommation déplacée",
        ev_dual="Voiture électrique, bihoraire", ev_imp="Voiture électrique, Impact déplacé",
        hp_dual="Pompe à chaleur, bihoraire", hp_imp="Pompe à chaleur, Impact déplacé",
        pros_rate="Tarif prosumer (€/kWe, HTVA)", pros_total="Installation de 4 kWc, par an (TVAC)",
        use="Utilisation du réseau", osp="Obligations de service public", sur="Surcharges",
        bal="Soldes régulatoires", sum="Total", cut_single="Réduction par kWh, compteur simple",
        cut_eco="Réduction par kWh, plage ECO", cut_500="Sur 500 kWh partagés (simple)",
        eco_net="Réseau d'un kWh en plage ECO (distribution + transport)",
        y0="2026", y1="2027 (grille publiée)", change="Évolution", pending="en attente",
        lines="Lignes aériennes basse tension (km)", lines_mt="Lignes aériennes moyenne tension (km)",
        towns="Communes desservies",
    ),
    "en": dict(
        dso="DSO", fixed="Fixed part (€/year)", rate="Distribution (c€/kWh)", total="Distribution per year",
        gap="Gap with the cheapest", single="Single rate", dual="Dual rate",
        dual_s="Dual rate, use shifted", impact="Impact tariff", impact_s="Impact, use shifted",
        ev_dual="Electric car, dual rate", ev_imp="Electric car, Impact shifted",
        hp_dual="Heat pump, dual rate", hp_imp="Heat pump, Impact shifted",
        pros_rate="Prosumer tariff (€/kWe, excl. VAT)", pros_total="4 kWp installation, per year (incl. VAT)",
        use="Network use", osp="Public service obligations", sur="Surcharges",
        bal="Regulatory balances", sum="Total", cut_single="Reduction per kWh, single rate",
        cut_eco="Reduction per kWh, ECO band", cut_500="On 500 kWh shared (single rate)",
        eco_net="Grid cost of a kWh in the ECO band (distribution + transmission)",
        y0="2026", y1="2027 (published grid)", change="Change", pending="pending",
        lines="Overhead low-voltage lines (km)", lines_mt="Overhead medium-voltage lines (km)",
        towns="Municipalities served",
    ),
    "de": dict(
        dso="Netzbetreiber", fixed="Festbetrag (€/Jahr)", rate="Verteilung (c€/kWh)", total="Verteilung pro Jahr",
        gap="Abstand zum günstigsten", single="Eintarif", dual="Zweitarif",
        dual_s="Zweitarif, Verbrauch verlagert", impact="Impact-Tarif", impact_s="Impact, Verbrauch verlagert",
        ev_dual="Elektroauto, Zweitarif", ev_imp="Elektroauto, Impact verlagert",
        hp_dual="Wärmepumpe, Zweitarif", hp_imp="Wärmepumpe, Impact verlagert",
        pros_rate="Prosumer-Tarif (€/kWe, ohne MwSt.)", pros_total="Anlage mit 4 kWp, pro Jahr (inkl. MwSt.)",
        use="Netznutzung", osp="Gemeinwirtschaftliche Verpflichtungen", sur="Zuschläge",
        bal="Regulierungssalden", sum="Gesamt", cut_single="Ermäßigung pro kWh, Eintarif",
        cut_eco="Ermäßigung pro kWh, ECO-Fenster", cut_500="Bei 500 kWh geteiltem Strom (Eintarif)",
        eco_net="Netzkosten einer kWh im ECO-Fenster (Verteilung + Übertragung)",
        y0="2026", y1="2027 (veröffentlichter Tarif)", change="Veränderung", pending="ausstehend",
        lines="Niederspannungs-Freileitungen (km)", lines_mt="Mittelspannungs-Freileitungen (km)",
        towns="Versorgte Gemeinden",
    ),
    "nl": dict(
        dso="Netbeheerder", fixed="Vast deel (€/jaar)", rate="Distributie (c€/kWh)", total="Distributie per jaar",
        gap="Verschil met de goedkoopste", single="Enkelvoudige meter", dual="Tweevoudig",
        dual_s="Tweevoudig, verbruik verschoven", impact="Impact-tarief", impact_s="Impact, verbruik verschoven",
        ev_dual="Elektrische auto, tweevoudig", ev_imp="Elektrische auto, Impact verschoven",
        hp_dual="Warmtepomp, tweevoudig", hp_imp="Warmtepomp, Impact verschoven",
        pros_rate="Prosumententarief (€/kWe, excl. btw)", pros_total="Installatie van 4 kWp, per jaar (incl. btw)",
        use="Netgebruik", osp="Openbaredienstverplichtingen", sur="Toeslagen",
        bal="Regulatoire saldi", sum="Totaal", cut_single="Korting per kWh, enkelvoudig",
        cut_eco="Korting per kWh, ECO-uren", cut_500="Op 500 kWh gedeeld (enkelvoudig)",
        eco_net="Netkosten van een kWh in de ECO-uren (distributie + transmissie)",
        y0="2026", y1="2027 (gepubliceerd tarief)", change="Evolutie", pending="in afwachting",
        lines="Bovengrondse laagspanningslijnen (km)", lines_mt="Bovengrondse middenspanningslijnen (km)",
        towns="Bediende gemeenten",
    ),
}


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


def results(year):
    grids = GRIDS[year]
    res = {}
    for dso, g in grids.items():
        for name, formula, variant, vol in cases():
            res[(dso, name, formula, variant)] = cost(g, formula, vol)
    return res


def order(year, res):
    """Cheapest first, on the site's reference case."""
    return sorted(GRIDS[year], key=lambda d: res[(d, "ref3500", "single", "base")])


def tables(year, lang):
    t = L[lang]
    g = GRIDS[year]
    res = results(year)
    dsos = order(year, res)
    ttc = {k: v * VAT for k, v in res.items()}
    tr = transport_rate(year)
    out = []

    # 1. reference case, single rate
    low = min(ttc[(d, "ref3500", "single", "base")] for d in dsos)
    rows = []
    for d in dsos:
        s = SUMMARY.get(year, {}).get(d)
        fixed = s[0] if s else g[d]["fixed"] * VAT
        r = s[1] if s else rate(g[d], "single") * VAT * 100
        tot = ttc[(d, "ref3500", "single", "base")]
        rows.append([d, num(fixed, lang, 2), num(r, lang, 2), f"**{eur(tot, lang)}**",
                     "—" if tot == low else f"+{eur(tot - low, lang)} (+{pct(tot / low - 1, lang)})"])
    out.append(("T1 3 500 kWh single rate", table([t["dso"], t["fixed"], t["rate"], t["total"], t["gap"]], rows)))

    # 2. P_Dc, the CWaPE's typical household
    rows = [[d] + [eur(ttc[(d, "P_Dc", f, v)], lang) for f, v in
                   (("single", "base"), ("dual", "base"), ("dual", "shifted"), ("impact", "base"), ("impact", "shifted"))]
            for d in dsos]
    out.append(("T2 P_Dc 3 408 kWh", table([t["dso"], t["single"], t["dual"], t["dual_s"], t["impact"], t["impact_s"]], rows)))

    # 3. P_Db, small consumer
    rows = [[d, eur(ttc[(d, "P_Db", "single", "base")], lang), eur(ttc[(d, "P_Db", "impact", "base")], lang)] for d in dsos]
    out.append(("T3 P_Db 2 077 kWh", table([t["dso"], t["single"], t["impact"]], rows)))

    # 4. EV and heat pump
    rows = [[d, eur(ttc[(d, "P_DcVE1", "dual", "base")], lang), eur(ttc[(d, "P_DcVE1", "impact", "shifted")], lang),
             eur(ttc[(d, "P_DcPAC", "dual", "base")], lang), eur(ttc[(d, "P_DcPAC", "impact", "shifted")], lang)] for d in dsos]
    out.append(("T4 EV 7 380 kWh / heat pump 7 502 kWh",
                table([t["dso"], t["ev_dual"], t["ev_imp"], t["hp_dual"], t["hp_imp"]], rows)))

    # 5. prosumer tariff
    rows = [[d, num(g[d]["prosumer"], lang, 2), eur(g[d]["prosumer"] * PV_KWC * VAT, lang)] for d in dsos]
    out.append(("T5 prosumer 4 kWc", table([t["dso"], t["pros_rate"], t["pros_total"]], rows)))

    # 6. what the single rate is made of, c€/kWh incl. VAT
    rows = []
    for d in dsos:
        x = g[d]
        parts = [x["single"], x["osp"], x["roads"] + x["corp_tax"] + x["other_tax"], x["balances"]]
        rows.append([d] + [num(p * VAT * 100, lang, 2) for p in parts] + [f"**{num(sum(parts) * VAT * 100, lang, 2)}**"])
    out.append(("T6 single rate breakdown c€/kWh incl. VAT",
                table([t["dso"], t["use"], t["osp"], t["sur"], t["bal"], t["sum"]], rows)))

    # 7. overhead lines and municipalities
    rows = [[d, num(OVERHEAD_KM[d][0], lang), num(OVERHEAD_KM[d][1], lang), num(MUNICIPALITIES[d], lang)] for d in dsos]
    out.append(("T7 overhead lines end 2024", table([t["dso"], t["lines"], t["lines_mt"], t["towns"]], rows)))

    # 8. sharing: grid cost of an ECO kWh, same-building reduction
    if tr is not None:
        tr_prop = TRANSPORT[year]["infrastructure"]
        rows = []
        for d in dsos:
            x = g[d]
            eco_net = (rate(x, "eco") + tr) * VAT * 100
            cut_s = SAME_BUILDING_CUT * (x["single"] + tr_prop) * VAT
            cut_e = SAME_BUILDING_CUT * (x["eco"] + tr_prop) * VAT
            rows.append([d, num(eco_net, lang, 2), num(cut_s * 100, lang, 2), num(cut_e * 100, lang, 2),
                         eur(cut_s * SHARED_KWH, lang)])
        out.append(("T8 sharing", table([t["dso"], t["eco_net"], t["cut_single"], t["cut_eco"], t["cut_500"]], rows)))

    # 9. next year, P_Dc dual rate, distribution only
    nxt = GRIDS.get(year + 1)
    if nxt:
        rows = []
        for d in dsos:
            now = res[(d, "P_Dc", "dual", "base")] * VAT
            if d in nxt:
                then = cost(nxt[d], "dual", PROFILES["P_Dc"]["dual"]) * VAT
                ch = then / now - 1
                rows.append([d, eur(now, lang), eur(then, lang), ("+" if ch >= 0 else "") + pct(ch, lang)])
            else:
                rows.append([d, eur(now, lang), t["pending"], "—"])
        out.append((f"T9 P_Dc dual {year} -> {year + 1}", table([t["dso"], t["y0"], t["y1"], t["change"]], rows)))
    return out


def facts(year):
    """Numbers quoted in the prose, so that none is typed by hand."""
    res = results(year)
    dsos = order(year, res)
    ttc = {k: v * VAT for k, v in res.items()}
    lines = []
    for name, formula, variant, _ in cases():
        vals = [ttc[(d, name, formula, variant)] for d in dsos]
        lo, hi = min(vals), max(vals)
        lines.append(f"{name:8} {formula:6} {variant:7} " + "  ".join(f"{d} {v:7.2f}" for d, v in zip(dsos, vals))
                     + f"   gap {hi - lo:6.2f} € ({(hi / lo - 1) * 100:4.1f} %)")
    htva = {d: res[(d, "P_Dc", "dual", "base")] for d in dsos}
    lines.append("P_Dc dual excl. VAT (press kit of July 2025: AIEG 305, ORES 325, RESA 329, AIESH 387): "
                 + ", ".join(f"{d} {v:.0f}" for d, v in htva.items()))
    for d in dsos:
        save = ttc[(d, "P_Dc", "dual", "base")] - ttc[(d, "P_Dc", "impact", "shifted")]
        save_ev = ttc[(d, "P_DcVE1", "dual", "base")] - ttc[(d, "P_DcVE1", "impact", "shifted")]
        lines.append(f"{d}: P_Dc dual -> Impact shifted saves {save:.2f} €; EV saves {save_ev:.2f} €")
    tr = transport_rate(year)
    if tr is not None:
        lines.append(f"transport {tr * VAT * 100:.5f} c€/kWh incl. VAT; 3 500 kWh: {3500 * tr * VAT:.2f} €; "
                     f"P_Dc: {3408 * tr * VAT:.2f} €")
    return "\n".join(lines)


# ---------------------------------------------------------------- CSV
def write_csv(year):
    path = ROOT / "assets" / "data" / f"distribution-tariffs-wallonia-{year}.csv"
    tr = transport_rate(year)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["year", "dso", "profile", "profile_source", "annual_kwh", "formula", "variant",
                "kwh_single", "kwh_peak", "kwh_offpeak", "kwh_eco", "kwh_medium", "kwh_pic",
                "fixed_eur_excl_vat", "distribution_eur_excl_vat", "distribution_eur_incl_vat",
                "transmission_eur_incl_vat", "network_eur_incl_vat", "grid_approved", "grid_url"])
    res = results(year)
    for d in order(year, res):
        g = GRIDS[year][d]
        for name, formula, variant, vol in cases():
            p = PROFILES[name]
            kwh = sum(vol)
            single = vol[0] if formula == "single" else ""
            peak, off = vol if formula == "dual" else ("", "")
            eco, med, pic = vol if formula == "impact" else ("", "", "")
            dist = res[(d, name, formula, variant)]
            trans = kwh * tr * VAT if tr is not None else None
            w.writerow([year, d, name, p["source"], p["kwh"], formula, variant, single, peak, off, eco, med, pic,
                        f"{g['fixed'] if formula != 'impact' else 0:.2f}", f"{dist:.2f}", f"{dist * VAT:.2f}",
                        "" if trans is None else f"{trans:.2f}",
                        "" if trans is None else f"{dist * VAT + trans:.2f}", g["approved"], g["url"]])
    path.write_text(buf.getvalue(), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT).as_posix()}: {buf.getvalue().count(chr(10)) - 1} rows", file=sys.stderr)


# ---------------------------------------------------------------- SVG
SVG_TEXT = {
    "fr": dict(
        title="Le même ménage, cinq factures de réseau",
        sub="Distribution par an en 2026, TVA comprise, ménage type de la CWaPE (3 408 kWh)",
        a="Bihoraire, sans rien changer", b="Tarif Impact, consommation déplacée",
        foot="Source : grilles 2026 des GRD approuvées par la CWaPE, profil P_Dc de la CWaPE. Calcul OptimCE, hors transport.",
        desc=("Graphique en barres : pour le même ménage de 3 408 kWh par an, la distribution coûte en 2026, TVA comprise, "
              "{a} en bihoraire sans rien changer, et {b} au tarif Impact en déplaçant une partie de la consommation."),
        join=", ", last=" et ", item="{d} {v}",
    ),
    "en": dict(
        title="The same household, five grid bills",
        sub="Distribution per year in 2026, VAT included, CWaPE typical household (3,408 kWh)",
        a="Dual rate, nothing changed", b="Impact tariff, use shifted",
        foot="Source: 2026 DSO grids approved by the CWaPE, CWaPE profile P_Dc. OptimCE calculation, transmission excluded.",
        desc=("Bar chart: for the same household using 3,408 kWh a year, distribution costs in 2026, VAT included, "
              "{a} on the dual rate with nothing changed, and {b} on the Impact tariff with part of the use shifted."),
        join=", ", last=" and ", item="{v} at {d}",
    ),
    "de": dict(
        title="Derselbe Haushalt, fünf Netzrechnungen",
        sub="Verteilung pro Jahr 2026, inkl. MwSt., typischer Haushalt der CWaPE (3 408 kWh)",
        a="Zweitarif, nichts geändert", b="Impact-Tarif, Verbrauch verlagert",
        foot="Quelle: von der CWaPE genehmigte Tarife 2026 der Netzbetreiber, Profil P_Dc der CWaPE. Berechnung OptimCE, ohne Übertragung.",
        desc=("Balkendiagramm: Für denselben Haushalt mit 3 408 kWh pro Jahr kostet die Verteilung 2026 inklusive Mehrwertsteuer "
              "{a} im Zweitarif ohne Änderung und {b} im Impact-Tarif mit teilweise verlagertem Verbrauch."),
        join=", ", last=" und ", item="{v} bei {d}",
    ),
    "nl": dict(
        title="Hetzelfde gezin, vijf netfacturen",
        sub="Distributie per jaar in 2026, incl. btw, typegezin van de CWaPE (3 408 kWh)",
        a="Tweevoudig, niets veranderd", b="Impact-tarief, verbruik verschoven",
        foot="Bron: door de CWaPE goedgekeurde tarieven 2026 van de netbeheerders, profiel P_Dc van de CWaPE. Berekening OptimCE, zonder transmissie.",
        desc=("Staafdiagram: voor hetzelfde gezin met 3 408 kWh per jaar kost de distributie in 2026, btw inbegrepen, "
              "{a} met het tweevoudig tarief zonder iets te veranderen, en {b} met het Impact-tarief en een deel van het verbruik verschoven."),
        join=", ", last=" en ", item="{v} bij {d}",
    ),
}
GREY, GREEN, INK, INK2, RULE = "#868E96", "#2E7D32", "#212529", "#495057", "#DEE2E6"
FR_ARTICLE = {"AIEG": "l'AIEG", "AIESH": "l'AIESH", "REW": "le REW"}
FONT = "system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"


def enumerate_values(vals, lang):
    s = SVG_TEXT[lang]
    if lang == "fr":
        items = [f"{v} chez {FR_ARTICLE.get(d, d)}" for d, v in vals]
    else:
        items = [s["item"].format(d=d, v=v) for d, v in vals]
    return s["join"].join(items[:-1]) + s["last"] + items[-1]


def svg(year, lang):
    s = SVG_TEXT[lang]
    res = results(year)
    dsos = order(year, res)
    a = [(d, res[(d, "P_Dc", "dual", "base")] * VAT) for d in dsos]
    b = [(d, res[(d, "P_Dc", "impact", "shifted")] * VAT) for d in dsos]
    W, H = 800, 470
    x0, x1 = 150, 690                   # bar area
    vmax = 450.0
    sx = (x1 - x0) / vmax
    top, row_h, bar_h, gap = 160, 52, 18, 2
    desc = s["desc"].format(a=enumerate_values([(d, eur(v, lang)) for d, v in a], lang),
                            b=enumerate_values([(d, eur(v, lang)) for d, v in b], lang))
    esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">',
         f'<title id="t">{esc(s["title"])}</title><desc id="d">{esc(desc)}</desc>',
         f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
         f'<g font-family="{FONT}">',
         f'<text x="60" y="52" font-size="22" fill="{INK}" font-weight="700">{esc(s["title"])}</text>',
         f'<text x="60" y="78" font-size="14" fill="{INK2}">{esc(s["sub"])}</text>',
         f'<rect x="60" y="104" width="14" height="14" rx="3" fill="{GREY}"/>',
         f'<text x="82" y="116" font-size="14" fill="{INK}">{esc(s["a"])}</text>',
         f'<rect x="380" y="104" width="14" height="14" rx="3" fill="{GREEN}"/>',
         f'<text x="402" y="116" font-size="14" fill="{INK}">{esc(s["b"])}</text>']
    # recessive grid: 0, 100, 200, 300, 400 €
    for v in range(0, 451, 100):
        x = x0 + v * sx
        o.append(f'<line x1="{x:.1f}" y1="{top - 14}" x2="{x:.1f}" y2="{top + row_h * len(dsos) - 14}" '
                 f'stroke="{RULE}" stroke-width="1"/>')
        o.append(f'<text x="{x:.1f}" y="{top + row_h * len(dsos) + 4}" font-size="12" fill="{INK2}" '
                 f'text-anchor="middle">{esc(eur(v, lang))}</text>')
    for i, d in enumerate(dsos):
        y = top + i * row_h
        o.append(f'<text x="{x0 - 14}" y="{y + bar_h + 6}" font-size="15" fill="{INK}" font-weight="600" '
                 f'text-anchor="end">{d}</text>')
        for j, (val, col) in enumerate(((a[i][1], GREY), (b[i][1], GREEN))):
            by = y + j * (bar_h + gap) - 6
            w = val * sx
            # 4 px rounded data end, square at the baseline
            o.append(f'<path d="M{x0},{by} h{w - 4:.1f} a4,4 0 0 1 4,4 v{bar_h - 8} a4,4 0 0 1 -4,4 h-{w - 4:.1f} z" fill="{col}"/>')
            o.append(f'<text x="{x0 + w + 8:.1f}" y="{by + bar_h - 4}" font-size="13" fill="{INK}" '
                     f'font-weight="{700 if j else 400}">{esc(eur(val, lang))}</text>')
    o.append(f'<text x="60" y="{H - 24}" font-size="12" fill="{INK2}">{esc(s["foot"])}</text>')
    o.append('</g>\n</svg>\n')
    path = ROOT / "assets" / "images" / "diagrams" / f"distribution-tariffs-dso-{lang}.svg"
    return path, "\n".join(o), desc


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--year", type=int, default=YEAR)
    ap.add_argument("--lang", choices=["fr", "en", "de", "nl", "all"], default="all")
    ap.add_argument("--dry-run", action="store_true", help="print only, write nothing")
    args = ap.parse_args()
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")   # the Windows console defaults to cp1252
    if args.year not in GRIDS:
        sys.exit(f"no grids transcribed for {args.year}")
    check_summary(args.year)
    complete = set(GRIDS[args.year]) == {"AIEG", "AIESH", "ORES", "RESA", "REW"}
    langs = ["fr", "en", "de", "nl"] if args.lang == "all" else [args.lang]
    for lang in langs:
        print(f"\n======== {lang}")
        for name, md in tables(args.year, lang):
            print(f"\n--- {name}\n{md}")
    print("\n======== facts\n" + facts(args.year))
    if args.dry_run:
        return
    if not complete:
        sys.exit(f"{args.year}: not all five DSOs have a grid, nothing written")
    write_csv(args.year)
    for lang in ["fr", "en", "de", "nl"]:
        path, text, desc = svg(args.year, lang)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT).as_posix()}\n  alt/desc: {desc}", file=sys.stderr)


if __name__ == "__main__":
    main()
