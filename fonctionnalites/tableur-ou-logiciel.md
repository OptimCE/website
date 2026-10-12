---
layout: page
title: "Tableur ou logiciel pour gérer une communauté ?"
breadcrumb_title: "Tableur ou logiciel"
subtitle: "Une comparaison honnête : quand un tableur suffit pour gérer une communauté d'énergie, et où il commence à casser."
description: "Excel suffit-il pour gérer une communauté d'énergie ? Quand le tableur tient, où il casse (quart d'heure, clés, factures, CWaPE) et ce que fait un logiciel."
lang: fr
ref: product-vs-spreadsheet
permalink: /fonctionnalites/tableur-ou-logiciel/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Un tableur suffit-il pour une petite communauté d'énergie ?"
    a: "Souvent, oui. Avec une poignée de membres, une seule opération de partage et une clé standard qui ne change pas, un tableur bien tenu fait l'affaire. Il devient fragile quand la clé évolue, quand les factures se multiplient ou quand plusieurs personnes doivent y travailler."
  - q: "Pourquoi parle-t-on de 35 040 valeurs par compteur et par an ?"
    a: "Parce que le partage se calcule au quart d'heure : 96 quarts d'heure par jour, sur une année de 365 jours, font 35 040 valeurs par compteur. Les jours de changement d'heure comptent 92 ou 100 quarts d'heure, et le total annuel reste le même."
  - q: "OptimCE remplace-t-il la comptabilité de la communauté ?"
    a: "Non. OptimCE facture l'énergie partagée et suit le paiement de ces factures. La comptabilité générale de la communauté reste à tenir à part."
  - q: "Que coûte OptimCE par rapport à un tableur ?"
    a: "OptimCE Cloud est gratuit pendant toute la phase alpha, et l'auto-hébergement est gratuit pour toujours. Une offre payante pourra voir le jour plus tard pour la version hébergée ; les utilisateurs de l'alpha seront prévenus bien à l'avance."
---

La plupart des communautés d'énergie démarrent sur un tableur, et c'est souvent le bon choix : il
est déjà installé, tout le monde sait l'ouvrir, et une petite communauté n'a pas besoin de plus.
Mais un tableur n'a pas de mémoire. Il ne sait pas quelle version de la clé de répartition valait
en mars, quel numéro de facture vient ensuite, ni ce qui a été déposé à la CWaPE et quand. Cette
page compare honnêtement les deux, sans chercher à vous faire changer d'outil plus tôt que
nécessaire.

## Quand un tableur suffit

Un tableur bien tenu fait l'affaire quand la communauté reste simple :

- une poignée de membres et une seule opération de partage ;
- une clé de répartition standard, qui ne change pas d'une année à l'autre ;
- peu de documents à produire : quelques factures par période, un dossier CWaPE déjà déposé ;
- une seule personne qui tient le fichier, et qui le transmet proprement quand elle passe la main.

Si votre communauté ressemble à cela, gardez votre tableur. Le jour où l'un de ces points change,
la suite de cette page vous concerne.

## Comment OptimCE s'en charge

Voici les cinq endroits où un tableur commence à casser, et ce qu'OptimCE fait à la place.

### Les données au quart d'heure

En Belgique, le partage se calcule au quart d'heure : 96 valeurs par jour et par compteur, soit
35 040 sur une année de 365 jours. Rangées à raison d'une ligne par compteur et par quart d'heure,
les données d'une année pour 30 compteurs font 1 051 200 lignes : plus que les 1 048 576 lignes
d'une feuille Excel ([Microsoft](https://support.microsoft.com/fr-FR/Excel/excel-specifications-and-limits)).
Bien avant cette limite, le classeur devient lourd à ouvrir et à recalculer.

Dans OptimCE, les relevés au quart d'heure s'importent par opération et par période. La
facturation, la génération et la simulation de clé travaillent directement dessus.

### Les versions de la clé

Une clé de répartition change à chaque arrivée ou départ de membre. Dans un tableur, la version de
mars écrase celle de janvier, ou survit dans un fichier « cle_v3_final.xlsx » dont personne ne sait
plus s'il a été accepté.

Dans OptimCE, chaque version de la clé est historisée et l'acceptation par les membres est suivie.
Le détail est sur la page de [la clé de répartition]({{ "product-allocation-key" | ref_url }}).

### La numérotation des factures

Les factures se numérotent dans une série continue, sans trou, et une facture émise ne se modifie
plus : on la corrige par une note de crédit. Dans un tableur, rien n'empêche d'écraser une ligne,
de sauter un numéro ou de recopier une communication structurée erronée.

Dans OptimCE, le numéro et la communication structurée sont attribués à l'émission, une correction
passe par une note de crédit, et l'historique reste complet. Voir le
[logiciel de facturation]({{ "product-billing" | ref_url }}).

{% include product-shot.html name="billing-member" alt="Espace « Mes factures » d'un membre : un décompte de rémunération DP-2025-00001 au statut « Émise », de 36,69 €, avec sa communication structurée." caption="Chaque membre voit ses propres documents, avec la communication structurée à reprendre dans son virement (données de test)." %}

### Les dossiers CWaPE

Les mêmes données (membres, points de fourniture, installations) se recopient dans plusieurs
formulaires de la CWaPE, et chaque modification de la communauté en appelle de nouveaux, avec des
délais en jours ouvrables. Un tableur ne sait pas qu'un dossier vient de changer de statut, ni
quelle version d'un formulaire est partie.

Dans OptimCE, les formulaires officiels sont préremplis à partir de la liste des membres, chaque
version est conservée et les échéances sont calculées en jours ouvrables. Voir le
[dossier CWaPE]({{ "product-cwape" | ref_url }}).

{% include product-shot.html name="cwape-deadlines" alt="Onglet « Échéances » des documents administratifs : un contrôle de complétude dû le 15/09/2026 pour le dossier n° 1, au statut « En cours »." caption="Les échéances ouvertes de tous les dossiers, calculées à partir des changements de statut (données de test)." %}

### L'accès des membres et la passation

Pour montrer à chaque membre sa facture ou ce qui a été déclaré à son sujet, un tableur oblige à
extraire et à envoyer un fichier par personne : partager le classeur entier exposerait les données
de tous. Et le fichier dépend de la personne qui le tient : quand elle s'en va, l'historique part
souvent avec sa boîte mail.

Dans OptimCE, chaque membre voit ses propres factures et ce qui a été déclaré à son sujet, et rien
d'autre. Plusieurs personnes peuvent gérer la communauté, chacune avec son rôle, et l'historique
reste dans l'application.

## Ce que ça ne fait pas

**OptimCE ne remplace pas votre comptabilité.** Il facture l'énergie partagée et suit le paiement
de ces factures. La comptabilité générale de la communauté reste à tenir à part.

**Pas de temps réel.** Comme votre tableur, OptimCE travaille sur les relevés transmis par le
gestionnaire de réseau et sur les fichiers que vous importez : il n'affiche pas de données en temps
réel.

**Il ne corrige pas des données fausses.** Un logiciel évite les erreurs de recopie, pas les
erreurs de saisie. Une adresse ou un EAN erronés restent faux, dans un tableur comme dans OptimCE.

## Questions fréquentes {#faq}

### Un tableur suffit-il pour une petite communauté d'énergie ?

Souvent, oui. Avec une poignée de membres, une seule opération de partage et une clé standard qui
ne change pas, un tableur bien tenu fait l'affaire. Il devient fragile quand la clé évolue, quand
les factures se multiplient ou quand plusieurs personnes doivent y travailler.

### Pourquoi parle-t-on de 35 040 valeurs par compteur et par an ?

Parce que le partage se calcule au quart d'heure : 96 quarts d'heure par jour, sur une année de
365 jours, font 35 040 valeurs par compteur. Les jours de changement d'heure comptent 92 ou 100
quarts d'heure, et le total annuel reste le même.

### OptimCE remplace-t-il la comptabilité de la communauté ?

Non. OptimCE facture l'énergie partagée et suit le paiement de ces factures. La comptabilité
générale de la communauté reste à tenir à part.

### Que coûte OptimCE par rapport à un tableur ?

OptimCE Cloud est gratuit pendant toute la phase alpha, et l'auto-hébergement est gratuit pour
toujours. Une offre payante pourra voir le jour plus tard pour la version hébergée ; les
utilisateurs de l'alpha seront prévenus bien à l'avance.

## Pour aller plus loin

- [Communauté d'énergie : documents et délais CWaPE]({{ "cwape-administrative-documents" | ref_url }}) :
  chaque formulaire, ses délais, et par où commencer quand tout est déjà dans des tableurs.
- [Facturer l'électricité partagée en Belgique]({{ "invoice-shared-electricity" | ref_url }}) :
  qui facture quoi, la TVA et les mentions obligatoires.
- [Clé de répartition en Belgique : les 3 régions]({{ "allocation-key-belgium" | ref_url }}) :
  les clés standards et les règles de chaque région.

{% include product-cta.html page_key="vs-spreadsheet" guide="getting-started" title="Passer du tableur à OptimCE" %}
