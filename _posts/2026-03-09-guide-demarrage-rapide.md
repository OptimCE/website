---
layout: post
title: "Installer OptimCE : guide de démarrage"
date: 2026-03-09 14:00:00 +0100
last_modified_at: 2026-07-26 10:00:00 +0200
author: "Eric d'OptimCE"
excerpt: "Deux façons de démarrer avec OptimCE : la version hébergée, sans rien installer, ou le déploiement local de la stack complète avec Docker Compose. Prérequis, clonage avec sous-modules, variables d'environnement et démarrage, étape par étape."
description: "Prérequis, clonage du dépôt, variables d'environnement et premier démarrage : installer OptimCE en local, étape par étape."
tags: [app, guide]
lang: fr
ref: quick-start-guide
faq:
  - q: "Faut-il installer OptimCE pour l'utiliser ?"
    a: "Non. OptimCE Cloud est la version hébergée et gérée : vous créez un compte et vous commencez, sans installation ni maintenance. L'installation locale s'adresse aux équipes qui veulent héberger la plateforme sur leur propre infrastructure, garder la maîtrise complète des données, ou contribuer au code. Les deux donnent accès aux mêmes fonctionnalités."
  - q: "De quoi ai-je besoin pour installer OptimCE en local ?"
    a: "Trois choses seulement : Docker, Docker Compose et Git. Toute la stack — applications, bases de données PostgreSQL, Keycloak, passerelle API, stockage objet et messagerie — est orchestrée par Docker Compose depuis le dépôt monorepo. Vous n'avez pas à installer Node.js, Python ou PostgreSQL séparément sur votre machine."
  - q: "Pourquoi faut-il cloner avec --recurse-submodules ?"
    a: "Parce que le monorepo OptimCE agrège les différents services sous forme de sous-modules Git : CRM frontend et backend, génération et simulation de clés de répartition, facturation, génération documentaire et tableau d'actualités. Sans l'option --recurse-submodules, vous récupérez la configuration d'orchestration mais aucun code applicatif. Si l'oubli est déjà fait, git submodule update --init --recursive rattrape la situation."
  - q: "Les données de la stack de développement sont-elles conservées ?"
    a: "Non. Dans la configuration de développement, les bases de données ne sont pas persistantes : les données sont réinitialisées au redémarrage des conteneurs. C'est voulu — cela garantit un environnement propre à chaque test. Pour un déploiement destiné à durer, il faut configurer des volumes persistants et une stratégie de sauvegarde."
  - q: "Sous quelle licence OptimCE est-il publié ?"
    a: "Sous licence Apache 2.0. Vous pouvez déployer la plateforme sur votre propre infrastructure, gratuitement et sans restriction, y compris dans un cadre professionnel. En contrepartie de cette liberté, l'auto-hébergement implique que vous assuriez vous-même l'hébergement, les mises à jour et la disponibilité : aucune garantie de service n'est fournie sur cette voie."
---

Il y a deux façons de commencer avec OptimCE, et le bon choix dépend surtout de qui vous êtes.

Si vous gérez une communauté d'énergie et que vous voulez simplement l'outil, **[OptimCE Cloud](https://app.optimce.be)** est la version hébergée : pas d'installation, pas de maintenance, et actuellement gratuite en alpha. Passez directement au [guide utilisateur](https://guide.optimce.be).

Si vous êtes une équipe technique qui veut héberger la plateforme, garder la maîtrise complète des données ou contribuer au code, ce guide est pour vous. Il décrit le déploiement local de la stack complète.

## Ce que vous allez déployer

OptimCE n'est pas une application monolithique mais un **écosystème de microservices** orchestré depuis un dépôt central, le [monorepo](https://github.com/optimce/monorepo). Le démarrage lance :

- **sept applications** — CRM frontend et backend, génération de clés de répartition, simulation de clés, facturation, génération documentaire et tableau d'actualités ;
- **six bases PostgreSQL**, une par domaine fonctionnel ;
- les **services de plateforme** : Keycloak pour l'authentification, KrakenD comme passerelle API, Nginx en reverse proxy, MinIO pour le stockage objet, NATS pour la messagerie et Jaeger pour le tracing.

Cette architecture explique le choix d'outillage de la section suivante : vous n'installez pas les composants un par un, vous laissez Docker Compose s'en charger.

## Prérequis

Trois outils, et rien d'autre :

- **Docker**
- **Docker Compose**
- **Git**

Vous n'avez pas besoin d'installer Node.js, Python ou PostgreSQL sur votre machine : chaque service embarque son propre runtime dans son conteneur.

## 1. Cloner le dépôt

Le monorepo agrège les services sous forme de **sous-modules Git**. L'option `--recurse-submodules` n'est donc pas optionnelle :

```bash
git clone --recurse-submodules https://github.com/OptimCE/monorepo.git
cd monorepo
```

Si vous avez déjà cloné sans les sous-modules, vous récupérerez la configuration d'orchestration mais aucun code applicatif. Rattrapez avec :

```bash
git submodule update --init --recursive
```

## 2. Configurer les variables d'environnement

Avant le premier démarrage, renseignez les mots de passe dans le fichier `.env.dev` :

```
DB_PASSWORD=changeme_db_password
KEYCLOAK_DB_PASSWORD=changeme_keycloak_db_password
KEYCLOAK_ADMIN_PASSWORD=changeme_keycloak_admin_password
```

Changez ces valeurs, y compris en local. Un mot de passe de démonstration laissé en place est la façon la plus banale d'exposer une instance qui devait rester privée.

La base du CRM s'initialise automatiquement au premier démarrage à partir du script `crm-backend/database_script/init.sql`.

## 3. Démarrer la stack

La méthode recommandée passe par le script fourni :

```bash
chmod +x ./docker-stack.sh
./docker-stack.sh start
```

Si vous préférez piloter Docker Compose directement :

```bash
docker compose --env-file .env.dev -f docker-compose.dev.yml --profile dev up -d
```

Et pour reconstruire les images avant de lancer :

```bash
docker compose --env-file .env.dev -f docker-compose.dev.yml --profile dev up --build
```

> **Attention — les données ne sont pas persistantes.** Dans la configuration de développement, les bases sont réinitialisées au redémarrage des conteneurs. C'est un choix délibéré pour garantir un environnement propre à chaque test. Un déploiement durable exige des volumes persistants et une stratégie de sauvegarde.

## 4. Créer votre première communauté

Une fois la stack démarrée, connectez-vous à l'interface d'administration. L'authentification passe par **Keycloak** : utilisez le compte administrateur dont vous avez défini le mot de passe à l'étape 2.

L'ordre de mise en route est ensuite le même que sur la version hébergée :

1. créer la communauté et renseigner ses informations légales ;
2. ajouter les membres et associer leurs **points de fourniture** (EAN) ;
3. définir la **clé de répartition** de l'opération de partage ;
4. vérifier le calcul sur une période de test avant de transmettre au gestionnaire de réseau.

Le détail fonctionnel de chaque étape est couvert par le [guide utilisateur](https://guide.optimce.be), qui reste la référence à jour pour l'usage de l'application.

## Pour aller plus loin

Si vous découvrez le sujet plutôt que l'outil, commencez par le cadre :

> **[Communautés d'énergie en Belgique : CER, CEC, CEL](/actualites/2026/05/11/communautes-energie-belgique/)**
>
> Les trois statuts, le partage d'énergie et le rôle du régulateur et du GRD.

> **[Générer une clé de répartition optimale](/actualites/2026/05/26/generer-cle-repartition-optimale-optimce/)**
>
> Comment le module de génération propose une clé à partir de vos données réelles.

## FAQ

### Faut-il installer OptimCE pour l'utiliser ?

Non. OptimCE Cloud est la version hébergée et gérée : vous créez un compte et vous commencez, sans installation ni maintenance. L'installation locale s'adresse aux équipes qui veulent héberger la plateforme sur leur propre infrastructure, garder la maîtrise complète des données, ou contribuer au code. Les deux donnent accès aux mêmes fonctionnalités.

### De quoi ai-je besoin pour installer OptimCE en local ?

Trois choses seulement : Docker, Docker Compose et Git. Toute la stack — applications, bases de données PostgreSQL, Keycloak, passerelle API, stockage objet et messagerie — est orchestrée par Docker Compose depuis le dépôt monorepo. Vous n'avez pas à installer Node.js, Python ou PostgreSQL séparément sur votre machine.

### Pourquoi faut-il cloner avec `--recurse-submodules` ?

Parce que le monorepo OptimCE agrège les différents services sous forme de sous-modules Git : CRM frontend et backend, génération et simulation de clés de répartition, facturation, génération documentaire et tableau d'actualités. Sans l'option `--recurse-submodules`, vous récupérez la configuration d'orchestration mais aucun code applicatif. Si l'oubli est déjà fait, `git submodule update --init --recursive` rattrape la situation.

### Les données de la stack de développement sont-elles conservées ?

Non. Dans la configuration de développement, les bases de données ne sont pas persistantes : les données sont réinitialisées au redémarrage des conteneurs. C'est voulu — cela garantit un environnement propre à chaque test. Pour un déploiement destiné à durer, il faut configurer des volumes persistants et une stratégie de sauvegarde.

### Sous quelle licence OptimCE est-il publié ?

Sous licence Apache 2.0. Vous pouvez déployer la plateforme sur votre propre infrastructure, gratuitement et sans restriction, y compris dans un cadre professionnel. En contrepartie de cette liberté, l'auto-hébergement implique que vous assuriez vous-même l'hébergement, les mises à jour et la disponibilité : aucune garantie de service n'est fournie sur cette voie.

<div class="post-cta" markdown="0">
  <h3>Pas envie d'installer ? Utilisez OptimCE Cloud</h3>
  <p>La version hébergée est gratuite pendant l'alpha : aucune installation, aucune maintenance, les mêmes fonctionnalités. Créez votre communauté en quelques minutes ou parcourez les opérations de partage ouvertes.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="https://app.optimce.be">Ouvrir l'application OptimCE</a>
    <a class="btn btn-outline" href="https://github.com/optimce/monorepo">Voir le monorepo sur GitHub</a>
  </p>
</div>

## Sources

- [OptimCE — monorepo](https://github.com/optimce/monorepo) — configuration d'orchestration, script `docker-stack.sh` et instructions d'installation faisant foi.
- [OptimCE — organisation GitHub](https://github.com/optimce) — l'ensemble des services et leurs dépôts respectifs.
- [Guide utilisateur OptimCE](https://guide.optimce.be) — référence fonctionnelle à jour pour l'usage de l'application.
