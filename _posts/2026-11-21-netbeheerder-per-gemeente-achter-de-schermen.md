---
layout: post
title: "Netbeheerder per gemeente: achter de schermen"
date: 2026-11-21 06:00:00 +0100
author: "Eric van OptimCE"
excerpt: "Geen enkel officieel bestand vermeldt welke netbeheerder elke Belgische gemeente bedient. Wij hebben er een samengesteld uit 91 openbare bronnen: de valkuilen, het datamodel, de tests en hoe u de gegevens hergebruikt."
description: "Hoe wij de lijst van netbeheerders per gemeente in België hebben opgebouwd: bronnen per gewest, valkuilen, datamodel, tests en licentie CC BY 4.0."
tags: [app, news]
lang: nl
ref: dso-map-behind-the-scenes
permalink: /nl/nieuws/2026/11/21/netbeheerder-per-gemeente-achter-de-schermen/
faq:
  - q: "Bestaat er een officiële lijst van netbeheerders per gemeente in België?"
    a: "Niet als één bestand, voor zover wij weten. De CWaPE en Synergrid bieden een zoekfunctie op postcode, Fluvius publiceert een bestand voor Vlaanderen en Brugel wijst Sibelga aan voor de 19 Brusselse gemeenten. OptimCE heeft die bronnen samengebracht in de dataset belgian-dso-map: 565 gemeenten, elektriciteit en gas, elke toewijzing met haar bronnen, onder de licentie CC BY 4.0."
  - q: "Wat is de NIS-code van een gemeente, en waarom niet de postcode?"
    a: "De NIS-code, ook INS-code genoemd, is de code van vijf cijfers die Statbel, het Belgische statistiekbureau, aan elke gemeente toekent; het eerste cijfer staat voor de provincie. Postcodes komen van bpost en volgen niet altijd de gemeentegrenzen: 1040, 1050 en 1804 dekken elk twee gemeenten. De NIS-code, waar nodig aangevuld met de deelgemeente, is dus de betrouwbare sleutel om de netbeheerder te vinden. Bij een gemeentefusie verandert hij wel."
  - q: "Wat gebeurt er met de netbeheerder als gemeenten fuseren?"
    a: "Niets automatisch. Zwijndrecht fuseerde op 1 januari 2025 met Beveren en Kruibeke, maar ging pas op 1 januari 2026 van Fluvius Antwerpen naar Fluvius Midden-Vlaanderen. In Bastenaken, sinds 2 december 2024 gefuseerd met Bertogne, is ORES voor gas alleen in de vroegere gemeente Bastenaken aangewezen: Bertogne heeft geen netbeheerder voor gas. Een fusie geeft de gemeente ook een nieuwe NIS-code."
  - q: "Mag ik de lijst van netbeheerders per gemeente in mijn toepassing gebruiken?"
    a: "Ja, onder de licentie CC BY 4.0: vermeld “belgian-dso-map, OptimCE” met de versie en de datum, voeg een link naar de GitHub-repository toe en geef aan of u de gegevens hebt gewijzigd. De bronnen behouden hun eigen licenties, opgesomd in ATTRIBUTION.md. Download de bestanden van de release, die u met hun SHA-256-controlesommen kunt nagaan, en niet het JSON-bestand van de website, waarvan het formaat intern is."
  - q: "Hoe meld ik een fout in de lijst?"
    a: "Open een issue in de GitHub-repository belgian-dso-map met de gemeente, de energie en, indien mogelijk, het document dat de juiste netbeheerder vaststelt. De correctie verloopt via een pull request en daarna via een nieuwe versie, die de website overneemt. Zonder GitHub-account gebruikt u de link “Een fout melden” onder elk resultaat van de tool."
---

Voor zover wij weten, bestaat er geen officieel bestand met de lijst van netbeheerders per gemeente voor heel België. Dus hebben wij er een gemaakt. Het voedt de tool [“Wie is mijn netbeheerder?”](/nl/tools/wie-is-mijn-netbeheerder/) en de [tabel met de netbeheerder per gemeente](/nl/tools/wie-is-mijn-netbeheerder/gemeenten/): 565 gemeenten, elektriciteit en gas, en voor elke toewijzing haar bronnen.

[Ons nieuwsbericht van oktober](/nl/nieuws/2026/10/22/netbeheerder-vinden-tool/) stelde de tool voor. Dit bericht richt zich tot ontwikkelaars, opendata-actoren en journalisten: waar de gegevens vandaan komen, wat moeilijk bleek, hoe wij ze testen en hoe u ze hergebruikt. De dataset, belgian-dso-map, is openbaar, net als de code van OptimCE, het opensourceplatform uit het Waalse onderzoeksproject Locomotrice ([het ontstaan van het project](/nl/nieuws/2026/03/01/lancering-optimce/)).

## Het probleem: zoekfuncties, geen bestanden

Officiële antwoorden bestaan, maar één voor één. De CWaPE, de Waalse regulator, biedt een zoekfunctie op postcode voor Wallonië; Synergrid, de federatie van de netbeheerders, een voor het hele land. Een downloadbaar bestand of een licentie voor hergebruik vonden wij er niet.

De bestanden zijn regionaal. Fluvius publiceert de netbeheerder van elke Vlaamse gemeente als open data, laatst bijgewerkt op 1 april 2025. De CWaPE publiceert een Power BI-rapport “GRD par commune”, zonder vermelde licentie. In Brussel wijst Brugel Sibelga aan voor alle 19 gemeenten. Op data.gov.be vonden wij geen dataset die de drie gewesten samenbrengt.

## De bronnen, gewest per gewest

| Gewest | Wat rechtsgeldig is | Controles |
|---|---|---|
| Brussel (19 gemeenten) | Brugel: Sibelga, enige netbeheerder voor elektriciteit en gas | Advies van Brugel over zijn aanwijzing |
| Vlaanderen (285 gemeenten) | Beslissingen van de Vlaamse Nutsregulator (voorheen VREG): aanwijzingen en tariefbeslissingen 2026, met de gemeenten van elk van de acht Fluvius-netbeheerders | Open data van Fluvius |
| Wallonië (261 gemeenten) | 27 aanwijzingsbesluiten van de Waalse Regering, 15 voor elektriciteit en 12 voor gas | Adviezen van de CWaPE, open data van ORES, verslagen van de netbeheerders, Power BI-rapport van de CWaPE, met de hand gelezen |
| Heel België | Statbel: gemeentecodes, postcodetabel, Duitse namen | — |

*Hypothesen: versie 2026.10.0 van de dataset, gepubliceerd op 19 oktober 2026, op basis van bronnen die op 12 oktober werden opgehaald. Van de 91 bronnen zijn er 53 rechtsgeldig, dienen er 32 als controle en zijn er 6 machineleesbare datasets. Onze lezing van het Power BI-rapport is niet gepubliceerd, omdat er geen licentie vermeld staat: alleen of het met elke Waalse rij overeenstemt, is gepubliceerd.*

Een aanwijzing door de Waalse Regering geldt alleen voor Wallonië: in Vlaanderen wijst de Vlaamse Nutsregulator de netbeheerders aan. In Vlaanderen en Wallonië vermeldt elke toewijzing een rechtsgeldige bron en een bron van een andere uitgever; anders krijgt ze de vermelding “te bevestigen”. Elke officiële lijst werd bovendien twee keer onafhankelijk overgenomen en daarna vergeleken.

## De valkuilen

### Een postcode is geen gemeente

Statbel koppelt de postcodes van bpost aan de gemeenten door de postkantons over de gemeentegrenzen te leggen: 1 149 postcodes leveren 1 152 paren op. Drie postcodes dekken twee gemeenten: 1040 (Brussel en Etterbeek), 1050 (Brussel en Elsene) en 1804 (Vilvoorde en Zemst). De sleutel van het bestand is dus het drietal postcode, NIS-code en deelgemeente.

### Deelgemeenten

In Baarle-Hertog verdeelt de Nederlandse netbeheerder Enexis het gas, behalve in de deelgemeente Zondereigen, die Fluvius Kempen bedient. Volgens de Vlaamse Nutsregulator staat de aanwijzingsprocedure van Enexis on hold. Beide deelgemeenten delen postcode 2387: alleen hun naam onderscheidt ze.

### Gemeentefusie: de netbeheerder volgt niet

Zwijndrecht fuseerde op 1 januari 2025 met Beveren en Kruibeke, maar ging pas op 1 januari 2026 van Fluvius Antwerpen naar Fluvius Midden-Vlaanderen. De dataset van Fluvius, bevroren op 1 april 2025, toont nog de vroegere netbeheerder: de wijzigingsdatum in de rij verklaart het verschil.

In Wallonië hoort Bertogne sinds 2 december 2024 bij Bastenaken. Het besluit van 2022 dat ORES voor gas aanwijst, noemt Bastenaken, niet Bertogne, en ORES telt geen enkel toegangspunt voor gas in de postcodes 6686 tot 6688. De gemeente heeft dus twee deelgemeenten, waarvan één zonder netbeheerder voor gas.

### NIS-code en netbeheerder: ook de code verandert

Op namen kunt u de bronnen niet koppelen. Het rapport van de CWaPE schrijft gemeenten in hoofdletters zonder accenten, een besluit van 2022 bevat de tikfout “Fosse-la-ville”, en “Sibelgas” was tot 31 december 2024 de naam van het huidige Fluvius Halle-Vilvoorde, dat niets met Sibelga te maken heeft. Wij koppelen dus op de NIS-code van Statbel.

Maar ook die code beweegt. Statbel telde tot 31 december 2024 581 gemeenten, sindsdien 565. De gefuseerde gemeenten kregen een nieuwe code: Bastenaken (82003) en Bertogne (82005) vormen nu 82039. Alleen Antwerpen hield zijn code. Zwijndrecht gaat van 11056 naar 46030, omdat het eerste cijfer de provincie aangeeft. Een bestand dat op de codes van 2024 koppelt, verliest die gemeenten zonder zichtbare fout.

### Ingangsdata vóór de publicatie

In Vlaanderen wees de Vlaamse Nutsregulator de acht Fluvius-netbeheerders op 6 oktober 2026 opnieuw aan, voor twaalf jaar vanaf 5 september 2026, onder de ontbindende voorwaarde dat uiterlijk op 5 september 2027 aan alle aanwijzingsvoorwaarden is voldaan. De beslissingen staan sinds 3 november online. In Sankt Vith is RESA sinds 1 juni 2026 de netbeheerder voor gas, op grond van een Waals besluit van 25 juni, gepubliceerd op 7 juli.

Onze ophaling van 12 oktober kon die beslissingen niet zien: een opmerking in versie 2026.10.0 zegt dat er geen beslissing gepubliceerd was. Op 21 november vergeleken wij hun gemeentelijsten met onze gegevens: alle 285 Vlaamse gemeenten stemmen overeen. De toewijzingen kloppen; de opmerking is achterhaald.

### Een aanwijzing is geen net

Habay, Ramillies, Villers-la-Ville en Comblain-au-Pont hebben een aangewezen netbeheerder voor gas, die het rapport van de CWaPE niet toont. In Walcourt en Marchin is het omgekeerd: de CWaPE toont een netbeheerder voor gas, maar wij vonden geen besluit, vandaar de vermelding “te bevestigen”. Op 12 oktober toonde hetzelfde rapport ook nog ORES in Couvin, dat sinds 1 januari 2024 door AIESH wordt beheerd.

## Het datamodel en de testvectoren

Een versie is een GitHub-release van tien bestanden. Het belangrijkste, `dso_lookup.csv`, telt 1 153 rijen van 22 kolommen. Daarnaast: de catalogus van de netbeheerders, 14 opmerkingen in vier talen, de 91 bronnen met hun SHA-256-controlesom, 96 testgevallen, het wijzigingslogboek en het validatierapport. Hier de twee deelgemeenten van Bastenaken:

```text
postcode,ins,commune_fr,commune_nl,commune_de,region,province,section_key,section_fr,section_nl,section_de,elec_operator,elec_designated,gas_status,gas_operator,flags,note_key,source_ids,valid_from,first_seen,changed_at,data_version
6600,82039,Bastogne,Bastenaken,Bastnach,WAL,BE-WLX,bastogne,Bastogne,Bastenaken,Bastnach,ores,ores,designated,ores,,,agw-2022-06-09-ores-gaz|agw-ores-elec-2022|cwape-avis-0900-ores-gaz|cwape-powerbi-grd-elec-2026-10-12|cwape-powerbi-grd-gas-2026-10-12|odwb-ores-elec|odwb-ores-gas,,2026-10-19,2026-10-19,2026.10.0
6687,82039,Bastogne,Bastenaken,Bastnach,WAL,BE-WLX,bertogne,Bertogne,Bertogne,,ores,ores,none,,,bastogne-gas-territory,agw-2022-05-25-resa-gaz|agw-2022-06-09-ores-gaz|agw-ores-elec-2022|cwape-powerbi-grd-elec-2026-10-12|cwape-powerbi-grd-gas-2026-10-12|decret-2023-05-19-fusion-bastogne-bertogne|odwb-ores-elec|odwb-ores-gas,,2026-10-19,2026-10-19,2026.10.0
```

`elec_operator` is de netbeheerder die het net uitbaat en op de factuur staat; `elec_designated` is die welke de rechtshandeling aanwijst. De vlag `operator_differs` markeert een verschil tussen beide. `gas_status` is `designated`, `none` of `foreign` (Enexis).

De zoekfunctie heeft een referentie-implementatie in Python en twee regel-voor-regelvertalingen, in de tool en in de toepassing. Ze antwoordt `not_found`, `choose_commune`, `choose_section` of `ok`. Een postcode moet uit precies vier ASCII-cijfers bestaan, zonder de afkorting `\d`, die in Python ook cijfers van volle breedte aanvaardt.

De 96 testgevallen leggen de verwachte antwoorden vast. De website voert haar 73 postcodegevallen twee keer uit, op het CSV-bestand en op het JSON-bestand dat de build ervan afleidt. Versie 2026.10.0 doorstaat de validatie zonder fouten, met 16 waarschuwingen, die allemaal verklaard zijn.

Twee toepassingen lezen dezelfde versie: de website en de OptimCE-toepassing, in alfafase, die de netbeheerder voor elektriciteit voorstelt wanneer een beheerder van een gemeenschap een meter toevoegt. Een fout wordt dus op één plaats verbeterd, de datarepository.

## Betrouwbare wijzigingsdata voor zoekmachines

Google gebruikt de `lastmod`-datum van een sitemap alleen als die consequent en aantoonbaar klopt. Bing stelde in 2023 vast dat 18 % van de sitemaps die hem invullen, dat verkeerd doet, meestal met overal dezelfde datum.

Elke rij van de dataset draagt daarom twee data, `first_seen` en `changed_at`, afgeleid van een controlesom van haar gegevenskolommen: een rij die niet verandert, behoudt haar data. Geen enkele datum komt van de klok, een bestandsdatum of git. De tabel per gemeente neemt de recentste van drie data: die van de pagina, van haar sjabloon en van de gegevens. Bij elke deployment herberekent een script die data en vergelijkt ze met de sitemap. De wekelijkse gegevensupdate bouwt de website twee keer en eist twee identieke sitemaps.

## De gegevens hergebruiken en een fout melden

De repository [belgian-dso-map](https://github.com/OptimCE/belgian-dso-map) publiceert de gegevens onder de licentie CC BY 4.0 en de scripts onder Apache 2.0. Elke versie downloadt u met haar controlesommen:

```bash
curl -LO https://github.com/OptimCE/belgian-dso-map/releases/download/2026.10.0/dso_lookup.csv
curl -LO https://github.com/OptimCE/belgian-dso-map/releases/download/2026.10.0/SHA256SUMS
sha256sum --check --ignore-missing SHA256SUMS
```

- Vermeld “belgian-dso-map, OptimCE”, met de versie, de datum en een link naar de repository, en geef aan of u de gegevens hebt gewijzigd.
- Behoud de bronvermeldingen uit `ATTRIBUTION.md`: Statbel publiceert onder CC BY 4.0, Fluvius onder een eigen licentie, zonder garantie, en ORES vraagt om op de hoogte te worden gebracht van hergebruik (indicateurs@ores.be).
- Lees de bestanden van de release, niet het JSON-bestand van de website, waarvan het formaat intern is.

Een fout? [Open een issue](https://github.com/OptimCE/belgian-dso-map/issues) met de gemeente, de energie en het document dat de juiste netbeheerder vaststelt, of gebruik de link “Een fout melden” van de tool.

> ### De lijst van netbeheerders verbeteren
>
> De gegevens, hun bronnen en hun tests zijn openbaar. Een gemeente met de verkeerde netbeheerder? Open een issue, met het rechtsgeldige document.
>
> **[Een fout melden op GitHub →](https://github.com/OptimCE/belgian-dso-map/issues)**

## FAQ

### Bestaat er een officiële lijst van netbeheerders per gemeente in België?

Niet als één bestand, voor zover wij weten. De CWaPE en Synergrid bieden een zoekfunctie op postcode, Fluvius publiceert een bestand voor Vlaanderen en Brugel wijst Sibelga aan voor de 19 Brusselse gemeenten. OptimCE heeft die bronnen samengebracht in de dataset belgian-dso-map: 565 gemeenten, elektriciteit en gas, elke toewijzing met haar bronnen, onder de licentie CC BY 4.0.

### Wat is de NIS-code van een gemeente, en waarom niet de postcode?

De NIS-code, ook INS-code genoemd, is de code van vijf cijfers die Statbel, het Belgische statistiekbureau, aan elke gemeente toekent; het eerste cijfer staat voor de provincie. Postcodes komen van bpost en volgen niet altijd de gemeentegrenzen: 1040, 1050 en 1804 dekken elk twee gemeenten. De NIS-code, waar nodig aangevuld met de deelgemeente, is dus de betrouwbare sleutel om de netbeheerder te vinden. Bij een gemeentefusie verandert hij wel.

### Wat gebeurt er met de netbeheerder als gemeenten fuseren?

Niets automatisch. Zwijndrecht fuseerde op 1 januari 2025 met Beveren en Kruibeke, maar ging pas op 1 januari 2026 van Fluvius Antwerpen naar Fluvius Midden-Vlaanderen. In Bastenaken, sinds 2 december 2024 gefuseerd met Bertogne, is ORES voor gas alleen in de vroegere gemeente Bastenaken aangewezen: Bertogne heeft geen netbeheerder voor gas. Een fusie geeft de gemeente ook een nieuwe NIS-code.

### Mag ik de lijst van netbeheerders per gemeente in mijn toepassing gebruiken?

Ja, onder de licentie CC BY 4.0: vermeld “belgian-dso-map, OptimCE” met de versie en de datum, voeg een link naar de GitHub-repository toe en geef aan of u de gegevens hebt gewijzigd. De bronnen behouden hun eigen licenties, opgesomd in ATTRIBUTION.md. Download de bestanden van de release, die u met hun SHA-256-controlesommen kunt nagaan, en niet het JSON-bestand van de website, waarvan het formaat intern is.

### Hoe meld ik een fout in de lijst?

Open een issue in de GitHub-repository belgian-dso-map met de gemeente, de energie en, indien mogelijk, het document dat de juiste netbeheerder vaststelt. De correctie verloopt via een pull request en daarna via een nieuwe versie, die de website overneemt. Zonder GitHub-account gebruikt u de link “Een fout melden” onder elk resultaat van de tool.

## Bronnen

- [OptimCE — belgian-dso-map, README](https://github.com/OptimCE/belgian-dso-map) (in het Engels) — datacontract (bestanden van een versie, kolommen, vocabularia, inhoudsdata, normalisatie), zoekalgoritme en zijn twee vertalingen, validatieregels, licenties (gegevens onder CC BY 4.0, scripts onder Apache 2.0). Geraadpleegd op 21 november 2026.
- [OptimCE — belgian-dso-map, versie 2026.10.0](https://github.com/OptimCE/belgian-dso-map/releases/tag/2026.10.0) (in het Engels) — release van 19 oktober 2026: de tien bestanden, hun controlesommen en het validatierapport (geen fouten, 16 verklaarde waarschuwingen, 96 testgevallen), bron van de cijfers in dit bericht. Geraadpleegd op 21 november 2026.
- [OptimCE — belgian-dso-map, curatie](https://github.com/OptimCE/belgian-dso-map/blob/main/curation/README.md) (in het Engels) — dubbele overname van de officiële lijsten, naamaliassen, handmatige lezing van het Power BI-rapport van de CWaPE en waarom die lezing niet gepubliceerd wordt. Geraadpleegd op 21 november 2026.
- [Statbel — Geografie: gemeentecodes en postcodes](https://statbel.fgov.be/fr/propos-de-statbel/methodologie/classifications/geographie) (in het Frans) — REFNIS-nomenclatuur: 581 gemeenten van 1 januari 2019 tot 31 december 2024, 565 sinds 1 januari 2025, nieuwe code van Bastenaken geldig vanaf 2 december 2024; methode van de tabel postcode–gemeente (postkantons van bpost, gemeenten van de FOD Financiën) en haar drie uitzonderingen, 1040, 1050 en 1804. Geraadpleegd op 21 november 2026.
- [Statbel — REFNIS 2025 (CSV)](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2025.csv) en [REFNIS 2019 (CSV)](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2019.csv) — codes 82039 (Bastenaken) en 46030 (Beveren-Kruibeke-Zwijndrecht) in 2025; codes 82003 (Bastenaken), 82005 (Bertogne) en 11056 (Zwijndrecht) tot 2024. Geraadpleegd op 21 november 2026.
- [Statistiek Vlaanderen — Nieuwe NIS-codes voor gefuseerde gemeenten vanaf 1 januari 2025](https://www.vlaanderen.be/statistiek-vlaanderen/nieuwe-nis-codes-voor-gefuseerde-gemeenten-vanaf-1-januari-2025) — nieuwe codes van de gefuseerde gemeenten, uitzondering voor Antwerpen (11002 behouden), overgang van Zwijndrecht naar de provincie Oost-Vlaanderen. Geraadpleegd op 21 november 2026.
- [Fluvius — Netbeheerder en gas energie-inhoud per gemeente](https://opendata.fluvius.be/explore/dataset/1_23-dnb-per-gemeente-en-per-sector/) — netbeheerder van elke Vlaamse gemeente, 1 144 records, gewijzigd op 1 april 2025, onder de open-datalicentie van Fluvius, die volledigheid noch juistheid garandeert. Geraadpleegd op 21 november 2026.
- [ORES op Open Data Wallonie-Bruxelles — toegangspunten voor elektriciteit per plaats](https://www.odwb.be/explore/dataset/ores-electricite-_nb-points-prelevement-par-localite-et-type-client-tension-annu/) en [voor gas per plaats](https://www.odwb.be/explore/dataset/ores-gaz-nombre-de-points-de-prelevement-par-localite-annuel/) (in het Frans) — plaatsen die ORES bedient; metadata met de vermelding “CC0”. Geraadpleegd op 21 november 2026.
- [CWaPE — Trouver mon GRD](https://www.cwape.be/mon-grd) (in het Frans) — zoekfunctie van de Waalse regulator naar de netbeheerder op postcode. Geraadpleegd op 21 november 2026.
- [CWaPE — Statistieken: GRD par commune](https://www.cwape.be/node/6468) (in het Frans) — pagina van het Power BI-rapport “GRD par commune”, zonder vermelde licentie. Geraadpleegd op 21 november 2026.
- [Synergrid — Le GRD dans votre commune](https://www.synergrid.be/fr/au-sujet-des-reseaux/le-grd-dans-votre-commune) (in het Frans) — nationale zoekfunctie naar de netbeheerder op postcode of gemeente. Geraadpleegd op 21 november 2026.
- [Brugel — Le gestionnaire du réseau de distribution](https://www.brugel.brussels/brugel/grd-29) (in het Frans) — Sibelga, enige distributienetbeheerder voor elektriciteit en gas van het Brussels Hoofdstedelijk Gewest. Geraadpleegd op 21 november 2026.
- [Vlaamse Nutsregulator — Aanwijzing netbeheerders](https://www.vlaamsenutsregulator.be/elektriciteit-en-aardgas/technische-reglementen-flexibiliteit-niet-publieke-netten/wie-is-mijn-netbeheerder/aanwijzing-netbeheerders) — pagina bijgewerkt op 12 november 2026: aanwijzing van de acht Fluvius-netbeheerders op 6 oktober 2026, voor twaalf jaar vanaf 5 september 2026 en onder ontbindende voorwaarde, met hun gemeenten; vroegere naam van Fluvius Halle-Vilvoorde (“Sibelgas”); aanwijzingsprocedure van Enexis in Baarle-Hertog on hold. Geraadpleegd op 21 november 2026.
- [Vlaamse Nutsregulator — BESL-2026-74](https://www.vlaamsenutsregulator.be/publicaties/besl-2026-74) — aanwijzing van Fluvius Antwerpen, de eerste van de acht beslissingen (BESL-2026-74 tot 81), gepubliceerd op 3 november 2026. Geraadpleegd op 21 november 2026.
- [Vlaamse Nutsregulator — BESL-2026-30](https://assets.vlaamsenutsregulator.be/2026-02/BESL-2026-30.pdf?VersionId=ElUWU7F1ROzPe0DBorhKohDkgVri6GOX) — Fluvius Midden-Vlaanderen sinds 1 januari 2026 aangewezen voor elektriciteit en gas in Zwijndrecht, in de plaats van Fluvius Antwerpen. Geraadpleegd op 21 november 2026.
- [Decreet van 19 mei 2023 over de fusie van de gemeenten Bastenaken en Bertogne](https://etaamb.openjustice.be/fr/decret-du-19-mai-2023_n2023203212.html) (in het Frans) — artikel 2: fusiedatum vastgelegd op 2 december 2024. Geraadpleegd op 21 november 2026.
- [Besluit van de Waalse Regering van 25 juni 2026](https://www.ejustice.just.fgov.be/cgi/article.pl?language=fr&sum_date=2026-07-07&lg_txt=F&numac_search=2026201749) (in het Frans) — aanwijzing van RESA als distributienetbeheerder voor gas in Sankt Vith vanaf 1 juni 2026, gepubliceerd in het Belgisch Staatsblad op 7 juli 2026. Geraadpleegd op 21 november 2026.
- [Google Search Central — Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) (in het Engels) — Google gebruikt de waarde `lastmod` als die consequent en aantoonbaar juist is, en negeert `priority` en `changefreq`. Geraadpleegd op 21 november 2026.
- [Bing Webmaster Blog — The Importance of Setting the “lastmod” Tag in Your Sitemap](https://blogs.bing.com/webmaster/february-2023/The-Importance-of-Setting-the-lastmod-Tag-in-Your-Sitemap) (in het Engels) — bericht van Fabrice Canel van 1 februari 2023: 18 % van de sitemaps die `lastmod` invullen, doen dat verkeerd, meestal met dezelfde waarde voor elke URL; de datum moet de laatste wijziging van de pagina zijn, niet het aanmaken van de sitemap. Geraadpleegd op 21 november 2026.
- [Creative Commons — Naamsvermelding 4.0 Internationaal (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.nl) — licentie van de dataset die OptimCE heeft samengesteld. Geraadpleegd op 21 november 2026.
