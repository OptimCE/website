---
layout: page
title: "Open source et auto-hébergement"
breadcrumb_title: "Open source"
subtitle: "Tout le code sous licence Apache 2.0 : hébergez OptimCE vous-même, reliez-le à vos outils, ou laissez-nous l'héberger."
description: "OptimCE est un logiciel open source pour communautés d'énergie, sous licence Apache 2.0 : auto-hébergement gratuit, API REST, événements NATS, quatre langues."
lang: fr
ref: product-open-source
permalink: /fonctionnalites/open-source/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "OptimCE est-il vraiment open source ?"
    a: "Oui. Tout le code est publié sous licence Apache 2.0, dans l'organisation GitHub optimce : pas de version bridée, pas de cœur propriétaire. La version hébergée et la version que vous installez vous-même donnent accès aux mêmes fonctionnalités."
  - q: "Puis-je utiliser OptimCE dans un cadre professionnel ?"
    a: "Oui. La licence Apache 2.0 permet d'utiliser, de modifier et de redistribuer le logiciel, y compris dans un cadre professionnel, à condition de conserver les mentions de licence et de droit d'auteur."
  - q: "Quelle différence entre OptimCE Cloud et l'auto-hébergement ?"
    a: "Qui héberge l'application. OptimCE Cloud tourne sur nos serveurs, sans installation ni maintenance, et il est gratuit pendant l'alpha. En auto-hébergement, OptimCE tourne sur votre infrastructure, gratuitement et sans restriction, mais vous assurez l'hébergement, les mises à jour et la disponibilité."
  - q: "Comment relier OptimCE à mes autres outils ?"
    a: "Par ses événements ou par son API. Une architecture événementielle (NATS) permet de brancher des outils tiers, comme un système de gestion d'énergie, et une API REST permet d'intégrer OptimCE à vos propres outils."
---

Une communauté d'énergie confie à son logiciel la liste de ses membres, leurs compteurs, ses
factures et ses dossiers au régulateur. Elle doit pouvoir le garder si son fournisseur change de
cap, choisir où il est hébergé et le relier à ses autres outils. OptimCE est un logiciel open
source : tout son code est publié sous licence Apache 2.0, et la même application tourne sur nos
serveurs ou sur les vôtres.

## Comment OptimCE s'en charge

### Tout le code, sous licence Apache 2.0

Il n'y a ni version bridée, ni cœur propriétaire : tout le code d'OptimCE est publié sous licence
Apache 2.0, dans l'organisation GitHub [optimce](https://github.com/optimce). Cette licence permet
d'utiliser, de modifier et de redistribuer le logiciel, y compris dans un cadre professionnel. En
contrepartie, elle demande de conserver les mentions de licence et de droit d'auteur, et de
signaler les fichiers modifiés.

Pour une communauté, cela veut dire qu'elle n'est liée à personne : si OptimCE Cloud ne lui
convient plus, elle peut faire tourner la même application ailleurs.

### Chez nous ou chez vous

Le même logiciel s'utilise de deux façons.

- **OptimCE Cloud** est la version hébergée, sur app.optimce.be : rien à installer, rien à
  maintenir. Elle est gratuite pendant toute la phase alpha.
- **L'auto-hébergement** installe OptimCE sur votre propre infrastructure, gratuitement et sans
  restriction, pour toujours. Le guide d'installation décrit le déploiement local de la stack
  complète avec Docker Compose.

Les deux voies donnent accès aux mêmes fonctionnalités. Le choix dépend surtout de qui vous êtes :
une communauté qui veut simplement l'outil n'a rien à installer, tandis qu'une équipe technique peut
héberger la plateforme, garder la maîtrise complète des données ou contribuer au code. Ce qui est
gratuit, et pour combien de temps, est détaillé sur la page des [tarifs]({{ "pricing" | ref_url }}).

### Une installation, plusieurs communautés

Une même installation d'OptimCE gère plusieurs communautés d'énergie. Un compte peut appartenir à
plusieurs communautés et passer de l'une à l'autre depuis « Mes communautés ». Un acteur qui
accompagne plusieurs projets, ou qui choisit d'héberger OptimCE pour d'autres, n'a donc pas besoin
d'une installation distincte pour chaque communauté.

### Relier vos outils

Une architecture événementielle (NATS) permet de brancher des outils tiers sur OptimCE, comme un
système de gestion d'énergie. Une API REST permet de l'intégrer à vos propres outils. Un outil que
la communauté utilise déjà peut ainsi échanger des données avec OptimCE plutôt que de les faire
ressaisir, au prix d'un travail d'intégration.

### Une interface en quatre langues

L'interface existe en français, en anglais, en néerlandais et en allemand, ce qui compte dans un
pays à trois langues officielles. Les e-mails envoyés par la plateforme existent dans les mêmes
quatre langues.

### Contribuer

Le guide d'installation s'adresse aussi aux équipes qui veulent contribuer au code : la stack
complète se lance en local avec Docker Compose. Les traductions de
l'interface se proposent en commun sur [Weblate](https://hosted.weblate.org/engage/optimce/), sans
toucher au code.

## Ce que ça ne fait pas

**Pas de garantie de service en auto-hébergement.** Sur vos serveurs, vous assurez vous-même
l'hébergement, les mises à jour et la disponibilité : aucune garantie de service n'est fournie sur
cette voie.

**Le guide d'installation décrit une stack de développement.** Ses bases de données ne sont pas
persistantes : les données sont réinitialisées au redémarrage des conteneurs. Pour un déploiement
destiné à durer, il faut configurer vous-même des volumes persistants et une stratégie de
sauvegarde.

**L'open source ne fait pas le travail à votre place.** Héberger un logiciel qui gère des données
de membres demande quelqu'un pour l'administrer. Sans cette personne, OptimCE Cloud reste la voie
la plus simple.

## Questions fréquentes {#faq}

### OptimCE est-il vraiment open source ?

Oui. Tout le code est publié sous licence Apache 2.0, dans l'organisation GitHub optimce : pas de
version bridée, pas de cœur propriétaire. La version hébergée et la version que vous installez
vous-même donnent accès aux mêmes fonctionnalités.

### Puis-je utiliser OptimCE dans un cadre professionnel ?

Oui. La licence Apache 2.0 permet d'utiliser, de modifier et de redistribuer le logiciel, y compris
dans un cadre professionnel, à condition de conserver les mentions de licence et de droit d'auteur.

### Quelle différence entre OptimCE Cloud et l'auto-hébergement ?

Qui héberge l'application. OptimCE Cloud tourne sur nos serveurs, sans installation ni maintenance,
et il est gratuit pendant l'alpha. En auto-hébergement, OptimCE tourne sur votre infrastructure,
gratuitement et sans restriction, mais vous assurez l'hébergement, les mises à jour et la
disponibilité.

### Comment relier OptimCE à mes autres outils ?

Par ses événements ou par son API. Une architecture événementielle (NATS) permet de brancher des
outils tiers, comme un système de gestion d'énergie, et une API REST permet d'intégrer OptimCE à
vos propres outils.

## Pour aller plus loin

- [Installer OptimCE : guide de démarrage]({{ "quick-start-guide" | ref_url }}) : les prérequis,
  le clonage du dépôt et le premier démarrage, étape par étape.
- [Tarifs d'OptimCE]({{ "pricing" | ref_url }}) : ce qui est gratuit aujourd'hui, et ce qui pourrait
  changer.
- [Logiciel de gestion de communauté d'énergie]({{ "features" | ref_url }}) : tout ce que fait
  OptimCE aujourd'hui.

{% include product-cta.html page_key="open-source" guide="getting-started" title="Essayer OptimCE sans rien installer" %}
