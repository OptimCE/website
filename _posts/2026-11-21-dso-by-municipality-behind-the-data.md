---
layout: post
title: "DSO by municipality: behind the data"
date: 2026-11-21 06:00:00 +0100
author: "Eric from OptimCE"
excerpt: "No official file says which network operator serves each Belgian municipality. We built one from 91 public sources: the pitfalls we hit, the data model, the tests, and how to reuse it."
description: "How we built the list of distribution system operators by municipality in Belgium: sources by region, pitfalls, data model, tests, CC BY 4.0 licence."
tags: [app, news]
lang: en
ref: dso-map-behind-the-scenes
permalink: /en/news/2026/11/21/dso-by-municipality-behind-the-data/
faq:
  - q: "Is there an official list of DSOs by municipality in Belgium?"
    a: "Not as a single file, as far as we know. The CWaPE and Synergrid offer a search by postcode, Fluvius publishes a file for Flanders, and Brugel designates Sibelga for the 19 Brussels municipalities. OptimCE has compiled these sources into the belgian-dso-map dataset: 565 municipalities, electricity and gas, each attribution with its sources, under the CC BY 4.0 licence."
  - q: "What is a municipality's INS code, and why not use the postcode?"
    a: "The INS code, also called the NIS code, is the five-digit code that Statbel, the Belgian statistics office, gives each municipality; its first digit identifies the province. Postcodes come from bpost and do not always follow municipal boundaries: 1040, 1050 and 1804 each cover two municipalities. The INS code, with the section of the municipality where needed, is therefore the reliable key for finding the DSO. It does change, however, when municipalities merge."
  - q: "What happens to the DSO when municipalities merge?"
    a: "Nothing automatic. In Bastogne, which merged with Bertogne on 2 December 2024, ORES is designated for gas only in the former municipality of Bastogne: Bertogne has no gas DSO. Zwijndrecht, which merged on 1 January 2025, only changed operator a year later. A merger also gives the municipality a new INS code."
  - q: "Can I reuse the list of DSOs by municipality in my application?"
    a: "Yes, under the CC BY 4.0 licence: credit “belgian-dso-map, OptimCE” with the version and its date, add a link to the GitHub repository and say whether you changed the data. The sources keep their own licences, listed in ATTRIBUTION.md. Download the release files, which you can check against their SHA-256 hashes, rather than the website's JSON file, whose format is internal."
  - q: "How do I report an error in the list?"
    a: "Open an issue on the belgian-dso-map GitHub repository with the municipality, the energy and, if possible, the document that establishes the right operator. The fix goes through a pull request, then a new version, which the website picks up. Without a GitHub account, use the “Report an error” link under each result of the tool."
---

As far as we know, no official file gives the list of DSOs (distribution system operators) by municipality for the whole of Belgium. So we built one. It powers the [“Find your DSO”](/en/tools/find-my-dso/) tool and the [table of DSOs by municipality](/en/tools/find-my-dso/municipalities/): 565 municipalities, electricity and gas, and for each attribution, its sources.

[Our October news item](/en/news/2026/10/22/find-your-dso-tool/) introduced the tool. This one is for developers, open data people and journalists: where the data comes from, what resisted, how we test it and how to reuse it. The dataset, belgian-dso-map, is public, like the code of OptimCE, the open-source platform that grew out of Locomotrice, a Walloon research project ([the origins of the project](/en/news/2026/03/01/launch-optimce/)).

## The problem: searches, not files

Official answers exist, one at a time. The CWaPE, the Walloon regulator, offers a search by postcode for Wallonia; Synergrid, the federation of network operators, offers one for the whole country. We found neither a downloadable file nor a reuse licence behind them.

The files are regional. Fluvius publishes the operator of each Flemish municipality as open data, last updated on 1 April 2025. The CWaPE publishes a Power BI report, “GRD par commune”, with no licence stated. In Brussels, Brugel designates Sibelga for all 19 municipalities. We found no dataset on data.gov.be that covers all three regions.

## The sources, region by region

| Region | What is authoritative | Cross-checks |
|---|---|---|
| Brussels (19 municipalities) | Brugel: Sibelga, the only electricity and gas DSO | Brugel's opinion on its designation |
| Flanders (285 municipalities) | Decisions of the Flemish regulator: designations and the 2026 tariff decisions, which list the municipalities of each of the eight Fluvius operators | Fluvius open data |
| Wallonia (261 municipalities) | 27 designation orders of the Walloon Government, 15 for electricity and 12 for gas | CWaPE opinions, ORES open data, operators' reports, the CWaPE Power BI report read by hand |
| All of Belgium | Statbel: municipality codes, postcode table, German names | — |

*Assumptions: version 2026.10.0 of the dataset, published on 19 October 2026, from sources retrieved on 12 October. Of the 91 sources, 53 are authoritative, 32 are cross-checks and 6 are machine-readable datasets. Our reading of the Power BI report is not published, as no licence is stated: only whether it agrees with each Walloon row is.*

In Flanders and Wallonia, each attribution cites an authoritative source and a source from another publisher; otherwise it is flagged “to confirm”. Each official list was also transcribed twice, independently, then compared.

## The pitfalls

### A postcode is not a municipality

Statbel links bpost's postcodes to municipalities by overlaying the postal areas on municipal boundaries: 1,149 postcodes give 1,152 pairs. Three postcodes cover two municipalities: 1040 (Brussels and Etterbeek), 1050 (Brussels and Ixelles) and 1804 (Vilvoorde and Zemst). The key of the file is therefore the triple of postcode, INS code and section.

### Sections of a municipality

In Baarle-Hertog, gas is distributed by the Dutch operator Enexis, except in the Zondereigen section, served by Fluvius Kempen. Both sections share postcode 2387: only their name tells them apart.

### Municipal mergers: the DSO does not follow

Bertogne joined Bastogne on 2 December 2024. The 2022 order designating ORES for gas names Bastogne, not Bertogne, and ORES counts no gas access point in postcodes 6686 to 6688. The municipality therefore has two sections, one of them without a gas DSO.

Zwijndrecht merged with Beveren and Kruibeke on 1 January 2025, but only moved from Fluvius Antwerpen to Fluvius Midden-Vlaanderen on 1 January 2026. The Fluvius dataset, frozen on 1 April 2025, still shows the former operator: the change date recorded in the row explains the gap.

### INS codes and DSOs: the code changes too

Names cannot join the sources. The CWaPE report writes municipalities in capitals without accents, a 2022 order contains the typo “Fosse-la-ville”, and “Sibelgas” was, until 31 December 2024, the name of today's Fluvius Halle-Vilvoorde, which has nothing to do with Sibelga. We join on Statbel's INS code instead.

But that code moves as well. Statbel counted 581 municipalities until 31 December 2024, and 565 since. The merged municipalities got new codes: Bastogne (82003) and Bertogne (82005) are now 82039. Only Antwerp kept its code. Zwijndrecht goes from 11056 to 46030, because the first digit identifies the province. A file joined on the 2024 codes loses these municipalities without any visible error.

### Effective dates before publication

In Saint-Vith, RESA has been the gas DSO since 1 June 2026, under an order of 25 June published in the Belgian Official Gazette on 7 July. In Flanders, the regulator re-designated the eight Fluvius operators on 6 October 2026, effective 5 September, and published its decisions on 3 November.

Our retrieval of 12 October could not see them: a note in version 2026.10.0 says no decision had been published. On 21 November, we compared their lists of municipalities with our data: all 285 Flemish municipalities match. The attributions hold; the note is out of date.

### A designation is not a network

Habay, Ramillies, Villers-la-Ville and Comblain-au-Pont have a designated gas DSO that the CWaPE report does not show. In Walcourt and Marchin, it is the reverse: the CWaPE shows a gas DSO, but we found no order, hence the “to confirm” flag.

On 12 October, the same report still showed ORES in Couvin, run by AIESH since 1 January 2024, and in Brunehaut, which moved to AIEG on 1 January 2026. In Namur and Gesves, no public source yet confirms the network exchange between ORES and AIEG planned for 1 July 2026: “to confirm” again.

## The data model and the test vectors

A version is a GitHub release of ten files. The main one, `dso_lookup.csv`, has 1,153 rows of 22 columns. Around it: the operator catalogue, 14 notes in four languages, the 91 sources with their SHA-256 hashes, 96 test cases, the change log and the validation report. Here are the two sections of Bastogne:

```text
postcode,ins,commune_fr,commune_nl,commune_de,region,province,section_key,section_fr,section_nl,section_de,elec_operator,elec_designated,gas_status,gas_operator,flags,note_key,source_ids,valid_from,first_seen,changed_at,data_version
6600,82039,Bastogne,Bastenaken,Bastnach,WAL,BE-WLX,bastogne,Bastogne,Bastenaken,Bastnach,ores,ores,designated,ores,,,agw-2022-06-09-ores-gaz|agw-ores-elec-2022|cwape-avis-0900-ores-gaz|cwape-powerbi-grd-elec-2026-10-12|cwape-powerbi-grd-gas-2026-10-12|odwb-ores-elec|odwb-ores-gas,,2026-10-19,2026-10-19,2026.10.0
6687,82039,Bastogne,Bastenaken,Bastnach,WAL,BE-WLX,bertogne,Bertogne,Bertogne,,ores,ores,none,,,bastogne-gas-territory,agw-2022-05-25-resa-gaz|agw-2022-06-09-ores-gaz|agw-ores-elec-2022|cwape-powerbi-grd-elec-2026-10-12|cwape-powerbi-grd-gas-2026-10-12|decret-2023-05-19-fusion-bastogne-bertogne|odwb-ores-elec|odwb-ores-gas,,2026-10-19,2026-10-19,2026.10.0
```

`elec_operator` is the operator that runs the network, the one on the bill; `elec_designated` is the one the legal act designates. The `operator_differs` flag marks a difference between them. `gas_status` is `designated`, `none` or `foreign` (Enexis).

The lookup has a reference implementation in Python and two line-for-line ports, in the tool and in the application. It answers `not_found`, `choose_commune`, `choose_section` or `ok`. A postcode must be exactly four ASCII digits, without the `\d` shortcut, which in Python also accepts full-width digits.

The 96 test cases fix the expected answers. The website runs its 73 postcode cases twice, on the CSV and on the JSON file the build derives from it. Version 2026.10.0 passes validation with no errors and 16 warnings, all explained.

Two applications read the same version: the website, and the OptimCE application, in alpha, which suggests the electricity DSO when a community manager adds a meter. An error is therefore fixed in one place, the data repository.

## Reliable update dates for search engines

Google uses a sitemap's `lastmod` date only if it is “consistently and verifiably” accurate. In 2023, Bing found that 18% of the sitemaps that set it got it wrong, most often with the same date everywhere.

Each row of the dataset therefore carries two dates, `first_seen` and `changed_at`, derived from a hash of its data columns: a row that does not change keeps its dates. No date comes from the clock, a file's timestamp or git. The table by municipality takes the latest of three dates: its own, its template's and the data's. On every deployment, a script recomputes these dates and compares them with the sitemap. The weekly data update builds the site twice and requires two identical sitemaps.

## Reusing the data and reporting an error

The [belgian-dso-map](https://github.com/OptimCE/belgian-dso-map) repository publishes the data under the CC BY 4.0 licence and the scripts under Apache 2.0. Each version downloads with its hashes:

```bash
curl -LO https://github.com/OptimCE/belgian-dso-map/releases/download/2026.10.0/dso_lookup.csv
curl -LO https://github.com/OptimCE/belgian-dso-map/releases/download/2026.10.0/SHA256SUMS
sha256sum --check --ignore-missing SHA256SUMS
```

- Credit “belgian-dso-map, OptimCE”, with the version and its date and a link to the repository, and say whether you changed the data.
- Keep the credits of the sources, listed in `ATTRIBUTION.md`: Statbel publishes under CC BY 4.0, Fluvius under its own licence, without warranty, and ORES asks to be told about reuses (indicateurs@ores.be).
- Read the release files, not the website's JSON file, whose format is internal.

Found an error? [Open an issue](https://github.com/OptimCE/belgian-dso-map/issues) with the municipality, the energy and the document that establishes the right operator, or use the tool's “Report an error” link.

> ### Improve the list of DSOs
>
> The data, its sources and its tests are public. A municipality with the wrong operator? Open an issue, with the authoritative document.
>
> **[Report an error on GitHub →](https://github.com/OptimCE/belgian-dso-map/issues)**

## FAQ

### Is there an official list of DSOs by municipality in Belgium?

Not as a single file, as far as we know. The CWaPE and Synergrid offer a search by postcode, Fluvius publishes a file for Flanders, and Brugel designates Sibelga for the 19 Brussels municipalities. OptimCE has compiled these sources into the belgian-dso-map dataset: 565 municipalities, electricity and gas, each attribution with its sources, under the CC BY 4.0 licence.

### What is a municipality's INS code, and why not use the postcode?

The INS code, also called the NIS code, is the five-digit code that Statbel, the Belgian statistics office, gives each municipality; its first digit identifies the province. Postcodes come from bpost and do not always follow municipal boundaries: 1040, 1050 and 1804 each cover two municipalities. The INS code, with the section of the municipality where needed, is therefore the reliable key for finding the DSO. It does change, however, when municipalities merge.

### What happens to the DSO when municipalities merge?

Nothing automatic. In Bastogne, which merged with Bertogne on 2 December 2024, ORES is designated for gas only in the former municipality of Bastogne: Bertogne has no gas DSO. Zwijndrecht, which merged on 1 January 2025, only changed operator a year later. A merger also gives the municipality a new INS code.

### Can I reuse the list of DSOs by municipality in my application?

Yes, under the CC BY 4.0 licence: credit “belgian-dso-map, OptimCE” with the version and its date, add a link to the GitHub repository and say whether you changed the data. The sources keep their own licences, listed in ATTRIBUTION.md. Download the release files, which you can check against their SHA-256 hashes, rather than the website's JSON file, whose format is internal.

### How do I report an error in the list?

Open an issue on the belgian-dso-map GitHub repository with the municipality, the energy and, if possible, the document that establishes the right operator. The fix goes through a pull request, then a new version, which the website picks up. Without a GitHub account, use the “Report an error” link under each result of the tool.

## Sources

- [OptimCE — belgian-dso-map, README](https://github.com/OptimCE/belgian-dso-map) — data contract (files of a version, columns, vocabularies, content dates, normalisation), lookup algorithm and its two ports, validation rules, licences (data under CC BY 4.0, scripts under Apache 2.0). Accessed on 21 November 2026.
- [OptimCE — belgian-dso-map, version 2026.10.0](https://github.com/OptimCE/belgian-dso-map/releases/tag/2026.10.0) — release of 19 October 2026: the ten files, their hashes and the validation report (no errors, 16 explained warnings, 96 test cases), the source of the counts in this article. Accessed on 21 November 2026.
- [OptimCE — belgian-dso-map, curation](https://github.com/OptimCE/belgian-dso-map/blob/main/curation/README.md) — double transcription of the official lists, name aliases, manual reading of the CWaPE Power BI report and why that reading is not published. Accessed on 21 November 2026.
- [Statbel — Geography: municipality codes and postcodes](https://statbel.fgov.be/fr/propos-de-statbel/methodologie/classifications/geographie) (in French) — REFNIS nomenclature: 581 municipalities from 1 January 2019 to 31 December 2024, 565 since 1 January 2025, new code of Bastogne valid from 2 December 2024; method of the postcode–municipality table (bpost postal areas, municipalities of the Federal Public Service Finance) and its three exceptions, 1040, 1050 and 1804. Accessed on 21 November 2026.
- [Statbel — REFNIS 2025 (CSV)](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2025.csv) and [REFNIS 2019 (CSV)](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2019.csv) — codes 82039 (Bastogne) and 46030 (Beveren-Kruibeke-Zwijndrecht) in 2025; codes 82003 (Bastogne), 82005 (Bertogne) and 11056 (Zwijndrecht) until 2024. Accessed on 21 November 2026.
- [Statistiek Vlaanderen — Nieuwe NIS-codes voor gefuseerde gemeenten vanaf 1 januari 2025](https://www.vlaanderen.be/statistiek-vlaanderen/nieuwe-nis-codes-voor-gefuseerde-gemeenten-vanaf-1-januari-2025) (in Dutch) — new codes of the merged municipalities, the Antwerp exception (11002 kept), Zwijndrecht's move to the province of East Flanders. Accessed on 21 November 2026.
- [Fluvius — Netbeheerder en gas energie-inhoud per gemeente](https://opendata.fluvius.be/explore/dataset/1_23-dnb-per-gemeente-en-per-sector/) (in Dutch) — operator of each Flemish municipality, 1,144 records, dataset modified on 1 April 2025, under the Fluvius open data licence, which guarantees neither completeness nor accuracy. Accessed on 21 November 2026.
- [ORES on Open Data Wallonie-Bruxelles — electricity access points by locality](https://www.odwb.be/explore/dataset/ores-electricite-_nb-points-prelevement-par-localite-et-type-client-tension-annu/) and [gas access points by locality](https://www.odwb.be/explore/dataset/ores-gaz-nombre-de-points-de-prelevement-par-localite-annuel/) (in French) — localities served by ORES; metadata state “CC0”. Accessed on 21 November 2026.
- [CWaPE — Trouver mon GRD](https://www.cwape.be/mon-grd) (in French) — the Walloon regulator's search for a network operator by postcode. Accessed on 21 November 2026.
- [CWaPE — Statistics: GRD par commune](https://www.cwape.be/node/6468) (in French) — page of the “GRD par commune” Power BI report, with no licence stated. Accessed on 21 November 2026.
- [Synergrid — Le GRD dans votre commune](https://www.synergrid.be/fr/au-sujet-des-reseaux/le-grd-dans-votre-commune) (in French) — national search for the network operator by postcode or municipality. Accessed on 21 November 2026.
- [Brugel — Le gestionnaire du réseau de distribution](https://www.brugel.brussels/brugel/grd-29) (in French) — Sibelga, the only electricity and gas distribution system operator of the Brussels-Capital Region. Accessed on 21 November 2026.
- [Vlaamse Nutsregulator — Aanwijzing netbeheerders](https://www.vlaamsenutsregulator.be/elektriciteit-en-aardgas/technische-reglementen-flexibiliteit-niet-publieke-netten/wie-is-mijn-netbeheerder/aanwijzing-netbeheerders) (in Dutch) — page updated on 12 November 2026: designation of the eight Fluvius operators on 6 October 2026, for twelve years from 5 September 2026, with their municipalities; former name of Fluvius Halle-Vilvoorde (“Sibelgas”); designation procedure of Enexis in Baarle-Hertog on hold. Accessed on 21 November 2026.
- [Vlaamse Nutsregulator — BESL-2026-74](https://www.vlaamsenutsregulator.be/publicaties/besl-2026-74) (in Dutch) — designation of Fluvius Antwerpen, the first of the eight decisions (BESL-2026-74 to 81), published on 3 November 2026. Accessed on 21 November 2026.
- [Vlaamse Nutsregulator — BESL-2026-30](https://assets.vlaamsenutsregulator.be/2026-02/BESL-2026-30.pdf?VersionId=ElUWU7F1ROzPe0DBorhKohDkgVri6GOX) (in Dutch) — Fluvius Midden-Vlaanderen designated for electricity and gas in Zwijndrecht, in place of Fluvius Antwerpen, since 1 January 2026. Accessed on 21 November 2026.
- [Decree of 19 May 2023 on the merger of the municipalities of Bastogne and Bertogne](https://etaamb.openjustice.be/fr/decret-du-19-mai-2023_n2023203212.html) (in French) — article 2: merger date set at 2 December 2024. Accessed on 21 November 2026.
- [Walloon Government order of 25 June 2026](https://www.ejustice.just.fgov.be/cgi/article.pl?language=fr&sum_date=2026-07-07&lg_txt=F&numac_search=2026201749) (in French) — designation of RESA as gas distribution system operator for Saint-Vith from 1 June 2026, published in the Belgian Official Gazette on 7 July 2026. Accessed on 21 November 2026.
- [Google Search Central — Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) — Google uses the `lastmod` value if it is consistently and verifiably accurate, and ignores `priority` and `changefreq`. Accessed on 21 November 2026.
- [Bing Webmaster Blog — The Importance of Setting the “lastmod” Tag in Your Sitemap](https://blogs.bing.com/webmaster/february-2023/The-Importance-of-Setting-the-lastmod-Tag-in-Your-Sitemap) — post by Fabrice Canel of 1 February 2023: 18% of the sitemaps that set `lastmod` set it wrongly, most often with the same value for every URL; the date must be the page's last modification, not the sitemap's generation. Accessed on 21 November 2026.
- [Creative Commons — Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) — licence of the dataset compiled by OptimCE. Accessed on 21 November 2026.
