---
layout: post
title: "Lancement d'OptimCE : l'origine du projet"
date: 2026-03-01 10:00:00 +0100
last_modified_at: 2026-07-26 10:00:00 +0200
author: "Équipe OptimCE"
excerpt: "OptimCE n'est pas né dans un incubateur mais dans un laboratoire. Retour sur Locomotrice, le projet de recherche wallon qui a produit la plateforme, sur les partenaires qui l'ont porté, et sur les raisons qui ont conduit à la publier en open source."
description: "D'où vient OptimCE : le projet de recherche Locomotrice, les partenaires ULiège et CECOTEPE, et pourquoi la plateforme est open source."
tags: [app, announcement]
lang: fr
ref: launch-optimce
faq:
  - q: "Qui développe OptimCE ?"
    a: "OptimCE est issu de Locomotrice, un projet de recherche wallon mené entre 2023 et 2026, financé par le programme Win2Wal de la Région wallonne. Il est porté par l'Université de Liège, via son laboratoire BEMS, et par le centre de recherche CECOTEPE, en collaboration avec des coopératives citoyennes d'énergie. Le développement se poursuit aujourd'hui en open source, ouvert aux contributions extérieures."
  - q: "OptimCE est-il gratuit ?"
    a: "La plateforme est publiée sous licence Apache 2.0 : vous pouvez la déployer sur votre propre infrastructure gratuitement et sans restriction. La version hébergée, OptimCE Cloud, est actuellement en alpha et également gratuite. Une offre payante verra le jour à mesure que le produit mûrit ; les utilisateurs de l'alpha seront prévenus bien à l'avance."
  - q: "Pourquoi une plateforme open source pour les communautés d'énergie ?"
    a: "Parce qu'une communauté d'énergie repose sur la confiance de ses membres, et que cette confiance est difficile à établir sur une boîte noire. Le calcul de la clé de répartition détermine combien chaque membre reçoit et paie : pouvoir l'auditer n'est pas un luxe de développeur, c'est une condition de gouvernance. À cela s'ajoute la réalité économique — beaucoup de communautés sont de petites structures pour lesquelles une licence propriétaire annuelle est disproportionnée."
  - q: "OptimCE fonctionne-t-il en dehors de la Belgique ?"
    a: "L'architecture a été conçue pour s'adapter à des cadres réglementaires distincts, ce qui était une nécessité dès le départ : la Belgique compte déjà trois régimes régionaux différents. Les familles de clés de répartition, les statuts et les règles de facturation sont paramétrables. Les développements et validations à ce jour portent principalement sur le contexte belge."
  - q: "Comment contribuer au projet ?"
    a: "Tout se passe sur l'organisation GitHub OptimCE. Le dépôt monorepo agrège les différents services et contient la configuration d'orchestration qui permet de lancer la stack complète en local avec Docker Compose. Les contributions de code sont bienvenues, mais les retours d'usage de gestionnaires de communautés le sont tout autant — ce sont eux qui ont façonné le produit jusqu'ici."
---

La plupart des plateformes logicielles naissent d'une intuition commerciale. OptimCE est né d'un **projet de recherche** — et cette origine explique à peu près tout le reste : le choix de l'open source, le périmètre fonctionnel, et jusqu'à la façon dont les fonctionnalités ont été priorisées.

## Locomotrice, un projet de recherche wallon

OptimCE est le produit logiciel de **Locomotrice**, un projet de recherche mené en Wallonie entre **2023 et 2026** et financé par le programme **Win2Wal** de la Région wallonne. Ce programme finance des recherches menées par des acteurs académiques en vue d'un transfert vers le tissu économique régional — autrement dit, de la recherche destinée à sortir du laboratoire.

Trois familles d'acteurs ont porté le projet :

- l'**Université de Liège**, via son laboratoire **BEMS** ;
- le centre de recherche **CECOTEPE** ;
- des **coopératives citoyennes d'énergie**, présentes non comme utilisatrices finales à qui l'on livre un outil, mais comme partenaires de co-construction.

Cette dernière particularité compte plus qu'il n'y paraît. Une communauté d'énergie n'est pas un problème d'ingénierie pure : c'est un objet réglementaire, comptable et social autant que technique. Les fonctionnalités développées ont donc été validées sur le terrain, avec des gestionnaires qui géraient déjà des membres, des compteurs et des clés de répartition — souvent dans des tableurs.

## Le problème que la recherche a mis en évidence

Le constat de départ est simple à énoncer et pénible à vivre : **la complexité administrative d'une communauté d'énergie est disproportionnée par rapport à sa taille**.

Une communauté de trente ménages doit gérer les mêmes objets qu'un fournisseur d'énergie — points de fourniture, relevés au quart d'heure, clés de répartition, facturation, reporting au gestionnaire de réseau — sans en avoir ni les effectifs ni les systèmes. Et le cadre applicable n'est pas stable : en Belgique, la compétence énergie est régionale, si bien que la Wallonie, Bruxelles et la Flandre imposent trois cadres distincts, avec leurs propres régulateurs et leurs propres familles de clés. Le cadre européen qui les surplombe est décrit dans notre article [« Communautés d'énergie en Europe : RED II et IEMD »](/actualites/2026/03/05/communautes-energie-en-europe/).

Les outils disponibles étaient soit des tableurs — souples mais non auditables et vite ingérables — soit des solutions propriétaires conçues pour des acteurs d'une tout autre taille.

## Pourquoi l'open source n'est pas un détail

La décision de publier OptimCE en open source, sous licence **Apache 2.0**, découle directement de la nature de l'objet géré.

Une communauté d'énergie fonctionne sur la **confiance entre ses membres**. Or la clé de répartition détermine, quart d'heure par quart d'heure, combien d'énergie chaque membre reçoit et donc combien il paie. Demander à trente ménages de faire confiance à une boîte noire pour ce calcul, c'est demander beaucoup. Pouvoir ouvrir le code n'est pas ici un confort de développeur : c'est une **condition de gouvernance**.

S'y ajoute une raison plus prosaïque. Beaucoup de communautés sont de petites structures bénévoles ou semi-bénévoles, pour lesquelles une licence propriétaire annuelle est hors de proportion avec le budget. Un outil qu'on ne peut pas se payer ne résout aucun problème.

## Ce que la plateforme fait aujourd'hui

OptimCE couvre le cycle de gestion complet d'une communauté :

- **Gestion des membres** — intégration, rôles, liens entre communautés et utilisateurs ;
- **Suivi des compteurs** — centralisation des points de fourniture et des relevés ;
- **Clés de répartition** — configuration, historisation des avenants et suivi de l'acceptation par les membres ;
- **Génération et simulation de clés** — proposition d'une clé optimisée à partir des données réelles, et mesure de sa performance avant validation ;
- **Facturation** — du prix au kWh jusqu'au PDF et au suivi des paiements ;
- **Animation** — tableau d'actualités et sondages, parce que la gouvernance participative est une exigence réglementaire autant qu'une bonne pratique ;
- **Multi-communautés** — une instance unique pour plusieurs communautés.

L'architecture est **événementielle et modulaire**, ce qui permet d'intégrer des modules tiers sans toucher au cœur — un choix directement hérité de l'incertitude réglementaire : ce qui change tous les deux ans doit pouvoir changer sans réécrire la plateforme.

## Deux façons de l'utiliser

**En auto-hébergement**, sous licence Apache 2.0, gratuitement et sans restriction. Vous gardez la maîtrise totale des données, et vous assumez l'hébergement, les mises à jour et la disponibilité. La marche à suivre est décrite dans [« Installer OptimCE : guide de démarrage »](/actualites/2026/03/09/guide-demarrage-rapide/).

**Via [OptimCE Cloud](https://app.optimce.be)**, la version hébergée et gérée, actuellement en alpha et gratuite. Aucune installation, aucune maintenance.

Les détails du projet, de ses partenaires et de son financement figurent sur la page [À propos](/a-propos/).

Depuis ce lancement, la plateforme a continué d'évoluer : voir la [version de mai 2026](/actualites/2026/05/07/nouveautes-release/), qui a introduit le registre public des opérations de partage et le guide utilisateur.

## FAQ

### Qui développe OptimCE ?

OptimCE est issu de Locomotrice, un projet de recherche wallon mené entre 2023 et 2026, financé par le programme Win2Wal de la Région wallonne. Il est porté par l'Université de Liège, via son laboratoire BEMS, et par le centre de recherche CECOTEPE, en collaboration avec des coopératives citoyennes d'énergie. Le développement se poursuit aujourd'hui en open source, ouvert aux contributions extérieures.

### OptimCE est-il gratuit ?

La plateforme est publiée sous licence Apache 2.0 : vous pouvez la déployer sur votre propre infrastructure gratuitement et sans restriction. La version hébergée, OptimCE Cloud, est actuellement en alpha et également gratuite. Une offre payante verra le jour à mesure que le produit mûrit ; les utilisateurs de l'alpha seront prévenus bien à l'avance.

### Pourquoi une plateforme open source pour les communautés d'énergie ?

Parce qu'une communauté d'énergie repose sur la confiance de ses membres, et que cette confiance est difficile à établir sur une boîte noire. Le calcul de la clé de répartition détermine combien chaque membre reçoit et paie : pouvoir l'auditer n'est pas un luxe de développeur, c'est une condition de gouvernance. À cela s'ajoute la réalité économique — beaucoup de communautés sont de petites structures pour lesquelles une licence propriétaire annuelle est disproportionnée.

### OptimCE fonctionne-t-il en dehors de la Belgique ?

L'architecture a été conçue pour s'adapter à des cadres réglementaires distincts, ce qui était une nécessité dès le départ : la Belgique compte déjà trois régimes régionaux différents. Les familles de clés de répartition, les statuts et les règles de facturation sont paramétrables. Les développements et validations à ce jour portent principalement sur le contexte belge.

### Comment contribuer au projet ?

Tout se passe sur l'organisation GitHub OptimCE. Le dépôt monorepo agrège les différents services et contient la configuration d'orchestration qui permet de lancer la stack complète en local avec Docker Compose. Les contributions de code sont bienvenues, mais les retours d'usage de gestionnaires de communautés le sont tout autant — ce sont eux qui ont façonné le produit jusqu'ici.

## Pour aller plus loin

> **[Communautés d'énergie en Belgique : CER, CEC, CEL](/actualites/2026/05/11/communautes-energie-belgique/)**
>
> Les trois statuts belges, le partage d'énergie et le rôle du régulateur et du GRD.

> **[Installer OptimCE : guide de démarrage](/actualites/2026/03/09/guide-demarrage-rapide/)**
>
> Déployer la stack complète en local, ou démarrer sans rien installer.

<div class="post-cta" markdown="0">
  <h3>Découvrez OptimCE</h3>
  <p>Créez votre communauté d'énergie en quelques minutes sur la version hébergée, ou déployez la plateforme sur votre propre infrastructure. Le code est ouvert, les contributions bienvenues.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="https://app.optimce.be">Ouvrir l'application OptimCE</a>
    <a class="btn btn-outline" href="https://github.com/optimce">Voir le projet sur GitHub</a>
  </p>
</div>
