---
layout: post
title: "Quick start guide with OptimCE"
date: 2026-03-09 14:00:00 +0100
author: "OptimCE Team"
excerpt: "Discover how to install and configure OptimCE in a few steps to start managing your energy community."
categories: [tutorials]
lang: en
ref: quick-start-guide
permalink: /en/news/2026/03/09/quick-start-guide/
---

This guide walks you through the installation and initial setup of OptimCE. In just a few steps, you will be ready to manage your energy community.

## Prerequisites

Before starting, make sure you have the following installed on your machine:

- **Node.js** (version 18 or higher)
- **Angular CLI** for the frontend
- **Python 3.10+** for the analytics backend (FastAPI)
- **PostgreSQL** as database
- **Docker** (optional, but recommended to simplify deployment)

## Installation

Clone the main repository from GitHub and install the dependencies for each component. The project is organised into several independent modules: the Angular frontend, the main Node.js/TypeScript backend and the FastAPI analytics backend.

## Initial configuration

Once the installation is complete, you will need to configure the environment variables for each component: database connection, authentication parameters and messaging system configuration.

## Create your first community

After deployment, log in to the administration interface to create your first energy community. You can then add members, configure their meters and define allocation keys for energy sharing.

## Next steps

Check the full documentation on GitHub to discover advanced features: external module integration, multi-tenant configuration and interface customisation.
