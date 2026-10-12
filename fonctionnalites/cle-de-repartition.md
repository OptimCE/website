---
layout: page
title: "Clé de répartition : générer, simuler, suivre"
breadcrumb_title: "Clé de répartition"
subtitle: "De la première proposition à l'avenant : créer, générer, tester et faire évoluer la clé de votre communauté au même endroit."
description: "Générez, simulez et suivez la clé de répartition de votre communauté d'énergie : données au quart d'heure, deux algorithmes, versions et acceptation."
lang: fr
ref: product-allocation-key
permalink: /fonctionnalites/cle-de-repartition/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Quelle différence entre générer et simuler une clé ?"
    a: "La génération part de vos données et propose une clé candidate, avec le taux d'autoconsommation collective attendu. La simulation part d'une clé que vous avez choisie et mesure ce qu'elle aurait donné sur vos données. On génère pour chercher une clé, on simule pour vérifier celle qu'on envisage."
  - q: "Quelles données faut-il pour générer ou simuler une clé ?"
    a: "Un fichier CSV de consommation et de production au quart d'heure, avec une colonne par consommateur et une colonne pour la production injectée, dont vous indiquez le nom. C'est le pas de temps de la répartition en Belgique : 96 valeurs par jour et par compteur."
  - q: "La clé générée est-elle envoyée au gestionnaire de réseau ?"
    a: "Non. OptimCE propose une clé, il ne l'envoie jamais seule au gestionnaire de réseau. Une nouvelle clé suit le circuit habituel de l'avenant ; OptimCE en garde chaque version et suit son acceptation par les membres."
  - q: "Qu'est-ce que LOGAAS ?"
    a: "LOGAAS est l'un des deux algorithmes de génération, issu de la recherche du CeCoTePe dans le projet Locomotrice. Il combine optimisation linéaire et algorithme génétique, et ses réglages avancés ont des valeurs par défaut qui conviennent à la plupart des usages. L'application l'affiche sous le nom « OLAGSA ». L'autre algorithme parcourt les clés standards de votre région."
---

La clé de répartition décide, quart d'heure par quart d'heure, qui reçoit quelle part de la
production locale. La choisir n'est qu'un début : il faut la faire accepter par les membres, la
tester sur des données réelles, puis la faire évoluer par avenant au fil des arrivées et des
départs. Dans un tableur, ses coefficients vivent dans des fichiers qu'on recopie et qu'on finit
par ne plus savoir dater. OptimCE couvre tout ce cycle de vie. Nos guides expliquent comment
choisir une clé ; cette page montre où chaque étape se fait dans l'outil.

## Comment OptimCE s'en charge

### Créer une clé

Une clé se construit de deux façons : dans une grille complète, ou avec un assistant pas à pas.
Les deux aboutissent à la même clé. L'assistant demande le nombre de consommateurs et leur nom,
puis des itérations : chacune répartit un pourcentage de l'énergie disponible, par exemple au
prorata de la consommation réelle de chacun, jusqu'à atteindre 100 %. Une page de revue montre la
grille complète avant l'enregistrement.

{% include product-shot.html name="key-wizard" alt="Grille de revue d'une clé créée avec l'assistant : une première itération de 70 % puis une seconde de 30 % de l'énergie, réparties au prorata entre trois consommateurs." caption="Une clé en deux itérations au prorata, relue avant son enregistrement (données de test)." %}

### Générer une clé candidate

À partir d'un fichier CSV de consommation et de production au quart d'heure, le module de
génération propose une clé candidate, avec le taux d'autoconsommation collective attendu. Deux
algorithmes sont disponibles :

- le **parcours exhaustif des clés standards** de votre région ;
- **LOGAAS** (affiché « OLAGSA » dans l'application), issu de la recherche du CeCoTePe dans le
  projet Locomotrice, qui combine optimisation linéaire et algorithme génétique.

Le premier reste dans le catalogue des clés standards de votre région. Le second cherche aussi en
dehors de ce catalogue : il peut trouver un meilleur partage, mais la clé qu'il propose demande
alors une procédure particulière (voir plus bas).

La génération est mise en file d'attente, puis la liste des clés calculées apparaît, chacune avec
le détail de sa répartition par itération. Vous enregistrez celle qui vous convient dans vos clés
de répartition. Le module de génération s'active parmi les services annexes de la communauté.

{% include product-shot.html name="key-generation" alt="Formulaire « Lancer une génération » : l'algorithme « Optimisation Linéaire et Algorithme Génétique avec Spéciation Atypique » est sélectionné, avec le nom de la génération, la colonne d'injection « Production » et la zone d'import du fichier de données." caption="Le lancement d'une génération : l'algorithme, la colonne de production et le fichier de données (données de test)." %}

### Simuler une clé sur vos données

La simulation part d'une clé de votre choix et la rejoue sur votre propre fichier, sans toucher à
la clé appliquée. Vous lisez l'autoconsommation, le surplus, le taux d'autosuffisance et le taux de
partage, au global, par pas de temps et par itération. Le détail par consommateur montre
l'allocation, la consommation, l'énergie autoconsommée, le surplus et le volume résiduel : c'est
là qu'on compare deux répartitions avant de proposer un avenant.

### Suivre les versions et l'acceptation

Chaque version de la clé est historisée, et l'acceptation par les membres est suivie. Quand un
membre arrive ou part, la nouvelle version s'ajoute à l'historique au lieu de remplacer
l'ancienne. Une clé proposée par l'outil ne part jamais seule chez le gestionnaire de réseau :
elle suit le circuit habituel de l'avenant, comme une clé construite à la main.

## Ce que ça ne fait pas

**Rien n'est envoyé au gestionnaire de réseau.** OptimCE prépare et conserve la clé ; sa
transmission suit la procédure de l'avenant, que la communauté mène elle-même.

**Pas de temps réel.** La génération et la simulation travaillent sur les fichiers que vous
importez, pas sur des mesures en direct.

**La génération propose, elle ne décide pas.** Le choix de la clé reste celui de la communauté et
de ses membres. Une clé qui sort du catalogue standard suit en Wallonie une procédure particulière :
le guide de génération la détaille.

**Une simulation vaut ce que vaut le fichier.** Elle rejoue la période et les profils que vous lui
donnez. Ses résultats ne disent rien d'une année qui n'y figure pas.

## Questions fréquentes {#faq}

### Quelle différence entre générer et simuler une clé ?

La génération part de vos données et propose une clé candidate, avec le taux d'autoconsommation
collective attendu. La simulation part d'une clé que vous avez choisie et mesure ce qu'elle aurait
donné sur vos données. On génère pour chercher une clé, on simule pour vérifier celle qu'on
envisage.

### Quelles données faut-il pour générer ou simuler une clé ?

Un fichier CSV de consommation et de production au quart d'heure, avec une colonne par
consommateur et une colonne pour la production injectée, dont vous indiquez le nom. C'est le pas
de temps de la répartition en Belgique : 96 valeurs par jour et par compteur.

### La clé générée est-elle envoyée au gestionnaire de réseau ?

Non. OptimCE propose une clé, il ne l'envoie jamais seule au gestionnaire de réseau. Une nouvelle
clé suit le circuit habituel de l'avenant ; OptimCE en garde chaque version et suit son acceptation
par les membres.

### Qu'est-ce que LOGAAS ?

LOGAAS est l'un des deux algorithmes de génération, issu de la recherche du CeCoTePe dans le projet
Locomotrice. Il combine optimisation linéaire et algorithme génétique, et ses réglages avancés ont
des valeurs par défaut qui conviennent à la plupart des usages. L'application l'affiche sous le nom
« OLAGSA ». L'autre algorithme parcourt les clés standards de votre région.

## Pour aller plus loin

- [Générer une clé de répartition optimale]({{ "optimce-allocation-key-generator" | ref_url }}) :
  les deux algorithmes en détail, et quand choisir l'un ou l'autre.
- [Simuler une clé de répartition : scénarios]({{ "optimce-allocation-key-simulation" | ref_url }}) :
  lire les indicateurs et comparer des scénarios.
- [Clé de répartition en Belgique : les 3 régions]({{ "allocation-key-belgium" | ref_url }}) :
  les clés standards et les règles de chaque région.

{% include product-cta.html page_key="allocation-key" guide="key-generation" title="Gérer votre clé de répartition avec OptimCE" %}
