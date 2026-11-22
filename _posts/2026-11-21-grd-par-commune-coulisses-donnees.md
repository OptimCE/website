---
layout: post
title: "GRD par commune : les coulisses des données"
date: 2026-11-21 06:00:00 +0100
author: "Eric d'OptimCE"
excerpt: "Aucun fichier officiel ne dit quel gestionnaire de réseau dessert chaque commune belge. Nous l'avons construit à partir de 91 sources publiques : les pièges rencontrés, le modèle de données, les tests, et comment le réutiliser."
description: "Comment nous avons construit la liste des GRD par commune en Belgique : sources par région, pièges, modèle de données, tests et licence CC BY 4.0."
tags: [app, news]
lang: fr
ref: dso-map-behind-the-scenes
faq:
  - q: "Existe-t-il une liste officielle des GRD par commune en Belgique ?"
    a: "Pas sous la forme d'un fichier unique, à notre connaissance. La CWaPE et Synergrid proposent une recherche par code postal, Fluvius publie un fichier pour la Flandre et Brugel désigne Sibelga à Bruxelles. OptimCE a réuni ces sources dans belgian-dso-map : 565 communes, électricité et gaz, chaque attribution sourcée, sous licence CC BY 4.0."
  - q: "Qu'est-ce que le code INS d'une commune, et pourquoi pas le code postal ?"
    a: "Le code INS, ou code NIS, est le code à cinq chiffres que Statbel attribue à chaque commune ; son premier chiffre désigne la province. Le code postal vient de bpost : 1040, 1050 et 1804 couvrent chacun deux communes. Le code INS, complété au besoin par la section de commune, est donc la clé fiable pour trouver le GRD. Il change toutefois lors d'une fusion."
  - q: "Que devient le GRD quand des communes fusionnent ?"
    a: "Rien d'automatique. À Bastogne, fusionnée avec Bertogne le 2 décembre 2024, ORES n'est désigné pour le gaz que dans l'ancienne commune de Bastogne : Bertogne n'a pas de GRD gaz. Zwijndrecht, fusionnée le 1er janvier 2025, n'a changé de gestionnaire qu'un an plus tard."
  - q: "Puis-je réutiliser la liste des GRD par commune dans mon application ?"
    a: "Oui, sous licence CC BY 4.0 : créditez « belgian-dso-map, OptimCE » avec la version et sa date, ajoutez un lien vers le dépôt GitHub et indiquez si vous avez modifié les données. Les sources gardent leurs propres licences, listées dans ATTRIBUTION.md. Téléchargez les fichiers de la release, vérifiables par leurs empreintes SHA-256."
  - q: "Comment signaler une erreur dans la liste des GRD ?"
    a: "Ouvrez une issue sur le dépôt GitHub belgian-dso-map avec la commune, l'énergie et, si possible, le document qui établit le bon gestionnaire. La correction passe par une pull request, puis par une nouvelle version que le site reprend. Sans compte GitHub, utilisez le lien « Signaler une erreur » sous chaque résultat de l'outil."
---

À notre connaissance, aucun fichier officiel ne donne la liste des GRD par commune pour toute la Belgique. Nous l'avons donc construit. Il alimente l'outil [« Quel est mon GRD ? »](/outils/quel-est-mon-grd/) et le [tableau des GRD par commune](/outils/quel-est-mon-grd/communes/) : 565 communes, l'électricité et le gaz, et pour chaque attribution, ses sources.

[Notre actualité d'octobre](/actualites/2026/10/22/outil-trouver-gestionnaire-reseau/) présentait l'outil. Celle-ci s'adresse aux développeurs, aux acteurs de l'open data et aux journalistes : d'où viennent les données, ce qui a résisté, comment nous les testons et comment les réutiliser. Ce jeu, belgian-dso-map, est public, comme le code d'OptimCE, plateforme open source née du projet de recherche wallon Locomotrice ([l'origine du projet](/actualites/2026/03/01/lancement-optimce/)).

## Le problème : des recherches, pas de fichier

Les réponses officielles existent, mais une à une. La CWaPE propose une recherche par code postal pour la Wallonie ; Synergrid, la fédération des gestionnaires de réseau, une recherche pour tout le pays. Nous n'y avons trouvé ni fichier à télécharger ni licence de réutilisation.

Les fichiers, eux, sont régionaux. Fluvius publie en données ouvertes le gestionnaire de chaque commune flamande, mis à jour le 1er avril 2025. La CWaPE publie un rapport Power BI « GRD par commune », sans licence indiquée. À Bruxelles, Brugel désigne Sibelga pour les 19 communes. Nous n'avons trouvé sur data.gov.be aucun jeu qui réunisse les trois régions.

## Les sources, région par région

| Région | Ce qui fait foi | Recoupements |
|---|---|---|
| Bruxelles (19 communes) | Brugel : Sibelga, seul GRD d'électricité et de gaz | Avis de Brugel sur sa désignation |
| Flandre (285 communes) | Décisions du régulateur flamand : désignations et décisions tarifaires 2026, qui listent les communes de chacun des huit gestionnaires Fluvius | Données ouvertes de Fluvius |
| Wallonie (261 communes) | 27 arrêtés de désignation du Gouvernement wallon, 15 pour l'électricité et 12 pour le gaz | Avis de la CWaPE, données ouvertes d'ORES, rapports des GRD, rapport Power BI de la CWaPE lu à la main |
| Toute la Belgique | Statbel : codes des communes, table des codes postaux, noms allemands | — |

*Hypothèses : version 2026.10.0 du jeu de données, publiée le 19 octobre 2026, à partir de sources relevées le 12 octobre. Sur 91 sources, 53 font foi, 32 servent de recoupement et 6 sont des jeux de données lisibles par machine. Notre relevé du rapport Power BI n'est pas publié, faute de licence indiquée : seule la concordance de chaque ligne wallonne l'est.*

En Flandre et en Wallonie, chaque attribution cite une source qui fait foi et une source d'un autre éditeur ; sinon, elle porte la mention « à confirmer ». Chaque liste officielle a aussi été transcrite deux fois, indépendamment, puis comparée.

## Les pièges rencontrés

### Un code postal n'est pas une commune

Statbel relie les codes postaux de bpost aux communes en superposant les cantons postaux aux limites communales : 1 149 codes donnent 1 152 paires. Trois codes couvrent deux communes : 1040 (Bruxelles et Etterbeek), 1050 (Bruxelles et Ixelles) et 1804 (Vilvorde et Zemst). La clé du fichier est donc le triplet code postal, code INS et section.

### Sections de commune

À Baerle-Duc (Baarle-Hertog), le gaz est distribué par le gestionnaire néerlandais Enexis, sauf dans la section de Zondereigen, desservie par Fluvius Kempen. Les deux sections partagent le code postal 2387 : seul leur nom les distingue.

### Fusion de communes : le GRD ne suit pas

Bertogne a rejoint Bastogne le 2 décembre 2024. L'arrêté de 2022 qui désigne ORES pour le gaz cite Bastogne, pas Bertogne, et ORES ne compte aucun point d'accès au gaz dans les codes postaux 6686 à 6688. La commune a donc deux sections, dont une sans GRD gaz.

Zwijndrecht a fusionné avec Beveren et Kruibeke le 1er janvier 2025, mais n'est passée de Fluvius Antwerpen à Fluvius Midden-Vlaanderen que le 1er janvier 2026. Le jeu de Fluvius, arrêté au 1er avril 2025, indique encore l'ancien gestionnaire : la date de changement inscrite dans la ligne explique l'écart.

### Code INS et GRD : le code change aussi

Les noms ne permettent pas de joindre les sources. Le rapport de la CWaPE écrit les communes en majuscules et sans accents, un arrêté de 2022 porte la coquille « Fosse-la-ville », et « Sibelgas » était, jusqu'au 31 décembre 2024, le nom de l'actuel Fluvius Halle-Vilvoorde, sans rapport avec Sibelga. Nous joignons donc sur le code INS de Statbel.

Mais ce code bouge aussi. Statbel comptait 581 communes jusqu'au 31 décembre 2024, et 565 depuis. Les communes fusionnées ont reçu un nouveau code : Bastogne (82003) et Bertogne (82005) forment le 82039. Seule Anvers a gardé le sien. Zwijndrecht passe de 11056 à 46030, car le premier chiffre désigne la province. Un fichier joint sur les codes de 2024 perd ces communes sans signaler d'erreur.

### Des dates d'effet antérieures à la publication

À Saint-Vith, RESA est le GRD gaz depuis le 1er juin 2026, en vertu d'un arrêté du 25 juin publié au Moniteur belge le 7 juillet. En Flandre, le régulateur a redésigné les huit gestionnaires Fluvius le 6 octobre 2026, avec effet au 5 septembre, et publié ses décisions le 3 novembre.

Notre relevé du 12 octobre ne pouvait pas les voir : une note de la version 2026.10.0 dit qu'aucune décision n'était publiée. Le 21 novembre, nous avons comparé leurs listes de communes à nos données : les 285 communes flamandes concordent. Les attributions tiennent ; la note, elle, est dépassée.

### Une désignation n'est pas un réseau

Habay, Ramillies, Villers-la-Ville et Comblain-au-Pont ont un GRD gaz désigné, que le rapport de la CWaPE n'affiche pas. À Walcourt et à Marchin, c'est l'inverse : la CWaPE indique un GRD gaz, mais nous n'avons trouvé aucun arrêté, d'où la mention « à confirmer ».

Le 12 octobre, le même rapport montrait encore ORES à Couvin, gérée par l'AIESH depuis le 1er janvier 2024, et à Brunehaut, passée à l'AIEG le 1er janvier 2026. À Namur et à Gesves, aucune source publique ne confirme encore l'échange de réseaux entre ORES et l'AIEG prévu au 1er juillet 2026 : « à confirmer », là aussi.

## Le modèle de données et les vecteurs de test

Une version est une release GitHub de dix fichiers. Le principal, `dso_lookup.csv`, compte 1 153 lignes de 22 colonnes. Autour de lui : le catalogue des opérateurs, 14 notes en quatre langues, les 91 sources avec leur empreinte SHA-256, 96 cas de test, le journal des changements et le rapport de validation. Voici les deux sections de Bastogne :

```text
postcode,ins,commune_fr,commune_nl,commune_de,region,province,section_key,section_fr,section_nl,section_de,elec_operator,elec_designated,gas_status,gas_operator,flags,note_key,source_ids,valid_from,first_seen,changed_at,data_version
6600,82039,Bastogne,Bastenaken,Bastnach,WAL,BE-WLX,bastogne,Bastogne,Bastenaken,Bastnach,ores,ores,designated,ores,,,agw-2022-06-09-ores-gaz|agw-ores-elec-2022|cwape-avis-0900-ores-gaz|cwape-powerbi-grd-elec-2026-10-12|cwape-powerbi-grd-gas-2026-10-12|odwb-ores-elec|odwb-ores-gas,,2026-10-19,2026-10-19,2026.10.0
6687,82039,Bastogne,Bastenaken,Bastnach,WAL,BE-WLX,bertogne,Bertogne,Bertogne,,ores,ores,none,,,bastogne-gas-territory,agw-2022-05-25-resa-gaz|agw-2022-06-09-ores-gaz|agw-ores-elec-2022|cwape-powerbi-grd-elec-2026-10-12|cwape-powerbi-grd-gas-2026-10-12|decret-2023-05-19-fusion-bastogne-bertogne|odwb-ores-elec|odwb-ores-gas,,2026-10-19,2026-10-19,2026.10.0
```

`elec_operator` est le gestionnaire qui exploite le réseau, celui de la facture ; `elec_designated`, celui que l'acte désigne. Le drapeau `operator_differs` signale un écart entre les deux. `gas_status` vaut `designated`, `none` ou `foreign` (Enexis).

La recherche a une implémentation de référence en Python et deux portages ligne à ligne, dans l'outil et dans l'application. Elle répond `not_found`, `choose_commune`, `choose_section` ou `ok`. Un code postal compte exactement quatre chiffres ASCII, sans le raccourci `\d`, qui accepte en Python les chiffres pleine chasse.

Les 96 cas de test fixent les réponses attendues. Le site exécute ses 73 cas « code postal » deux fois, sur le CSV et sur le fichier JSON que le build en tire. La version 2026.10.0 passe la validation sans erreur, avec 16 avertissements, tous expliqués.

Deux applications lisent la même version : le site, et l'application OptimCE, en alpha, qui propose le GRD d'électricité quand un gestionnaire de communauté ajoute un compteur. Une erreur se corrige donc à un seul endroit, le dépôt de données.

## Des dates de mise à jour fiables pour les moteurs de recherche

Google n'utilise la date `lastmod` d'un sitemap que « si elle est cohérente et vérifiable ». Bing a constaté en 2023 que 18 % des sitemaps qui la renseignent le font mal, le plus souvent avec la même date partout.

Chaque ligne du jeu porte donc deux dates, `first_seen` et `changed_at`, tirées d'une empreinte de ses colonnes de données : une ligne qui ne change pas garde ses dates. Aucune date ne vient de l'horloge, d'un fichier ou de git. Le tableau par commune prend la plus récente de trois dates : la sienne, celle de son gabarit et celle des données. À chaque déploiement, un script recalcule ces dates et les compare au sitemap. La mise à jour hebdomadaire des données construit le site deux fois et exige deux sitemaps identiques.

## Réutiliser les données et signaler une erreur

Le dépôt [belgian-dso-map](https://github.com/OptimCE/belgian-dso-map) publie les données sous licence CC BY 4.0 et les scripts sous Apache 2.0. Chaque version se télécharge avec ses empreintes :

```bash
curl -LO https://github.com/OptimCE/belgian-dso-map/releases/download/2026.10.0/dso_lookup.csv
curl -LO https://github.com/OptimCE/belgian-dso-map/releases/download/2026.10.0/SHA256SUMS
sha256sum --check --ignore-missing SHA256SUMS
```

- Créditez « belgian-dso-map, OptimCE », avec la version et sa date et un lien vers le dépôt, et indiquez si vous avez modifié les données.
- Gardez les mentions des sources, listées dans `ATTRIBUTION.md` : Statbel publie sous CC BY 4.0, Fluvius sous sa propre licence, sans garantie, et ORES demande d'être informé des réutilisations (indicateurs@ores.be).
- Lisez les fichiers de la release, pas le fichier JSON du site, dont le format est interne.

Une erreur ? [Ouvrez une issue](https://github.com/OptimCE/belgian-dso-map/issues) avec la commune, l'énergie et le document qui établit le bon gestionnaire, ou utilisez le lien « Signaler une erreur » de l'outil.

> ### Améliorer la liste des GRD
>
> Les données, leurs sources et leurs tests sont publics. Une commune mal attribuée ? Ouvrez une issue, avec le document qui fait foi.
>
> **[Signaler une erreur sur GitHub →](https://github.com/OptimCE/belgian-dso-map/issues)**

## FAQ

### Existe-t-il une liste officielle des GRD par commune en Belgique ?

Pas sous la forme d'un fichier unique, à notre connaissance. La CWaPE et Synergrid proposent une recherche par code postal, Fluvius publie un fichier pour la Flandre et Brugel désigne Sibelga à Bruxelles. OptimCE a réuni ces sources dans belgian-dso-map : 565 communes, électricité et gaz, chaque attribution sourcée, sous licence CC BY 4.0.

### Qu'est-ce que le code INS d'une commune, et pourquoi pas le code postal ?

Le code INS, ou code NIS, est le code à cinq chiffres que Statbel attribue à chaque commune ; son premier chiffre désigne la province. Le code postal vient de bpost : 1040, 1050 et 1804 couvrent chacun deux communes. Le code INS, complété au besoin par la section de commune, est donc la clé fiable pour trouver le GRD. Il change toutefois lors d'une fusion.

### Que devient le GRD quand des communes fusionnent ?

Rien d'automatique. À Bastogne, fusionnée avec Bertogne le 2 décembre 2024, ORES n'est désigné pour le gaz que dans l'ancienne commune de Bastogne : Bertogne n'a pas de GRD gaz. Zwijndrecht, fusionnée le 1er janvier 2025, n'a changé de gestionnaire qu'un an plus tard.

### Puis-je réutiliser la liste des GRD par commune dans mon application ?

Oui, sous licence CC BY 4.0 : créditez « belgian-dso-map, OptimCE » avec la version et sa date, ajoutez un lien vers le dépôt GitHub et indiquez si vous avez modifié les données. Les sources gardent leurs propres licences, listées dans ATTRIBUTION.md. Téléchargez les fichiers de la release, vérifiables par leurs empreintes SHA-256.

### Comment signaler une erreur dans la liste des GRD ?

Ouvrez une issue sur le dépôt GitHub belgian-dso-map avec la commune, l'énergie et, si possible, le document qui établit le bon gestionnaire. La correction passe par une pull request, puis par une nouvelle version que le site reprend. Sans compte GitHub, utilisez le lien « Signaler une erreur » sous chaque résultat de l'outil.

## Sources

- [OptimCE — belgian-dso-map, README](https://github.com/OptimCE/belgian-dso-map) — contrat de données (fichiers d'une version, colonnes, vocabulaires, dates de contenu, normalisation), algorithme de recherche et ses deux portages, règles de validation, licences (données sous CC BY 4.0, scripts sous Apache 2.0). Consulté le 21 novembre 2026.
- [OptimCE — belgian-dso-map, version 2026.10.0](https://github.com/OptimCE/belgian-dso-map/releases/tag/2026.10.0) — release du 19 octobre 2026 : les dix fichiers, leurs empreintes et le rapport de validation (aucune erreur, 16 avertissements expliqués, 96 cas de test), d'où viennent les comptes de cet article. Consulté le 21 novembre 2026.
- [OptimCE — belgian-dso-map, curation](https://github.com/OptimCE/belgian-dso-map/blob/main/curation/README.md) — double transcription des listes officielles, feuilles de 351, 368 et 571 lignes, alias de noms, relevé manuel du rapport Power BI de la CWaPE et règle de non-publication de ce relevé. Consulté le 21 novembre 2026.
- [Statbel — Géographie : codes des communes et codes postaux](https://statbel.fgov.be/fr/propos-de-statbel/methodologie/classifications/geographie) — nomenclature REFNIS : 581 communes du 1er janvier 2019 au 31 décembre 2024, 565 depuis le 1er janvier 2025, nouveau code de Bastogne valable depuis le 2 décembre 2024 ; méthode de la table de conversion entre codes postaux et communes (cantons postaux de bpost, communes du SPF Finances) et ses trois exceptions, 1040, 1050 et 1804. Consulté le 21 novembre 2026.
- [Statbel — REFNIS 2025 (CSV)](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2025.csv) et [REFNIS 2019 (CSV)](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2019.csv) — codes 82039 (Bastogne) et 46030 (Beveren-Kruibeke-Zwijndrecht) en 2025 ; codes 82003 (Bastogne), 82005 (Bertogne) et 11056 (Zwijndrecht) jusqu'en 2024. Consulté le 21 novembre 2026.
- [Statistiek Vlaanderen — Nieuwe NIS-codes voor gefuseerde gemeenten vanaf 1 januari 2025](https://www.vlaanderen.be/statistiek-vlaanderen/nieuwe-nis-codes-voor-gefuseerde-gemeenten-vanaf-1-januari-2025) (en néerlandais) — nouveaux codes des communes fusionnées, exception d'Anvers (11002 conservé), passage de Zwijndrecht dans la province de Flandre-Orientale. Consulté le 21 novembre 2026.
- [Fluvius — Netbeheerder en gas energie-inhoud per gemeente](https://opendata.fluvius.be/explore/dataset/1_23-dnb-per-gemeente-en-per-sector/) (en néerlandais) — gestionnaire de chaque commune flamande, 1 144 lignes, jeu modifié le 1er avril 2025, sous la licence open data de Fluvius, qui ne garantit ni l'exhaustivité ni l'exactitude des données. Consulté le 21 novembre 2026.
- [ORES sur Open Data Wallonie-Bruxelles — points de prélèvement d'électricité par localité](https://www.odwb.be/explore/dataset/ores-electricite-_nb-points-prelevement-par-localite-et-type-client-tension-annu/) et [de gaz par localité](https://www.odwb.be/explore/dataset/ores-gaz-nombre-de-points-de-prelevement-par-localite-annuel/) — localités desservies par ORES ; métadonnées « CC0 ». Consulté le 21 novembre 2026.
- [CWaPE — Trouver mon GRD](https://www.cwape.be/mon-grd) — recherche du gestionnaire de réseau par code postal, en Wallonie. Consulté le 21 novembre 2026.
- [CWaPE — Statistiques : GRD par commune](https://www.cwape.be/node/6468) — page du rapport Power BI « GRD par commune », sans licence indiquée. Consulté le 21 novembre 2026.
- [Synergrid — Le GRD dans votre commune](https://www.synergrid.be/fr/au-sujet-des-reseaux/le-grd-dans-votre-commune) — recherche nationale du gestionnaire de réseau par code postal ou par commune. Consulté le 21 novembre 2026.
- [Brugel — Le gestionnaire du réseau de distribution](https://www.brugel.brussels/brugel/grd-29) — Sibelga, seul gestionnaire de réseau de distribution d'électricité et de gaz de la Région de Bruxelles-Capitale. Consulté le 21 novembre 2026.
- [Vlaamse Nutsregulator — Aanwijzing netbeheerders](https://www.vlaamsenutsregulator.be/elektriciteit-en-aardgas/technische-reglementen-flexibiliteit-niet-publieke-netten/wie-is-mijn-netbeheerder/aanwijzing-netbeheerders) (en néerlandais) — page mise à jour le 12 novembre 2026 : désignation des huit gestionnaires Fluvius le 6 octobre 2026, pour douze ans à compter du 5 septembre 2026, avec la liste de leurs communes ; ancien nom de Fluvius Halle-Vilvoorde (« Sibelgas ») ; procédure de désignation d'Enexis à Baerle-Duc suspendue. Consulté le 21 novembre 2026.
- [Vlaamse Nutsregulator — BESL-2026-74](https://www.vlaamsenutsregulator.be/publicaties/besl-2026-74) (en néerlandais) — désignation de Fluvius Antwerpen, première des huit décisions (BESL-2026-74 à 81), publiée le 3 novembre 2026. Consulté le 21 novembre 2026.
- [Vlaamse Nutsregulator — BESL-2026-30](https://assets.vlaamsenutsregulator.be/2026-02/BESL-2026-30.pdf?VersionId=ElUWU7F1ROzPe0DBorhKohDkgVri6GOX) (en néerlandais) — Fluvius Midden-Vlaanderen désigné pour l'électricité et le gaz à Zwijndrecht, à la place de Fluvius Antwerpen, depuis le 1er janvier 2026. Consulté le 21 novembre 2026.
- [Décret du 19 mai 2023 relatif à la fusion des communes de Bastogne et de Bertogne](https://etaamb.openjustice.be/fr/decret-du-19-mai-2023_n2023203212.html) — article 2 : date de fusion fixée au 2 décembre 2024. Consulté le 21 novembre 2026.
- [Arrêté du Gouvernement wallon du 25 juin 2026](https://www.ejustice.just.fgov.be/cgi/article.pl?language=fr&sum_date=2026-07-07&lg_txt=F&numac_search=2026201749) — désignation de RESA comme gestionnaire de réseau de distribution de gaz pour Saint-Vith à partir du 1er juin 2026, publiée au Moniteur belge le 7 juillet 2026. Consulté le 21 novembre 2026.
- [Google Search Central — Créer et envoyer un sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=fr) — Google utilise la valeur `lastmod` si elle est cohérente et vérifiable, et ignore `priority` et `changefreq`. Consulté le 21 novembre 2026.
- [Bing Webmaster Blog — The Importance of Setting the “lastmod” Tag in Your Sitemap](https://blogs.bing.com/webmaster/february-2023/The-Importance-of-Setting-the-lastmod-Tag-in-Your-Sitemap) (en anglais) — billet de Fabrice Canel du 1er février 2023 : 18 % des sitemaps qui renseignent `lastmod` le font mal, l'erreur la plus courante étant une valeur identique pour toutes les adresses ; la date doit être celle de la modification de la page, pas celle de la génération du sitemap. Consulté le 21 novembre 2026.
- [Creative Commons — Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.fr) — licence du jeu de données compilé par OptimCE. Consulté le 21 novembre 2026.
