---
layout: post
title: "Facturation d'une communauté d'énergie : OptimCE génère vos factures"
date: 2026-07-16 10:00:00 +0200
author: "Équipe OptimCE"
excerpt: "Nouvelle fonctionnalité OptimCE : générez automatiquement les factures de votre communauté d'énergie, du prix au kWh jusqu'au PDF et au suivi des paiements."
tags: [administrative, app, news]
lang: fr
ref: optimce-billing
last_modified_at: 2026-07-20 10:00:00 +0200
faq:
  - q: "D'où viennent les données utilisées pour facturer ?"
    a: "Des données de répartition officielles transmises par le gestionnaire de réseau et déjà importées dans OptimCE : énergie partagée consommée et injection partagée, par EAN et par période. Au lancement d'un cycle de facturation, OptimCE fige un instantané de ces volumes : les montants sont calculés sur des données gelées et traçables."
  - q: "Qui fixe les prix de l'énergie partagée ?"
    a: "La communauté elle-même. Vous définissez librement deux prix en €/kWh : le prix de vente de l'énergie partagée aux consommateurs et le prix de rachat de l'injection versé aux producteurs. Chaque prix peut s'appliquer globalement, par segment de clientèle (résidentiel, professionnel, industriel) ou à un EAN précis, avec une période de validité — la règle la plus spécifique l'emporte."
  - q: "Quels documents OptimCE génère-t-il ?"
    a: "Trois documents, chacun avec sa propre série de numérotation : la facture (F-…) pour l'énergie partagée consommée par un membre, la note de crédit (NC-…) pour corriger une facture émise, et le décompte de rémunération (DP-…) pour l'injection partagée d'un producteur. Tous sont générés en PDF ; les brouillons portent un filigrane « proforma »."
  - q: "Que couvre la facture d'une communauté d'énergie ?"
    a: "Uniquement l'énergie partagée, valorisée au prix interne de la communauté, hors frais de réseau et taxes. L'énergie résiduelle — celle que le partage n'a pas couverte — reste facturée par le fournisseur de chaque membre au tarif de son contrat."
  - q: "Peut-on corriger une facture déjà émise ?"
    a: "Pas directement : une fois émise, une facture reçoit un numéro légal dans une numérotation continue et ne peut plus être modifiée ni supprimée. Pour corriger, vous émettez une note de crédit qui l'annule, puis vous refacturez. Un brouillon, en revanche, peut être supprimé ou recalculé librement."
  - q: "Comment les membres accèdent-ils à leurs factures ?"
    a: "Chaque membre retrouve ses propres factures dans l'application et télécharge le PDF quand il le souhaite. Côté gestionnaire, le suivi des paiements est intégré : vous enregistrez les versements — même partiels —, la facture passe automatiquement en « payée » et les retards sont signalés après l'échéance."
---

Une communauté d'énergie qui fonctionne produit deux choses : des kWh partagés… et des montants à facturer. Chaque période, la répartition officielle attribue à chaque membre sa part de l'énergie produite localement — puis quelqu'un doit transformer ces volumes en euros : calculer ce que doit chaque consommateur, ce que touche chaque producteur, produire des documents en règle, encaisser et suivre les paiements. Jusqu'ici, ce travail se faisait le plus souvent à la main, entre tableur et modèle de facture bricolé. C'est terminé : OptimCE intègre désormais un **module de facturation**, dont la première version est opérationnelle.

Le principe est simple : vous fixez vos prix, vous choisissez une période, et OptimCE **génère les factures de tous les membres** à partir des données de répartition déjà présentes dans la plateforme — avec PDF, numérotation légale, communication structurée et suivi des paiements.

Si la mécanique de la répartition est encore floue pour vous, commencez par notre article de référence [« Clé de répartition en Belgique : Wallonie, Bruxelles, Flandre »](/actualites/2026/05/19/cle-repartition-communaute-energie-belgique/) — la facturation en est la suite directe.

## Pourquoi la facturation interne est le maillon critique

Dans le partage d'énergie, le gestionnaire de réseau calcule et transmet, mais **ne facture pas** : il applique la clé de répartition quart d'heure par quart d'heure et communique les volumes. La valorisation de ces volumes — à quel prix le consommateur paie l'énergie partagée, à quel prix le producteur est rémunéré pour son injection — relève de la communauté elle-même.

Concrètement, cette charge retombe sur le gestionnaire de la communauté. Pour chaque période, il faut :

- **reprendre les volumes exacts** par point de raccordement (EAN) ;
- **appliquer le bon prix** à chaque profil, sans erreur de calcul ni d'arrondi ;
- **produire un document en règle** : TVA, mentions obligatoires, numérotation continue ;
- **joindre une communication de paiement** et réconcilier les virements reçus ;
- **répondre aux questions** des membres sur leur décompte.

À dix membres, c'est fastidieux ; à cinquante, intenable. Et l'enjeu dépasse l'administratif : une facturation claire et régulière est la première condition de la **confiance des membres** — c'est elle qui rend visible, noir sur blanc, l'avantage économique du partage. Nous l'écrivions déjà dans notre [guide de création d'une communauté d'énergie en Wallonie](/actualites/2026/05/11/creer-communaute-energie-wallonie/) : c'est en phase d'exploitation qu'un outil de gestion devient indispensable.

## Comment ça marche : du volume partagé à la facture

Le module s'intègre au reste de la plateforme et suit un parcours en quatre étapes.

1. **Les données sont déjà là.** La facturation s'appuie sur les données de répartition officielles déjà importées dans OptimCE : énergie partagée consommée et injection partagée, par EAN et par période. Rien à ressaisir, rien à exporter — la facturation lit les mêmes volumes que vos tableaux de bord.
2. **Vous définissez vos prix.** Deux prix, en €/kWh, librement fixés par la communauté : le **prix de vente** de l'énergie partagée aux consommateurs et le **prix de rachat** de l'injection versé aux producteurs. Chaque prix peut s'appliquer globalement, par segment de clientèle (résidentiel, professionnel, industriel) ou à un EAN précis — la règle la plus spécifique l'emporte — et porte une période de validité. Reste à décider quels montants inscrire : notre guide [« Prix de l'électricité en communauté d'énergie : comment fixer le prix de cession interne »](/actualites/2026/07/20/prix-electricite-communaute-energie/) détaille la fourchette défendable et cinq méthodes de calcul.
3. **Vous lancez un cycle de facturation.** Vous choisissez la période — mensuelle, trimestrielle, à votre convenance — et OptimCE vérifie que tout est en ordre avant de calculer : données de consommation présentes, coordonnées bancaires et dénomination légale de la communauté, tarif applicable, absence de doublon dans les données. Puis il **fige un instantané** de la répartition : les montants sont calculés sur des volumes gelés, traçables.
4. **Vous relisez, puis vous émettez.** Le cycle produit un **brouillon par membre**, téléchargeable en PDF avec filigrane « proforma ». Vous vérifiez, puis vous émettez : la facture reçoit alors son numéro légal, sa communication structurée et sa date d'échéance.

En résumé, voici ce que vous apportez et ce que vous obtenez :

| Vous définissez | OptimCE génère |
|---|---|
| Le prix de vente aux consommateurs (€/kWh) | Une facture par membre consommateur |
| Le prix de rachat aux producteurs (€/kWh) | Un décompte de rémunération par producteur |
| La période à facturer | Les totaux hors TVA, la TVA et le montant à payer |
| | Le PDF prêt à transmettre, avec IBAN et communication structurée |

## Trois documents, une numérotation sans trou

Le module distingue trois documents, chacun avec sa propre série :

| Document | Série | Rôle |
|---|---|---|
| **Facture** | F-2026-00001 | L'énergie partagée consommée par un membre, au prix interne |
| **Note de crédit** | NC-2026-00001 | La correction d'une facture déjà émise |
| **Décompte de rémunération** | DP-2026-00001 | L'injection partagée d'un producteur, au prix de rachat |

Chaque document détaille, ligne par ligne et EAN par EAN, les kWh multipliés par le prix unitaire, puis le total hors TVA, la TVA et le montant à payer. On y retrouve l'émetteur (la communauté, en tant que représentant du partage), le destinataire, l'IBAN de la communauté, une **communication structurée** belge pour réconcilier les virements sans ambiguïté, la date d'émission et l'échéance, ainsi que les mentions légales — dont la précision que la facture porte sur l'énergie partagée **hors frais de réseau et taxes**.

Un membre à la fois consommateur et producteur reçoit deux documents distincts : sa facture d'énergie partagée et son décompte de rémunération.

La numérotation est **continue et sans trou**, comme l'exigent les règles de facturation : une facture émise ne peut plus être modifiée ni supprimée. Une erreur ? Vous émettez une **note de crédit** qui l'annule, puis vous refacturez correctement — l'historique reste intact et vérifiable.

## Du brouillon au paiement : le cycle de vie

Chaque facture suit un cycle de vie explicite, visible d'un coup d'œil :

| Statut | Ce qu'il signifie |
|---|---|
| **Brouillon** | Proposition calculée, modifiable et supprimable — PDF proforma en filigrane |
| **Émise** | Numéro légal attribué, document définitif, échéance fixée |
| **Envoyée** | Transmise au membre |
| **Payée** | Paiements enregistrés à hauteur du montant total |
| **En retard** | Échéance dépassée sans paiement complet |

Le suivi des paiements est intégré : vous enregistrez chaque versement — y compris les **paiements partiels** — et la facture passe automatiquement en « payée » une fois le montant atteint. Les factures dont l'échéance est dépassée sont marquées **en retard**, pour cibler les rappels sans éplucher un extrait de compte.

## Côté membres : la transparence par le document

Chaque membre retrouve **ses propres factures** dans l'application et en télécharge le PDF quand il le souhaite. Plus besoin d'attendre un e-mail du gestionnaire ou de réclamer un récapitulatif : le document de référence est disponible, au même endroit, pour tout le monde.

Rappelons le périmètre : la facture de la communauté couvre l'**énergie partagée**, valorisée au prix interne. L'énergie résiduelle — celle que le partage n'a pas couverte — reste facturée par le fournisseur de chaque membre, au tarif de son contrat. Ce sont les deux documents ensemble qui racontent l'économie réalisée ; notre article sur [la réduction de la facture d'électricité grâce au partage](/actualites/2026/06/03/communaute-energie-reduire-facture-electricite/) détaille ce mécanisme.

## Une première version pensée pour la Wallonie — et la suite

Cette première version est conçue pour le **cadre wallon** (CWaPE) : mentions légales adaptées et application automatique de la TVA sur les factures. Les documents sont générés en français ; la chaîne de génération est déjà prête pour le multilingue, qui suivra.

Au programme des prochaines versions : l'**envoi automatique des factures par e-mail**, la prise en charge des cadres **flamand et bruxellois**, et des structures tarifaires plus riches. Fidèle à la démarche d'OptimCE : livrer tôt, éprouver sur le terrain, itérer avec les communautés.

Le module est disponible dès maintenant sur [app.optimce.be](https://app.optimce.be) — gratuit, comme toute la plateforme pendant la phase alpha.

## Conclusion

Avec la facturation, OptimCE ferme la boucle : import des données, [choix et simulation de la clé de répartition](/actualites/2026/06/09/simuler-cle-repartition-optimce/), opérations de partage, et désormais les factures — la dernière étape qui transformait encore chaque trimestre en corvée de tableur. Les volumes deviennent des documents en règle, les paiements se suivent d'un coup d'œil, et chaque membre voit clairement ce que le partage lui apporte.

> ### Facturez votre communauté d'énergie avec OptimCE
>
> Plateforme open source pensée pour les communautés d'énergie belges : importez vos données de répartition, définissez vos prix, générez factures et décomptes en PDF et suivez les paiements — le tout dans une seule application.
>
> **[Démarrer sur app.optimce.be →](https://app.optimce.be)**

## FAQ

### D'où viennent les données utilisées pour facturer ?

Des données de répartition officielles transmises par le gestionnaire de réseau et **déjà importées dans OptimCE** : énergie partagée consommée et injection partagée, par EAN et par période. Au lancement d'un cycle de facturation, OptimCE fige un instantané de ces volumes : les montants sont calculés sur des données gelées et traçables.

### Qui fixe les prix de l'énergie partagée ?

**La communauté elle-même.** Vous définissez librement deux prix en €/kWh : le prix de vente de l'énergie partagée aux consommateurs et le prix de rachat de l'injection versé aux producteurs. Chaque prix peut s'appliquer globalement, par segment de clientèle (résidentiel, professionnel, industriel) ou à un EAN précis, avec une période de validité — la règle la plus spécifique l'emporte.

### Quels documents OptimCE génère-t-il ?

Trois documents, chacun avec sa propre série de numérotation : la **facture** (F-…) pour l'énergie partagée consommée par un membre, la **note de crédit** (NC-…) pour corriger une facture émise, et le **décompte de rémunération** (DP-…) pour l'injection partagée d'un producteur. Tous sont générés en PDF ; les brouillons portent un filigrane « proforma ».

### Que couvre la facture d'une communauté d'énergie ?

Uniquement l'**énergie partagée**, valorisée au prix interne de la communauté, hors frais de réseau et taxes. L'énergie résiduelle — celle que le partage n'a pas couverte — reste facturée par le fournisseur de chaque membre au tarif de son contrat.

### Peut-on corriger une facture déjà émise ?

Pas directement : une fois émise, une facture reçoit un numéro légal dans une **numérotation continue** et ne peut plus être modifiée ni supprimée. Pour corriger, vous émettez une **note de crédit** qui l'annule, puis vous refacturez. Un brouillon, en revanche, peut être supprimé ou recalculé librement.

### Comment les membres accèdent-ils à leurs factures ?

Chaque membre retrouve **ses propres factures** dans l'application et télécharge le PDF quand il le souhaite. Côté gestionnaire, le suivi des paiements est intégré : vous enregistrez les versements — même partiels —, la facture passe automatiquement en « payée » et les retards sont signalés après l'échéance.

## Sources

- [CWaPE — Communautés d'énergie](https://www.cwape.be/node/158) — cadre wallon des communautés d'énergie : types, bases légales, notification et rapportage annuel.
- [CWaPE — Communautés d'énergie et partage d'énergie](https://www.cwape.be/secteur/communautes-partage-energie) — cadre général wallon du partage d'énergie.
- [SPF Finances — TVA](https://finances.belgium.be/fr/entreprises/tva) — obligations de facturation, de comptabilité et de TVA pour les entreprises et personnes morales belges.
- [Pricing and sharing rules for energy communities](https://econpapers.repec.org/article/eeejuipol/v_3a96_3ay_3a2025_3ai_3ac_3as0957178725001109.htm) — recherche sur les règles de partage et la fixation des prix internes dans les communautés d'énergie.
