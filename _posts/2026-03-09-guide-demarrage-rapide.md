---
layout: post
title: "Guide de démarrage rapide avec OptimCE"
date: 2026-03-09 14:00:00 +0100
author: "Équipe OptimCE"
excerpt: "Découvrez comment installer et configurer OptimCE en quelques étapes pour commencer à gérer votre communauté d'énergie."
categories: [tutoriels]
lang: fr
ref: quick-start-guide
---

Ce guide vous accompagne dans l'installation et la première configuration d'OptimCE. En quelques étapes, vous serez prêt à gérer votre communauté d'énergie.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :

- **Node.js** (version 18 ou supérieure)
- **Angular CLI** pour le frontend
- **Python 3.10+** pour le backend analytique (FastAPI)
- **PostgreSQL** comme base de données
- **Docker** (optionnel, mais recommandé pour simplifier le déploiement)

## Installation

Clonez le dépôt principal depuis GitHub et installez les dépendances de chaque composant. Le projet est organisé en plusieurs modules indépendants : le frontend Angular, le backend principal en Node.js/TypeScript et le backend analytique en FastAPI.

## Configuration initiale

Une fois l'installation terminée, vous devrez configurer les variables d'environnement pour chaque composant : connexion à la base de données, paramètres d'authentification et configuration du système de messages.

## Créer votre première communauté

Après le déploiement, connectez-vous à l'interface d'administration pour créer votre première communauté d'énergie. Vous pourrez ensuite ajouter des membres, configurer leurs compteurs et définir les clés de répartition pour le partage d'énergie.

## Prochaines étapes

Consultez la documentation complète sur GitHub pour découvrir les fonctionnalités avancées : intégration de modules externes, configuration multi-tenant et personnalisation de l'interface.
