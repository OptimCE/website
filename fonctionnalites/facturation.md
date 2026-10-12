---
layout: page
title: "Logiciel de facturation pour communauté d'énergie"
breadcrumb_title: "Facturation"
subtitle: "Du prix au kWh jusqu'au paiement reçu : les factures de vos membres, calculées sur la répartition transmise par le gestionnaire de réseau."
description: "Facturez les membres de votre communauté d'énergie sans tableur : prix au kWh, brouillons, numérotation continue, PDF et suivi des paiements."
lang: fr
ref: product-billing
permalink: /fonctionnalites/facturation/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "D'où viennent les données utilisées pour facturer ?"
    a: "De la répartition transmise par le gestionnaire de réseau : les volumes partagés au quart d'heure, que vous importez pour l'opération et la période à facturer. Au lancement du cycle, OptimCE fige un instantané de ces volumes ; les montants sont calculés sur ces données gelées, que l'on peut retracer."
  - q: "Peut-on appliquer des prix différents selon les membres ?"
    a: "Oui. Chaque prix s'applique à toute l'opération, à un segment de clientèle (résidentiel, professionnel, industriel) ou à un point de fourniture (EAN) précis, pour une période de validité. Quand plusieurs règles visent le même membre, la plus précise l'emporte : le prix d'un EAN passe avant celui de son segment, qui passe avant le prix global."
  - q: "Comment corriger une facture déjà émise ?"
    a: "Une facture émise a reçu un numéro dans une numérotation continue : elle ne se modifie plus et ne se supprime plus. Pour la corriger, vous émettez une note de crédit qui l'annule, puis vous refacturez. Tant qu'un document est au stade de brouillon, vous pouvez au contraire le supprimer ou le recalculer."
  - q: "OptimCE gère-t-il la TVA ?"
    a: "[À VÉRIFIER : traitement de la TVA par le module de facturation.] Le régime de TVA de la communauté (assujettissement, taux applicables à chaque membre) se décide avec un comptable avant la première facture."
---

À chaque période, le gestionnaire d'une communauté d'énergie transforme les volumes partagés en
une facture par membre : appliquer le bon prix, numéroter sans trou, ajouter une communication
structurée, puis vérifier qui a payé. Dans un tableur, chacune de ces étapes se refait à la main,
et chaque erreur se corrige à la main. Le module de facturation d'OptimCE reprend ce travail à
partir de la répartition transmise par le gestionnaire de réseau, dans le cadre wallon.

## Comment OptimCE s'en charge

Le module suit le cycle complet, du tarif à l'encaissement. Les tarifs et les factures sont
toujours rattachés à une opération de partage : une communauté qui en exploite plusieurs les
facture séparément.

### Vous fixez deux prix

La communauté décide de ses prix, en €/kWh. Le **prix de vente** s'applique à l'énergie partagée
consommée par les membres ; le **prix de rachat** rémunère l'injection que les producteurs
partagent avec la communauté.

Chaque prix vaut pour toute l'opération, pour un segment de clientèle (résidentiel, professionnel,
industriel) ou pour un point de fourniture précis, et porte une période de validité. Quand
plusieurs règles visent le même membre, la plus précise l'emporte. Un tarif réduit pour une école
ou pour un ménage ne demande donc pas de seconde opération : il suffit d'un prix sur son EAN.

{% include product-shot.html name="billing-tariffs" alt="Onglet « Tarifs » du module de facturation : un prix de vente au consommateur de 0,12 €/kWh et un prix de rachat au producteur de 0,05 €/kWh, tous deux de portée globale et valables à partir du 1er janvier 2025." caption="Les deux prix d'une opération de partage, tels que les montre le guide pas à pas (données de test)." %}

### Vous lancez un cycle sur une période

Vous choisissez l'opération et la période à facturer : un mois, un trimestre, au rythme de la
communauté. La facturation s'appuie sur les relevés au quart d'heure que le gestionnaire de réseau
transmet pour l'opération. Au lancement, OptimCE fige un instantané de ces volumes : les montants
sont calculés sur des données gelées, que l'on peut retracer si un membre pose une question.

Le calcul tourne en arrière-plan. Il produit un **brouillon par membre**, téléchargeable en PDF
avec le filigrane « proforma ». Un brouillon se relit, se supprime ou se recalcule librement :
rien n'est définitif tant que vous n'avez pas émis.

### Vous émettez les documents

À l'émission, chaque document reçoit un numéro dans une numérotation continue, une communication
structurée et une date d'échéance. OptimCE génère trois documents en PDF, chacun avec sa série :

- la **facture** (F-…), pour l'énergie partagée consommée par un membre ;
- la **note de crédit** (NC-…), pour annuler une facture déjà émise ;
- le **décompte de rémunération** (DP-…), pour l'injection partagée d'un producteur.

Un membre à la fois consommateur et producteur reçoit deux documents distincts. Une facture émise
ne se modifie plus : une erreur se corrige par une note de crédit, puis par une nouvelle facture,
et l'historique reste complet.

### Vous suivez les paiements

Les membres paient par virement, en reprenant la communication structurée. Vous enregistrez chaque
paiement reçu ; le montant est prérempli avec le total du document, et les paiements partiels sont
acceptés. La facture passe au statut « payée » quand le total est atteint, et celles dont
l'échéance est dépassée apparaissent en retard.

De son côté, chaque membre retrouve ses propres documents dans l'application, avec leur numéro,
leur montant, leur statut et leur communication structurée. Il ne voit que les siens.

{% include product-shot.html name="billing-member" alt="Espace « Mes factures » d'un membre : un décompte de rémunération DP-2025-00001 au statut « Émise », de 36,69 €, avec sa communication structurée." caption="Ce que voit un membre : ses documents et la communication structurée à reprendre dans son virement (données de test)." %}

## Ce que ça ne fait pas

**Bruxelles et la Flandre : prévues, pas encore là.** Le module de facturation est conçu
aujourd'hui pour les communautés wallonnes, sous le contrôle de la CWaPE. Les cadres flamand et
bruxellois sont prévus, mais pas encore implémentés.

**L'énergie partagée seulement.** La facture de la communauté valorise l'énergie partagée au prix
interne, hors frais de réseau et taxes. L'énergie que le partage n'a pas couverte reste facturée
par le fournisseur de chaque membre, au tarif de son contrat.

**Pas d'encaissement.** OptimCE ne prélève rien et ne reçoit aucun paiement : les membres paient
par virement sur le compte de la communauté, et vous enregistrez ce qui est arrivé.

**Des documents en français.** Les PDF sont générés en français, quelle que soit la langue de
l'interface.

**La TVA se décide avec un comptable.** [À VÉRIFIER : traitement de la TVA par le module de
facturation.] Le régime de la communauté, assujettie ou non et à quels taux selon les membres,
se tranche avant la première facture : notre guide sur la facturation de l'électricité partagée
présente les cas.

## Questions fréquentes {#faq}

### D'où viennent les données utilisées pour facturer ?

De la répartition transmise par le gestionnaire de réseau : les volumes partagés au quart d'heure,
que vous importez pour l'opération et la période à facturer. Au lancement du cycle, OptimCE fige un
instantané de ces volumes ; les montants sont calculés sur ces données gelées, que l'on peut
retracer.

### Peut-on appliquer des prix différents selon les membres ?

Oui. Chaque prix s'applique à toute l'opération, à un segment de clientèle (résidentiel,
professionnel, industriel) ou à un point de fourniture (EAN) précis, pour une période de validité.
Quand plusieurs règles visent le même membre, la plus précise l'emporte : le prix d'un EAN passe
avant celui de son segment, qui passe avant le prix global.

### Comment corriger une facture déjà émise ?

Une facture émise a reçu un numéro dans une numérotation continue : elle ne se modifie plus et ne
se supprime plus. Pour la corriger, vous émettez une note de crédit qui l'annule, puis vous
refacturez. Tant qu'un document est au stade de brouillon, vous pouvez au contraire le supprimer ou
le recalculer.

### OptimCE gère-t-il la TVA ?

[À VÉRIFIER : traitement de la TVA par le module de facturation.] Le régime de TVA de la
communauté (assujettissement, taux applicables à chaque membre) se décide avec un comptable avant
la première facture.

## Pour aller plus loin

- [Facturer l'électricité partagée en Belgique]({{ "invoice-shared-electricity" | ref_url }}) :
  qui facture quoi, la TVA et les mentions obligatoires.
- [Prix de cession interne en communauté d'énergie]({{ "internal-price-shared-energy" | ref_url }}) :
  comment fixer un prix défendable devant l'assemblée générale.
- [Facturation d'une communauté d'énergie]({{ "optimce-billing" | ref_url }}) : l'annonce du module,
  avec le détail des documents et de leur cycle de vie.

{% include product-cta.html page_key="billing" guide="billing-tarification-pay" title="Facturer votre communauté avec OptimCE" %}
