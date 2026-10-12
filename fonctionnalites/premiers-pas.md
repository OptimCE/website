---
layout: page
title: "Démarrer une communauté sur OptimCE"
breadcrumb_title: "Premiers pas"
subtitle: "Six étapes, de la création de la communauté à la première facture, chacune avec son guide pas à pas."
description: "Créer la communauté, ajouter membres et compteurs, ouvrir l'opération de partage, définir la clé, facturer : démarrer sur OptimCE en six étapes."
lang: fr
ref: product-getting-started
permalink: /fonctionnalites/premiers-pas/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Faut-il installer OptimCE pour démarrer ?"
    a: "Non. OptimCE Cloud, sur app.optimce.be, ne demande aucune installation : vous créez un compte, puis votre communauté. L'auto-hébergement est une autre voie, pour les équipes qui veulent héberger la plateforme elles-mêmes."
  - q: "Que coûte OptimCE ?"
    a: "OptimCE Cloud est gratuit pendant toute la phase alpha, et l'auto-hébergement est gratuit pour toujours. Une offre payante pourra voir le jour plus tard pour la version hébergée ; les utilisateurs de l'alpha seront prévenus bien à l'avance."
  - q: "Dans quel ordre faut-il faire les étapes ?"
    a: "Dans l'ordre de cette page, qui suit les dépendances entre les modules : les compteurs sont rattachés à des membres, les tarifs et les factures à une opération de partage, et la facturation applique la répartition de cette opération."
  - q: "Peut-on gérer plusieurs communautés avec le même compte ?"
    a: "Oui. Une même installation d'OptimCE gère plusieurs communautés, et un compte peut appartenir à plusieurs d'entre elles. Vous passez de l'une à l'autre depuis « Mes communautés »."
---

Démarrer une communauté d'énergie dans un logiciel, c'est surtout savoir dans quel ordre faire les
choses. Cette page suit l'ordre dans lequel un gestionnaire configure une communauté wallonne dans
OptimCE, de sa création à la première facture. Chaque étape renvoie à son guide pas à pas, qui
montre chaque écran avec des données de test, et à la page qui décrit le module en détail.

## Ce qu'il vous faut sous la main

- **Pour la communauté** : sa dénomination légale, son numéro de TVA, l'adresse de son siège, son
  IBAN et le titulaire du compte.
- **Pour chaque membre** : son statut (particulier ou entreprise), son nom, son adresse e-mail, son
  numéro de téléphone, son adresse et son IBAN ; pour un particulier, son numéro national.
- **Pour chaque compteur** : l'adresse d'installation, l'EAN, le numéro du compteur, ses
  caractéristiques techniques (phases, fréquence de relevé, puissance) et son gestionnaire de
  réseau.

Rien n'oblige à tout avoir le premier jour : le tableau de bord liste ce qui manque encore.

## Le parcours, étape par étape

### 1. Créer la communauté

Depuis « Mes communautés », créez la communauté : un nom et son régulateur, présélectionné sur la
CWaPE pour la Wallonie. Vous en devenez administrateur ; il reste à l'activer pour la configurer.

Guide : [créer une communauté](https://guide.optimce.be/community-create/fr.html). Pour la vue
d'ensemble : [le logiciel de gestion de communauté d'énergie]({{ "features" | ref_url }}).

{% include product-shot.html name="start-dashboard" alt="Tableau de bord d'une nouvelle communauté : « Points à vérifier » liste cinq informations manquantes (numéro de TVA, dénomination légale, IBAN, titulaire du compte, adresse du siège), et aucune opération de partage n'existe encore." caption="Le tableau de bord d'une communauté qui vient d'être créée : ce qu'il reste à compléter (données de test)." %}

### 2. Ajouter les membres

Un assistant en quatre étapes enregistre chaque membre : son statut, ses informations
personnelles, ses adresses et ses coordonnées bancaires. Une fenêtre propose ensuite d'enchaîner
avec son compteur, ce que vous pouvez aussi faire plus tard depuis sa fiche. Vous pouvez également
ajouter des membres par invitation.

Guide : [créer un membre](https://guide.optimce.be/member-create/fr.html). Module :
[membres, compteurs et communautés]({{ "features" | ref_url }}).

{% include product-shot.html name="start-member" alt="Première étape de l'assistant « Ajout d'un membre » : le choix du statut, particulier ou entreprise, suivi des étapes informations personnelles, adresses et informations bancaires." caption="L'assistant de création d'un membre, à sa première étape (données de test)." %}

### 3. Ajouter les compteurs

Pour chaque compteur, renseignez son emplacement et son EAN, ses caractéristiques, son
gestionnaire de réseau, le membre qui en est titulaire et sa date d'activation. Ses valeurs
énergétiques, comme la puissance de prélèvement et la capacité de production, alimentent les
calculs de répartition. Avant sa date d'activation, le compteur n'entre dans aucun calcul.

Guide : [créer un compteur](https://guide.optimce.be/meter-create/fr.html). Module :
[membres, compteurs et communautés]({{ "features" | ref_url }}).

### 4. Créer l'opération de partage

Donnez-lui un nom, un type (au sein d'un bâtiment, communauté d'énergie renouvelable ou communauté
d'énergie citoyenne) et les communes qu'elle couvre. Les tarifs, les factures et les dossiers
administratifs sont ensuite rattachés à cette opération.

Guide : [créer une opération de partage](https://guide.optimce.be/sharing-op-create/fr.html).
Module : [le dossier CWaPE de l'opération]({{ "product-cwape" | ref_url }}).

### 5. Définir la clé de répartition

Avec l'assistant, indiquez le nombre de consommateurs et leurs noms, puis des itérations qui
répartissent chacune un pourcentage de l'énergie, jusqu'à 100 %. Vous pouvez aussi faire proposer
une clé à partir de vos données, puis la simuler avant de l'adopter.

Guide : [créer une clé avec l'assistant](https://guide.optimce.be/key-create-wizard/fr.html).
Module : [clé de répartition : générer, simuler, suivre]({{ "product-allocation-key" | ref_url }}).

### 6. Facturer

Fixez le prix de vente de l'énergie partagée et le prix de rachat de l'injection, importez les
relevés de la période, générez un brouillon par membre, émettez, puis suivez les paiements.

Guide : [facturer une opération, du tarif à l'encaissement](https://guide.optimce.be/billing-tarification-pay/fr.html).
Module : [le logiciel de facturation]({{ "product-billing" | ref_url }}).

### Et ensuite

Chaque membre retrouve ses factures dans l'application et peut consulter ce qui a été déclaré à son
sujet au régulateur. Pour les démarches auprès de la CWaPE, le module des documents administratifs
prépare les formulaires officiels de l'opération et calcule leurs échéances en jours ouvrables.

## Ce que ça ne fait pas

**OptimCE ne crée pas la personne morale.** La forme juridique de la communauté, ses statuts et
son assemblée générale se règlent en dehors de l'application.

**OptimCE ne dépose rien à votre place.** Les notifications à la CWaPE et les conventions avec le
gestionnaire de réseau restent de votre ressort ; OptimCE prépare les documents et suit les
échéances.

**Bruxelles et la Flandre : prévues, pas encore là.** Le régulateur se choisit à la création, mais
la facturation et les documents administratifs couvrent aujourd'hui le cadre wallon. Bruxelles et
la Flandre sont prévues, mais pas encore implémentées.

## Questions fréquentes {#faq}

### Faut-il installer OptimCE pour démarrer ?

Non. OptimCE Cloud, sur app.optimce.be, ne demande aucune installation : vous créez un compte, puis
votre communauté. L'auto-hébergement est une autre voie, pour les équipes qui veulent héberger la
plateforme elles-mêmes.

### Que coûte OptimCE ?

OptimCE Cloud est gratuit pendant toute la phase alpha, et l'auto-hébergement est gratuit pour
toujours. Une offre payante pourra voir le jour plus tard pour la version hébergée ; les
utilisateurs de l'alpha seront prévenus bien à l'avance.

### Dans quel ordre faut-il faire les étapes ?

Dans l'ordre de cette page, qui suit les dépendances entre les modules : les compteurs sont
rattachés à des membres, les tarifs et les factures à une opération de partage, et la facturation
applique la répartition de cette opération.

### Peut-on gérer plusieurs communautés avec le même compte ?

Oui. Une même installation d'OptimCE gère plusieurs communautés, et un compte peut appartenir à
plusieurs d'entre elles. Vous passez de l'une à l'autre depuis « Mes communautés ».

## Pour aller plus loin

- [Créer une communauté d'énergie en Wallonie]({{ "create-energy-community-wallonia" | ref_url }}) :
  les étapes, de la forme juridique à la notification.
- [Communauté d'énergie : documents et délais CWaPE]({{ "cwape-administrative-documents" | ref_url }}) :
  ce qu'il faut déposer, où et dans quel délai.
- [Tableur ou logiciel pour gérer une communauté ?]({{ "product-vs-spreadsheet" | ref_url }}) :
  quand un tableur suffit encore, et où il commence à casser.

{% include product-cta.html page_key="getting-started" guide="getting-started" title="Créer votre communauté sur OptimCE" %}
