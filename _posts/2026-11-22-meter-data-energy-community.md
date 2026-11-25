---
layout: post
title: "Meter data in an energy community"
date: 2026-11-22 06:00:00 +0100
author: "Eric from OptimCE"
excerpt: "An energy community measures nothing itself. Every month, by the twelfth working day at the latest, the grid operator sends its representative each member's volumes, quarter-hour by quarter-hour: 2,880 values per meter and per quantity for a thirty-day month. That flow is a condition of taking part, not a matter of consent. Everything else, from the history used to simulate a key to a box plugged into the P1 port, needs each member's agreement."
description: "How meter data reaches an energy community in Wallonia: what the DSO sends and when, on what legal basis, what each member sees, and the P1 port."
tags: [guide, community]
lang: en
ref: meter-data-energy-community
pillar: communautes-energie
last_modified_at: 2026-11-24 06:00:00 +0100
permalink: /en/guides/meter-data-energy-community/
faq:
  - q: "What meter data does the DSO send to an energy community?"
    a: "In Wallonia, the distribution system operator sends the sharing representative, for each member and each quarter-hour, the offtake, the shared volume consumed and the residual consumption, which the CWaPE calls “alloconsommation”: the part the supplier bills. It adds each producer's injection, the total shared volume, the surplus and the allocation method used. The model agreement approved by the CWaPE on 12 October 2023 requires it to make these data available every month, by the twelfth working day of the following month at the latest. It is a best-efforts obligation, and unvalidated data may arrive every week. The channel and the format are those the DSO has chosen. At ORES, they are two CSV files sent by email, one for production and one for consumption, with one row per quarter-hour, per EAN code and per iteration of the allocation key."
  - q: "Do I have to consent to my data going to the community?"
    a: "Not for the sharing flow itself. The Walloon electricity decree requires the DSO to send the representative each participant's metering data, and the CWaPE's model agreement states that any participation requires the DSO to collect and use load curves. This flow is a condition of taking part: you cannot stay in the sharing and refuse it. The participant does, however, sign annex 8 of the sharing form. In it, they mandate the representative to communicate their data in the procedure, and authorise the DSO to send their quarter-hour curve to their supplier. Anything outside this framework requires prior, free, specific, informed and unambiguous agreement: the history requested to simulate a key, a box plugged into the P1 port, individual curves shown to other members."
  - q: "Can other members see my consumption?"
    a: "Not by default. The DSO sends each member's data to the representative, not to the other members, and the Walloon decree requires the agreement between each participant and the community to settle privacy protection and the procedure for passing data between participants. The Belgian Data Protection Authority points out that smart meters make it possible to infer sensitive data about residents' behaviour: a quarter-hour curve shows when a household gets up, leaves and comes home. A prudent practice is to show each member their own figures, and the group only aggregates: production, shared volume, share of consumption covered. A ranking by name or an individual curve is only shown with the person's explicit agreement. The one exception in practice: when the community has a single producer, the shared production is that member's injection."
  - q: "How do I access my smart meter data?"
    a: "Through your grid operator's portal, free of charge: the Walloon decree requires it. The Walloon Government order of 1 December 2022 sets the minimum: yearly, monthly, weekly and daily views over the last twenty-four months, intraday detail on explicit request, and an export to a spreadsheet. At ORES, you request the quarter-hour view in the myORES customer area; ORES says these data do not go up to your supplier, but that the activation itself is passed on to it, which may lead some suppliers to issue an interim bill, with no effect on the annual bill. RESA offers a quarter-hour profile in MyRESA, AIEG and AIESH in MyConso. These are the same data a community will ask you for to simulate an allocation key before sharing starts: you can export them and hand them over, with a written agreement for that use. During sharing, your shared volumes reach you through the community, which receives them from the DSO every month."
  - q: "Can the P1 port be used for energy sharing?"
    a: "Not for the calculation. The smart meter's P1 port sends a reading every second, useful for following your consumption in real time, but it only shows your own meter: neither the production of the shared roof nor the share allocated to you. Sharing volumes are those the DSO determines from the meter readings and the allocation key, and sends every month to the representative; the sharing invoice is based on them. In Wallonia, the port is switched off by default, and switching it on is free on simple request to the DSO. The decree makes whoever collects data through this port the controller of that processing: a community that hands out P1 boxes and centralises their measurements must obtain each member's prior agreement and tell them what it uses the data for."
  - q: "How long are sharing data kept?"
    a: "In Wallonia, the electricity decree sets the rule for the CWaPE and the grid operator: personal data linked to sharing are kept five years after the sharing activity stops, and those of a participant who has left the sharing are deleted five years after their departure was notified. The text sets no period for the representative. As controller of the data it receives from the DSO, the representative may use them only for the purposes set by the decree, and the GDPR requires it to set a retention period itself and announce it to members. On the meter side, the decree requires the device to keep, readable remotely, the load curves of the last ten days, the daily readings of the last forty days and the monthly readings of the last thirteen months."
---

An energy community lives on data it does not produce. Its **meter data** all come from the distribution system operator (DSO), to which the Walloon decree reserves the collection of metering data. Every month, the DSO sends the sharing representative each member's volumes, quarter-hour by quarter-hour: **2,880 values per meter** and per quantity for a thirty-day month, **by the twelfth working day** of the following month at the latest.

These data travel under two regimes. The first is set by law: the DSO sends, the community receives, and no member has any consent to give. The second covers everything else, from the history used to simulate a key to a box plugged into the P1 port, and it requires each member's agreement.

This site already covers metering regimes and the P1 port ([“Smart meters in Wallonia: the complete guide”](/en/guides/smart-meter-wallonia/)), how the key is applied ([“Allocation key in Belgium: the 3 regions”](/en/guides/allocation-key-belgium/)), simulation ([“Simulate an allocation key: test your scenarios”](/en/guides/simulate-allocation-key-optimce/)), the quarter-hour rule ([“Local electricity: the short-circuit guide”](/en/guides/local-electricity-short-circuit-guide/)) and the forms ([“Energy community: CWaPE documents and deadlines”](/en/guides/energy-community-administrative-documents-wallonia/)).

**The question here is how the data flow: which data pass from the DSO to the community, how often, on what legal basis, and what a member is entitled to see, of their own data and of other members'.** The article describes Wallonia and electricity as of 22 November 2026; Flanders and Brussels are summarised at the end.

## The data a community needs

A community needs data at three points. **Before sharing**, to choose its allocation key: each future member's history and the production profile, ideally a full year at quarter-hour resolution. The DSO sends nothing at this stage; the members supply these curves. **During sharing**, to invoice: the volumes the DSO calculates every month. **Afterwards**, to report: every year, the DSO sends the CWaPE each community's metering data (article 35*sexdecies*, § 3 of the decree of 12 April 2001).

The sharing quantities are defined by the model agreement the CWaPE approved on 12 October 2023, which each community signs with its DSO. They are calculated for each EAN code and each quarter-hour. The abbreviations are those of the French text.

| Quantity | Abbreviation | What it measures |
|---|---|---|
| Injection | I | Production not consumed on site, injected into the grid |
| Offtake | Pl | Consumption drawn from the grid: Pl = VPC + AL |
| Shared volume | VP | The sum of the injections made available for sharing |
| Shared volume consumed | VPC | The part of a participant's consumption covered by sharing |
| Excess | E | The volume allocated to a participant that they did not consume |
| Surplus | S | The shared volume nobody consumed: S = VP − ∑ VPC |
| Residual consumption (“alloconsommation”) | AL | The part not covered, billed by the supplier: AL = Pl − VPC |

*Assumptions: definitions from article 6.2.1 of the model agreement (CWaPE decision CD-23j12-CWaPE-0818), reworded; the formulas are those of the text, which also calls the alloconsommation “volume résiduel” (residual volume).*

### The meter must be able to measure them

For a smart meter, the CWaPE's explanatory guide to the sharing form sets two conditions: a communication function that is “activated and working” (our translation), and metering regime 3, which sends the quarter-hour curve to the market, activated “with the supplier, at the participant's request”. Until this regime is in place, annex 8 of the form stands in for it: in it, the participant authorises the DSO to send their quarter-hourly metering data to their supplier.

A member should therefore know this before signing: **their curve goes to the representative, but also to their supplier.** Our [barometer of authorised sharing activities](/en/guides/energy-communities-wallonia-barometer/) found the same thing: when the CWaPE authorises a sharing activity under a suspensive condition, the condition always consists in switching every participant to regime 3.

## What the DSO sends, to whom and when

Grid operators “determine the volumes of electricity consumed as part of the sharing operation” (our translation), then send the community “the metering data” of production and of each participant, and the suppliers “the data needed for invoicing” (article 35*sexdecies*, § 2). The decree sets no frequency, no deadline and no format.

The model agreement sets them: the DSO “uses all means” (our translation) to provide these data “monthly, and by the twelfth working day of the following month at the latest” (article 6.2.2). It is a best-efforts obligation. Unvalidated data may arrive every week, through the channel the DSO has chosen.

At ORES, these are two CSV files sent by email every month, one for production and one for consumption. Each row of the second file carries a quarter-hour, an EAN code and an iteration of the key; a member's result is the sum of their iterations. Twelve consumers and a key in three iterations make up to **103,680 rows** for a thirty-day month.

| Recipient | What it receives | Frequency |
|---|---|---|
| Sharing representative | The quantities above, per EAN and per quarter-hour, and the allocation method | Every month, by the 12th working day of the following month at the latest |
| Each member's supplier | The quarter-hour curve and the shared volumes, to bill the remainder | Every month, outside market processes |
| Member | What the community passes on; their curve on the DSO's portal | As set in their agreement; portal open at any time |
| CWaPE | Each community's metering data | Every year |

*Assumptions: rules in force in Wallonia on 22 November 2026: decree of 12 April 2001 (articles 35ter, 35duodecies and 35sexdecies), the CWaPE's model agreement and the CWaPE's evaluation report of 20 February 2025.*

Suppliers do not receive the shared volumes through the usual channel: according to the CWaPE's evaluation report of 20 February 2025, they travel “outside market processes through a separate channel (SFTP servers)” (our translation), and each supplier recalculates what it bills.

The new technical regulation, approved by the CWaPE on 27 August 2026, keeps the twelfth-working-day deadline. Data will be sent “as a quarter-hourly curve as well as aggregated over the month” (our translation), through an application programming interface if the DSO has developed one (article IX.7), and corrections will be possible up to twelve months after the month concerned (article IX.17). Published in the Belgian Official Gazette on 20 November 2026, it comes into force on 30 November 2026.

For whoever runs the community, this sets a calendar: a month's volumes arrive by around the middle of the following month at the latest, and the sharing invoices go out after that. A late correction goes through a credit note, as [“Invoicing shared electricity in Belgium”](/en/guides/who-invoices-shared-electricity-belgium/) explains. If a member disputes a volume, the representative forwards the complaint to the DSO within five working days, and the DSO answers within thirty days (model agreement, article 6.1.4).

## Legal basis and consent: two regimes

### What flows under the law

The DSO is the controller of the meter data, and processes them “only to carry out its legal or regulatory tasks” (article 35*septies*, § 2; our translation). For the notification and authorisation of sharing, the CWaPE bases the processing on article 6(1)(e) of the GDPR, a task carried out in the public interest. The model agreement is clear: “Any participation requires the collection and use of the Load Curves” of the participants by the DSO (article 6.1.3). Once it has received the data, the representative in turn becomes their controller, for the purposes set by the decree only (article 9.4 of the model agreement).

This flow therefore does not rest on a consent that a member could withdraw while staying in the sharing: it is the condition of taking part. Annex 8 documents it, with the mandate given to the representative and the authorisation to send the curve to the supplier. The CWaPE and the DSO keep these data five years after the sharing stops; those of a member who has left are deleted five years after their departure was notified (article 35*quaterdecies*, § 3).

### What needs each member's agreement

Everything else falls under a strict rule. Outside a legal provision and outside the DSO's processors, “no one may read, export or process the information” (our translation) of a smart meter without its user's “prior, free, specific, informed and unambiguous” agreement (article 35*septies*, § 3). For a community, this covers the history requested to simulate a key, a box plugged into the P1 port, a curve or volumes shown by name to other members, and any data handed to a third party for another use.

A clause buried in the articles of association is not enough. As early as 2018, the Belgian Privacy Commission, since replaced by the Data Protection Authority, wrote that “the common practice of granting ‘consent’ through a clause in the general terms and conditions can no longer be accepted” (our translation). An agreement is asked for separately, for a precise use, and can be withdrawn as easily as it was given (article 7(3) of the GDPR). Whatever the agreement, the decree prohibits trading in metering data and in profiles from which consumption behaviour can be inferred.

These rules are written into the agreement between each participant and the community, which must contain “the rules and responsibilities applicable to privacy and the protection of personal data” (our translation) and “the procedure for passing data between participants” (article 35*duodecies*, § 2). If the community entrusts its files to online software, the publisher that hosts them is a processor within the meaning of article 28 of the GDPR, with a contract to match. We have found no Belgian guidance specific to communities on this point: the general GDPR rules apply.

### The history, before sharing

Before authorisation, the curves used to simulate a key come from the members. The simplest route is an export: the Walloon Government order of 1 December 2022 requires the DSO's portal to cover twenty-four months, to show intraday detail “at the customer's explicit request” (our translation) and to allow the data to be exported “in a form usable by a spreadsheet” (article 4). The member exports, then hands the file to the community with a written agreement for that use.

The other route is delegated access. ORES opens an application programming interface to energy service providers, who retrieve up to three years of quarter-hour volumes with the consent the customer gives in myORES. Implementing Regulation (EU) 2023/1162 also lists renewable energy communities and citizen energy communities among the eligible parties to which a customer can grant access to their metering data.

## What each member can see, and what they should not see of others

The DSO sends the sharing volumes to the representative, not to the members. What a member receives depends on the community: their sharing invoice, which shows their shared volume consumed, and whatever their agreement adds. They can see their full curve free of charge on their DSO's portal (article 35*ter*, § 3). At ORES, the quarter-hour view is requested in the myORES customer area. It does not send these data up to the supplier, which has to request them from ORES itself to use them; but, according to the myORES FAQ, the activation “est transmise à votre fournisseur d'énergie” (is passed on to your energy supplier), and some suppliers then issue an interim bill, with no effect on the annual bill or on compensation. RESA offers a quarter-hour profile in MyRESA, AIEG and AIESH in MyConso. If a member exercises their right of access with the representative for data held by the DSO, the representative forwards the request without delay and the DSO answers the member directly (model agreement, article 9.4).

What members see of each other is another matter. The Data Protection Authority pointed it out in 2023: smart meters “make it possible to infer potentially sensitive data about residents' behaviour” (our translation). A quarter-hour curve shows when a household gets up, when the house empties and when it fills again. The decree leaves this point to each participant's agreement; failing that, the GDPR requires data minimisation (article 5(1)(c)). We recommend three rules:

- each member sees their own figures, quarter-hours included;
- the group sees aggregates: production, shared volume, share of consumption covered;
- a ranking by name or an individual curve is only shown with the person's explicit agreement.

One exception: when there is a single producer, the community's production is that producer's injection, and everyone sees it, at least as a total. It is better to tell them so before they sign. [“Engaging energy community members”](/en/guides/engage-energy-community-members/) gives examples of what can be shared with the group.

## The P1 port: real-time measurement, alongside the official data

The smart meter has a second, local output. The decree requires it to provide information “in near real time” (our translation), “usable on an output port” (article 35*bis*, § 1): this is the P1 port. In Wallonia, it is “switched off by default” and is switched on at simple request to the DSO (article 35*bis*, § 4), free of charge according to the 2026 grid of harmonised non-periodic tariffs; our [smart meter guide](/en/guides/smart-meter-wallonia/) describes the steps. The port follows the Belgian eMUCS-P1 specification, based on the Dutch DSMR 5.0.2 specification: one reading every second, with the power drawn and injected, the voltage and current per phase, the register readings and the gas meter's last value. One quarter-hour of official metering equals **900 readings** on the P1 port.

For a community, it has three limits.

**It only shows your meter.** A consumer reads their offtake there, a producer their net injection. Nobody sees the production of the shared roof there, nor the share allocated to them, which only exists after the DSO's calculation.

**It does not produce the official volumes.** Sharing volumes are those the DSO “determines” (our translation) and sends every month; the CWaPE points out that sharing invoices are based on the data received from the grid operator.

**It makes whoever reads it a data controller.** The third party that collects information through the port “becomes the controller of personal data for the information it collects” (article 35*septies*, § 3; our translation), and ORES warns that once the port is open, it no longer controls the data. A community that hands out P1 boxes and centralises their measurements must obtain each member's prior agreement, tell them what the data will be used for and secure what it collects.

To know live that the shared roof is producing, someone would have to bring the producers' measurements together and pass them on to the group, again with everyone's agreement. A function of this kind is being studied at OptimCE; it is not available today.

## Reading a load curve

A quarter-hour load curve is 96 values per day and per meter. Take the case behind the quarter-hour grid on our home page, which [“Impact tariff and energy communities”](/en/guides/impact-tariff-energy-community/) also uses: a 24 kWp roof in Namur, shared between twelve households that each use 3,500 kWh a year.

<img src="/assets/images/diagrams/community-load-curve-day-en.svg"
     alt="Chart of one day of energy sharing, Tuesday 13 June 2023, for a reference community: a 24 kilowatt-peak solar roof in Namur and twelve households that each use 3,500 kilowatt-hours a year. The horizontal axis covers the 96 quarter-hours of the day, from midnight to midnight; the vertical axis shows the energy of each quarter-hour, from 0 to 5 kilowatt-hours. Roof production is zero at night, starts around 05:15, peaks at 4.72 kilowatt-hours in the 13:00 quarter-hour and fades out around 22:00: 152.9 kilowatt-hours over the day. The twelve households use between 0.68 and 1.73 kilowatt-hours per quarter-hour, with a peak around 07:15 and a higher one around 18:45: 93.9 kilowatt-hours. The green area, the shared energy, is in each quarter-hour the smaller of the two volumes: 50.6 kilowatt-hours. From 08:15 to 18:30 production exceeds consumption, and the surplus, 102.3 kilowatt-hours shown in amber, goes to the grid. In the morning and evening it is the other way round: the remainder, 43.3 kilowatt-hours shown in grey, comes from each household's supplier. Three markers show 07:00, 12:30 and 19:00, the quarter-hours detailed in the article's table. A note recalls that one kilowatt-hour used in a quarter-hour equals 4 kilowatts of average power. Sources: PVGIS for production, a synthetic consumption profile that is not a Synergrid profile."
     width="800" height="520" loading="lazy" decoding="async"
     style="width:100%;height:auto">

**Units first.** Each value is an energy, in kilowatt-hours per quarter-hour, not a power. To get the average power, multiply by four: at 12:30, the roof produces 4.57 kWh in a quarter-hour, or 18.3 kW on average for a 24 kWp installation.

| Quarter-hour | Production | Consumption | Shared | Surplus injected | Remainder from suppliers |
|---|---|---|---|---|---|
| 07:00–07:15 | 0.24 | 1.10 | 0.24 | 0 | 0.86 |
| 12:30–12:45 | 4.57 | 0.99 | 0.99 | 3.58 | 0 |
| 19:00–19:15 | 0.90 | 1.73 | 0.90 | 0 | 0.83 |
| **Whole day** | **152.9** | **93.9** | **50.6** | **102.3** | **43.3** |

*Assumptions: values in kWh for the twelve households together. A 24 kWp roof facing due south, tilted at 35°, in Namur, production from PVGIS v5.3 (SARAH-3) with the weather of 13 June 2023; twelve households of 3,500 kWh a year with a synthetic profile, which is not a Synergrid profile. Shared is the smaller of the two volumes in each quarter-hour, that is, the most a key can allocate; a fixed key can leave an excess with one member while another falls short.*

In the morning and evening, everything the roof injects is shared; at midday, the households consume only a fifth of it. Over the day, sharing covers 54% of consumption, but two thirds of production find no taker. Over the whole of 2023, the same community produces 24,812 kWh, consumes 42,000 and shares 12,624: half of production (50.9%) finds a taker, and sharing covers 30.1% of consumption.

### Reading a member's row

Here, the twelve households have the same profile. At 19:00, a member draws 0.144 kWh; sharing covers 0.075 kWh of it, and the remaining 0.069 kWh make up their residual consumption. In ORES's consumption file, these are the columns “Prélèvement brut” (gross offtake), “Prélèvement couvert par le partage” (offtake covered by sharing) and “Allo Consommation” (residual consumption): Pl = VPC + AL. The representative bills the monthly sum of the offtake covered by sharing; the supplier bills the residual consumption and, in the example in ORES's guide, the grid charges on the whole offtake.

### Four checks before invoicing

- **The number of rows**: 96 per day and per EAN, times the number of iterations. With timestamps in local time, the day the clocks go forward has 92 quarter-hours, the day they go back 100.
- **The member's equation**: offtake = shared volume consumed + residual consumption. A gap often points to a forgotten iteration.
- **The group's equation**: the sum of the shared volumes consumed never exceeds the shared volume; the difference is the surplus.
- **The silences**: a member who is missing, or at zero throughout, points to a meter that is not sending its quarter-hours. Check with the DSO before invoicing.

## Brussels and Flanders

**In Flanders**, Fluvius calculates sharing every month from quarter-hour values; the results are usually available around the 25th of the following month in Mijn Fluvius, where the community's manager downloads a CSV file and where each participant sees only their own volumes. The digital meter must be in “meetregime 3” (metering regime 3). Since 2026, Fluvius reads quarter-hour values by default, but only passes them on to the supplier in cases such as a dynamic contract or sharing. The regulator is the Vlaamse Nutsregulator (formerly VREG).

**In Brussels**, the technical regulation requires Sibelga to send the sharing activity's single point of contact, every month, the offtake, the injections, each participant's shared consumption and each producer's surplus, per quarter-hour or as a monthly total (article 4.70); in practice, an Excel file placed in a private online folder. The electricity ordinance makes remote collection subject to the user's consent (article 26*octies*, § 4), and the P1 port is active by default there. The regulator is Brugel.

## Key takeaways

1. **A community measures nothing itself.** The DSO collects the data, determines the shared volumes and sends them to the representative and the suppliers.
2. **The rhythm is monthly**: by the twelfth working day of the following month at the latest, per quarter-hour and per EAN; at ORES, two CSV files by email.
3. **This flow needs no consent: it is the condition of taking part.** The representative becomes the controller of the data it receives; annex 8 authorises sending the curve to the supplier.
4. **Everything else requires prior, free, specific, informed and unambiguous agreement**: history to simulate a key, P1 box, curves shown to others.
5. **Each member sees their own figures, the group sees aggregates**, and each participant's agreement must say so.
6. **The P1 port measures every second, but only your meter**, and whoever collects its data becomes responsible for them.
7. **A curve is read in kilowatt-hours per quarter-hour**: multiply by four for power, and check that offtake = shared volume consumed + residual consumption.

> ### Test a key on your members' curves
>
> OptimCE is an open-source platform, in alpha, designed to manage an energy community. Its allocation key feature generates and simulates a key from a CSV file at quarter-hour resolution, with one column per consumer and one for production: the curves your members have exported, with their agreement. It works on the files you import, not in real time.
>
> **[See the allocation key feature →](/en/features/allocation-key/)**

## FAQ

### What meter data does the DSO send to an energy community?

In Wallonia, the grid operator sends the sharing representative, for each member and each quarter-hour, the offtake, the shared volume consumed and the residual consumption, the part the supplier bills. It adds each producer's injection, the total shared volume, the surplus and the allocation method used.

The model agreement approved by the CWaPE on 12 October 2023 requires it to make these data available every month, by the twelfth working day of the following month at the latest; it is a best-efforts obligation. At ORES, they are two CSV files sent by email, with one row per quarter-hour, per EAN code and per iteration of the key.

### Do I have to consent to my data going to the community?

Not for the sharing flow itself. The Walloon decree requires the DSO to send the representative each participant's metering data, and the model agreement states that any participation requires the collection and use of load curves. You cannot stay in the sharing and refuse this flow. The participant does, however, sign annex 8, which among other things authorises sending their curve to their supplier.

Anything outside this framework requires prior, free, specific, informed and unambiguous agreement: the history requested to simulate a key, a box on the P1 port, individual curves shown to other members.

### Can other members see my consumption?

Not by default. The DSO sends each member's data to the representative, not to the other members, and each participant's agreement must settle privacy and the passing of data between participants. The Data Protection Authority points out that a quarter-hour curve makes it possible to infer a household's behaviour.

A prudent practice is to show each member their own figures, and the group only aggregates. A ranking by name or an individual curve is only shown with the person's explicit agreement. When the community has a single producer, that producer's production is, by construction, visible to all as a total.

### How do I access my smart meter data?

Through your grid operator's portal, free of charge. The order of 1 December 2022 requires twenty-four months of history, intraday detail on explicit request and an export to a spreadsheet. At ORES, you request the quarter-hour view in the myORES customer area; RESA offers a quarter-hour profile in MyRESA, AIEG and AIESH in MyConso.

These are also the data a community will ask you for to simulate a key before sharing starts: you can export them and hand them over, with a written agreement for that use.

### Can the P1 port be used for energy sharing?

Not for the calculation. The P1 port sends a reading every second, but it only shows your own meter: neither the production of the shared roof nor the share allocated to you. Sharing volumes are those the DSO determines and sends every month, and the invoice is based on them.

In Wallonia, the port is switched off by default and is switched on free of charge at simple request to the DSO. Whoever collects data through this port becomes responsible for them: a community that hands out P1 boxes must obtain each member's prior agreement.

### How long are sharing data kept?

In Wallonia, the CWaPE and the grid operator keep the data linked to sharing five years after the activity stops. Those of a participant who has left the sharing are deleted five years after their departure was notified.

The decree sets no period for the representative. As controller of the data it receives, it must set one itself and announce it to members, as the GDPR requires. The meter, for its part, keeps the load curves of the last ten days, the daily readings of forty days and the monthly readings of thirteen months, readable remotely.

## Sources

- [Wallex — Decree of 12 April 2001 on the organisation of the regional electricity market, coordinated text](https://wallex.wallonie.be/sites/wallex/contents/acts/19/19848.html) (in French) — source for the collection of metering data reserved to the DSO (article 11), the near-real-time output port switched off by default (article 35*bis*, § 1, § 2 and § 4), the default metering regime and free consultation (article 35*ter*, § 2 and § 3), the DSO's status as controller, the prior-agreement rule, the trading bans and the responsibility of a third party reading the port (article 35*septies*, § 2 and § 3), the content required in the participant's agreement (article 35*duodecies*, § 2), the five-year retention (article 35*quaterdecies*, § 3) and the DSO's transmissions to the representative, the suppliers and the CWaPE (article 35*sexdecies*, § 2 and § 3). Accessed on 22 November 2026.
- [CWaPE — Decision CD-23j12-CWaPE-0818 approving the model sharing agreements](https://cwape.be/sites/default/files/cwape-documents/2023.10.12-0818-D%C3%A9cision%20approbation%20conventions-types%20partage%20-%20avec%20annexes.pdf) (in French) — decision of 12 October 2023, annexes included. Source for the definition of the seven quantities and their formulas (article 6.2.1), the twelfth-working-day deadline and the best-efforts obligation (article 6.2.2), the collection of load curves as a condition of taking part (article 6.1.3), the complaints procedure (article 6.1.4) and the split of processing responsibilities (article 9.4). Accessed on 22 November 2026.
- [CWaPE — Explanatory guide to the electricity sharing form](https://www.cwape.be/documents/download/5610) (in French) — July 2025 version. Source for the metering conditions (communication function activated, regime 3 requested from the supplier, annex 8 authorisation, point 9.1) and for the data protection statement: basis in article 6(1)(e) of the GDPR, joint controllership of the DSOs and the CWaPE, five-year retention. Accessed on 22 November 2026.
- [CWaPE — Annex 8: sworn declaration of persons taking part in the sharing](https://www.cwape.be/documents/download/5612) (in French) — version of 12 October 2023. Source for the mandate given to the representative and the authorisation to send quarter-hourly metering data to the supplier until regime 3 is in place. Accessed on 22 November 2026.
- [CWaPE — Evaluation report on energy communities and sharing (CD-25b20-CWaPE-0109)](https://www.cwape.be/sites/default/files/cwape-documents/2025.02.20-0109-Rapport%20%C3%A9valuation%20CE%20et%20partage.pdf) (in French) — report of 20 February 2025. Source for the current rhythm (the past month plus twelve working days at most) and the separate channel, outside market processes, through which shared volumes reach suppliers. Accessed on 22 November 2026.
- [CWaPE — Decision CD-26h27-CWaPE-1284 approving the technical regulation for electricity distribution](https://www.cwape.be/sites/default/files/cwape-documents/CD-26h27-CWaPE-1284-D%C3%A9cision%20d%27approbation%20du%20RTDE%20%26%20annexes_site.pdf) (in French) — decision of 27 August 2026. Source for articles IX.6 (move to the MIG once the MIG allows it), IX.7 (quarter-hourly curve and monthly aggregate, application programming interface) and IX.17 (corrections over twelve months and how they are allocated). Decision [published in the Belgian Official Gazette on 20 November 2026](https://www.ejustice.just.fgov.be/cgi/article_body.pl?language=fr&caller=summary&pub_date=2026-11-20&numac=2026007520), in force on 30 November 2026 according to the page [Règlements et contrats](https://www.cwape.be/node/161) (regulations and contracts). Accessed on 22 and 24 November 2026.
- [CWaPE — Qui facture l'électricité partagée ?](https://www.cwape.be/node/6059) (in French) — a question in the regulator's FAQ (who invoices shared electricity), source for the principle that sharing invoices are based on the consumption data received from the grid operator. Accessed on 22 November 2026.
- [Wallex — Walloon Government order of 1 December 2022 on smart meters](https://wallex.wallonie.be/eli/arrete/2022/12/01/2022034594) (in French) — article 4, source for the minimum content of the portal: twenty-four months, intraday detail on explicit request, export to a spreadsheet. Accessed on 22 November 2026.
- [ORES — Explanatory guide to invoicing for the representative of an energy-sharing activity](https://media.ores.be/ores-cms/vi2eqxam/ores_guide_explicatif_facturation_representant_partage_energie_fr.pdf) (in French) — guide of July 2024. Source for the description of the two CSV files, the column names, the row per iteration, the sum of iterations per EAN and per period, and the example in which the supplier bills grid charges on the whole offtake. Accessed on 22 November 2026.
- [ORES — Energy sharing in practice](https://www.ores.be/particulier/en-pratique) (in French) — source for the monthly sending of the two CSV files by email, and for ORES's statement that the data of the myORES quarter-hour view do not go up to the supplier, which has to request them from ORES itself. Accessed on 22 November 2026.
- [ORES — myORES FAQ](https://www.ores.be/faq/myores) (in French) — source for the activation of the quarter-hour view being passed on to the supplier, the interim bill some suppliers may then issue, and its lack of effect on the annual bill and on compensation. Accessed on 22 November 2026.
- [ORES — Sharing data with energy service providers (API)](https://media.ores.be/ores-cms/ahgjzcld/utilisation-des-api-tpda-ores.pdf) (in French) — document of September 2025. Source for delegated access: daily and quarter-hourly volumes, a history of three years at most, consent given by the customer in myORES. Accessed on 22 November 2026.
- [CWaPE — Annex TNP-E0: 2026 non-periodic tariffs, electricity, harmonised tariffs](https://www.cwape.be/sites/default/files/cwape-documents/ANNEXE%20TNP-E0%20-%20Tarifs%20non-p%C3%A9riodiques%202026%20-%20Electricit%C3%A9%20-%20Tarifs%20harmonis%C3%A9s%20et%20uniformis%C3%A9s.pdf) (in French) — source for free activation and deactivation of the P1 port in 2026. Accessed on 22 November 2026.
- [Fluvius — Digital Metering System eMUCS-P1, version 2.1](https://partner.fluvius.be/sites/fluvius/files/2025-09/digital-metering-system-emucs-p1-v2-1.pdf) — Belgian specification of the P1 port, based on DSMR 5.0.2: telegram updated every second and list of the values published. Accessed on 22 November 2026.
- [Privacy Commission — Opinion no. 23/2018](https://www.autoriteprotectiondonnees.be/publications/avis-n-23-2018.pdf) (in French) — opinion of 21 March 2018, published on the site of the Data Protection Authority that succeeded the Commission, on the preliminary draft decree on smart meters, source for the sentence on “consent” through a clause in general terms and conditions. Accessed on 22 November 2026.
- [Data Protection Authority — Opinion no. 132/2023](https://www.autoriteprotectiondonnees.be/publications/avis-n-132-2023.pdf) (in French) — opinion of 8 September 2023, source for the quote on the potentially sensitive data that can be inferred from smart meters. Accessed on 22 November 2026.
- [Data Protection Authority — Opinion no. 130/2025](https://www.autoriteprotectiondonnees.be/publications/avis-n0-130-2025.pdf) (in French) — opinion of 3 December 2025, source for the current Brussels rule: article 26*octies*, § 4 of the electricity ordinance makes remote collection subject to the user's consent. Accessed on 22 November 2026.
- [EUR-Lex — Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — articles 5(1)(c) (data minimisation), 6(1)(e) (task carried out in the public interest), 7(3) (withdrawal of consent) and 28 (processor). Accessed on 22 November 2026.
- [EUR-Lex — Directive (EU) 2019/944](https://eur-lex.europa.eu/eli/dir/2019/944/oj) — article 20, source for the customer's access, at no extra cost, to their unvalidated near-real-time data. Accessed on 22 November 2026.
- [EUR-Lex — Implementing Regulation (EU) 2023/1162](https://eur-lex.europa.eu/eli/reg_impl/2023/1162/oj) — article 2, definitions of eligible party, which includes renewable energy communities and citizen energy communities, and of the authorisation given by the customer. Accessed on 22 November 2026.
- [Fluvius — Frequently asked questions on energy sharing](https://www.fluvius.be/nl/veelgestelde-vragen/energiedelen-persoon-aan-persoonverkoop-energiegemeenschappen) (in Dutch) — source for the monthly calculation, the results available around the 25th of the following month in Mijn Fluvius, and the “meetregime 3” requirement. Accessed on 22 November 2026.
- [Fluvius — Kwartierwaarden](https://www.fluvius.be/nl/factuur-en-tarieven/kwartierwaarden) (in Dutch) — page on quarter-hour values, source for reading them by default since 2026 and passing them to the supplier only in the case of a dynamic contract or sharing. Accessed on 22 November 2026.
- [Fluvius — Protocol energiedelen, persoon-aan-persoonverkoop en verkoop in gebouwen, version 3.2](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf) (in Dutch) — protocol on energy sharing, peer-to-peer selling and selling within buildings. Source for the CSV download options for the manager and for each participant's visibility being limited to their own volumes. Accessed on 22 November 2026.
- [Brugel — Technical regulations for electricity and gas, version as of 1 January 2025](https://brugel.brussels/publication/document/notype/2024/fr/Reglements-techniques-2025.pdf) (in French) — article 4.70, source for the data Sibelga sends every month to the single point of contact of a sharing activity. Accessed on 22 November 2026.
- [Sibelga — Energy sharing invoicing method](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methode-de-facturation) and [The smart meter's P1 port](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents/le-port-p1-du-compteur-intelligent) (in French) — source for the monthly Excel file placed in an online folder, the quarter-hour option and the P1 port active by default in Brussels. Accessed on 22 November 2026.
- [JRC — PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/fr/) — the European Commission tool that provides the production values of the reference case (version 5.3, SARAH-3 database, 2023 weather). The consumption profile is synthetic and documented in the site's source code; it is not a Synergrid profile. Accessed on 22 November 2026.
