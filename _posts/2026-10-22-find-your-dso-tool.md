---
layout: post
title: "New tool: find your DSO in Belgium"
date: 2026-10-22 06:00:00 +0200
author: "Eric from OptimCE"
excerpt: "Who runs the electricity and gas network in your municipality? Our free tool answers from your postcode, for all 565 Belgian municipalities, in your browser and without an account."
description: "Find your distribution network operator for electricity and gas from your postcode: our free tool covers all 565 Belgian municipalities, no account."
tags: [app, announcement, news]
lang: en
ref: dso-tool-launch
permalink: /en/news/2026/10/22/find-your-dso-tool/
faq:
  - q: "Is there a free tool to find your DSO in Belgium?"
    a: "Yes. OptimCE's “Find your DSO” tool is free and needs no account: you enter your postcode and it shows the distribution system operator (DSO) for electricity and the one for natural gas in your municipality. It covers all 565 municipalities in Belgium, in Brussels, Flanders and Wallonia."
  - q: "Is my postcode stored when I use the tool?"
    a: "No. The search runs in your browser, which loads all of the tool's data once: your postcode is not sent to any server. It only appears in the page address so that you can copy a link to the result, and the “Report an error” email does not contain it. Our audience measurement receives only the region and the operators found."
  - q: "Why does the tool ask for my municipality or my section of the municipality?"
    a: "Because your postcode is not always enough. Three postcodes cover two municipalities: 1040 (Brussels and Etterbeek), 1050 (Brussels and Ixelles) and 1804 (Vilvoorde and Zemst). In Baarle-Hertog, the gas operator depends on the section of the municipality: Enexis, a Dutch operator, except in Zondereigen, served by Fluvius Kempen. The tool then asks before showing the result."
  - q: "What should I do if the tool shows the wrong network operator?"
    a: "Report it with the “Report an error” link below the result: it opens an email to contact@optimce.be that states the data version, without your postcode. To check in the meantime, look at your electricity settlement or final bill: for a household, it gives the name and phone number of the network operator to call in case of a power cut."
  - q: "Will the tool be built into the OptimCE application?"
    a: "That is planned. When an energy community manager adds a meter in the application, it will suggest the municipality's network operator, which the manager can correct. Until then, the tool remains open to everyone, free of charge, on optimce.be."
---

To find your distribution network operator for electricity and gas, a postcode is now enough. Our free tool, [“Find your DSO”](/en/tools/find-my-dso/), gives the distribution system operator (DSO) for electricity and the one for natural gas in each of Belgium's 565 municipalities. The search runs in your browser, without an account. It is the first page of the site's new [Tools](/en/tools/) section.

## What the tool does

You enter your postcode. The result separates electricity and gas, with the name and website of each operator, then lists what to know about your municipality, the regulator and its tariffs, how to check on your bill and what energy sharing allows in your region. A button copies a link to the result, so you can send it to a neighbour or to a future member of your community.

It answers for a municipality or a section of a municipality, not for an address: it does not say whether the gas network runs down your street, and it does not cover businesses connected directly to Elia's network. Without JavaScript, the [table of DSOs by municipality](/en/tools/find-my-dso/municipalities/) gives the same information.

## Why we built it

The question “who runs my network?” comes up at specific moments.

- **When you move**, the operator may change, and its tariffs with it. In Wallonia, for 3,500 kWh a year on a single-rate meter, distribution alone costs about 400 € including VAT with AIEG in 2026, 433 € with ORES and 495 € with AIESH (CWaPE tariff summary, excluding transmission and surcharges).
- **When the power goes out**, you call the DSO, not your supplier. For a household, its name and phone number are printed on the settlement or final bill (royal decree of 9 December 2021, article 4, 7°). Our guide [“Read your Belgian electricity bill line by line”](/en/guides/read-electricity-bill-belgium/) helps you find them.
- **In an energy-sharing project**, the DSO receives the request, signs the agreement with the sharing representative, sends the metering data and applies the allocation key (CWaPE, for Wallonia). Project leaders therefore need to know which operator each participant depends on.

Official answers exist, but region by region. In Wallonia, the CWaPE offers a “Trouver mon GRD” search by postcode. In Flanders, the regulator publishes the municipalities of each of the eight Fluvius operators. In Brussels, Sibelga is the only designated operator (Brugel). We wanted one answer for all three regions, electricity and gas together, with its sources.

## DSO by municipality: the special cases

One municipality, one operator: the rule has exceptions, and the tool handles them.

| Case | Example | What the tool does |
|---|---|---|
| One postcode, two municipalities | 1040 (Brussels and Etterbeek), 1050 (Brussels and Ixelles), 1804 (Vilvoorde and Zemst) | It asks for your municipality |
| The operator depends on the section of the municipality | Baarle-Hertog: gas from Enexis, a Dutch operator, except in Zondereigen (Fluvius Kempen) | It asks for your section |
| One operator for electricity, another for gas | 22 municipalities, including Verviers, Eupen, Wavre and Couvin | It shows both |
| No designated gas DSO | 85 municipalities (84 in Wallonia, plus Voeren in Flanders) and the former municipality of Bertogne, in Bastogne | It says so |
| Change of operator in 2026 | Brunehaut (electricity: AIEG replaces ORES), Saint-Vith (gas: RESA, the first designated DSO), Beveren-Kruibeke-Zwijndrecht (Fluvius Midden-Vlaanderen) | Label “Recent change of operator” |
| Planned change, not yet confirmed | Namur and Gesves: network exchange between ORES and AIEG planned for 1 July 2026 | Label “Information to be confirmed” |

*Assumptions: counts based on version 2026.10.0 of the data, published on 19 October 2026; they change with each new version. A municipality counts as having no gas DSO when none of its sections has one.*

## Where the data comes from, and how to report an error

Every answer rests on public documents: orders published in the Belgian Official Journal, decisions of the Flemish regulator, opinions of the CWaPE and Brugel, operators' publications, and open data from Statbel, Fluvius and ORES. The current version cites 91 sources retrieved on 12 October 2026: 53 legal references, 32 cross-checks and 6 open datasets. The [table by municipality](/en/tools/find-my-dso/municipalities/#sources) lists them all.

When our sources fall short, the tool says so. In Walcourt and Marchin, the CWaPE names a gas operator, but we found no order designating one: the result carries the label “Information to be confirmed”.

The compiled dataset is published under the CC BY 4.0 licence in the [belgian-dso-map](https://github.com/OptimCE/belgian-dso-map) repository on GitHub: anyone may reuse it, with credit. Each result shows the data version. If an answer looks wrong, the “Report an error” link below the result opens an email to contact@optimce.be that contains the data version, never your postcode.

## Next: the tool inside the application

We plan to build the same lookup into the OptimCE application: when a community manager adds a meter, the application will suggest the municipality's DSO, which the manager can correct. OptimCE covers the Walloon framework today; Brussels and Flanders are planned but not yet implemented.

Leading a sharing project? Our guides explain how to [create an energy community in Wallonia](/en/guides/create-energy-community-wallonia/) or [join one](/en/guides/join-energy-community-wallonia/), and the [features](/en/features/) page shows what the application handles day to day.

> ### Find your network operator
>
> A postcode is enough to know the electricity and gas DSO of your municipality. Free, no account.
>
> **[Try “Find your DSO” →](/en/tools/find-my-dso/)**

## FAQ

### Is there a free tool to find your DSO in Belgium?

Yes. OptimCE's “Find your DSO” tool is free and needs no account: you enter your postcode and it shows the distribution system operator (DSO) for electricity and the one for natural gas in your municipality. It covers all 565 municipalities in Belgium, in Brussels, Flanders and Wallonia.

### Is my postcode stored when I use the tool?

No. The search runs in your browser, which loads all of the tool's data once: your postcode is not sent to any server. It only appears in the page address so that you can copy a link to the result, and the “Report an error” email does not contain it. Our audience measurement receives only the region and the operators found.

### Why does the tool ask for my municipality or my section of the municipality?

Because your postcode is not always enough. Three postcodes cover two municipalities: 1040 (Brussels and Etterbeek), 1050 (Brussels and Ixelles) and 1804 (Vilvoorde and Zemst). In Baarle-Hertog, the gas operator depends on the section of the municipality: Enexis, a Dutch operator, except in Zondereigen, served by Fluvius Kempen. The tool then asks before showing the result.

### What should I do if the tool shows the wrong network operator?

Report it with the “Report an error” link below the result: it opens an email to contact@optimce.be that states the data version, without your postcode. To check in the meantime, look at your electricity settlement or final bill: for a household, it gives the name and phone number of the network operator to call in case of a power cut.

### Will the tool be built into the OptimCE application?

That is planned. When an energy community manager adds a meter in the application, it will suggest the municipality's network operator, which the manager can correct. Until then, the tool remains open to everyone, free of charge, on optimce.be.

## Sources

- [CWaPE — Les gestionnaires de réseaux](https://www.cwape.be/node/160) (in French) — the five electricity DSOs active in Wallonia (AIEG, AIESH, ORES, RESA, REW), two of which, ORES and RESA, also distribute gas; the DSO's missions; link to the “Trouver mon GRD” search. Accessed on 21 October 2026.
- [CWaPE — Trouver mon GRD](https://www.cwape.be/mon-grd) (in French) — the Walloon regulator's search for a network operator by postcode. Accessed on 21 October 2026.
- [CWaPE — Synthèse des tarifs de réseaux 2026, électricité (TVAC)](https://www.cwape.be/sites/default/files/cwape-documents/SYNTHESE%20DES%20TARIFS%20DE%20DISTRIBUTION%20ELEC%202026%20(TVAC-pdf)_0.pdf) (in French) — tariffs for residential customers connected at low voltage, from 1 January to 31 December 2026, updated on 5 January 2026. Source of the fixed term (19.50 € a year with AIEG, 14.10 € with ORES, 17.93 € with AIESH) and of the single-rate proportional term (10.86965, 11.98070 and 13.63965 c€/kWh) from which we derive the amounts for 3,500 kWh, the consumption profile used in our other articles. The document states that network tariffs are proposed by the DSOs and approved by the CWaPE. Accessed on 21 October 2026.
- [Vlaamse Nutsregulator — Aanwijzing netbeheerders](https://www.vlaamsenutsregulator.be/elektriciteit-en-aardgas/technische-reglementen-flexibiliteit-niet-publieke-netten/wie-is-mijn-netbeheerder/aanwijzing-netbeheerders) (in Dutch) — designations of the distribution system operators in Flanders, with the municipalities of each, and the case of gas in Baarle-Hertog, operated by the Dutch operator Enexis. Accessed on 21 October 2026.
- [Brugel — Le gestionnaire du réseau de distribution](https://www.brugel.brussels/brugel/grd-29) (in French) — designation of Sibelga as the only electricity and natural gas distribution system operator of the Brussels-Capital Region. Accessed on 21 October 2026.
- [CWaPE — Partage d'énergie](https://www.cwape.be/node/5618) (in French) — the network operator's role in a Walloon sharing operation: request, agreement with the representative, transmission of metering data and application of the allocation key. Accessed on 21 October 2026.
- [Royal decree of 9 December 2021 on the other minimum requirements for bills](https://www.ejustice.just.fgov.be/eli/arrete/2021/12/09/2021022724/justel) (in French) — article 4, 7°: settlement and final bills for residential customers give the name and phone number of the DSO to contact in case of a power cut. Accessed on 21 October 2026.
- [ORES Assets — Rapport annuel 2025](https://media.ores.be/ores-cms/ueqhj4jd/ores-assets-rapport-annuel-2025.pdf) (in French) — page 79: the transfer of Brunehaut to AIEG for the management of the electricity network took effect on 1 January 2026. Accessed on 21 October 2026.
- [Walloon Government order of 25 June 2026](https://www.ejustice.just.fgov.be/cgi/article.pl?language=fr&sum_date=2026-07-07&lg_txt=F&numac_search=2026201749) (in French) — designation of RESA as gas distribution system operator for Saint-Vith, from 1 June 2026. Accessed on 21 October 2026.
- [Vlaamse Nutsregulator — Decision BESL-2026-30](https://assets.vlaamsenutsregulator.be/2026-02/BESL-2026-30.pdf?VersionId=ElUWU7F1ROzPe0DBorhKohDkgVri6GOX) (in Dutch) — final designation of Fluvius Midden-Vlaanderen for electricity and gas in the Zwijndrecht section, replacing Fluvius Antwerpen, in force since 1 January 2026. Accessed on 21 October 2026.
- [ORES Assets — General meeting of 21 May 2026, item 6: transfer of the Namur and Gesves networks](https://media.ores.be/ores-cms/depfic4r/20260521-ag-ores-assets-point-06-transfert-r%C3%A9seaux-namur-et-gesves.pdf) (in French) — network exchange between ORES and AIEG in Namur (Flawinne, Marche-les-Dames, Saint-Marc and Vedrin) and in Gesves, planned for 1 January 2026 or, failing that, 1 July 2026. Accessed on 21 October 2026.
- [Statbel — REFNIS code 2025](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2025.csv) — nomenclature of administrative units in force since 1 January 2025: 565 municipalities. Accessed on 21 October 2026.
- [Creative Commons — Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) — licence of the dataset compiled by OptimCE; the sources keep their own licences. Accessed on 21 October 2026.
