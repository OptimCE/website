---
layout: post
title: "Netzbetreiber nach Gemeinde: hinter den Kulissen"
date: 2026-11-21 06:00:00 +0100
author: "Eric von OptimCE"
excerpt: "Keine offizielle Datei sagt, welcher Netzbetreiber jede belgische Gemeinde versorgt. Wir haben eine aus 91 öffentlichen Quellen erstellt: die Fallstricke, das Datenmodell, die Tests und wie Sie die Daten weiterverwenden."
description: "Wie wir die Liste der Netzbetreiber nach Gemeinde in Belgien erstellt haben: Quellen je Region, Fallstricke, Datenmodell, Tests, Lizenz CC BY 4.0."
tags: [app, news]
lang: de
ref: dso-map-behind-the-scenes
permalink: /de/aktuelles/2026/11/21/netzbetreiber-nach-gemeinde-hinter-den-kulissen/
faq:
  - q: "Gibt es eine offizielle Liste der Netzbetreiber nach Gemeinde in Belgien?"
    a: "Nicht als einzelne Datei, soweit wir wissen. Die CWaPE und Synergrid bieten eine Suche nach Postleitzahl an, Fluvius veröffentlicht eine Datei für Flandern, und Brugel bezeichnet Sibelga für die 19 Brüsseler Gemeinden. OptimCE hat diese Quellen im Datensatz belgian-dso-map zusammengeführt: 565 Gemeinden, Strom und Gas, jede Zuordnung mit ihren Quellen, unter der Lizenz CC BY 4.0."
  - q: "Was ist der INS-Code einer Gemeinde, und warum nicht die Postleitzahl?"
    a: "Der INS-Code, auch NIS-Code genannt, ist der fünfstellige Code, den Statbel, das belgische Statistikamt, jeder Gemeinde zuweist; seine erste Ziffer bezeichnet die Provinz. Postleitzahlen stammen von bpost und folgen nicht immer den Gemeindegrenzen: 1040, 1050 und 1804 decken jeweils zwei Gemeinden ab. Der INS-Code, bei Bedarf ergänzt um den Ortsteil, ist daher der verlässliche Schlüssel für den Netzbetreiber. Bei einer Gemeindefusion ändert er sich allerdings."
  - q: "Was geschieht mit dem Netzbetreiber, wenn Gemeinden fusionieren?"
    a: "Nichts automatisch. In Bastnach, das am 2. Dezember 2024 mit Bertogne fusionierte, ist ORES für Gas nur in der früheren Gemeinde Bastnach bezeichnet: Bertogne hat keinen Gasnetzbetreiber. Zwijndrecht, das am 1. Januar 2025 fusionierte, wechselte den Netzbetreiber erst ein Jahr später. Eine Fusion gibt der Gemeinde außerdem einen neuen INS-Code."
  - q: "Darf ich die Liste der Netzbetreiber nach Gemeinde in meiner Anwendung verwenden?"
    a: "Ja, unter der Lizenz CC BY 4.0: Nennen Sie „belgian-dso-map, OptimCE“ mit Version und Datum, verlinken Sie das GitHub-Repository und geben Sie an, ob Sie die Daten geändert haben. Die Quellen behalten ihre eigenen Lizenzen, aufgeführt in ATTRIBUTION.md. Laden Sie die Dateien des Releases herunter, die Sie anhand ihrer SHA-256-Prüfsummen kontrollieren können, und nicht die JSON-Datei der Website, deren Format intern ist."
  - q: "Wie melde ich einen Fehler in der Liste?"
    a: "Eröffnen Sie ein Issue im GitHub-Repository belgian-dso-map mit der Gemeinde, der Energie und, wenn möglich, dem Dokument, das den richtigen Netzbetreiber belegt. Die Korrektur läuft über einen Pull Request und dann über eine neue Version, die die Website übernimmt. Ohne GitHub-Konto nutzen Sie den Link „Fehler melden“ unter jedem Ergebnis des Werkzeugs."
---

Soweit wir wissen, gibt keine offizielle Datei die Liste der Netzbetreiber nach Gemeinde für ganz Belgien an. Also haben wir eine erstellt. Sie speist das Werkzeug [„Netzbetreiber finden“](/de/werkzeuge/netzbetreiber-finden/) und die [Tabelle der Netzbetreiber nach Gemeinde](/de/werkzeuge/netzbetreiber-finden/gemeinden/): 565 Gemeinden, Strom und Gas, und für jede Zuordnung ihre Quellen.

[Unsere Meldung vom Oktober](/de/aktuelles/2026/10/22/netzbetreiber-finden-werkzeug/) stellte das Werkzeug vor. Diese richtet sich an Entwickler, Open-Data-Akteure und Journalisten: woher die Daten kommen, was sich als schwierig erwies, wie wir sie testen und wie Sie sie weiterverwenden. Der Datensatz, belgian-dso-map, ist öffentlich, wie der Code von OptimCE, der Open-Source-Plattform aus dem wallonischen Forschungsprojekt Locomotrice ([die Ursprünge des Projekts](/de/aktuelles/2026/03/01/start-optimce/)).

## Das Problem: Suchmasken, keine Dateien

Offizielle Antworten gibt es, aber nur einzeln. Die CWaPE, die wallonische Regulierungsbehörde, bietet eine Suche nach Postleitzahl für die Wallonie an; Synergrid, der Verband der Netzbetreiber, eine für das ganze Land. Eine herunterladbare Datei oder eine Lizenz zur Weiterverwendung haben wir dort nicht gefunden.

Die Dateien sind regional. Fluvius veröffentlicht den Netzbetreiber jeder flämischen Gemeinde als Open Data, zuletzt aktualisiert am 1. April 2025. Die CWaPE veröffentlicht einen Power-BI-Bericht „GRD par commune“ ohne Angabe einer Lizenz. In Brüssel bezeichnet Brugel Sibelga für alle 19 Gemeinden. Auf data.gov.be haben wir keinen Datensatz gefunden, der alle drei Regionen abdeckt.

## Die Quellen, Region für Region

| Region | Was maßgeblich ist | Abgleich |
|---|---|---|
| Brüssel (19 Gemeinden) | Brugel: Sibelga, einziger Netzbetreiber für Strom und Gas | Stellungnahme von Brugel zu seiner Bezeichnung |
| Flandern (285 Gemeinden) | Beschlüsse der flämischen Regulierungsbehörde: Bezeichnungen und Tarifbeschlüsse 2026, die die Gemeinden jedes der acht Fluvius-Netzbetreiber auflisten | Open Data von Fluvius |
| Wallonie (261 Gemeinden) | 27 Bezeichnungserlasse der Wallonischen Regierung, 15 für Strom und 12 für Gas | Stellungnahmen der CWaPE, Open Data von ORES, Berichte der Netzbetreiber, Power-BI-Bericht der CWaPE, von Hand gelesen |
| Ganz Belgien | Statbel: Gemeindecodes, Postleitzahlentabelle, deutsche Namen | — |

*Annahmen: Version 2026.10.0 des Datensatzes, veröffentlicht am 19. Oktober 2026, auf Grundlage von Quellen, die am 12. Oktober abgerufen wurden. Von den 91 Quellen sind 53 maßgeblich, 32 dienen dem Abgleich und 6 sind maschinenlesbare Datensätze. Unsere Ablesung des Power-BI-Berichts ist nicht veröffentlicht, da keine Lizenz angegeben ist: Veröffentlicht ist nur, ob er mit jeder wallonischen Zeile übereinstimmt.*

In Flandern und in der Wallonie nennt jede Zuordnung eine maßgebliche Quelle und eine Quelle eines anderen Herausgebers; sonst trägt sie den Vermerk „zu bestätigen“. Jede offizielle Liste wurde außerdem zweimal unabhängig abgeschrieben und dann verglichen.

## Die Fallstricke

### Eine Postleitzahl ist keine Gemeinde

Statbel verknüpft die Postleitzahlen von bpost mit den Gemeinden, indem es die Postbezirke über die Gemeindegrenzen legt: 1 149 Postleitzahlen ergeben 1 152 Paare. Drei Postleitzahlen decken zwei Gemeinden ab: 1040 (Brüssel und Etterbeek), 1050 (Brüssel und Ixelles) und 1804 (Vilvoorde und Zemst). Der Schlüssel der Datei ist daher das Tripel aus Postleitzahl, INS-Code und Ortsteil.

### Ortsteile

In Baarle-Hertog verteilt der niederländische Netzbetreiber Enexis das Gas, außer im Ortsteil Zondereigen, den Fluvius Kempen versorgt. Beide Ortsteile teilen sich die Postleitzahl 2387: Nur ihr Name unterscheidet sie.

### Gemeindefusion: Der Netzbetreiber folgt nicht

Bertogne gehört seit dem 2. Dezember 2024 zu Bastnach. Der Erlass von 2022, der ORES für Gas bezeichnet, nennt Bastnach, nicht Bertogne, und ORES zählt in den Postleitzahlen 6686 bis 6688 keinen Gas-Zugangspunkt. Die Gemeinde hat daher zwei Ortsteile, einen davon ohne Gasnetzbetreiber.

Zwijndrecht fusionierte am 1. Januar 2025 mit Beveren und Kruibeke, wechselte aber erst am 1. Januar 2026 von Fluvius Antwerpen zu Fluvius Midden-Vlaanderen. Der Fluvius-Datensatz vom 1. April 2025 zeigt noch den früheren Netzbetreiber: Das in der Zeile vermerkte Wechseldatum erklärt die Abweichung.

### INS-Code und Netzbetreiber: Auch der Code ändert sich

Über die Namen lassen sich die Quellen nicht verknüpfen. Der Bericht der CWaPE schreibt die Gemeinden in Großbuchstaben ohne Akzente, ein Erlass von 2022 enthält den Tippfehler „Fosse-la-ville“, und „Sibelgas“ war bis zum 31. Dezember 2024 der Name des heutigen Fluvius Halle-Vilvoorde, der nichts mit Sibelga zu tun hat. Die deutschen Gemeindenamen, etwa Bastnach oder Sankt Vith, stammen aus einer Datei von Statbel. Verknüpft wird über den INS-Code.

Doch auch dieser Code ändert sich. Statbel zählte bis zum 31. Dezember 2024 581 Gemeinden, seitdem 565. Die fusionierten Gemeinden erhielten einen neuen Code: Bastnach (82003) und Bertogne (82005) bilden heute 82039. Nur Antwerpen behielt seinen Code. Zwijndrecht wechselt von 11056 zu 46030, weil die erste Ziffer die Provinz bezeichnet. Eine Datei, die über die Codes von 2024 verknüpft, verliert diese Gemeinden ohne sichtbaren Fehler.

### Wirksamkeit vor der Veröffentlichung

In Sankt Vith ist RESA seit dem 1. Juni 2026 Gasnetzbetreiber, aufgrund eines Erlasses vom 25. Juni, der am 7. Juli im Belgischen Staatsblatt erschien; zuvor hatte die Gemeinde kein Erdgasnetz. Wie in Eupen, Raeren, Lontzen und Kelmis betreibt dort nun ORES das Stromnetz und RESA das Gasnetz. In Flandern bezeichnete die Regulierungsbehörde die acht Fluvius-Netzbetreiber am 6. Oktober 2026 neu, mit Wirkung zum 5. September, und veröffentlichte ihre Beschlüsse am 3. November.

Unsere Abfrage vom 12. Oktober konnte sie nicht sehen: Ein Hinweis der Version 2026.10.0 besagt, dass kein Beschluss veröffentlicht war. Am 21. November haben wir ihre Gemeindelisten mit unseren Daten verglichen: Alle 285 flämischen Gemeinden stimmen überein. Die Zuordnungen halten; der Hinweis ist überholt.

### Eine Bezeichnung ist kein Netz

Habay, Ramillies, Villers-la-Ville und Comblain-au-Pont haben einen bezeichneten Gasnetzbetreiber, den der Bericht der CWaPE nicht anzeigt. In Walcourt und Marchin ist es umgekehrt: Die CWaPE zeigt einen Gasnetzbetreiber, wir haben aber keinen Erlass gefunden, daher der Vermerk „zu bestätigen“.

Am 12. Oktober zeigte derselbe Bericht noch ORES in Couvin, das die AIESH seit dem 1. Januar 2024 versorgt, und in Brunehaut, das am 1. Januar 2026 zur AIEG wechselte. In Namur und Gesves bestätigt noch keine öffentliche Quelle den zum 1. Juli 2026 geplanten Netztausch zwischen ORES und AIEG: auch hier „zu bestätigen“.

## Das Datenmodell und die Testvektoren

Eine Version ist ein GitHub-Release aus zehn Dateien. Die wichtigste, `dso_lookup.csv`, hat 1 153 Zeilen mit 22 Spalten. Dazu kommen der Katalog der Netzbetreiber, 14 Hinweise in vier Sprachen, die 91 Quellen mit ihren SHA-256-Prüfsummen, 96 Testfälle, das Änderungsprotokoll und der Validierungsbericht. Hier die beiden Ortsteile von Bastnach:

```text
postcode,ins,commune_fr,commune_nl,commune_de,region,province,section_key,section_fr,section_nl,section_de,elec_operator,elec_designated,gas_status,gas_operator,flags,note_key,source_ids,valid_from,first_seen,changed_at,data_version
6600,82039,Bastogne,Bastenaken,Bastnach,WAL,BE-WLX,bastogne,Bastogne,Bastenaken,Bastnach,ores,ores,designated,ores,,,agw-2022-06-09-ores-gaz|agw-ores-elec-2022|cwape-avis-0900-ores-gaz|cwape-powerbi-grd-elec-2026-10-12|cwape-powerbi-grd-gas-2026-10-12|odwb-ores-elec|odwb-ores-gas,,2026-10-19,2026-10-19,2026.10.0
6687,82039,Bastogne,Bastenaken,Bastnach,WAL,BE-WLX,bertogne,Bertogne,Bertogne,,ores,ores,none,,,bastogne-gas-territory,agw-2022-05-25-resa-gaz|agw-2022-06-09-ores-gaz|agw-ores-elec-2022|cwape-powerbi-grd-elec-2026-10-12|cwape-powerbi-grd-gas-2026-10-12|decret-2023-05-19-fusion-bastogne-bertogne|odwb-ores-elec|odwb-ores-gas,,2026-10-19,2026-10-19,2026.10.0
```

`elec_operator` ist der Netzbetreiber, der das Netz betreibt und auf der Rechnung steht; `elec_designated` derjenige, den der Rechtsakt bezeichnet. Das Kennzeichen `operator_differs` markiert eine Abweichung zwischen beiden. `gas_status` ist `designated`, `none` oder `foreign` (Enexis).

Die Suche hat eine Referenzimplementierung in Python und zwei zeilengetreue Portierungen, im Werkzeug und in der Anwendung. Sie antwortet mit `not_found`, `choose_commune`, `choose_section` oder `ok`. Eine Postleitzahl muss aus genau vier ASCII-Ziffern bestehen, ohne die Kurzform `\d`, die in Python auch Ziffern voller Breite akzeptiert.

Die 96 Testfälle legen die erwarteten Antworten fest. Die Website führt ihre 73 Postleitzahl-Fälle zweimal aus, auf der CSV-Datei und auf der JSON-Datei, die der Build daraus erzeugt. Version 2026.10.0 besteht die Validierung ohne Fehler, mit 16 Warnungen, die alle erklärt sind.

Zwei Anwendungen lesen dieselbe Version: die Website und die OptimCE-Anwendung, in der Alpha-Phase, die den Stromnetzbetreiber vorschlägt, wenn ein Verwalter einer Gemeinschaft einen Zähler hinzufügt. Ein Fehler wird daher an einer einzigen Stelle korrigiert, im Daten-Repository.

## Verlässliche Änderungsdaten für Suchmaschinen

Google verwendet das `lastmod`-Datum einer Sitemap nur, „wenn er konsistent und nachweisbar korrekt ist“. Bing stellte 2023 fest, dass 18 % der Sitemaps, die es angeben, es falsch setzen, meist mit demselben Datum überall.

Jede Zeile des Datensatzes trägt daher zwei Daten, `first_seen` und `changed_at`, abgeleitet aus einer Prüfsumme ihrer Datenspalten: Eine unveränderte Zeile behält ihre Daten. Kein Datum stammt aus der Uhr, aus einem Dateidatum oder aus Git. Die Tabelle nach Gemeinde nimmt das jüngste von drei Daten: ihr eigenes, das ihrer Vorlage und das der Daten. Bei jedem Deployment berechnet ein Skript diese Daten neu und vergleicht sie mit der Sitemap. Die wöchentliche Datenaktualisierung baut die Website zweimal und verlangt zwei identische Sitemaps.

## Die Daten weiterverwenden und Fehler melden

Das Repository [belgian-dso-map](https://github.com/OptimCE/belgian-dso-map) veröffentlicht die Daten unter der Lizenz CC BY 4.0 und die Skripte unter Apache 2.0. Jede Version lässt sich mit ihren Prüfsummen herunterladen:

```bash
curl -LO https://github.com/OptimCE/belgian-dso-map/releases/download/2026.10.0/dso_lookup.csv
curl -LO https://github.com/OptimCE/belgian-dso-map/releases/download/2026.10.0/SHA256SUMS
sha256sum --check --ignore-missing SHA256SUMS
```

- Nennen Sie „belgian-dso-map, OptimCE“ mit Version, Datum und einem Link zum Repository, und geben Sie an, ob Sie die Daten geändert haben.
- Behalten Sie die Quellenangaben aus `ATTRIBUTION.md` bei: Statbel veröffentlicht unter CC BY 4.0, Fluvius unter einer eigenen Lizenz ohne Gewähr, und ORES bittet darum, über Weiterverwendungen informiert zu werden (indicateurs@ores.be).
- Lesen Sie die Dateien des Releases, nicht die JSON-Datei der Website, deren Format intern ist.

Ein Fehler? [Eröffnen Sie ein Issue](https://github.com/OptimCE/belgian-dso-map/issues) mit der Gemeinde, der Energie und dem Dokument, das den richtigen Netzbetreiber belegt, oder nutzen Sie den Link „Fehler melden“ des Werkzeugs.

> ### Die Liste der Netzbetreiber verbessern
>
> Die Daten, ihre Quellen und ihre Tests sind öffentlich. Eine Gemeinde mit dem falschen Netzbetreiber? Eröffnen Sie ein Issue, mit dem maßgeblichen Dokument.
>
> **[Fehler auf GitHub melden →](https://github.com/OptimCE/belgian-dso-map/issues)**

## FAQ

### Gibt es eine offizielle Liste der Netzbetreiber nach Gemeinde in Belgien?

Nicht als einzelne Datei, soweit wir wissen. Die CWaPE und Synergrid bieten eine Suche nach Postleitzahl an, Fluvius veröffentlicht eine Datei für Flandern, und Brugel bezeichnet Sibelga für die 19 Brüsseler Gemeinden. OptimCE hat diese Quellen im Datensatz belgian-dso-map zusammengeführt: 565 Gemeinden, Strom und Gas, jede Zuordnung mit ihren Quellen, unter der Lizenz CC BY 4.0.

### Was ist der INS-Code einer Gemeinde, und warum nicht die Postleitzahl?

Der INS-Code, auch NIS-Code genannt, ist der fünfstellige Code, den Statbel, das belgische Statistikamt, jeder Gemeinde zuweist; seine erste Ziffer bezeichnet die Provinz. Postleitzahlen stammen von bpost und folgen nicht immer den Gemeindegrenzen: 1040, 1050 und 1804 decken jeweils zwei Gemeinden ab. Der INS-Code, bei Bedarf ergänzt um den Ortsteil, ist daher der verlässliche Schlüssel für den Netzbetreiber. Bei einer Gemeindefusion ändert er sich allerdings.

### Was geschieht mit dem Netzbetreiber, wenn Gemeinden fusionieren?

Nichts automatisch. In Bastnach, das am 2. Dezember 2024 mit Bertogne fusionierte, ist ORES für Gas nur in der früheren Gemeinde Bastnach bezeichnet: Bertogne hat keinen Gasnetzbetreiber. Zwijndrecht, das am 1. Januar 2025 fusionierte, wechselte den Netzbetreiber erst ein Jahr später. Eine Fusion gibt der Gemeinde außerdem einen neuen INS-Code.

### Darf ich die Liste der Netzbetreiber nach Gemeinde in meiner Anwendung verwenden?

Ja, unter der Lizenz CC BY 4.0: Nennen Sie „belgian-dso-map, OptimCE“ mit Version und Datum, verlinken Sie das GitHub-Repository und geben Sie an, ob Sie die Daten geändert haben. Die Quellen behalten ihre eigenen Lizenzen, aufgeführt in ATTRIBUTION.md. Laden Sie die Dateien des Releases herunter, die Sie anhand ihrer SHA-256-Prüfsummen kontrollieren können, und nicht die JSON-Datei der Website, deren Format intern ist.

### Wie melde ich einen Fehler in der Liste?

Eröffnen Sie ein Issue im GitHub-Repository belgian-dso-map mit der Gemeinde, der Energie und, wenn möglich, dem Dokument, das den richtigen Netzbetreiber belegt. Die Korrektur läuft über einen Pull Request und dann über eine neue Version, die die Website übernimmt. Ohne GitHub-Konto nutzen Sie den Link „Fehler melden“ unter jedem Ergebnis des Werkzeugs.

## Quellen

- [OptimCE — belgian-dso-map, README](https://github.com/OptimCE/belgian-dso-map) (auf Englisch) — Datenvertrag (Dateien einer Version, Spalten, Vokabulare, Inhaltsdaten, Normalisierung), Suchalgorithmus und seine zwei Portierungen, Validierungsregeln, Lizenzen (Daten unter CC BY 4.0, Skripte unter Apache 2.0). Abgerufen am 21. November 2026.
- [OptimCE — belgian-dso-map, Version 2026.10.0](https://github.com/OptimCE/belgian-dso-map/releases/tag/2026.10.0) (auf Englisch) — Release vom 19. Oktober 2026: die zehn Dateien, ihre Prüfsummen und der Validierungsbericht (keine Fehler, 16 erklärte Warnungen, 96 Testfälle), Quelle der Zahlen dieses Artikels. Abgerufen am 21. November 2026.
- [OptimCE — belgian-dso-map, Kuratierung](https://github.com/OptimCE/belgian-dso-map/blob/main/curation/README.md) (auf Englisch) — doppelte Abschrift der offiziellen Listen, Namensaliasse, manuelle Ablesung des Power-BI-Berichts der CWaPE und warum diese Ablesung nicht veröffentlicht wird. Abgerufen am 21. November 2026.
- [Statbel — Geografie: Gemeindecodes und Postleitzahlen](https://statbel.fgov.be/fr/propos-de-statbel/methodologie/classifications/geographie) (auf Französisch) — REFNIS-Nomenklatur: 581 Gemeinden vom 1. Januar 2019 bis zum 31. Dezember 2024, 565 seit dem 1. Januar 2025, neuer Code von Bastnach gültig seit dem 2. Dezember 2024; Methode der Tabelle Postleitzahl–Gemeinde (Postbezirke von bpost, Gemeinden des FÖD Finanzen) und ihre drei Ausnahmen 1040, 1050 und 1804. Abgerufen am 21. November 2026.
- [Statbel — REFNIS 2025 (CSV)](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2025.csv) und [REFNIS 2019 (CSV)](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2019.csv) — Codes 82039 (Bastnach) und 46030 (Beveren-Kruibeke-Zwijndrecht) im Jahr 2025; Codes 82003 (Bastnach), 82005 (Bertogne) und 11056 (Zwijndrecht) bis 2024. Abgerufen am 21. November 2026.
- [Statistiek Vlaanderen — Nieuwe NIS-codes voor gefuseerde gemeenten vanaf 1 januari 2025](https://www.vlaanderen.be/statistiek-vlaanderen/nieuwe-nis-codes-voor-gefuseerde-gemeenten-vanaf-1-januari-2025) (auf Niederländisch) — neue Codes der fusionierten Gemeinden, Ausnahme Antwerpen (11002 behalten), Wechsel von Zwijndrecht in die Provinz Ostflandern. Abgerufen am 21. November 2026.
- [Fluvius — Netbeheerder en gas energie-inhoud per gemeente](https://opendata.fluvius.be/explore/dataset/1_23-dnb-per-gemeente-en-per-sector/) (auf Niederländisch) — Netzbetreiber jeder flämischen Gemeinde, 1 144 Datensätze, geändert am 1. April 2025, unter der Open-Data-Lizenz von Fluvius, die weder Vollständigkeit noch Richtigkeit garantiert. Abgerufen am 21. November 2026.
- [ORES auf Open Data Wallonie-Bruxelles — Strom-Zugangspunkte nach Ortschaft](https://www.odwb.be/explore/dataset/ores-electricite-_nb-points-prelevement-par-localite-et-type-client-tension-annu/) und [Gas-Zugangspunkte nach Ortschaft](https://www.odwb.be/explore/dataset/ores-gaz-nombre-de-points-de-prelevement-par-localite-annuel/) (auf Französisch) — von ORES versorgte Ortschaften; Metadaten mit der Angabe „CC0“. Abgerufen am 21. November 2026.
- [CWaPE — Trouver mon GRD](https://www.cwape.be/mon-grd) (auf Französisch) — Suche des Netzbetreibers nach Postleitzahl auf der Website der wallonischen Regulierungsbehörde. Abgerufen am 21. November 2026.
- [CWaPE — Statistiken: GRD par commune](https://www.cwape.be/node/6468) (auf Französisch) — Seite des Power-BI-Berichts „GRD par commune“, ohne Angabe einer Lizenz. Abgerufen am 21. November 2026.
- [Synergrid — Le GRD dans votre commune](https://www.synergrid.be/fr/au-sujet-des-reseaux/le-grd-dans-votre-commune) (auf Französisch) — landesweite Suche des Netzbetreibers nach Postleitzahl oder Gemeinde. Abgerufen am 21. November 2026.
- [Brugel — Le gestionnaire du réseau de distribution](https://www.brugel.brussels/brugel/grd-29) (auf Französisch) — Sibelga, einziger Verteilernetzbetreiber für Strom und Gas der Region Brüssel-Hauptstadt. Abgerufen am 21. November 2026.
- [Vlaamse Nutsregulator — Aanwijzing netbeheerders](https://www.vlaamsenutsregulator.be/elektriciteit-en-aardgas/technische-reglementen-flexibiliteit-niet-publieke-netten/wie-is-mijn-netbeheerder/aanwijzing-netbeheerders) (auf Niederländisch) — Seite vom 12. November 2026: Bezeichnung der acht Fluvius-Netzbetreiber am 6. Oktober 2026 für zwölf Jahre ab dem 5. September 2026, mit ihren Gemeinden; früherer Name von Fluvius Halle-Vilvoorde („Sibelgas“); ruhendes Bezeichnungsverfahren von Enexis in Baarle-Hertog. Abgerufen am 21. November 2026.
- [Vlaamse Nutsregulator — BESL-2026-74](https://www.vlaamsenutsregulator.be/publicaties/besl-2026-74) (auf Niederländisch) — Bezeichnung von Fluvius Antwerpen, der erste der acht Beschlüsse (BESL-2026-74 bis 81), veröffentlicht am 3. November 2026. Abgerufen am 21. November 2026.
- [Vlaamse Nutsregulator — BESL-2026-30](https://assets.vlaamsenutsregulator.be/2026-02/BESL-2026-30.pdf?VersionId=ElUWU7F1ROzPe0DBorhKohDkgVri6GOX) (auf Niederländisch) — Fluvius Midden-Vlaanderen seit dem 1. Januar 2026 für Strom und Gas in Zwijndrecht bezeichnet, anstelle von Fluvius Antwerpen. Abgerufen am 21. November 2026.
- [Dekret vom 19. Mai 2023 über die Fusion der Gemeinden Bastnach und Bertogne](https://etaamb.openjustice.be/fr/decret-du-19-mai-2023_n2023203212.html) (auf Französisch) — Artikel 2: Fusionsdatum 2. Dezember 2024. Abgerufen am 21. November 2026.
- [Erlass der Wallonischen Regierung vom 25. Juni 2026](https://www.ejustice.just.fgov.be/cgi/article.pl?language=fr&sum_date=2026-07-07&lg_txt=F&numac_search=2026201749) (auf Französisch) — Bezeichnung von RESA als Gasverteilernetzbetreiber für Sankt Vith ab dem 1. Juni 2026, veröffentlicht im Belgischen Staatsblatt am 7. Juli 2026. Abgerufen am 21. November 2026.
- [RESA — Rapport annuel 2024](https://cms.resa.be/app/uploads/2025/09/Rapport-annuel-2024.pdf) (auf Französisch) — Seite 32: die 17 Gemeinden im Osten, in denen RESA das Gas und ORES den Strom verteilt. Abgerufen am 21. November 2026.
- [Google Search Central — Sitemap erstellen und einreichen](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=de) — Google verwendet den Wert `lastmod`, wenn er konsistent und nachweisbar korrekt ist, und ignoriert `priority` und `changefreq`. Abgerufen am 21. November 2026.
- [Bing Webmaster Blog — The Importance of Setting the “lastmod” Tag in Your Sitemap](https://blogs.bing.com/webmaster/february-2023/The-Importance-of-Setting-the-lastmod-Tag-in-Your-Sitemap) (auf Englisch) — Beitrag von Fabrice Canel vom 1. Februar 2023: 18 % der Sitemaps, die `lastmod` angeben, setzen es falsch, meist mit demselben Wert für alle Adressen; das Datum muss die letzte Änderung der Seite sein, nicht die Erzeugung der Sitemap. Abgerufen am 21. November 2026.
- [Creative Commons — Namensnennung 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.de) — Lizenz des von OptimCE zusammengestellten Datensatzes. Abgerufen am 21. November 2026.
