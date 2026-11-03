---
layout: post
title: "Smart meters in Wallonia: the complete guide"
date: 2026-11-02 06:00:00 +0100
author: "Eric from OptimCE"
excerpt: "Since January 2026, every supply point in Wallonia must get a smart meter by the end of 2029, and you can no longer refuse the installation. This guide explains how to ask for one early from each of the five Walloon grid operators, what it costs, what switching off its communication costs, and what it opens up: the Impact tariff, the P1 port, your quarter-hour data and energy sharing."
description: "Smart meters in Wallonia: who gets one, how to request one from your DSO, what it costs, how to switch off communication and what it unlocks."
tags: [guide, community]
lang: en
ref: smart-meter-wallonia
pillar: facture-electricite
permalink: /en/guides/smart-meter-wallonia/
faq:
  - q: "How do I request a smart meter in Wallonia?"
    a: "Ask your distribution system operator (DSO), not your supplier. ORES has an online form to replace your meter with a smart one; RESA has a “Demander un compteur communicant” section on its website; AIEG asks you to use its request form and to state in the remarks that you want a smart meter. AIESH and REW describe no online procedure: contact their customer service. A Walloon government order of 1 December 2022 sets what follows: an acknowledgement within ten days, an offer within the next ten days, and installation no later than four months after your complete request. Replacing a conventional meter with a smart meter is free on all five Walloon networks."
  - q: "Is a smart meter mandatory in Wallonia?"
    a: "Yes, for the installation. Since the decree of 19 December 2025, in force on 9 January 2026, the DSO installs a communicating meter at every supply point, unless access is impossible, installation is technically impossible or the cost is not economically reasonable, and it must reach 100% smart meters on its network by 31 December 2029. ORES, RESA and REW state that you can no longer refuse the replacement. What remains your choice is the communication function: you can refuse its activation or ask for it to be switched off, with consequences that the decree lists."
  - q: "Can I switch off the communication function, and what does it cost?"
    a: "Yes, on request to your DSO. Switching it off is free if you ask within fifteen calendar days of installation; after that, it costs 128.33 € excluding VAT in 2026, the same harmonised fee at all five Walloon DSOs. Switching it back on is free. At RESA, the request is made with a form sent to desacom@resa.be and cannot be handled on the day of installation. The consequences are significant: manual meter readings, no energy sharing or peer-to-peer trading, no prepayment, no flexibility services, and a compensation claim for an inverter that tripped becomes inadmissible. Anyone who has bought a production installation of 10 kVA or less since 1 January 2024 can only refuse activation."
  - q: "How do I activate the P1 port on my smart meter?"
    a: "In Wallonia, the meter's output port is switched off by default and is switched on at your simple request to the DSO. It is free: the 2026 tariff grids list activating and deactivating the P1 port among remote operations, free and harmonised across Wallonia. At ORES, you request it by phone on 078/15.78.01; the port is only activated with your explicit authorisation and is connected with an RJ12 cable. RESA, AIEG, AIESH and REW use a form. According to the Belgian meter specification, the P1 port provides instantaneous values every second; you then need a P1 module or an energy management app to read them."
  - q: "Do I need a smart meter for the Impact tariff?"
    a: "Yes. The CWaPE, the Walloon regulator, restricts the Impact tariff to connections of 56 kVA or less with a smart meter whose communication function is active. It is not automatic: you ask your supplier for it. The CWaPE refused to impose quarter-hour metering (regime R3) for this tariff, which must also work under regime R1, but some suppliers require R3 in their terms. A meter whose communication is switched off therefore rules out the Impact tariff."
  - q: "Do I need a smart meter to join an energy community?"
    a: "You need a meter that measures consumption and injection separately and sends quarter-hour data: the Walloon electricity decree requires it from every participant in energy sharing. For a household, that means a smart meter in practice; ORES also accepts an AMR meter, usually found on larger connections. The communication function must also be active and your data must be sent per quarter-hour, regime R3, which you ask your supplier for. If you do not have a smart meter yet, ask your DSO: the replacement is free and must happen within four months."
---

In Wallonia, every home must have a smart meter by the end of 2029. Since January 2026 you can no longer refuse the installation, but you can still switch off its communication, and that choice closes several doors. This guide answers three practical questions: when you will get one, how to get it sooner and what it costs. It also covers what the meter lets you do, and why energy sharing cannot work without it.

This article does not repeat what other guides on this site already cover. The Impact tariff calculation for a community member is in [“Impact tariff and energy communities”](/en/guides/impact-tariff-energy-community/), and the quarter-hour rule in [“Local electricity: the short-circuit guide”](/en/guides/local-electricity-short-circuit-guide/). Dynamic contracts, which also need this meter, are covered in [“Which electricity tariff to choose in Belgium?”](/en/guides/choose-electricity-tariff-belgium/).

**The rules described here are Walloon.** Brussels and Flanders are summarised at the end.

## What a smart meter is, and what it is not

In Wallonia the official term is *compteur communicant*, a communicating meter. It is an electronic two-way meter: it measures separately the electricity you take from the grid and the electricity you feed into it. It records these data by time band and can send them remotely to the distribution system operator (DSO).

Two things are often confused:

- **the meter**, which measures and displays;
- **its communication function**, which sends the data remotely. It is switched on at installation, but you can refuse it or have it switched off (see below).

Even when communication is active, the meter does not send everything to the market. The electricity decree is explicit: by default, “seuls les index du compteur et les volumes d'énergie sont utilisés dans les processus de marché” (only the meter readings and energy volumes are used in market processes), and they are passed to suppliers once a year (article 35*ter* § 2). Your quarter-hour consumption curve only leaves the DSO if you ask for it.

The technical regulation approved by the CWaPE on 27 August 2026 calls these levels “metering regimes”:

| Regime | When it applies | What the DSO sends to the market |
|---|---|---|
| R0 | communication function switched off | nothing remotely: readings are taken on site |
| R1 | default, communication active | start and end readings, volumes per time band; once a year, or monthly on request |
| R3 | on explicit request, through your supplier | also the quarter-hour load curve, at least monthly |

*Assumptions: Walloon technical regulation for electricity distribution networks, article V.45bis, in the version approved by the CWaPE on 27 August 2026. Suppliers also call R3 “SMR3”; it is mandatory for a dynamic-price offer and for energy sharing.*

A smart meter is not the only remotely read meter either. Larger connections often have an AMR meter, read remotely per quarter-hour, which the energy-sharing rules also accept. For a household, the smart meter is the normal route.

## Who gets one, and when

Until 2025, the Walloon rollout targeted priority groups. The decree of 19 December 2025, in force since 9 January 2026, dropped that approach. Article 35 of the electricity decree now says that the DSO installs a communicating meter “à chaque point de fourniture” (at every supply point), unless access is impossible, installation is technically impossible or it is not economically reasonable. It sets the deadline: 100% smart meters on every network by 31 December 2029.

There is therefore no legal order of priority among households any more: each DSO plans the replacements in its investment plan, usually municipality by municipality. ORES and RESA let you check the planned date online, ORES on its “Placement du compteur” page, RESA from your EAN code. Three situations speed things up:

- **A new production installation of 10 kVA or less.** Since 1 January 2024, a smart meter is installed systematically when it is commissioned, as explained in [our guide to solar for tenants](/en/guides/tenant-solar-without-roof-guide/).
- **Prepayment.** The old card-based budget meters have been replaced by smart meters with a prepayment function, as the card top-up platform closed on 1 January 2026. At the end of 2025, 98.8% of the 59,294 active electricity prepayment meters were smart meters, with a few still to be replaced at RESA (CWaPE, 2025 report on public service obligations).
- **Your request.** You do not have to wait for your turn (next section).

How far has the rollout got? At the end of 2025, more than 537,000 electricity smart meters were installed on Walloon networks, about 28% of all meters (CWaPE, 2025 annual report). More than two in three are therefore still to be installed in four years. Among the DSOs, only RESA publishes a recent figure of its own: 84,862 smart meters at the end of 2024, or 18.42% of its meters (2024 annual report). AIEG, AIESH and REW publish no count of their own.

## Requesting a smart meter: procedure and cost by DSO

You can request a smart meter without waiting for the schedule. The Walloon government order of 1 December 2022 sets the procedure: the DSO acknowledges receipt within ten days, sends an offer within the next ten days (estimated date, meter functions, any cost), and installation “n'excède pas quatre mois” (does not exceed four months) after your complete request (article 2 §§ 1–3).

You ask the DSO, never the supplier. **Check first which one is yours**: [the “Find my DSO” tool](/en/tools/find-my-dso/) finds it from your postcode, and [the list by municipality](/en/tools/find-my-dso/municipalities/) covers all 565 Belgian municipalities.

| DSO | Requesting a smart meter | Activating the P1 port | Switching off communication after 15 days |
|---|---|---|---|
| ORES | online form “compteur intelligent”; planned date on the “Placement du compteur” page | by phone, 078/15.78.01; free | 128.33 € excl. VAT |
| RESA | “Demander un compteur communicant” section; planned date from your EAN code | “port client” form; free | form to desacom@resa.be; 128.33 € excl. VAT |
| AIEG | request form, writing “compteur communicant” in the remarks | form sent to stech@aieg.be; free | 128.33 € excl. VAT |
| AIESH | no online procedure: customer service, 060/45.91.60 | “Activation/désactivation port P1” form; free | 128.33 € excl. VAT |
| REW | no online procedure: customer service | activation form; free | 128.33 € excl. VAT |

*Assumptions: procedures taken from the five DSOs' websites on 2 November 2026. Amounts from the 2026 non-periodic tariffs approved by the CWaPE (ORES, RESA, AIESH, REW) and from the grid harmonised across Wallonia (AIEG). Replacing a conventional meter with a smart meter is free everywhere; extra work (moving the meter, increasing capacity) is still charged on quotation.*

Two points on cost. The meter itself is borne by the DSO, “qui en est le propriétaire” (which owns it), under the same order (article 2 § 5). And the CWaPE confirms in its 2025 annual report that on low voltage, replacing one type of meter with another “est devenu gratuit” (has become free), as have all remote operations and activating the communication function. ORES adds that the box and the circuit breaker fitted with the meter are also free.

## Is a smart meter mandatory? Can you refuse one?

**The installation: no.** ORES puts it plainly: “il n'est donc plus possible de refuser la pose du compteur communicant” (it is no longer possible to refuse the installation). RESA and REW say the same.

**The communication: yes.** The decree provides that the grid user “peut refuser l'activation de la fonction communicante du compteur ou demander la désactivation de celle-ci” (may refuse activation of the communication function or ask for it to be switched off; article 35 § 3). Switching it off is free if you ask within fifteen calendar days of installation. After that, it costs 128.33 € excluding VAT in 2026, the same at all five DSOs. Switching it back on is free. At RESA, it cannot be done on the spot on installation day: you must send back the form.

One exception: if you have commissioned a production installation of 10 kVA or less since 1 January 2024, you can only refuse activation (order of 1 December 2022, article 3 § 1).

The DSO must inform you of the consequences, which the decree lists:

1. manual meter readings whenever a market process requires one;
2. no technical possibility of taking part in energy sharing;
3. no technical possibility of peer-to-peer trading;
4. no possibility of providing flexibility services to the grid;
5. no other market activity that needs daily data transmission;
6. no prepayment function;
7. a compensation claim for an inverter that tripped becomes inadmissible, as voltage quality can no longer be checked.

RESA adds that for a prosumer still under net metering (“compensation”), switching off triggers an interim bill on the date communication stops, so the annual compensation is split into two periods. The P1 port is switched off too.

If your concern is privacy, there is a middle way: keep communication active, in regime R1. The DSO then only sends your readings and volumes to the market, once a year, and nothing per quarter-hour unless you ask. A third party can only read your data with your prior, free, specific, informed and unambiguous consent (electricity decree, article 35*septies* § 3).

## What it unlocks

### The Impact tariff

The [Impact tariff](/en/guides/impact-tariff-energy-community/), in force since 1 January 2026, bills the network in three time bands. The CWaPE restricts it to customers with a smart meter whose communication function is active and a connection of 56 kVA or less. It is not automatic: you ask your supplier for it.

The CWaPE refused to impose regime R3 for this tariff, which must work “tant en régime de comptage R1 qu'en régime de comptage R3” (under both R1 and R3; press kit of 3 November 2025). Some suppliers nevertheless require R3 in their terms. Read your offer's conditions before asking for the switch.

### Your data, free of charge

The DSO must allow “la consultation libre et gratuite” (free consultation) of your consumption data (decree, article 35*ter* § 3). Its platform shows them by year, month, week and day and, on explicit request, by quarter-hour, for the last 24 months, with a spreadsheet export (order of 1 December 2022, article 4).

In practice:

- **at ORES**, the myORES account shows the previous day's data with a delay of about 72 hours; the quarter-hour view is switched on in the portal, and this “est transmise à votre fournisseur d'énergie” (is passed to your supplier), which may issue an interim bill;
- **at RESA**, the MyRESA account shows your consumption and injection profile quarter-hour by quarter-hour;
- **at AIESH**, it is Arewal's MyConso platform.

These data are enough to see when your consumption happens, and so what shifting a use or sharing energy would change.

### The P1 port

The meter also provides near real-time information on a local output port, the P1 port. It is switched off by default and is switched on at the user's simple request to the DSO (decree, article 35*bis* § 4). Activation is free at all five DSOs. At ORES, it is only activated “après avoir reçu votre autorisation explicite” (after your explicit authorisation), and it connects “via un câble RJ12”.

The Belgian meter specification (eMUCs-P1) states that the P1 port “provides every second instantaneous values”. According to Sibelga, it only communicates locally. To use it, you need a P1 module or an energy manager that reads these values and, for example, starts an appliance when your panels feed into the grid. Your data only leave your home if you plug in a device connected to the internet.

## Why energy sharing requires one

Energy sharing allocates the electricity fed in by an installation among the participants, quarter-hour by quarter-hour. The technical regulation says so: allocation is done “sur une base quart horaire” (on a quarter-hour basis; article IX.14). To do this, the DSO needs each participant's consumption at that resolution. That is why the electricity decree requires every participant to have a meter that measures consumption and injection separately and sends data aggregated per imbalance settlement period, in other words per quarter-hour (article 35*octies* § 3). The rule applies to sharing within one building (article 35*nonies*) as well as to energy communities (article 35*quaterdecies*).

In practice, three conditions:

1. **a smart meter**, or an AMR meter: ORES states that a two-way meter, smart or AMR, “doit être installé chez tous les participants” (must be installed at every participant's home);
2. **the communication function active**: switching it off makes sharing technically impossible (decree, article 35 § 3);
3. **regime R3**, which participants activate “en faisant la demande à leur fournisseur d'énergie” (by asking their supplier; ORES). The technical regulation makes it mandatory for sharing.

If you want to join a community and do not have a smart meter yet, ask your DSO as soon as the project takes shape: it is the longest step, up to four months. The next steps are in [“Join an energy community in Wallonia”](/en/guides/join-energy-community-wallonia/), and the forms of sharing in [“Energy self-consumption in Belgium”](/en/guides/energy-self-consumption-belgium/).

The meter only opens the door. Sharing only lowers the energy component of the shared kilowatt-hours: network costs, taxes and levies remain due on all your consumption, with the sole exception of the reduction granted to sharing within one building.

## Brussels and Flanders

**In Brussels**, Sibelga started its large-scale rollout in October 2023 and aims to replace 80% of electricity meters by 2030. Replacement is free, and you can request a smart meter without waiting for the schedule. Some cases require you to request one yourself: production (solar panels), a charging point, a battery and energy sharing. The P1 port is switched on by default ([Sibelga](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents/quand-recevrai-je-un-compteur-intelligent)).

**In Flanders**, the digital meter is mandatory: “je kan de plaatsing van een digitale meter niet weigeren” (you cannot refuse it). A refusal can lead to legal proceedings, with formal-notice fees of 298.76 €, then 322.59 € ([Fluvius](https://www.fluvius.be/nl/meters-en-meterstanden/digitale-meter/weigeren)). The P1 port is activated online in Mijn Fluvius, within 72 hours at most.

## Key takeaways

1. **Every supply point in Wallonia must have a smart meter by 31 December 2029**; there have been no priority groups since the decree of 19 December 2025.
2. **You can no longer refuse the installation, but you can refuse the communication**: free within fifteen days, then 128.33 € excluding VAT in 2026, with consequences listed in the decree.
3. **You can request one without waiting** from your DSO: free replacement, installation within four months at most.
4. **By default, only your readings go to the supplier, once a year**; quarter-hour data (R3) must be requested explicitly.
5. **The P1 port is free** and gives your values every second, at home, without sending them to the grid.
6. **No energy sharing without an active smart meter in regime R3** (or an AMR meter); no Impact tariff without active communication.

## FAQ

### How do I request a smart meter in Wallonia?

From your DSO: online form at ORES, a dedicated section at RESA, a form with a remark at AIEG, customer service at AIESH and REW. The replacement is free and must take place no later than four months after your complete request.

### Is a smart meter mandatory in Wallonia?

The installation is: the DSO must fit one at every supply point by the end of 2029, and you can no longer refuse it. You can, however, refuse or switch off its communication function.

### Can I switch off the communication function, and what does it cost?

Yes. It is free within fifteen days of installation, then 128.33 € excluding VAT in 2026; switching it back on is free. Without communication, you lose energy sharing, prepayment and the Impact tariff, and readings are taken by hand.

### How do I activate the P1 port on my smart meter?

Ask your DSO: by phone at ORES (078/15.78.01), by form at the others. It is free. You then need a P1 module or an energy manager, connected with an RJ12 cable.

### Do I need a smart meter for the Impact tariff?

Yes, with the communication function active and a connection of 56 kVA or less. You ask your supplier for the tariff; the CWaPE does not impose regime R3, but some suppliers do.

### Do I need a smart meter to join an energy community?

Yes, or an AMR meter, with communication active and regime R3 requested from your supplier. Without a smart meter, ask your DSO at the start of the project.

## Sources

- [Wallex — Decree of 12 April 2001 on the organisation of the regional electricity market, consolidated version](https://wallex.wallonie.be/eli/loi-decret/2001/04/12/2001027238) — article 35 § 1 (installation at every supply point, exceptions, 100% by 31 December 2029, wording of the decree of 19 December 2025) and § 3 (refusing or switching off the communication function and its seven consequences), article 35*bis* §§ 1 and 4 (near real-time information, output port off by default), article 35*ter* §§ 2 and 3 (default metering regime, annual transmission, free consultation), article 35*septies* § 3 (prior consent for third-party access), articles 35*octies* § 3, 35*nonies* and 35*quaterdecies* (meter required for sharing). Version in force on 2 November 2026, accessed on 2 November 2026.
- [Wallex — Decree of 19 December 2025 laying down various provisions on energy](https://wallex.wallonie.be/files/pdfs/22/124958_D%C3%A9cret_portant_dispositions_diverses_en_mati%C3%A8re_d'%C3%A9nergie_09-01-2026-.pdf) — article 26, rewriting article 35 of the electricity decree, in force on 9 January 2026. Accessed on 2 November 2026.
- [Wallex — Walloon government order of 1 December 2022 on communicating meters](https://wallex.wallonie.be/eli/arrete/2022/12/01/2022034594) — article 2 (request, acknowledgement, offer, installation within four months, meter cost borne by the DSO), article 3 § 1 (producers of 10 kVA or less since 1 January 2024), article 4 (consultation platform, 24 months, export). Accessed on 2 November 2026.
- [CWaPE — Decision CD-26h27-CWaPE-1284 approving the technical regulation for electricity distribution networks in Wallonia](https://www.cwape.be/sites/default/files/cwape-documents/CD-26h27-CWaPE-1284-D%C3%A9cision%20d%27approbation%20du%20RTDE%20%26%20annexes_site.pdf) — article V.45*bis* (regimes R0, R1, R3; R3 mandatory for sharing and dynamic-price offers), article IX.14 (quarter-hour allocation). Document of 27 August 2026, accessed on 2 November 2026.
- [CWaPE — 2025 general annual report](https://www.cwape.be/sites/default/files/cwape-documents/2026.07.03-RAG%202025.pdf) — more than 537,000 electricity smart meters at the end of 2025, about 28% of meters; free meter replacement, remote operations and activation; switching off charged more than two weeks after installation. Report of 3 July 2026, accessed on 2 November 2026.
- [CWaPE — 2025 specific annual report on public service obligations](https://www.cwape.be/sites/default/files/cwape-documents/2026.07.03-RAS%20OSP%202025.pdf) — end of budget meters on 1 January 2026, 59,294 active prepayment meters of which 98.8% are smart meters. Report of 3 July 2026, accessed on 2 November 2026.
- [CWaPE — Incentive tariff FAQ](https://cwape.be/sites/default/files/cwape-documents/2024.07.15-Tarification%20incitative-FAQ.pdf) — smart meter with active communication, 56 kVA or less. Document of 15 July 2024. [CWaPE — Press kit on distribution tariffs](https://www.cwape.be/sites/default/files/cwape-documents/2025.11.03-Tarifs%20distribution_dossier%20de%20presse%20-%20final.pdf) — refusal to impose R3 for the Impact tariff, definition of R1 and R3. Document of 3 November 2025. Accessed on 2 November 2026.
- 2026 non-periodic tariffs approved by the CWaPE: [ORES, decision CD-26c26-CWaPE-1246, annex 8](https://www.cwape.be/sites/default/files/cwape-documents/2026.03.26-1246-ORES-D%C3%A9cision%20TPDA%20%26%20Rectification%20TNP%202025-29%20%2B%20annexes.pdf), [RESA](https://cwape.be/sites/default/files/cwape-documents/ANNEXE%20TNP-E0_B%20-%20RESA_ELEC_TARIFS%20NP_2026_0.pdf), [AIEG, decision of 19 December 2024](https://cwape.be/sites/default/files/cwape-documents/2024.12.19-1026-AIEG-D%C3%A9cision%20approbation%20TNP%202025-2029%2Bannexes.pdf), [AIESH, decision of 19 December 2024](https://cwape.be/sites/default/files/cwape-documents/2024.12.19-1027-AIESH-D%C3%A9cision%20approbation%20TNP%202025-2029%2Bannexes.pdf) and [REW](https://www.rew.be/document/download/191/fdd71d0b-f3ed-4a70-8731-6eb4dccc1610/118) — remote operations including the P1 port free, switching off communication 128.33 € excluding VAT more than fifteen days after installation, switching back on free, replacing an electromechanical meter with a smart meter free. Accessed on 2 November 2026.
- ORES — [Meters (FAQ)](https://www.ores.be/faq/les-compteurs), [Customer port](https://www.ores.be/particulier/port-client/), [The smart meter](https://www.ores.be/particulier/compteur-communicant-fonctionnement), [myORES (FAQ)](https://www.ores.be/faq/myores) and [Starting energy sharing](https://www.ores.be/particulier/demarrer-partage-cer-cec) — request form, free replacement, installation can no longer be refused, P1 by phone, RJ12 cable, rollout by the end of 2029, quarter-hour view and 72-hour delay, smart or AMR meter and “régime 3” for sharing. Undated pages, accessed on 2 November 2026.
- [RESA — The smart meter](https://www.resa.be/fr/ma-situation/mon-compteur/compteur-communicant/) — request, replacement date from the EAN code, free replacement, switching off by form, consequences, quarter-hour data in MyRESA. [RESA — 2024 annual report](https://cms.resa.be/app/uploads/2025/09/Rapport-annuel-2024.pdf) — 84,862 smart meters at the end of 2024, 18.42% of meters. Accessed on 2 November 2026.
- [AIEG — Smart meter](https://www.aieg.be/compteur-communicant-ou-smart-metering/) and [P1 port](https://www.aieg.be/le-port-p1/); [AIESH — Smart meters](https://aiesh.be/consommateurs/compteurs_communicants/); [REW — FAQ](https://www.rew.be/faq) — request and P1 activation forms, MyConso platform, replacement can no longer be refused and cost of switching off. Accessed on 2 November 2026.
- [Fluvius — eMUCs-P1, P1 port specification, version 1.7.1](https://partner.fluvius.be/sites/fluvius/files/2025-09/smart-metering-system-emucs-p1-v1-7.pdf) — instantaneous values every second, interface based on the Dutch DSMR P1 specification. Document of 5 September 2022, accessed on 2 November 2026.
- [Sibelga — When will I get a smart meter?](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents/quand-recevrai-je-un-compteur-intelligent), [Smart meters](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents) and [The P1 port](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents/le-port-p1-du-compteur-intelligent); [Fluvius — Refusing a digital meter](https://www.fluvius.be/nl/meters-en-meterstanden/digitale-meter/weigeren) and [Make your meter smart](https://www.fluvius.be/nl/meters-en-meterstanden/maak-je-meter-slim) — Brussels and Flemish rollout, free replacement, mandatory cases, P1 port. Accessed on 2 November 2026.
