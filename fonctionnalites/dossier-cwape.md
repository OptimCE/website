---
layout: page
title: "Dossier CWaPE de votre communauté d'énergie"
breadcrumb_title: "Dossier CWaPE"
subtitle: "Les formulaires officiels préremplis, les statuts et les échéances de chaque dossier, réunis au même endroit et gardés en mémoire."
description: "Préparez le dossier CWaPE de votre communauté d'énergie : formulaires officiels préremplis, versions conservées, statuts et échéances en jours ouvrables."
lang: fr
ref: product-cwape
permalink: /fonctionnalites/dossier-cwape/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "OptimCE dépose-t-il le dossier auprès de la CWaPE ?"
    a: "Non. OptimCE prépare les documents, mais le dépôt reste de votre ressort, par vos moyens habituels. Vous enregistrez ensuite dans la plateforme que le dossier a été déposé, et à quelle date : c'est cette date qui fait courir les délais. OptimCE ne signe rien non plus."
  - q: "Les formulaires sont-ils les versions officielles de la CWaPE ?"
    a: "Oui. OptimCE part des fichiers officiels, non modifiés : onze lots de PDF remplissables, de classeurs Excel et de conventions Word. Il les préremplit avec les données de la communauté ; les champs qu'il ne sait pas déduire restent modifiables."
  - q: "Comment les délais sont-ils calculés ?"
    a: "À partir du type de dossier, de la région et de la date de dépôt que vous avez enregistrée. Les délais en jours ouvrables suivent le calendrier belge. Les échéances remontent dans le tableau de bord du gestionnaire et sont signalées par e-mail."
  - q: "Les membres peuvent-ils voir ce qui a été déclaré à leur sujet ?"
    a: "Oui. Chaque membre dispose d'une page « Ce qui a été déclaré à mon sujet » : il y voit les documents où il apparaît et les valeurs transmises, telles qu'elles étaient à la date du dépôt. Elles ne changent pas si ses informations sont corrigées ensuite."
---

Créer ou modifier une communauté d'énergie en Wallonie, c'est remplir les formulaires de la CWaPE
et les conventions du gestionnaire de réseau, puis tenir des délais qui se comptent en jours
ouvrables. Les mêmes données passent d'un fichier à l'autre (membres, points de fourniture,
installations), et il faut pouvoir dire, des mois plus tard, ce qui a été déposé et quand. OptimCE
prépare ces documents à partir des données de la communauté et garde la trace de chaque étape.

## Comment OptimCE s'en charge

### Un dossier par opération de partage

Chaque dossier concerne une seule opération de partage : une communauté qui en exploite plusieurs
ouvre un dossier par opération. Son type, par exemple une notification de création, détermine les
échéances réglementaires qui seront calculées ensuite. Vous lui donnez un titre libre et la
référence attribuée par l'autorité, modifiable plus tard.

Tant que le dossier est « en préparation », il reste modifiable et aucune échéance ne court. Sa
fiche rassemble ses documents, ses échéances et l'historique de ses statuts, et ne propose que les
changements de statut autorisés à ce stade. Le module s'active par communauté.

{% include product-shot.html name="cwape-dossier" alt="Fiche d'un dossier de notification de création au statut « En préparation » : opération de partage, référence CWAPE-2026-0042, région Wallonie (CWaPE), boutons « Soumis » et « Caduc », onglets Documents, Échéances et Historique." caption="La fiche d'un dossier, juste après sa création, dans le guide pas à pas (données de test)." %}

### Les formulaires officiels, préremplis

OptimCE part des fichiers officiels de la CWaPE, **non modifiés** : onze lots de PDF
remplissables, de classeurs Excel et de conventions Word. Il les préremplit avec les données de la
communauté. La liste des membres, des points de fourniture et des compteurs est tenue une seule
fois, puis alimente chaque document qui la demande.

Avant de générer un document, vous relisez les données reprises et vous corrigez une valeur si
nécessaire, pour ce document seulement. Les champs que la plateforme ne sait pas déduire restent
modifiables. Chaque génération ajoute une nouvelle version, et un fichier enregistré n'est jamais
remplacé : on retrouve ce qui a été produit, quand et par qui. Un document que vous avez déjà en
main se joint au dossier de la même façon.

### Des statuts et un journal qui n'efface rien

Vous déposez le dossier par vos moyens habituels, puis vous enregistrez dans OptimCE que ce dépôt a
eu lieu, à sa date réelle. Le dossier passe alors au statut « soumis » ; il pourra ensuite être
déclaré complet, corrigé, ou devenir caduc.

Chaque changement de statut est consigné dans un journal. Une correction s'ajoute à la suite, elle
n'efface rien : la question « qu'avons-nous transmis, et quand ? » a toujours une réponse.

### Des échéances calculées, pas saisies

Vous n'encodez jamais une échéance à la main. OptimCE la calcule à partir du type de dossier, de la
région et de la date que vous avez enregistrée, en jours ouvrables sur le calendrier belge.
L'onglet « Échéances » réunit celles de tous les dossiers, et le tableau de bord du gestionnaire
les fait remonter. Des e-mails, en français, en néerlandais, en allemand ou en anglais, signalent
les échéances administratives.

Quand une obligation est remplie, vous marquez l'échéance comme respectée : elle quitte la liste
des échéances ouvertes, mais l'historique du dossier en garde la trace.

{% include product-shot.html name="cwape-deadlines" alt="Onglet « Échéances » des documents administratifs : un contrôle de complétude dû le 15/09/2026 pour le dossier n° 1, au statut « En cours »." caption="Le tableau des échéances ouvertes, calculées à partir des changements de statut enregistrés (données de test)." %}

### Ce que chaque membre peut vérifier

Un participant figure nommément dans les documents transmis au régulateur. OptimCE lui ouvre une
page « Ce qui a été déclaré à mon sujet », avec les documents où il apparaît et les valeurs
transmises, figées à la date du dépôt.

## Ce que ça ne fait pas

**OptimCE ne dépose rien.** Aucun document ne part automatiquement vers la CWaPE ou vers le
gestionnaire de réseau. Le dépôt reste de votre ressort ; la plateforme prépare le document,
enregistre la date de transmission et conserve la version exacte qui est partie.

**OptimCE ne signe rien.** Les conventions restent des contrats que les parties relisent et
signent. Un document prérempli est prêt à être signé, il n'est pas signé dans l'application.

**Bruxelles et la Flandre : prévues, pas encore là.** Le module prépare aujourd'hui les documents
de la CWaPE. Bruxelles et la Flandre imposent leurs propres documents : leur prise en charge est
prévue, mais pas encore implémentée.

**Il ne vérifie pas le fond à votre place.** Un formulaire prérempli à partir de données fausses
reste faux. Relisez ce que vous déposez, et gardez sous la main les guides de la CWaPE.

## Questions fréquentes {#faq}

### OptimCE dépose-t-il le dossier auprès de la CWaPE ?

Non. OptimCE prépare les documents, mais le dépôt reste de votre ressort, par vos moyens habituels.
Vous enregistrez ensuite dans la plateforme que le dossier a été déposé, et à quelle date : c'est
cette date qui fait courir les délais. OptimCE ne signe rien non plus.

### Les formulaires sont-ils les versions officielles de la CWaPE ?

Oui. OptimCE part des fichiers officiels, non modifiés : onze lots de PDF remplissables, de
classeurs Excel et de conventions Word. Il les préremplit avec les données de la communauté ; les
champs qu'il ne sait pas déduire restent modifiables.

### Comment les délais sont-ils calculés ?

À partir du type de dossier, de la région et de la date de dépôt que vous avez enregistrée. Les
délais en jours ouvrables suivent le calendrier belge. Les échéances remontent dans le tableau de
bord du gestionnaire et sont signalées par e-mail.

### Les membres peuvent-ils voir ce qui a été déclaré à leur sujet ?

Oui. Chaque membre dispose d'une page « Ce qui a été déclaré à mon sujet » : il y voit les
documents où il apparaît et les valeurs transmises, telles qu'elles étaient à la date du dépôt.
Elles ne changent pas si ses informations sont corrigées ensuite.

## Pour aller plus loin

- [Communauté d'énergie : documents et délais CWaPE]({{ "cwape-administrative-documents" | ref_url }}) :
  chaque formulaire, qui le dépose, où et dans quel délai.
- [Créer une communauté d'énergie en Wallonie]({{ "create-energy-community-wallonia" | ref_url }}) :
  les étapes, de la forme juridique à la notification.

{% include product-cta.html page_key="cwape" guide="admin-doc-dossier-create" title="Préparer votre dossier CWaPE avec OptimCE" %}
