---
layout: post
title: "Générer automatiquement une clé de répartition optimale avec OptimCE"
date: 2026-05-26 00:00:00 +0200
author: "Équipe OptimCE"
excerpt: "Le module de génération automatique d'OptimCE est en production. Il propose des clés de répartition optimisées à partir des données réelles de production et de consommation, avec deux algorithmes — brute force sur les clés standards et LOGAAS, issu de la recherche du CeCoTePe dans le projet Locomotrice."
tags: [allocation-key, app, guide]
lang: fr
ref: optimce-allocation-key-generator
---

Choisir la **clé de répartition** qui tire le meilleur d'une production locale est plus difficile qu'il n'y paraît. Le vocabulaire est posé par le régulateur, les clés standards sont listées dans un document CWaPE ou Fluvius, et pourtant le *bon* choix dépend de ce qu'aucun de ces textes ne peut vous dire : les profils réels, au quart d'heure, de vos membres. Un quartier résidentiel avec une seule école se comporte très différemment d'un parc d'entreprises avec une charge de base, et une même clé peut récupérer 70 % de la production disponible dans une communauté et à peine 50 % dans une autre.

Le **module de génération automatique de clés de répartition** d'OptimCE est désormais disponible pour sortir cette décision du domaine de l'intuition. Donnez-lui un CSV avec les données réelles de production et de consommation de la communauté, et il renvoie une clé candidate avec un taux d'autoconsommation collective attendu — calculé sur vos propres données, pas sur un exemple théorique. Deux algorithmes **indépendants** sont livrés aujourd'hui, tous deux consommant le même CSV : un **brute force** qui balaie les clés standards reconnues dans chaque région, et **LOGAAS**, une approche hybride d'optimisation linéaire et d'algorithme génétique développée par [**CeCoTePe**](https://cecotepe.be/) pour le projet **Locomotrice**. D'autres algorithmes pourront s'ajouter par la suite.

Si vous découvrez encore le paysage régulatoire — ce que CWaPE, BRUGEL et VREG considèrent comme une clé valide — commencez par notre article de référence [« Clé de répartition en Belgique : Wallonie, Bruxelles, Flandre »](/actualites/2026/05/19/cle-repartition-communaute-energie-belgique/).

## Pourquoi une clé de répartition mérite d'être pilotée par les données

Les cadres belges s'accordent sur un point : la clé de répartition s'applique **au quart d'heure**, sur les relevés réels des compteurs intelligents. Sa performance — le **taux d'autoconsommation collective**, la **part de l'énergie injectée effectivement consommée par les membres** — dépend donc entièrement de la façon dont chaque profil s'aligne avec la courbe de production.

Plusieurs raisons expliquent pourquoi le choix manuel sous-performe plus souvent qu'on ne le croit :

- **La diversité des profils s'élargit vite.** Une communauté qui démarre avec cinq ménages similaires est facile à servir avec une clé fixe égalitaire. Ajoutez un consommateur tertiaire (école, PME, bâtiment public) et la répartition égalitaire laisse aussitôt des volumes sur la table pendant les heures de bureau, alors que le gros consommateur aurait pu les absorber.
- **La production évolue.** Une extension de toiture, un changement d'onduleur, l'ajout d'une cogénération : chaque modification déplace la courbe. La clé optimale de l'an dernier peut être sous-optimale aujourd'hui.
- **Les clés standards ne sont pas interchangeables.** Les trois familles wallonnes (fixe égalitaire, fixe spécifique, dynamique) couvrent un large spectre de cas, mais la *meilleure* des trois pour une communauté donnée n'est pas évidente sans simulation. Idem pour les méthodes bruxelloises (fixe, prorata, hybride) et les *verdeelsleutels* flamands (vaste, relatieve, optimale).

La sélection manuelle a donc tendance à sous-utiliser la production disponible. Le rôle d'un module de génération automatique n'est pas de remplacer le jugement humain sur la gouvernance — c'est d'enlever le **coût de simulation** du choix. Une fois la clé candidate proposée, la communauté peut toujours voter, amender et affiner.

## Ce que fait le module OptimCE

Le module s'intègre dans le **module « Clés de répartition »** déjà présent dans le cœur open source d'OptimCE. Le workflow est direct :

1. **Entrée** — données de consommation au quart d'heure pour chaque membre, données de production au quart d'heure pour chaque producteur, liste des participants à l'opération de partage, et région (Wallonie / Bruxelles / Flandre) pour que l'algorithme respecte les familles de clés standards correspondantes.
2. **Choix d'un algorithme** — brute force ou LOGAAS.
3. **Exécution** — le module simule l'algorithme sélectionné sur les données réelles et renvoie une **clé candidate**, accompagnée du **taux d'autoconsommation collective attendu**, de la **part d'énergie partagée par membre** et de la **répartition de l'injection résiduelle**.
4. **Revue** — le gestionnaire de communauté peut comparer plusieurs candidats, ajuster les pourcentages et valider.
5. **Application** — la clé validée entre dans le module Clés de répartition comme un nouvel avenant, avec historisation complète et suivi du statut d'acceptation des membres.

Le module ne transmet **pas** une nouvelle clé au GRD de manière autonome. Il produit une proposition ; le workflow existant — avenant, signatures, transmission — reste en place, y compris l'étape d'autorisation régulateur pour les clés non standards en Wallonie.

## Algorithme 1 — Brute force sur les clés standards

Le premier algorithme est volontairement simple, et c'est précisément sa force.

Il construit un **ensemble de candidats** composé de toutes les clés standards autorisées dans la région de la communauté :

- En **Wallonie** : clé fixe égalitaire, clé fixe spécifique (pourcentages pondérés par les apports des membres), clé dynamique basée sur la consommation.
- À **Bruxelles** : méthode fixe (single-round et multi-round), méthode prorata, méthode hybride.
- En **Flandre** : *vaste verdeelsleutel*, *relatieve verdeelsleutel*, *optimale verdeelsleutel*.

Pour chaque candidat, l'algorithme **rejoue les données réelles au quart d'heure** à travers la règle de distribution correspondante et calcule le taux d'autoconsommation collective obtenu, la part que chaque membre aurait reçue et l'injection résiduelle. Le candidat le plus performant — par défaut, celui qui maximise l'autoconsommation collective — l'emporte, et le module remonte les suivants pour que la communauté puisse, si elle le souhaite, troquer quelques points de performance contre de la simplicité de gouvernance.

Le brute force a deux atouts majeurs :

- **Conforme au régulateur par construction.** La sortie est toujours l'une des clés standards, donc elle passe par la voie d'acceptation classique du GRD — aucune autorisation CWaPE non standard nécessaire en Wallonie.
- **Explicable.** Le résultat est une famille de clés connue, avec des propriétés connues. Vous pouvez le défendre devant une assemblée générale sans invoquer la théorie de l'optimisation.

Sa limite, c'est le catalogue lui-même. Si les profils d'une communauté sont atypiques — fortement asymétriques, très saisonniers, avec un consommateur dominant — la meilleure des clés standards peut malgré tout laisser une marge de performance significative. C'est là qu'intervient le second algorithme.

## Algorithme 2 — LOGAAS

**LOGAAS** signifie *Linear Optimization with Genetic Algorithm with Atypical Speciation*. Il est issu des travaux du [CeCoTePe](https://cecotepe.be/) pour le projet Locomotrice, formellement décrits dans le preprint *Paque, E. & Hiard, S. (2025), « LOGAAS : A hybrid algorithmic approach to ex-post electricity allocation for energy communities »*.

Là où le brute force est borné par le catalogue standard, LOGAAS explore un **espace plus large de clés candidates** — y compris des combinaisons non standards — en combinant **optimisation linéaire** (qui trouve la meilleure allocation ex-post pour une itération donnée) et **algorithme génétique** avec **spéciation atypique** (qui cherche la meilleure combinaison de pourcentages entre les jusqu'à trois itérations autorisées, en préservant la diversité de la population). En pratique, il peut aller chercher des points de performance là où les familles standards ne s'ajustent pas proprement aux profils : ensembles de membres très hétérogènes, gros consommateurs saisonniers associés à des ménages résidentiels, ou producteurs en surplus qui réinjecteraient sinon l'essentiel de leur production sur le réseau public.

LOGAAS produit une clé candidate **non standard**. En Wallonie, cela signifie que la communauté doit passer par la **voie d'autorisation CWaPE** avant que le GRD ne puisse l'appliquer — voir l'[article sur la clé de répartition en Belgique](/actualites/2026/05/19/cle-repartition-communaute-energie-belgique/) pour la procédure. À Bruxelles et en Flandre, la marge pour des clés non standards est plus étroite ; le résultat LOGAAS y sert souvent de **référence de performance** — à quoi pourrait ressembler le meilleur résultat possible — pour juger la clé standard retenue.

Utilisez LOGAAS quand le résultat du brute force est proche mais pas suffisant, quand les économies du projet dépendent des derniers points d'autoconsommation collective, ou quand vous voulez quantifier une borne supérieure pour étayer une décision d'investissement.

## Comparaison en un coup d'œil

| Critère | Choix manuel | Brute force | LOGAAS |
|---|---|---|---|
| Données requises | Liste des membres, cadre régional | Liste des membres + profils 15 min | Liste des membres + profils 15 min |
| Espace de recherche | Une clé pré-sélectionnée | Toutes les clés standards régionales | Combinaisons standards + non standards |
| Temps d'exécution | Instantané (pas de calcul) | Quelques secondes | Quelques minutes |
| Conforme au régulateur d'emblée | Oui (si standard) | Oui — toujours dans le catalogue standard | Wallonie : autorisation CWaPE requise. Bruxelles / Flandre : utilisé comme référence. |
| Explicabilité du résultat | Élevée | Élevée — famille de clés nommée | Plus faible — résultat numérique |
| Recommandé pour | Communauté homogène, projets orientés gouvernance | La plupart des projets — nouveau choix par défaut | Profils hétérogènes, projets critiques sur la performance |

Les deux algorithmes sont **deux manières indépendantes** de générer une clé à partir d'un même CSV — ce ne sont pas des étapes d'un pipeline. Le brute force est l'option par défaut, plus sûre, pour la plupart des projets ; LOGAAS est l'option à dégainer quand le catalogue standard laisse de la performance sur la table et qu'une clé non standard est envisageable.

## Comment utiliser le module

Le module est disponible dès aujourd'hui dans l'application OptimCE :

1. Ouvrez le module **Clés de répartition** de l'opération de partage à optimiser.
2. Cliquez sur **Générer une clé**. Importez un CSV avec les données de consommation au quart d'heure (par membre) et de production (par producteur).
3. Choisissez un algorithme — brute force ou LOGAAS. Les deux s'exécutent indépendamment sur le même CSV ; vous pouvez comparer leurs sorties côte à côte.
4. Lancez. Examinez la clé candidate, son taux d'autoconsommation collective attendu et la table des parts par membre.
5. Validez la clé candidate pour lancer le workflow d'avenant : signature des membres, transmission au GRD par le représentant, prise d'effet à la date convenue.

Toute la boucle, de l'import des données à l'avenant, vit dans OptimCE — plus de jonglage entre tableurs de simulation, gouvernance et rapportage.

## Et après ?

Le module est construit autour d'une interface d'algorithmes branchables, donc ajouter de nouvelles approches ne demande pas de toucher au cœur. Pistes plausibles pour les prochaines versions : **optimisation multi-objectifs** (équilibre entre autoconsommation collective et équité par membre), **variantes contraintes par l'équité** (plafonnement de l'écart entre membres les mieux et les moins servis) et **simulation par scénarios** (test d'une clé face à un turnover de membres ou à une croissance de production). Chaque ajout sera annoncé à sa sortie.

> ### Générez votre clé de répartition avec OptimCE
>
> Plateforme open source pensée pour les communautés d'énergie belges : génération de clés basée sur les données, historique des opérations de partage, suivi des acceptations membres et préparation du rapportage régulateur — dans une seule application.
>
> **[Démarrer sur app.optimce.be →](https://app.optimce.be)**

## FAQ — Génération automatique de clés de répartition

### Quelles données faut-il fournir au module ?

Les données de **consommation** au quart d'heure pour chaque membre, les données de **production** au quart d'heure pour chaque producteur de l'opération de partage, la liste des participants et la région. Quelques semaines de données suffisent pour un signal exploitable ; une année complète capture mieux les effets saisonniers.

### Quel algorithme choisir ?

Par défaut, prenez le **brute force** : rapide, totalement explicable, et il reste dans le catalogue standard accepté automatiquement par le GRD. Choisissez **LOGAAS** si vous voulez explicitement explorer au-delà du catalogue standard — profils hétérogènes, équilibre économique tendu, ou besoin de savoir combien de performance le catalogue standard laisse de côté. Les deux s'exécutent indépendamment sur le même CSV ; rien n'empêche de lancer les deux et de comparer.

### La clé générée sera-t-elle conforme au régulateur ?

La sortie du brute force est toujours l'une des clés standards régionales — directement acceptée par le GRD sans autorisation supplémentaire. La sortie de LOGAAS est une clé non standard ; en Wallonie, elle doit passer par la **voie d'autorisation CWaPE** avant que le GRD ne l'applique. À Bruxelles et en Flandre, les clés non standards ne sont pas la voie habituelle ; le résultat LOGAAS y sert le plus souvent de référence de performance.

### Peut-on modifier la clé suggérée avant de l'appliquer ?

Oui. Le module renvoie une **clé candidate**, pas une décision contraignante. Vous pouvez ajuster les pourcentages, changer de famille de clés ou remplacer entièrement le choix de l'algorithme avant de le pousser dans le workflow d'avenant.

### Le module remplace-t-il le jugement d'expert ?

Non. Le module quantifie les arbitrages ; il ne décide pas si votre communauté privilégie l'équité sur la performance, la prévisibilité sur l'optimisation ou la simplicité sur le dernier point d'autoconsommation. Ce sont des choix de gouvernance. Le module raccourcit la boucle technique pour que l'assemblée puisse consacrer sa réunion à la question de gouvernance plutôt qu'au calcul.

### À quelle fréquence relancer l'algorithme ?

Un bon rythme est **annuel**, idéalement avant l'assemblée générale qui approuve les avenants de l'opération de partage. Relancez plus tôt si la communauté grandit, si un producteur est ajouté ou retiré, ou si un membre change significativement de profil de consommation (installation d'une pompe à chaleur, cession d'un site industriel…).

## À retenir

Le module de génération automatique transforme le choix de la clé de répartition d'exercice théorique en décision pilotée par les données. Le **brute force** trouve la meilleure clé standard pour les profils réels de la communauté — rapide, explicable, conforme au régulateur. **LOGAAS** explore au-delà du catalogue standard quand les économies du projet ont besoin de chaque point. Ensemble, ils donnent aux gestionnaires de communauté un outil pour défendre leur choix devant l'assemblée générale, le GRD et le régulateur — chiffres à l'appui, tirés des données mêmes de la communauté.

Pour aller plus loin, voyez nos guides complémentaires :

> **[Clé de répartition en Belgique : Wallonie, Bruxelles, Flandre](/actualites/2026/05/19/cle-repartition-communaute-energie-belgique/)**
>
> Le primer régulatoire — ce que CWaPE, BRUGEL et VREG acceptent, les trois vocabulaires régionaux et comment choisir une famille de clés avant de laisser OptimCE l'optimiser.

> **[Comment créer une communauté d'énergie en Wallonie : guide étape par étape](/actualites/2026/05/11/creer-communaute-energie-wallonie/)**
>
> Cadrer le projet, choisir entre CER et CEC, notifier la CWaPE et lancer le partage — et où la clé de répartition s'insère dans le dossier.

> **[Comment rejoindre une communauté d'énergie en Wallonie : guide pratique](/actualites/2026/05/11/rejoindre-communaute-energie-wallonie/)**
>
> Où trouver une opération ouverte, étapes d'adhésion et points à vérifier avant de signer la convention de partage.

## Sources

- Paque, E. & Hiard, S. (2025). *LOGAAS : A hybrid algorithmic approach to ex-post electricity allocation for energy communities*. Preprint CeCoTePe — description formelle de l'algorithme, de sa fonction objectif et des résultats de simulation sur données synthétiques de communautés d'énergie.
- [CeCoTePe](https://cecotepe.be/) — centre de recherche à l'origine de l'algorithme LOGAAS, partenaire du projet Locomotrice.
- [CWaPE — Liste des clés de répartition standards](https://www.cwape.be/publications/document/5382) — proposition CD-23d27-CWaPE-0928 du 27 avril 2023, liste canonique des clés standards en Wallonie.
- [Sibelga — Méthodes de répartition pour le partage d'énergie](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methodes-de-repartition) — méthodes fixe, prorata et hybride à Bruxelles.
- [Fluvius — Protocol energiedelen, persoon-aan-persoonverkoop](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf) — protocole technique flamand (v3.x, juillet 2024).
