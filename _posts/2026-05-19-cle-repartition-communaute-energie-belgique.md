---
layout: post
title: "Clé de répartition en Belgique : Wallonie, Bruxelles, Flandre"
date: 2026-05-19 10:00:00 +0200
author: "Équipe OptimCE"
excerpt: "Clé de répartition d'une communauté d'énergie : types CWaPE, BRUGEL, VREG, différences Wallonie / Bruxelles / Flandre et conseils pour choisir."
tags: [allocation-key, administrative]
lang: fr
ref: allocation-key-belgium
---

La **clé de répartition** est le rouage discret qui transforme une production locale d'électricité en avantage tangible pour chaque membre d'une communauté d'énergie. Elle décide, quart d'heure par quart d'heure, *qui reçoit combien* d'énergie partagée. Et c'est précisément là que la Belgique se complique : la Wallonie, Bruxelles et la Flandre n'ont pas adopté la même grille de clés standards, n'utilisent pas le même vocabulaire, et n'imposent pas les mêmes règles de validation.

Cet article fait le tour des trois cadres régionaux — **CWaPE / ORES / RESA / AIEG** en Wallonie, **BRUGEL / Sibelga** à Bruxelles, **VREG / Fluvius** en Flandre — pour comparer ce qui est réellement permis dans chaque région et aider les gestionnaires de communauté à choisir une clé qui tienne dans le temps. Si vous découvrez la notion même de communauté d'énergie, commencez par notre article [« Communautés d'énergie en Belgique : CER, CEC, CEL expliqués »](/actualites/2026/05/11/communautes-energie-belgique/) — il pose le vocabulaire repris ici.

## Clé de répartition : rappel rapide

Une **clé de répartition** est la règle de calcul, exprimée en pourcentages, qui détermine comment l'énergie injectée sur le réseau par les producteurs d'une opération de partage est attribuée à chacun des consommateurs membres. Elle n'est pas physique : les électrons continuent de circuler normalement sur le réseau public. C'est administratif et virtuel, calculé par le **gestionnaire de réseau de distribution (GRD)** à partir des relevés des compteurs communicants au **pas de 15 minutes**.

Concrètement, pour chaque quart d'heure :

1. Le GRD relève l'énergie **injectée** par les producteurs de la communauté.
2. Il relève l'énergie **prélevée** par chaque consommateur.
3. Il applique la **clé de répartition** validée par la communauté pour attribuer une part du volume injecté à chaque consommateur.
4. Le volume partagé attribué à chaque membre est transmis à son **fournisseur d'énergie**, qui le valorise au tarif interne de la communauté plutôt qu'au tarif standard.

Cette logique vaut pour toutes les configurations de partage d'énergie : **autoconsommation collective intra-bâtiment**, **CER**, **CEC** et **CEL** (à Bruxelles). Pour une présentation détaillée du fonctionnement administratif, voir la page de référence de la [CWaPE sur la répartition des volumes partagés](https://www.cwape.be/node/6068).

Le rôle stratégique d'une clé est donc double : **distribuer équitablement** une ressource limitée entre les membres et **maximiser la consommation locale** d'une production locale. Mais le « bon » équilibre dépend du projet : un quartier résidentiel autour d'une toiture photovoltaïque communale n'a pas les mêmes besoins qu'un parc d'entreprises raccordé à une cogénération.

## Le cadre wallon : trois clés standards validées par la CWaPE

En Wallonie, le partage d'énergie est encadré par le décret du 12 avril 2001 sur l'organisation du marché régional de l'électricité (article 35sexdecies, § 2). Sur cette base, la [CWaPE](https://www.cwape.be/secteur/communautes-partage-energie) a publié — en concertation avec les gestionnaires de réseau — une **liste de clés de répartition standards** que les GRD acceptent automatiquement. Le document de référence est la [proposition CD-23d27-CWaPE-0928 du 27 avril 2023](https://www.cwape.be/publications/document/5382).

### Les trois clés standards wallonnes

| Clé | Logique | Adaptée à |
|---|---|---|
| **Clé fixe égalitaire** | Volume partagé divisé à parts égales entre tous les participants. Adaptation automatique à l'arrivée ou au départ d'un membre. | Projets citoyens où l'équité est la priorité. |
| **Clé fixe spécifique** | Pourcentages prédéfinis, souvent calés sur les **quotes-parts d'investissement** dans les unités de production. | Coopératives, parcs d'entreprises co-financés, configurations où certains membres ont investi davantage. |
| **Clé dynamique basée sur la consommation** | Répartition au prorata de la consommation réelle de chaque membre durant le quart d'heure. Avantage les gros consommateurs en heures de production. | Projets mixtes où l'objectif est de **maximiser l'autoconsommation collective**. |

### Clés non standards

La communauté peut **proposer une clé alternative**, mais elle doit alors être **autorisée spécifiquement** : ORES, RESA ou AIEG la transmet à la CWaPE qui valide ou demande des ajustements. Cette voie reste minoritaire ; en pratique, les trois clés standards couvrent l'écrasante majorité des projets wallons.

### Modifier une clé après le démarrage

C'est possible. Le **représentant de la communauté** introduit la demande auprès du GRD, les membres signent un **avenant à la convention de partage**, et le changement prend effet à la date convenue avec le gestionnaire de réseau. La page [ORES — Le partage d'énergie en pratique](https://www.ores.be/professionnel/en-pratique) détaille les modalités opérationnelles côté gestionnaire.

Pour la procédure complète de création et la place de la clé dans la notification CWaPE, voyez notre guide [« Créer une communauté d'énergie en Wallonie : guide étape par étape »](/actualites/2026/05/11/creer-communaute-energie-wallonie/).

## Le cadre bruxellois : méthodes fixe, prorata et hybride

À Bruxelles, le régulateur est [BRUGEL](https://www.brugel.brussels/themes/energies-renouvelables-11/partage-d-energie-420) et le gestionnaire de réseau unique est **Sibelga**. Le cadre bruxellois reconnaît trois configurations de partage — **CEL (Communauté d'Énergie Locale)**, **autoconsommation collective intra-bâtiment** et **vente de pair à pair (P2P)** — et **trois méthodes de répartition** sont opérées par Sibelga pour les deux premières (le P2P, lui, ne nécessite pas de clé).

### Les trois méthodes officielles à Bruxelles

| Méthode | Logique | Spécificité bruxelloise |
|---|---|---|
| **Méthode fixe** | Pourcentage constant attribué à chaque participant par quart d'heure. Variante **« 1 tour »** (distribution unique) ou **« plusieurs tours »** (l'énergie non consommée est redistribuée parmi ceux qui n'ont pas saturé leur allocation). | La variante « plusieurs tours » améliore le taux d'autoconsommation collective. |
| **Méthode prorata** | Répartition au prorata de la consommation individuelle sur le quart d'heure. Si votre consommation représente **20 % du total** du groupe, vous recevez **20 % de l'injection** disponible. | Distribution en **un seul tour**. |
| **Méthode hybride** | Combinaison séquentielle : d'abord une allocation **fixe**, puis le surplus est redistribué au **prorata** parmi les participants encore en demande. | Compromis entre prévisibilité (fixe) et optimisation (prorata). |

L'exemple type donné par [Sibelga](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methodes-de-repartition) — 1 producteur, 4 consommateurs, clé fixe — attribue **25 % de l'injection à chaque consommateur** par quart d'heure. Si l'un d'eux consomme moins que sa quote-part, la variante « plusieurs tours » redistribue le solde aux trois autres.

### Modification et facturation

La méthode peut être **modifiée à tout moment** sur demande du point de contact unique de l'opération. C'est aussi ce point de contact unique qui prend en charge la **facturation interne** aux membres à partir des données mensuelles fournies par Sibelga — Sibelga n'arbitre pas, il calcule et transmet.

Pour le contexte économique et l'impact tarifaire à Bruxelles, voyez l'analyse de [Renouvelle sur les coûts-avantages du partage d'électricité à Bruxelles](https://www.renouvelle.be/fr/quels-couts-avantages-sur-le-partage-delectricite-et-les-communautes-denergie-a-bruxelles/) et l'[étude 2024 sur le potentiel des communautés d'énergie bruxelloises](https://document.environnement.brussels/opac_css/elecfile/RAP_2024_CommunautesEnergie.pdf).

## Le cadre flamand : verdeelsleutel selon le protocole Fluvius

En Flandre, le régulateur est le [VREG](https://www.vlaamsenutsregulator.be) et le gestionnaire de réseau Fluvius. Le cadre s'applique au **partage d'énergie** (*energiedelen*) entre membres d'un groupe, à la **vente de pair à pair** (*persoon-aan-persoonverkoop*) et aux **communautés d'énergie** (CER et CEC, traduites en *hernieuwbare-energiegemeenschap* et *burgerenergiegemeenschap*).

Côté technique, le pas de 15 minutes et l'obligation d'un **compteur digital « meetregime 3 »** sont la règle. Trois clés — appelées *verdeelsleutels* — sont supportées par le [protocole Fluvius](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf).

### Les trois verdeelsleutels

| Verdeelsleutel | Équivalent FR | Logique |
|---|---|---|
| **Vaste verdeelsleutel** | Clé fixe | Pourcentage prédéfini par participant pour chaque quart d'heure. |
| **Relatieve verdeelsleutel** | Clé relative | Clé fixe **+ un tour de redistribution** : l'énergie injectée non consommée par les uns est répartie au prorata parmi les participants qui n'ont pas saturé leur quote-part. |
| **Optimale verdeelsleutel** | Clé optimale | Démarre de la clé convenue mais **itère plusieurs tours** jusqu'à épuisement complet de l'injection disponible sur le quart d'heure. Maximise le taux d'autoconsommation collective. |

Le gestionnaire du groupe choisit la clé en fonction de la **puissance installée chez chaque participant**, du **nombre de membres**, de la **production attendue**, des **apports financiers** et d'autres critères locaux. Les accords doivent être documentés et communiqués à tous les membres avant la mise en service.

Différence pratique avec la Wallonie : la Flandre n'a **pas de liste de clés « standards » publiée comme telle par le VREG** ; c'est le protocole opérationnel Fluvius qui fait foi, et chaque communauté définit sa clé dans ce cadre. Pour des éclairages réglementaires côté Wallonie touchant aussi à la Flandre, voir la [décision CWaPE sur les clés de répartition entre Flandre et Wallonie](https://www.cwape.be/documents-recents/decision-relative-lapprobation-de-la-proposition-de-cles-de-repartition-entre) pour les configurations transfrontalières.

## Tableau récapitulatif : les trois régions en un coup d'œil

| Critère | Wallonie | Bruxelles | Flandre |
|---|---|---|---|
| Régulateur | **CWaPE** | **BRUGEL** | **VREG** |
| GRD | ORES / RESA / AIEG | **Sibelga** (unique) | **Fluvius** (unique) |
| Documentation de référence | Proposition CD-23d27-CWaPE-0928 (27/04/2023) | Page « Méthodes de répartition » de Sibelga | Protocole Fluvius v3.x (juillet 2024) |
| Clé n°1 — Égalitaire | Clé fixe égalitaire | Méthode fixe (1 tour, parts égales) | Vaste verdeelsleutel |
| Clé n°2 — Pourcentages spécifiques | Clé fixe spécifique | Méthode fixe (pourcentages prédéfinis) | Vaste verdeelsleutel (pourcentages négociés) |
| Clé n°3 — Logique « optimisation » | **Clé dynamique** (prorata consommation) | **Méthode prorata** + **méthode hybride** | **Relatieve** + **Optimale verdeelsleutel** |
| Clés non standards | Possible avec autorisation CWaPE | Modification possible à tout moment | Définies dans le cadre du protocole Fluvius |
| Compteur communicant | Obligatoire | Obligatoire | Compteur digital « meetregime 3 » |
| Pas de calcul | 15 minutes | 15 minutes | 15 minutes |

Trois cadres, trois vocabulaires, mais une **convergence forte sur le fond** : tous reposent sur le quart d'heure et le compteur communicant, et tous offrent au minimum une famille **« fixe »** et une famille **« dynamique / optimisée »**. Les nuances comptent surtout pour la gouvernance et la prévisibilité financière des membres.

## Comment choisir sa clé de répartition ?

Aucune clé n'est universellement « meilleure ». Le bon choix dépend du projet, des membres et des objectifs. Voici quatre questions à se poser, valables dans les trois régions.

### 1. Quel est l'objectif politique du partage ?

- **Égalité et solidarité** — chacun reçoit la même part, indépendamment de ce qu'il consomme : **clé fixe égalitaire** (Wallonie), **méthode fixe 25/25/25/25** (Bruxelles), **vaste verdeelsleutel** (Flandre).
- **Reconnaissance de l'investissement** — les membres qui ont financé les panneaux récupèrent une part plus grande : **clé fixe spécifique** (Wallonie), **méthode fixe avec pourcentages négociés** (Bruxelles / Flandre).
- **Maximisation de l'autoconsommation** — utiliser au mieux chaque kWh produit localement : **clé dynamique** (Wallonie), **méthode prorata ou hybride** (Bruxelles), **relatieve ou optimale verdeelsleutel** (Flandre).

### 2. Quelle est la diversité des profils de consommation ?

Un quartier résidentiel avec des profils similaires (chacun ~3 500 kWh/an) fonctionne très bien en **clé fixe égalitaire**. Mais dès qu'un gros consommateur entre dans la communauté — une école, une commune, une PME — l'égalité stricte cesse d'être optimale : la part allouée au gros consommateur reste sous-utilisée pendant que ses voisins paient leur surplus au tarif marché. Dans ce cas, basculer vers une **clé dynamique / prorata / optimale** récupère ce qui se perdait.

### 3. Quelle prévisibilité financière les membres attendent-ils ?

Les clés **fixes** offrent une lecture immédiate : « j'ai droit à X % du partage chaque quart d'heure ». Les clés **dynamiques / optimales** offrent une meilleure performance globale mais une part variable d'un mois à l'autre. Si vous communiquez à des ménages peu familiers de l'énergie, la prévisibilité d'une clé fixe simplifie l'adhésion. Si vos membres sont aguerris (coopérative, parc d'entreprises), la clé dynamique se défend mieux.

### 4. Quelle souplesse pour faire évoluer la clé ?

Les **trois régions autorisent la modification** d'une clé après le démarrage. En Wallonie, l'avenant à la convention + le passage par le GRD prennent quelques semaines ; à Bruxelles et en Flandre, la modification est annoncée par le point de contact unique au gestionnaire de réseau. Évitez les clés trop rigides au lancement : prévoyez d'emblée une revue annuelle en assemblée générale.

### Quatre cas pratiques typiques

| Profil de communauté | Wallonie | Bruxelles | Flandre |
|---|---|---|---|
| Quartier résidentiel + 1 toiture PV communale | Clé fixe égalitaire | Méthode fixe | Vaste verdeelsleutel |
| Coopérative avec apports différents | Clé fixe spécifique | Méthode fixe (pourcentages investis) | Vaste verdeelsleutel (pourcentages investis) |
| Mix résidentiel + 1 école / PME consommatrice | Clé dynamique | Méthode prorata ou hybride | Relatieve verdeelsleutel |
| Production excédentaire à valoriser localement | Clé dynamique | Méthode hybride | Optimale verdeelsleutel |

## Configurer, suivre et faire évoluer la clé : le rôle d'un outil dédié

Une clé de répartition n'est pas une décision prise une fois pour toutes. Elle vit avec la communauté : un membre entre, un autre part, la production augmente après l'ajout d'une nouvelle toiture, l'assemblée générale révise les pourcentages, le régulateur valide une clé non standard. Chaque changement implique un **avenant à la convention**, une **transmission au GRD** et une **trace historique** que la communauté doit conserver pour son rapportage annuel.

C'est précisément ce qu'**OptimCE** outille au cœur de l'application. Le **module « Clés de répartition »** du noyau open source permet de :

- **Configurer la clé** directement sur une opération de partage, en cohérence avec les types reconnus dans votre région (CWaPE en Wallonie, Sibelga à Bruxelles, Fluvius en Flandre).
- **Suivre l'historique** complet des clés appliquées au fil du temps — utile pour les avenants, les recalculs en cas de litige et le rapportage régulateur.
- **Tracer le statut d'acceptation** de chaque membre face à une nouvelle clé : qui a signé l'avenant, qui n'a pas encore validé, qui a refusé.

Le **module de génération automatique** est désormais disponible : à partir des **données réelles de production et de consommation** des membres, il propose des clés candidates optimisées — via un **brute force** sur les clés standards régionales et via **LOGAAS**, une approche par algorithme génétique développée par **CeCoTePe** dans le cadre du projet de recherche **Locomotrice**. Voir notre guide dédié : [« Générer automatiquement une clé de répartition optimale avec OptimCE »](/actualites/2026/05/26/generer-cle-repartition-optimale-optimce/).

> ### Pilotez vos clés de répartition avec OptimCE
>
> Plateforme open source pensée pour les communautés d'énergie belges : configuration des clés, historique des opérations de partage, statut d'acceptation des membres et préparation du rapportage régulateur — le tout dans une seule application.
>
> **[Démarrer sur app.optimce.be →](https://app.optimce.be)**

## FAQ — Clé de répartition

### Peut-on changer de clé de répartition après le démarrage ?

Oui, dans les trois régions. Il faut signer un **avenant à la convention** de partage entre les membres concernés, puis transmettre la nouvelle clé au GRD via le **représentant** (Wallonie) ou le **point de contact unique** (Bruxelles, Flandre). Le changement prend effet à la date convenue avec le gestionnaire de réseau, typiquement quelques semaines après la demande.

### La clé est-elle calculée à l'année, au mois ou au quart d'heure ?

Au **quart d'heure**, dans les trois régions. Le GRD relève l'injection des producteurs et la consommation des consommateurs sur chaque créneau de 15 minutes, applique la clé, et agrège ensuite les volumes partagés au mois pour transmission aux fournisseurs.

### Si la production excède la consommation des membres, que devient le surplus ?

L'énergie injectée non consommée par la communauté est **réinjectée sur le réseau** et revendue par le fournisseur du producteur au tarif de rachat en vigueur. Une **clé dynamique** (Wallonie), **hybride** (Bruxelles) ou **optimale** (Flandre) réduit ce surplus en maximisant la consommation locale, mais ne l'élimine pas totalement.

### Peut-on mélanger plusieurs clés au sein d'une même communauté ?

Au sein d'une **même opération de partage**, une seule clé s'applique. En revanche, une **même communauté d'énergie** peut héberger **plusieurs opérations de partage** (par exemple : une opération intra-bâtiment + une CER de quartier), chacune avec sa propre clé. C'est l'un des intérêts du modèle juridique belge.

### Faut-il faire valider la clé par le régulateur ?

En **Wallonie**, les **clés standards** sont acceptées automatiquement par le GRD ; les **clés non standards** doivent être autorisées par la CWaPE. À **Bruxelles**, les trois méthodes opérées par Sibelga sont prévues par BRUGEL et ne demandent pas d'autorisation supplémentaire. En **Flandre**, la clé est définie dans le cadre du protocole Fluvius et n'exige pas de validation préalable du VREG.

### Quelle clé recommander pour une petite communauté de quartier ?

Pour une dizaine de ménages aux profils similaires autour d'une toiture photovoltaïque commune, la **clé fixe égalitaire** (Wallonie) / **méthode fixe** (Bruxelles) / **vaste verdeelsleutel** (Flandre) est très souvent le bon point de départ. Elle est lisible pour les membres, robuste aux entrées/sorties, et évite les débats sur les pourcentages. Une revue annuelle permettra d'évaluer s'il faut passer à une clé plus dynamique.

### Que se passe-t-il quand un nouveau membre rejoint la communauté ?

La clé est **recalculée** pour intégrer le nouveau membre. Avec une **clé fixe égalitaire**, le pourcentage de chacun baisse mécaniquement (10 % à 5 membres → 9,09 % à 11 membres). Avec une **clé fixe spécifique**, les pourcentages doivent être renégociés. Avec une **clé dynamique / optimale**, l'intégration est automatique puisque la répartition suit la consommation réelle. Un avenant à la convention formalise l'arrivée dans tous les cas.

## Ce qu'il faut retenir

Trois régulateurs (CWaPE, BRUGEL, VREG), trois gestionnaires de réseau de référence (ORES/RESA/AIEG, Sibelga, Fluvius), trois vocabulaires (« clé », « méthode », « verdeelsleutel ») — mais une mécanique commune au quart d'heure, dépendante des compteurs communicants, et organisée autour de deux grandes familles : les clés **fixes** (égalitaires ou pondérées) et les clés **dynamiques / optimisées** (prorata, hybride, optimale).

Le choix d'une clé n'est pas une question technique : c'est un choix politique de gouvernance, qui doit refléter les valeurs et les contraintes des membres. Et parce qu'aucune clé n'est figée, il faut un outil pour la configurer, l'historiser, la faire évoluer proprement — et désormais la **générer automatiquement à partir des données réelles** de la communauté : c'est exactement ce qu'**OptimCE** propose aujourd'hui.

Pour aller plus loin, consultez nos guides :

> **[Générer automatiquement une clé de répartition optimale avec OptimCE](/actualites/2026/05/26/generer-cle-repartition-optimale-optimce/)**
>
> Le prolongement pratique — comment le brute force et LOGAAS trouvent la meilleure clé de répartition à partir des données réelles de production et de consommation d'une communauté.

> **[Communautés d'énergie en Belgique : CER, CEC, CEL expliqués](/actualites/2026/05/11/communautes-energie-belgique/)**
>
> Le panorama complet des formes juridiques, des directives européennes et du fonctionnement opérationnel du partage d'énergie en Belgique.

> **[Créer une communauté d'énergie en Wallonie : guide étape par étape](/actualites/2026/05/11/creer-communaute-energie-wallonie/)**
>
> Choix entre CER et CEC, cadrage du projet, notification à la CWaPE, accusé de réception et démarrage du partage avec ORES, RESA ou AIEG — dont la place de la clé de répartition dans le dossier.

> **[Rejoindre une communauté d'énergie en Wallonie : guide pratique](/actualites/2026/05/11/rejoindre-communaute-energie-wallonie/)**
>
> Où trouver une opération ouverte, démarches d'adhésion, points de vigilance avant de signer la convention de partage.

## Sources

- [CWaPE — Liste de clés de répartition standards permettant la répartition des volumes partagés](https://www.cwape.be/publications/document/5382) — proposition CD-23d27-CWaPE-0928 du 27 avril 2023.
- [CWaPE — Comment l'électricité partagée est-elle répartie entre les participants ?](https://www.cwape.be/node/6068) — principe de la répartition et rôle d'une clé de répartition.
- [CWaPE — Partage d'énergie](https://www.cwape.be/node/5618) — synthèse sur le partage d'énergie en Wallonie.
- [CWaPE — Communautés d'énergie et partage d'énergie](https://www.cwape.be/secteur/communautes-partage-energie) — portail général wallon.
- [CWaPE — Répartition des volumes partagés : liste des clés de répartition standards](https://www.cwape.be/documents-recents/repartition-des-volumes-partages-liste-des-cles-de-repartition-standards) — version courte du document de référence.
- [CWaPE — Décision relative à l'approbation de la proposition de clés de répartition entre Flandre et Wallonie](https://www.cwape.be/documents-recents/decision-relative-lapprobation-de-la-proposition-de-cles-de-repartition-entre) — cas transfrontalier.
- [ORES — Le partage d'énergie en pratique](https://www.ores.be/professionnel/en-pratique) — explication pratique des clés fixes, spécifiques et dynamiques.
- [BRUGEL — Partage d'énergie](https://www.brugel.brussels/themes/energies-renouvelables-11/partage-d-energie-420) — cadre réglementaire bruxellois.
- [Sibelga — Le partage d'énergie renouvelable à Bruxelles](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie) — page pratique bruxelloise.
- [Sibelga — Les méthodes de répartition pour le partage d'énergie](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methodes-de-repartition) — méthodes fixe, prorata et hybride.
- [Bruxelles Environnement — Étude relative au potentiel, au développement et au fonctionnement des communautés d'énergie](https://document.environnement.brussels/opac_css/elecfile/RAP_2024_CommunautesEnergie.pdf) — étude de fond 2024.
- [VREG — Vlaamse Nutsregulator](https://www.vlaamsenutsregulator.be) — régulateur flamand.
- [Fluvius — Protocole energiedelen, persoon-aan-persoonverkoop](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf) — protocole technique v3.x (juillet 2024).
- [Renouvelle — Coûts et avantages du partage d'électricité et des communautés d'énergie à Bruxelles](https://www.renouvelle.be/fr/quels-couts-avantages-sur-le-partage-delectricite-et-les-communautes-denergie-a-bruxelles/) — analyse économique.
