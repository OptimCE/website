---
layout: page
title: "Fonctionnalités de la plateforme OptimCE"
subtitle: "Ce que la plateforme fait aujourd'hui pour gérer une communauté d'énergie, de l'arrivée des membres à la facture."
description: "Membres, compteurs, clés de répartition générées et simulées, facturation, documents CWaPE, sondages : ce que fait OptimCE, open source et gratuit en alpha."
lang: fr
ref: features
permalink: /fonctionnalites/
last_modified_at: 2026-09-26
feature_list:
  - "Gestion des membres, des points de fourniture et des compteurs"
  - "Clés de répartition historisées, avec suivi de l'acceptation par les membres"
  - "Génération automatique de clés de répartition (parcours des clés standards, LOGAAS)"
  - "Simulation d'une clé de répartition sur ses propres données"
  - "Facturation de l'énergie partagée (première version, cadre wallon)"
  - "Documents administratifs CWaPE préremplis et suivi des échéances"
  - "Notifications par e-mail en quatre langues"
  - "Tableau d'actualités et sondages"
  - "Registre public des opérations de partage"
  - "Multi-communautés, intégration événementielle, API REST"
---

OptimCE est une plateforme open source de gestion des communautés d'énergie. Cette page décrit ce
qu'elle fait **aujourd'hui**, dans sa version alpha, sans rien annoncer de ce qui n'est pas encore
livré. Le [guide utilisateur](https://guide.optimce.be) détaille ensuite chaque écran.

## Membres, compteurs et communautés

- **Gestion des membres** : intégration de nouveaux membres, rôles, liens entre les utilisateurs et
  les communautés.
- **Points de fourniture et compteurs** : les membres, leurs points de fourniture, leurs
  installations et leurs compteurs sont centralisés au même endroit. La liste des participants,
  tenue une seule fois, alimente ensuite les documents administratifs et la facturation.
- **Plusieurs communautés, une seule instance** : une même installation d'OptimCE gère plusieurs
  communautés d'énergie.

## Clés de répartition : configurer, générer, simuler

La clé de répartition décide, quart d'heure par quart d'heure, qui reçoit quelle part de la
production locale. OptimCE en couvre tout le cycle de vie.

- **Configuration et avenants** : chaque version de la clé est historisée et l'acceptation par les
  membres est suivie.
- **Génération automatique** : à partir d'un fichier CSV de consommation et de production au quart
  d'heure, le module propose une clé candidate avec le taux d'autoconsommation collective attendu.
  Deux algorithmes sont disponibles : un parcours exhaustif des clés standards de votre région, et
  LOGAAS, issu de la recherche du CeCoTePe dans le projet Locomotrice. La proposition ne part
  jamais seule chez le gestionnaire de réseau : elle suit le circuit habituel de l'avenant.
- **Simulation** : testez une clé de votre choix sur vos propres données et lisez
  l'autoconsommation, le surplus, le taux d'autosuffisance et le taux de partage, au global, par
  pas de temps et par itération, sans toucher à la clé appliquée.

Pour aller plus loin : [générer une clé de répartition optimale]({{ "optimce-allocation-key-generator" | ref_url }})
et [simuler une clé sur ses données]({{ "optimce-allocation-key-simulation" | ref_url }}).

## Facturation de l'énergie partagée

La première version du module de facturation est conçue pour le cadre wallon.

- Vous fixez vos prix en €/kWh : un prix de vente de l'énergie partagée et un prix de rachat de
  l'injection, pour toute la communauté, par segment de clientèle ou par point de fourniture, avec
  une période de validité.
- Un cycle de facturation produit un brouillon par membre à partir des données de répartition
  importées. Une fois émis, chaque document reçoit un numéro dans une numérotation continue et une
  communication structurée.
- Trois documents sont générés en PDF : la facture, la note de crédit et le décompte de
  rémunération des producteurs.
- Le suivi des paiements est intégré, paiements partiels compris, et chaque membre retrouve ses
  factures dans l'application.

Le détail figure dans [l'annonce du module de facturation]({{ "optimce-billing" | ref_url }}).

## Documents administratifs et échéances

Pour les communautés wallonnes, OptimCE prépare les documents de la CWaPE à partir des fichiers
officiels, non modifiés : onze lots de PDF remplissables, de classeurs Excel et de conventions
Word, préremplis avec les données de la communauté. Les champs que la plateforme ne sait pas
déduire restent modifiables.

- Chaque dossier et chaque document suivent des statuts consignés dans un journal : une correction
  s'ajoute, elle n'efface rien.
- Les échéances sont calculées en jours ouvrables sur le calendrier belge et remontées dans le
  tableau de bord du gestionnaire.
- Des e-mails, en français, en néerlandais, en allemand et en anglais, signalent les invitations,
  les factures et les échéances administratives.
- Chaque membre peut consulter ce qui a été déclaré à son sujet au régulateur.

OptimCE ne dépose rien et ne signe rien à votre place : le dépôt reste de votre ressort. Voir
[les documents et délais de la CWaPE]({{ "cwape-administrative-documents" | ref_url }}).

## Animer la communauté

Un tableau d'actualités informe les membres ; des sondages les consultent. Trois modes de
visibilité des résultats sont prévus : anonyme, transparent, ou résultats dévoilés à la clôture.
Un mode avancé règle séparément ce que voient le gestionnaire et les membres. Voir
[animer une communauté d'énergie au quotidien]({{ "engage-energy-community" | ref_url }}).

## Registre public des opérations de partage

Un gestionnaire peut publier son opération de partage dans un registre public intégré à
l'application. Chacun peut le parcourir pour trouver une opération ouverte à de nouveaux membres.

## Une plateforme ouverte

- **Open source** : tout le code est publié sous licence Apache 2.0.
- **Auto-hébergement** : vous pouvez installer OptimCE sur votre propre infrastructure,
  gratuitement et sans restriction. La marche à suivre est décrite dans
  [le guide d'installation]({{ "quick-start-guide" | ref_url }}).
- **OptimCE Cloud** : la version hébergée est gratuite pendant toute la phase alpha. Une offre
  payante pourra voir le jour plus tard ; les utilisateurs de l'alpha seront prévenus bien à
  l'avance, et l'auto-hébergement restera gratuit.
- **Intégrations** : une architecture événementielle (NATS) permet de brancher des outils tiers,
  comme un système de gestion d'énergie, et une API REST permet d'intégrer OptimCE à vos propres
  outils.
- **Multilingue** : l'interface existe en français, en anglais, en néerlandais et en allemand.

## Ce que la plateforme ne fait pas

OptimCE travaille sur les données de répartition transmises par le gestionnaire de réseau et sur
les fichiers que vous importez : il n'affiche pas de données en temps réel. Il ne dépose pas vos
documents auprès de la CWaPE et ne signe pas vos conventions. Sa facturation couvre, pour
l'instant, le seul cadre wallon.

<div class="post-cta" markdown="0">
  <h2>Gérer ou créer une communauté avec OptimCE</h2>
  <p>L'application est gratuite pendant l'alpha. Créez votre communauté, invitez vos membres et
  configurez votre clé de répartition ; le guide utilisateur vous accompagne écran par écran.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="{{ site.cta.app_url }}">Ouvrir l'application</a>
    <a class="btn btn-outline" href="https://guide.optimce.be">Lire le guide utilisateur</a>
    <a class="btn btn-outline" href="https://github.com/{{ site.github_username }}">Voir le code sur GitHub</a>
  </p>
</div>
