---
layout: post
title: "Simuler une clé de répartition : scénarios"
date: 2026-06-09 10:00:00 +0200
author: "Équipe OptimCE"
excerpt: "Nouvelle fonctionnalité OptimCE : simulez une clé de répartition sur vos données et mesurez autoconsommation, surplus, autosuffisance et taux de partage."
description: "Simulez une clé sur vos propres données et mesurez autoconsommation, surplus, autosuffisance et taux de partage avant de la valider."
tags: [allocation-key, app, news]
lang: fr
ref: optimce-allocation-key-simulation
faq:
  - q: "Qu'est-ce que la simulation d'une clé de répartition ?"
    a: "C'est le fait de rejouer des données réelles de production et de consommation à travers une clé de répartition choisie, sans l'appliquer en production, pour mesurer à l'avance ses indicateurs : autoconsommation collective, surplus, taux d'autosuffisance et taux de partage. C'est un outil de test « et si ? » avant de décider."
  - q: "Quelle différence entre simuler et générer une clé de répartition ?"
    a: "La génération automatique propose la meilleure clé à partir des données (brute force sur les clés standards ou algorithme LOGAAS). La simulation, elle, teste une clé que vous avez choisie sur un jeu de données donné et en affiche les indicateurs. Les deux sont complémentaires : on génère pour trouver un bon candidat, on simule pour comprendre et comparer des scénarios."
  - q: "Quelle est la différence entre taux d'autoconsommation, taux d'autosuffisance et taux de partage ?"
    a: "Le taux d'autoconsommation se mesure côté production : la part de l'énergie produite localement qui est consommée par les membres. Le taux d'autosuffisance se mesure côté consommation : la part de la consommation des membres couverte par la production locale. Le taux de partage indique quelle part de l'injection a effectivement été distribuée aux membres via la clé."
  - q: "Que signifient les résultats « par itération » ?"
    a: "Beaucoup de clés distribuent l'énergie en plusieurs tours (itérations) : un premier tour alloue selon la règle, puis l'énergie non consommée est redistribuée au tour suivant. La simulation montre le résultat global, par pas de temps et par itération, pour voir comment le partage progresse tour après tour."
  - q: "Quelles données faut-il importer pour lancer une simulation ?"
    a: "Un fichier CSV contenant la consommation au pas de temps (souvent au quart d'heure) de chaque membre et la production de chaque producteur de l'opération de partage. Chaque ligne correspond à un pas de temps. Quelques semaines de données donnent déjà un signal exploitable ; une année complète capture mieux la saisonnalité."
  - q: "La simulation modifie-t-elle ma clé de répartition en production ?"
    a: "Non. La simulation est un calcul « hors production » : elle ne touche ni à la clé appliquée par le gestionnaire de réseau, ni à vos données réelles. Vous testez autant de scénarios que vous voulez sans aucun effet sur l'opération de partage en cours."
---

Choisir une **clé de répartition**, c'est décider quart d'heure par quart d'heure qui reçoit quelle part de l'énergie produite localement. Mais comment savoir, *avant* de la mettre en place, si une clé donnée va réellement améliorer l'autoconsommation de votre communauté — ou laisser de la production filer sur le réseau ? La nouvelle fonctionnalité d'OptimCE répond à cette question : **simuler une clé de répartition** sur vos propres données et lire immédiatement ses indicateurs de performance.

L'idée est simple : vous importez un jeu de données, vous choisissez une clé, et la simulation rejoue chaque pas de temps à travers cette clé pour vous restituer l'**autoconsommation**, le **surplus**, le **taux d'autosuffisance** et le **taux de partage** — en résultats globaux, par pas de temps et par itération. Vous testez un scénario sans l'appliquer, sans risque, et vous décidez sur des chiffres plutôt que sur une intuition.

Si la notion même de clé de répartition est nouvelle pour vous, commencez par notre article de référence [« Clé de répartition en Belgique : les 3 régions »](/actualites/2026/05/19/cle-repartition-communaute-energie-belgique/) — il pose le vocabulaire repris ici.

## Pourquoi simuler une clé de répartition ?

Une clé de répartition n'est pas neutre : selon les profils de consommation et de production de la communauté, **la même clé peut créer beaucoup de valeur dans un projet et en détruire dans un autre**. Une clé fixe égalitaire convient parfaitement à dix ménages aux profils similaires, mais laisse des volumes inutilisés dès qu'un gros consommateur — une école, une PME, un bâtiment public — rejoint le groupe. À l'inverse, une clé dynamique récupère cette production perdue, au prix d'une part variable d'un mois à l'autre.

Le problème, c'est qu'**arbitrer à l'intuition est risqué**. Les courbes de production solaire et les profils de consommation se croisent de façon non triviale au pas de 15 minutes ; à l'œil nu, impossible de prédire si la clé A battra la clé B sur une année entière. Et l'enjeu est concret : chaque point d'autoconsommation gagné, c'est du surplus en moins réinjecté à bas prix, donc plus de valeur conservée dans la communauté.

Simuler, c'est précisément **sortir cet arbitrage du domaine de l'intuition**. Vous mesurez l'effet réel d'une clé sur les indicateurs qui comptent — autoconsommation, surplus, autosuffisance, taux de partage — avant d'engager quoi que ce soit. Pour comprendre pourquoi ces indicateurs sont au cœur de la valeur d'une communauté, voyez notre article [« Autoconsommation collective en Belgique »](/actualites/2026/06/05/autoconsommation-energie-belgique/).

## Ce que permet la simulation

La fonctionnalité s'intègre dans le **module « Clés de répartition »** du cœur open source d'OptimCE. Le flux utilisateur tient en quelques étapes :

1. **Importer un CSV** contenant les données de consommation au pas de temps (souvent au quart d'heure) pour chaque membre et les données de production pour chaque producteur de l'opération de partage. Chaque ligne du fichier correspond à un pas de temps.
2. **Choisir une clé de répartition** à tester — une clé standard de votre région, une clé existante de la communauté, ou un scénario que vous voulez explorer.
3. **Lancer la simulation.** OptimCE rejoue chaque pas de temps à travers la clé et ses différentes itérations, puis agrège les résultats.
4. **Lire les indicateurs** restitués, à trois niveaux de granularité : **global** (sur toute la période), **par pas de temps** (quart d'heure par quart d'heure) et **par itération** (tour après tour de la distribution).

Voici, en un coup d'œil, ce que vous fournissez et ce que vous obtenez :

| Vous importez | Vous obtenez |
|---|---|
| Consommation au pas de temps, par membre | Taux d'autoconsommation collective simulé |
| Production au pas de temps, par producteur | Surplus simulé (énergie injectée non partagée) |
| La clé de répartition à tester | Taux d'autosuffisance et taux de partage |
| | Détail global, par pas de temps et par itération |

Le résultat n'est pas une estimation théorique tirée d'un exemple type : il est calculé **sur vos propres données**. C'est ce qui rend la simulation utile pour décider.

## Lire les indicateurs

Quatre indicateurs résument la performance d'une clé. Ils sont simples une fois qu'on les distingue clairement — et c'est souvent là que naît la confusion.

### Le taux d'autoconsommation

Le **taux d'autoconsommation collective** se mesure **côté production** : c'est la part de l'énergie produite localement qui est effectivement consommée par les membres, plutôt qu'injectée sur le réseau. Plus il est élevé, mieux la production locale est valorisée au sein de la communauté.

### Le surplus

Le **surplus** est l'autre face de l'autoconsommation : c'est l'énergie injectée par les producteurs que **personne dans la communauté n'a consommée**, et qui repart donc sur le réseau public, généralement revendue à faible valeur. Le lien est direct : **plus la consommation locale absorbe la production, plus le surplus diminue**. Une bonne clé est celle qui réduit le surplus en orientant l'énergie vers les membres qui en ont besoin au bon moment.

### Le taux d'autosuffisance

Le **taux d'autosuffisance** se mesure **côté consommation** : c'est la part de la consommation des membres qui est couverte par la production locale partagée, plutôt qu'achetée au fournisseur. C'est le miroir de l'autoconsommation, vu depuis la facture des membres plutôt que depuis les panneaux.

### Le taux de partage et la lecture par itération

Le **taux de partage** indique quelle part de l'injection disponible a effectivement été **distribuée aux membres via la clé**. C'est là qu'intervient la lecture **par itération**. Beaucoup de clés distribuent en plusieurs tours : un premier tour alloue l'énergie selon la règle, puis l'énergie qu'un membre n'a pas consommée est **redistribuée au tour suivant** parmi ceux qui en demandent encore (c'est le principe des clés « plusieurs tours », relatives ou optimales). La simulation montre comment le taux de partage **progresse à chaque itération**, jusqu'à épuisement de l'injection partageable — vous voyez précisément ce qu'apportent les tours successifs.

Pour éviter toute confusion, ce tableau résume où se situe chaque indicateur :

| Indicateur | Se mesure… | Répond à la question |
|---|---|---|
| Taux d'autoconsommation | côté **production** | Quelle part de la production est consommée localement ? |
| Surplus | côté **production** | Quelle part de la production part sur le réseau ? |
| Taux d'autosuffisance | côté **consommation** | Quelle part de la consommation est couverte localement ? |
| Taux de partage | mécanique de la **clé** | Quelle part de l'injection a été distribuée, tour par tour ? |

## Quand utiliser la simulation ?

La simulation est utile à chaque étape de la vie d'une communauté d'énergie.

- **Avant le lancement.** Vous comparez plusieurs clés candidates sur des données historiques ou estimées et vous choisissez celle qui sert le mieux les objectifs du projet, en connaissance de cause.
- **Pendant la conception.** Vous arbitrez explicitement entre **équité** (une clé lisible, prévisible pour les membres) et **performance globale** (une clé qui maximise l'autoconsommation collective), chiffres à l'appui.
- **En phase d'animation.** Vous mesurez l'effet d'un **nouveau jeu de données** ou d'un **changement de profils** (un membre installe une pompe à chaleur, un autre une borne de recharge) sur les indicateurs — sans rien casser dans l'opération en cours.
- **À la mise à jour de la clé.** Lorsqu'un **membre rejoint ou quitte** la communauté, vous simulez la clé recalculée avant de la soumettre, pour vérifier qu'elle reste performante. Notre article sur la [clé de répartition en Belgique](/actualites/2026/05/19/cle-repartition-communaute-energie-belgique/) détaille la procédure de modification d'une clé après le démarrage, et le [guide de création d'une communauté en Wallonie](/actualites/2026/05/11/creer-communaute-energie-wallonie/) replace cette étape dans le dossier régulateur.

## La valeur pour les communautés

Pour un gestionnaire de communauté, un facilitateur ou un porteur de projet, la simulation change la manière de décider :

- **Une décision plus rapide et plus rationnelle.** Plus besoin de jongler entre tableurs de simulation et estimations approximatives : les indicateurs s'affichent directement dans l'outil qui gère déjà la communauté.
- **De la pédagogie.** En voyant *pourquoi* une clé fonctionne mieux qu'une autre sur des données réelles, les membres comprennent et adhèrent plus facilement au choix. La simulation transforme une discussion technique abstraite en démonstration concrète.
- **Un argumentaire solide.** Devant une assemblée générale, un gestionnaire de réseau ou un régulateur, défendre une clé chiffres à l'appui — tirés des données mêmes de la communauté — pèse bien plus qu'une recommandation de principe.

C'est aussi un levier pour valoriser la production locale, donc pour [réduire la facture d'électricité des membres](/actualites/2026/06/03/communaute-energie-reduire-facture-electricite/) : chaque point de surplus évité reste de la valeur dans la communauté.

## Simulation et génération automatique : deux outils complémentaires

OptimCE propose déjà un **module de génération automatique** qui *propose* la meilleure clé à partir des données — via un **brute force** sur les clés standards régionales et via **LOGAAS**, un algorithme issu de la recherche du CeCoTePe pour le projet Locomotrice. La simulation, elle, *teste* une clé que **vous** avez choisie.

Ce sont deux usages complémentaires, pas concurrents :

| | Simulation | Génération automatique |
|---|---|---|
| Question posée | « Que donne *cette* clé sur ces données ? » | « *Quelle* clé est la meilleure pour ces données ? » |
| Entrée | Une clé choisie + un CSV | Un CSV |
| Sortie | Les KPI de la clé testée | Une (des) clé(s) candidate(s) optimisée(s) |
| Usage type | Comparer des scénarios, comprendre, justifier | Trouver un bon point de départ |

En pratique, on génère pour trouver un candidat solide, puis on simule pour comprendre son comportement, comparer des variantes et le défendre. Pour le détail des algorithmes, voyez [« Générer une clé de répartition optimale »](/actualites/2026/05/26/generer-cle-repartition-optimale-optimce/).

## Les communautés d'énergie en Belgique, en bref

Une **communauté d'énergie** regroupe producteurs et consommateurs qui partagent localement une production renouvelable. Le partage est administratif : les compteurs communicants sont relevés au pas de **15 minutes**, et le **gestionnaire de réseau de distribution (GRD)** applique la clé de répartition choisie pour attribuer à chaque membre une part de l'énergie injectée. La Belgique reconnaît plusieurs formes — CER, CEC et, à Bruxelles, CEL — encadrées par les régulateurs régionaux ([Brugel](https://energysharing.brugel.brussels) à Bruxelles, avec [Sibelga](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie) comme gestionnaire de réseau).

Dans ce paysage, la clé de répartition est le paramètre central de la performance d'une communauté — et la simulation répond à un besoin réel : **structurer et comprendre le partage d'énergie** avant de l'engager. Pour le panorama complet des formes juridiques, voyez [« Communautés d'énergie en Belgique : CER, CEC, CEL »](/actualites/2026/05/11/communautes-energie-belgique/).

## Conclusion

La simulation de clé de répartition apporte une chose simple mais décisive : **la possibilité de tester avant de déployer**. Plutôt que de choisir une clé à l'intuition et d'en découvrir les effets après coup, vous mesurez à l'avance l'autoconsommation, le surplus, l'autosuffisance et le taux de partage sur vos propres données — globalement et tour par tour. C'est moins de risque, plus de pédagogie, et des décisions de gouvernance étayées par des chiffres.

> ### Simulez votre clé de répartition avec OptimCE
>
> Plateforme open source pensée pour les communautés d'énergie belges : simulez une clé sur vos données, comparez des scénarios, générez une clé optimale, historisez les opérations de partage et préparez le rapportage régulateur — le tout dans une seule application.
>
> **[Démarrer sur app.optimce.be →](https://app.optimce.be)**

## FAQ

### Qu'est-ce que la simulation d'une clé de répartition ?

C'est le fait de rejouer des données réelles de production et de consommation à travers une clé de répartition choisie, **sans l'appliquer en production**, pour mesurer à l'avance ses indicateurs : autoconsommation collective, surplus, taux d'autosuffisance et taux de partage. C'est un outil de test « et si ? » avant de décider.

### Quelle différence entre simuler et générer une clé de répartition ?

La **génération automatique** propose la meilleure clé à partir des données (brute force sur les clés standards ou algorithme LOGAAS). La **simulation** teste une clé que vous avez choisie sur un jeu de données donné et en affiche les indicateurs. Les deux sont complémentaires : on génère pour trouver un bon candidat, on simule pour comprendre et comparer des scénarios.

### Quelle est la différence entre taux d'autoconsommation, taux d'autosuffisance et taux de partage ?

Le **taux d'autoconsommation** se mesure côté production : la part de l'énergie produite localement qui est consommée par les membres. Le **taux d'autosuffisance** se mesure côté consommation : la part de la consommation des membres couverte par la production locale. Le **taux de partage** indique quelle part de l'injection a effectivement été distribuée aux membres via la clé.

### Que signifient les résultats « par itération » ?

Beaucoup de clés distribuent l'énergie en plusieurs tours (itérations) : un premier tour alloue selon la règle, puis l'énergie non consommée est redistribuée au tour suivant. La simulation montre le résultat **global**, **par pas de temps** et **par itération**, pour voir comment le partage progresse tour après tour.

### Quelles données faut-il importer pour lancer une simulation ?

Un fichier **CSV** contenant la consommation au pas de temps (souvent au quart d'heure) de chaque membre et la production de chaque producteur de l'opération de partage. Chaque ligne correspond à un pas de temps. Quelques semaines de données donnent déjà un signal exploitable ; une année complète capture mieux la saisonnalité.

### La simulation modifie-t-elle ma clé de répartition en production ?

Non. La simulation est un calcul « hors production » : elle ne touche ni à la clé appliquée par le gestionnaire de réseau, ni à vos données réelles. Vous testez autant de scénarios que vous voulez sans aucun effet sur l'opération de partage en cours.

## Sources

- [Brugel — Energy Sharing](https://energysharing.brugel.brussels) — portail officiel du régulateur bruxellois sur le partage d'énergie et le cadre des communautés d'énergie.
- [Brugel — Communautés d'énergie](https://energysharing.brugel.brussels/blog/energy-sharing-18/communautes-d-energie-406) — autorisation, durée de validité et cadre réglementaire à Bruxelles.
- [Sibelga — Le partage d'énergie en communauté](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie) — conditions, acteurs et principes du partage à Bruxelles.
- [IÖW — Self-consumption and self-sufficiency in energy sharing communities](https://www.ioew.de/en/publication/self_consumption_and_self_sufficiency_in_energy_sharing_communities_in_germany) — référence méthodologique sur les indicateurs d'autoconsommation et d'autosuffisance.
- [KPMG — Energy sharing in Belgium: overview and policy recommendations](https://kpmg.com/be/en/insights/industries/energy-natural-resources-insights/energy-sharing-in-belgium-overview-and-policy-recom.html) — vue d'ensemble du partage d'énergie en Belgique.
- [Pricing and sharing rules for energy communities](https://econpapers.repec.org/article/eeejuipol/v_3a96_3ay_3a2025_3ai_3ac_3as0957178725001109.htm) — recherche sur les règles de partage et les prix internes, qui justifie l'intérêt d'une simulation.
