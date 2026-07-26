---
layout: post
title: "Install OptimCE: quick start guide"
date: 2026-03-09 14:00:00 +0100
last_modified_at: 2026-07-26 10:00:00 +0200
author: "OptimCE Team"
excerpt: "Two ways to get started with OptimCE: the hosted version, with nothing to install, or a local deployment of the full stack with Docker Compose. Prerequisites, cloning with submodules, environment variables and first run, step by step."
description: "Prerequisites, cloning the repository, environment variables and first run: install OptimCE locally, step by step."
tags: [app, guide]
lang: en
ref: quick-start-guide
permalink: /en/news/2026/03/09/quick-start-guide/
faq:
  - q: "Do I have to install OptimCE to use it?"
    a: "No. OptimCE Cloud is the hosted, managed version: you create an account and start, with no installation and no maintenance. The local install is for teams that want to host the platform on their own infrastructure, keep full control of their data, or contribute to the code. Both give access to the same features."
  - q: "What do I need to install OptimCE locally?"
    a: "Three things only: Docker, Docker Compose and Git. The whole stack — applications, PostgreSQL databases, Keycloak, API gateway, object storage and messaging — is orchestrated by Docker Compose from the monorepo. You do not need to install Node.js, Python or PostgreSQL separately on your machine."
  - q: "Why do I have to clone with --recurse-submodules?"
    a: "Because the OptimCE monorepo aggregates the individual services as Git submodules: CRM frontend and backend, allocation key generation and simulation, billing, document generation and the news board. Without --recurse-submodules you get the orchestration configuration but no application code. If you already cloned without it, git submodule update --init --recursive fixes things."
  - q: "Is data in the development stack preserved?"
    a: "No. In the development configuration the databases are not persistent: data resets when the containers restart. That is deliberate — it guarantees a clean environment for every test. A deployment meant to last needs persistent volumes and a backup strategy."
  - q: "Under which licence is OptimCE published?"
    a: "Under the Apache 2.0 licence. You can deploy the platform on your own infrastructure, free of charge and without restriction, including in a professional setting. In exchange for that freedom, self-hosting means you handle hosting, updates and availability yourself: no service guarantee is provided on that path."
---

There are two ways to start with OptimCE, and the right one depends mostly on who you are.

If you run an energy community and simply want the tool, **[OptimCE Cloud](https://app.optimce.be)** is the hosted version: no installation, no maintenance, and currently free while in alpha. Go straight to the [user guide](https://guide.optimce.be).

If you are a technical team that wants to host the platform, keep full control of the data, or contribute to the code, this guide is for you. It covers deploying the full stack locally.

## What you are about to deploy

OptimCE is not a monolithic application but an **ecosystem of microservices**, orchestrated from a central repository, the [monorepo](https://github.com/optimce/monorepo). Starting it brings up:

- **seven applications** — CRM frontend and backend, allocation key generation, key simulation, billing, document generation and the news board;
- **six PostgreSQL databases**, one per functional domain;
- the **platform services**: Keycloak for authentication, KrakenD as the API gateway, Nginx as reverse proxy, MinIO for object storage, NATS for messaging and Jaeger for tracing.

That architecture explains the tooling choice in the next section: you do not install the components one by one, you let Docker Compose handle them.

## Prerequisites

Three tools, and nothing else:

- **Docker**
- **Docker Compose**
- **Git**

You do not need Node.js, Python or PostgreSQL on your machine: each service ships its own runtime inside its container.

## 1. Clone the repository

The monorepo aggregates the services as **Git submodules**, so `--recurse-submodules` is not optional:

```bash
git clone --recurse-submodules https://github.com/OptimCE/monorepo.git
cd monorepo
```

If you already cloned without submodules, you have the orchestration configuration but no application code. Recover with:

```bash
git submodule update --init --recursive
```

## 2. Configure the environment variables

Before the first run, set the passwords in `.env.dev`:

```
DB_PASSWORD=changeme_db_password
KEYCLOAK_DB_PASSWORD=changeme_keycloak_db_password
KEYCLOAK_ADMIN_PASSWORD=changeme_keycloak_admin_password
```

Change these values, local install or not. A demo password left in place is the most ordinary way to expose an instance that was meant to stay private.

The CRM database initialises automatically on first startup from the `crm-backend/database_script/init.sql` script.

## 3. Start the stack

The recommended route is the bundled script:

```bash
chmod +x ./docker-stack.sh
./docker-stack.sh start
```

If you would rather drive Docker Compose directly:

```bash
docker compose --env-file .env.dev -f docker-compose.dev.yml --profile dev up -d
```

And to rebuild the images before starting:

```bash
docker compose --env-file .env.dev -f docker-compose.dev.yml --profile dev up --build
```

> **Careful — data is not persistent.** In the development configuration the databases reset when the containers restart. This is a deliberate choice that guarantees a clean environment for every test. A lasting deployment requires persistent volumes and a backup strategy.

## 4. Create your first community

Once the stack is up, sign in to the admin interface. Authentication goes through **Keycloak**: use the admin account whose password you set in step 2.

The start-up order is then the same as on the hosted version:

1. create the community and fill in its legal details;
2. add the members and attach their **supply points** (EAN);
3. define the **allocation key** for the sharing operation;
4. check the calculation over a test period before submitting it to the grid operator.

The functional detail of each step is covered by the [user guide](https://guide.optimce.be), which remains the up-to-date reference for using the application.

## Going further

If the subject is new to you rather than the tool, start with the framework:

> **[Energy communities in Belgium: CER, CEC, CEL](/en/news/2026/05/11/energy-communities-belgium/)**
>
> The three statuses, energy sharing, and the role of the regulator and the grid operator.

> **[Automatic allocation key generation](/en/news/2026/05/26/automatic-allocation-key-generation/)**
>
> How the generation module proposes a key from your community's real data.

## FAQ

### Do I have to install OptimCE to use it?

No. OptimCE Cloud is the hosted, managed version: you create an account and start, with no installation and no maintenance. The local install is for teams that want to host the platform on their own infrastructure, keep full control of their data, or contribute to the code. Both give access to the same features.

### What do I need to install OptimCE locally?

Three things only: Docker, Docker Compose and Git. The whole stack — applications, PostgreSQL databases, Keycloak, API gateway, object storage and messaging — is orchestrated by Docker Compose from the monorepo. You do not need to install Node.js, Python or PostgreSQL separately on your machine.

### Why do I have to clone with `--recurse-submodules`?

Because the OptimCE monorepo aggregates the individual services as Git submodules: CRM frontend and backend, allocation key generation and simulation, billing, document generation and the news board. Without `--recurse-submodules` you get the orchestration configuration but no application code. If you already cloned without it, `git submodule update --init --recursive` fixes things.

### Is data in the development stack preserved?

No. In the development configuration the databases are not persistent: data resets when the containers restart. That is deliberate — it guarantees a clean environment for every test. A deployment meant to last needs persistent volumes and a backup strategy.

### Under which licence is OptimCE published?

Under the Apache 2.0 licence. You can deploy the platform on your own infrastructure, free of charge and without restriction, including in a professional setting. In exchange for that freedom, self-hosting means you handle hosting, updates and availability yourself: no service guarantee is provided on that path.

<div class="post-cta" markdown="0">
  <h3>Would rather not install? Use OptimCE Cloud</h3>
  <p>The hosted version is free during the alpha: no installation, no maintenance, the same features. Create your community in minutes or browse the open sharing operations.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="https://app.optimce.be">Open the OptimCE app</a>
    <a class="btn btn-outline" href="https://github.com/optimce/monorepo">See the monorepo on GitHub</a>
  </p>
</div>

## Sources

- [OptimCE — monorepo](https://github.com/optimce/monorepo) — orchestration configuration, the `docker-stack.sh` script and the authoritative install instructions.
- [OptimCE — GitHub organisation](https://github.com/optimce) — all services and their respective repositories.
- [OptimCE user guide](https://guide.optimce.be) — the up-to-date functional reference for using the application.
