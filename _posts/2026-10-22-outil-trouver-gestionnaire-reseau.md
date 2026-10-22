---
layout: post
title: "Nouvel outil : trouver son gestionnaire de réseau"
date: 2026-10-22 06:00:00 +0200
author: "Eric d'OptimCE"
excerpt: "Qui gère le réseau d'électricité et de gaz de votre commune ? Notre outil gratuit répond à partir du code postal, pour les 565 communes de Belgique, dans votre navigateur et sans compte."
description: "Trouver son gestionnaire de réseau d'électricité et de gaz avec son code postal : notre outil gratuit couvre les 565 communes belges, sans compte."
tags: [app, announcement, news]
lang: fr
ref: dso-tool-launch
faq:
  - q: "Existe-t-il un outil gratuit pour connaître son GRD en Belgique ?"
    a: "Oui. L'outil « Quel est mon GRD ? » d'OptimCE est gratuit et ne demande aucun compte : vous entrez votre code postal et il affiche le gestionnaire de réseau d'électricité et celui du gaz naturel de votre commune. Il couvre les 565 communes de Belgique, à Bruxelles, en Flandre et en Wallonie."
  - q: "Mon code postal est-il enregistré quand j'utilise l'outil ?"
    a: "Non. La recherche se fait dans votre navigateur, qui charge une fois toutes les données de l'outil : votre code postal n'est envoyé à aucun serveur. Il n'apparaît dans l'adresse de la page que pour vous permettre de copier le lien du résultat, et le message « Signaler une erreur » ne le contient pas. Notre mesure d'audience ne reçoit que la région et les gestionnaires trouvés."
  - q: "Pourquoi l'outil me demande-t-il ma commune ou ma section de commune ?"
    a: "Parce que votre code postal ne suffit pas toujours. Trois codes postaux couvrent deux communes : 1040 (Bruxelles et Etterbeek), 1050 (Bruxelles et Ixelles) et 1804 (Vilvorde et Zemst). À Baerle-Duc, le gestionnaire du gaz dépend de la section de commune : Enexis, un gestionnaire néerlandais, sauf à Zondereigen, desservie par Fluvius Kempen. L'outil vous pose alors la question avant d'afficher le résultat."
  - q: "Que faire si l'outil donne un mauvais gestionnaire de réseau ?"
    a: "Signalez-le avec le lien « Signaler une erreur » placé sous le résultat : il ouvre un e-mail vers contact@optimce.be qui indique la version des données, sans votre code postal. Pour vérifier en attendant, regardez votre facture de décompte ou de clôture d'électricité : pour un ménage, elle donne le nom et le numéro de téléphone du gestionnaire de réseau à appeler en cas de panne."
  - q: "L'outil sera-t-il intégré à l'application OptimCE ?"
    a: "C'est prévu. Quand un gestionnaire de communauté d'énergie ajoutera un compteur dans l'application, celle-ci proposera le gestionnaire de réseau de la commune, qu'il pourra corriger. En attendant, l'outil reste accessible à tous, gratuitement, sur le site optimce.be."
---

Pour trouver son gestionnaire de réseau d'électricité et de gaz, un code postal suffit désormais. Notre outil gratuit [« Quel est mon GRD ? »](/outils/quel-est-mon-grd/) donne, pour chacune des 565 communes belges, le gestionnaire de réseau de distribution (GRD) d'électricité et celui du gaz naturel. La recherche se fait dans votre navigateur, sans compte. L'outil inaugure la rubrique [Outils](/outils/) du site.

## Ce que fait l'outil

Vous entrez votre code postal. Le résultat sépare l'électricité et le gaz, avec le nom et le site web de chaque gestionnaire, puis donne les points à savoir pour votre commune, le régulateur et ses tarifs, la façon de vérifier sur votre facture et ce que permet le partage d'énergie dans votre région. Un bouton copie le lien du résultat, pour l'envoyer à un voisin ou à un futur membre de votre communauté.

Il répond pour une commune ou une section de commune, pas pour une adresse : il ne dit pas si le gaz passe dans votre rue et ne couvre pas les entreprises raccordées directement au réseau d'Elia. Sans JavaScript, le [tableau des GRD par commune](/outils/quel-est-mon-grd/communes/) donne les mêmes informations.

## Pourquoi nous l'avons construit

La question « qui gère mon réseau ? » revient à des moments précis.

- **Au déménagement**, le gestionnaire peut changer, et ses tarifs avec lui. En Wallonie, pour 3 500 kWh par an au compteur simple, la distribution seule coûte en 2026 environ 400 € TVAC chez l'AIEG, 433 € chez ORES et 495 € chez l'AIESH (synthèse tarifaire de la CWaPE, hors transport et surcharges).
- **En cas de panne**, on appelle le GRD, pas le fournisseur. Pour un ménage, son nom et son numéro figurent sur la facture de décompte ou de clôture (arrêté royal du 9 décembre 2021, article 4, 7°). Notre guide [« Lire sa facture d'électricité ligne par ligne »](/guides/comprendre-facture-electricite-ligne-par-ligne/) aide à les retrouver.
- **Dans un projet de partage d'énergie**, le GRD reçoit la demande, signe la convention avec le représentant du partage, transmet les données de comptage et applique la clé de répartition (CWaPE). Le porteur de projet doit donc savoir de quel gestionnaire dépend chaque participant.

Les réponses officielles existent, mais région par région. En Wallonie, la CWaPE propose une recherche « Trouver mon GRD » par code postal. En Flandre, le régulateur publie la liste des communes de chacun des huit gestionnaires Fluvius. À Bruxelles, Sibelga est le seul gestionnaire désigné (Brugel). Nous voulions une seule réponse pour les trois régions, électricité et gaz ensemble, avec ses sources.

## GRD par commune : les cas particuliers

Une commune, un gestionnaire : la règle a ses exceptions, et l'outil les traite.

| Cas | Exemple | Ce que fait l'outil |
|---|---|---|
| Un code postal pour deux communes | 1040 (Bruxelles et Etterbeek), 1050 (Bruxelles et Ixelles), 1804 (Vilvorde et Zemst) | Il demande votre commune |
| Un gestionnaire selon la section de commune | Baerle-Duc : gaz par Enexis, gestionnaire néerlandais, sauf à Zondereigen (Fluvius Kempen) | Il demande votre section |
| Un gestionnaire pour l'électricité, un autre pour le gaz | 22 communes, dont Verviers, Eupen, Wavre et Couvin | Il affiche les deux |
| Aucun GRD gaz désigné | 85 communes (84 en Wallonie, plus Fourons en Flandre) et l'ancienne commune de Bertogne, à Bastogne | Il l'indique |
| Changement de gestionnaire en 2026 | Brunehaut (électricité : l'AIEG remplace ORES), Saint-Vith (gaz : RESA, premier GRD désigné), Beveren-Kruibeke-Zwijndrecht (Fluvius Midden-Vlaanderen) | Mention « Changement récent de gestionnaire » |
| Changement prévu, pas encore confirmé | Namur et Gesves : échange de réseaux entre ORES et l'AIEG prévu au 1er juillet 2026 | Mention « Information à confirmer » |

*Hypothèses : comptes établis sur la version 2026.10.0 des données, publiée le 19 octobre 2026 ; ils changent avec chaque nouvelle version. Une commune est comptée sans GRD gaz quand aucune de ses sections n'en a.*

## D'où viennent les données, et comment signaler une erreur

Chaque réponse repose sur des documents publics : arrêtés publiés au Moniteur belge, décisions du régulateur flamand, avis de la CWaPE et de Brugel, publications des gestionnaires, données ouvertes de Statbel, de Fluvius et d'ORES. La version actuelle cite 91 sources relevées le 12 octobre 2026 : 53 références légales, 32 recoupements et 6 jeux de données ouvertes. Le [tableau par commune](/outils/quel-est-mon-grd/communes/#sources) les liste toutes.

Quand nos sources ne suffisent pas, l'outil le dit. À Walcourt et à Marchin, la CWaPE indique un gestionnaire de gaz, mais nous n'avons trouvé aucun arrêté qui le désigne : le résultat porte la mention « Information à confirmer ».

Le jeu de données compilé est publié sous licence CC BY 4.0 dans le dépôt [belgian-dso-map](https://github.com/OptimCE/belgian-dso-map) sur GitHub : chacun peut le réutiliser en citant la source. Chaque résultat affiche la version des données. Si une réponse vous semble fausse, le lien « Signaler une erreur », sous le résultat, ouvre un e-mail vers contact@optimce.be qui contient la version des données, jamais votre code postal.

## La suite : l'outil dans l'application

Nous prévoyons d'intégrer la même recherche à l'application OptimCE : quand un gestionnaire de communauté ajoutera un compteur, l'application proposera le GRD de la commune, qu'il pourra corriger. OptimCE couvre aujourd'hui le cadre wallon ; Bruxelles et la Flandre sont prévues, mais pas encore implémentées.

Vous portez un projet de partage ? Nos guides expliquent comment [créer une communauté d'énergie en Wallonie](/guides/creer-communaute-energie-wallonie/) ou [en rejoindre une](/guides/rejoindre-communaute-energie-wallonie/), et la page [Fonctionnalités](/fonctionnalites/) présente ce que l'application gère au quotidien.

> ### Trouvez votre gestionnaire de réseau
>
> Un code postal suffit pour connaître le GRD d'électricité et de gaz de votre commune. Gratuit, sans compte.
>
> **[Essayer « Quel est mon GRD ? » →](/outils/quel-est-mon-grd/)**

## FAQ

### Existe-t-il un outil gratuit pour connaître son GRD en Belgique ?

Oui. L'outil « Quel est mon GRD ? » d'OptimCE est gratuit et ne demande aucun compte : vous entrez votre code postal et il affiche le gestionnaire de réseau d'électricité et celui du gaz naturel de votre commune. Il couvre les 565 communes de Belgique, à Bruxelles, en Flandre et en Wallonie.

### Mon code postal est-il enregistré quand j'utilise l'outil ?

Non. La recherche se fait dans votre navigateur, qui charge une fois toutes les données de l'outil : votre code postal n'est envoyé à aucun serveur. Il n'apparaît dans l'adresse de la page que pour vous permettre de copier le lien du résultat, et le message « Signaler une erreur » ne le contient pas. Notre mesure d'audience ne reçoit que la région et les gestionnaires trouvés.

### Pourquoi l'outil me demande-t-il ma commune ou ma section de commune ?

Parce que votre code postal ne suffit pas toujours. Trois codes postaux couvrent deux communes : 1040 (Bruxelles et Etterbeek), 1050 (Bruxelles et Ixelles) et 1804 (Vilvorde et Zemst). À Baerle-Duc, le gestionnaire du gaz dépend de la section de commune : Enexis, un gestionnaire néerlandais, sauf à Zondereigen, desservie par Fluvius Kempen. L'outil vous pose alors la question avant d'afficher le résultat.

### Que faire si l'outil donne un mauvais gestionnaire de réseau ?

Signalez-le avec le lien « Signaler une erreur » placé sous le résultat : il ouvre un e-mail vers contact@optimce.be qui indique la version des données, sans votre code postal. Pour vérifier en attendant, regardez votre facture de décompte ou de clôture d'électricité : pour un ménage, elle donne le nom et le numéro de téléphone du gestionnaire de réseau à appeler en cas de panne.

### L'outil sera-t-il intégré à l'application OptimCE ?

C'est prévu. Quand un gestionnaire de communauté d'énergie ajoutera un compteur dans l'application, celle-ci proposera le gestionnaire de réseau de la commune, qu'il pourra corriger. En attendant, l'outil reste accessible à tous, gratuitement, sur le site optimce.be.

## Sources

- [CWaPE — Les gestionnaires de réseaux](https://www.cwape.be/node/160) — liste des cinq GRD d'électricité actifs en Wallonie (AIEG, AIESH, ORES, RESA, REW), dont deux, ORES et RESA, distribuent aussi le gaz ; missions du GRD ; lien vers la recherche « Trouver mon GRD ». Consulté le 21 octobre 2026.
- [CWaPE — Trouver mon GRD](https://www.cwape.be/mon-grd) — recherche du gestionnaire de réseau par code postal, sur le site du régulateur wallon. Consulté le 21 octobre 2026.
- [CWaPE — Synthèse des tarifs de réseaux 2026, électricité (TVAC)](https://www.cwape.be/sites/default/files/cwape-documents/SYNTHESE%20DES%20TARIFS%20DE%20DISTRIBUTION%20ELEC%202026%20(TVAC-pdf)_0.pdf) — tarifs des clients résidentiels raccordés en basse tension, du 1er janvier au 31 décembre 2026, mise à jour du 5 janvier 2026. Source du terme fixe (19,50 € par an chez l'AIEG, 14,10 € chez ORES, 17,93 € chez l'AIESH) et du terme proportionnel en compteur simple (10,86965, 11,98070 et 13,63965 c€/kWh) dont nous tirons les montants pour 3 500 kWh, le profil de consommation retenu dans nos autres articles. Le document précise que les tarifs de réseau sont proposés par les GRD et approuvés par la CWaPE. Consulté le 21 octobre 2026.
- [Vlaamse Nutsregulator — Aanwijzing netbeheerders](https://www.vlaamsenutsregulator.be/elektriciteit-en-aardgas/technische-reglementen-flexibiliteit-niet-publieke-netten/wie-is-mijn-netbeheerder/aanwijzing-netbeheerders) (en néerlandais) — désignations des gestionnaires de réseau de distribution en Flandre, avec les communes de chacun, et le cas du gaz à Baerle-Duc, exploité par le gestionnaire néerlandais Enexis. Consulté le 21 octobre 2026.
- [Brugel — Le gestionnaire du réseau de distribution](https://www.brugel.brussels/brugel/grd-29) — désignation de Sibelga comme seul gestionnaire de réseau de distribution d'électricité et de gaz naturel de la Région de Bruxelles-Capitale. Consulté le 21 octobre 2026.
- [CWaPE — Partage d'énergie](https://www.cwape.be/node/5618) — rôle du gestionnaire de réseau dans une opération de partage : demande, convention avec le représentant, transmission des données de comptage et application de la clé de répartition. Consulté le 21 octobre 2026.
- [Arrêté royal du 9 décembre 2021 fixant les autres exigences minimales auxquelles doivent répondre les factures](https://www.ejustice.just.fgov.be/eli/arrete/2021/12/09/2021022724/justel) — article 4, 7° : les factures de décompte et de clôture des clients résidentiels donnent le nom et le numéro de téléphone du GRD à contacter en cas de panne d'électricité. Consulté le 21 octobre 2026.
- [ORES Assets — Rapport annuel 2025](https://media.ores.be/ores-cms/ueqhj4jd/ores-assets-rapport-annuel-2025.pdf) — page 79 : le transfert de Brunehaut vers l'AIEG pour la gestion du réseau d'électricité est entré en vigueur le 1er janvier 2026. Consulté le 21 octobre 2026.
- [Arrêté du Gouvernement wallon du 25 juin 2026](https://www.ejustice.just.fgov.be/cgi/article.pl?language=fr&sum_date=2026-07-07&lg_txt=F&numac_search=2026201749) — désignation de RESA comme gestionnaire de réseau de distribution de gaz pour Saint-Vith, à partir du 1er juin 2026. Consulté le 21 octobre 2026.
- [Vlaamse Nutsregulator — Décision BESL-2026-30](https://assets.vlaamsenutsregulator.be/2026-02/BESL-2026-30.pdf?VersionId=ElUWU7F1ROzPe0DBorhKohDkgVri6GOX) (en néerlandais) — désignation définitive de Fluvius Midden-Vlaanderen pour l'électricité et le gaz dans la section de Zwijndrecht, à la place de Fluvius Antwerpen, en vigueur depuis le 1er janvier 2026. Consulté le 21 octobre 2026.
- [ORES Assets — Assemblée générale du 21 mai 2026, point 6 : transfert de réseaux Namur et Gesves](https://media.ores.be/ores-cms/depfic4r/20260521-ag-ores-assets-point-06-transfert-r%C3%A9seaux-namur-et-gesves.pdf) — échange de réseaux entre ORES et l'AIEG à Namur (Flawinne, Marche-les-Dames, Saint-Marc et Vedrin) et à Gesves, prévu au 1er janvier 2026 ou, à défaut, au 1er juillet 2026. Consulté le 21 octobre 2026.
- [Statbel — Code REFNIS 2025](https://statbel.fgov.be/sites/default/files/Over_Statbel_FR/Nomenclaturen/REFNIS_2025.csv) — nomenclature des unités administratives en vigueur depuis le 1er janvier 2025 : 565 communes. Consulté le 21 octobre 2026.
- [Creative Commons — Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.fr) — licence du jeu de données compilé par OptimCE ; les sources gardent leurs propres licences. Consulté le 21 octobre 2026.
