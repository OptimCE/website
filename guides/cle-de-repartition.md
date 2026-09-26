---
layout: pillar
title: "Clé de répartition : comprendre, choisir, tester"
subtitle: "Ce que chaque région accepte, comment choisir une famille de clés, puis comment la tester sur vos propres données."
description: "Clé de répartition d'une communauté d'énergie : ce que la CWaPE, BRUGEL et le VREG acceptent, le choix d'une famille de clés, la génération et la simulation."
lang: fr
ref: pillar-cle-de-repartition
pillar: cle-de-repartition
permalink: /guides/cle-de-repartition/
breadcrumb_parent: guides
last_modified_at: 2026-09-26
sections:
  - title: "Comprendre la clé et ce que chaque région accepte"
    refs: [allocation-key-belgium]
  - title: "Générer et simuler votre clé avec OptimCE"
    refs: [optimce-allocation-key-generator, optimce-allocation-key-simulation]
---
Dans une opération de partage d'énergie, la **clé de répartition** est la règle de calcul, exprimée en pourcentages, qui attribue à chaque membre consommateur une part de l'énergie injectée par les producteurs. Elle n'a rien de physique : le gestionnaire de réseau de distribution (GRD) l'applique quart d'heure par quart d'heure aux relevés des compteurs communicants. Une seule clé s'applique par opération, et elle ne décide que des kWh : ce qu'ils valent en euros relève du [prix de cession interne]({{ "internal-price-shared-energy" | ref_url }}), fixé séparément dans la même convention.

La Belgique compte trois cadres, et notre [comparatif des trois régions]({{ "allocation-key-belgium" | ref_url }}) détaille ce que chacun admet :

- **Wallonie** : trois clés standards publiées par la CWaPE — fixe égalitaire, fixe spécifique, dynamique basée sur la consommation — que les GRD acceptent automatiquement ; toute autre clé doit être autorisée par la CWaPE.
- **Bruxelles** : trois méthodes opérées par Sibelga et prévues par BRUGEL — fixe (en un ou plusieurs tours), prorata, hybride —, modifiables à tout moment sur demande du point de contact unique.
- **Flandre** : pas de liste de clés « standards » publiée par le VREG ; le protocole Fluvius, qui fait foi, supporte trois *verdeelsleutels* : vaste, relatieve et optimale.

Derrière ces trois vocabulaires, on retrouve partout deux familles : les clés **fixes**, égalitaires ou pondérées selon les apports des membres, et les clés **dynamiques ou optimisées**, qui suivent la consommation réelle. Trancher entre elles n'est pas une question technique mais un choix de gouvernance : égalité entre membres, reconnaissance de l'investissement ou maximisation de l'autoconsommation collective. La diversité des profils compte aussi — dès qu'une école ou une PME rejoint le groupe, l'égalité stricte cesse d'être optimale —, tout comme la prévisibilité financière attendue par les membres. Enfin, les trois régions autorisent à modifier une clé après le démarrage : mieux vaut prévoir d'emblée une revue annuelle en assemblée générale.

Reste à confronter ces principes à vos propres profils, car une même clé peut récupérer 70 % de la production disponible dans une communauté et à peine 50 % dans une autre. OptimCE propose pour cela deux fonctionnalités, alimentées par un CSV de vos données de production et de consommation. La [génération automatique]({{ "optimce-allocation-key-generator" | ref_url }}) propose une clé candidate, soit en balayant les clés standards de votre région (brute force), soit avec l'algorithme LOGAAS, dont la clé non standard doit, en Wallonie, passer par la voie d'autorisation de la CWaPE. La [simulation]({{ "optimce-allocation-key-simulation" | ref_url }}) rejoue une clé que vous avez choisie et en restitue l'autoconsommation, le surplus, l'autosuffisance et le taux de partage, sans toucher à la clé appliquée par le gestionnaire de réseau. Aucune des deux ne transmet de clé au GRD : avenant, signatures et transmission restent entre vos mains.

Les guides ci-dessous suivent le même ordre : d'abord le cadre des trois régions, ensuite la génération et la simulation d'une clé sur vos données.
