---
layout: post
title: "Launching OptimCE: the origins of the project"
date: 2026-03-01 10:00:00 +0100
last_modified_at: 2026-07-26 10:00:00 +0200
author: "Eric from OptimCE"
excerpt: "OptimCE was not born in an incubator but in a laboratory. A look back at Locomotrice, the Walloon research project that produced the platform, at the partners behind it, and at the reasons it was released as open source."
description: "Where OptimCE comes from: the Locomotrice research project, the ULiège and CECOTEPE partners, and why the platform is open source."
tags: [app, announcement]
lang: en
ref: launch-optimce
permalink: /en/news/2026/03/01/launch-optimce/
faq:
  - q: "Who develops OptimCE?"
    a: "OptimCE comes out of Locomotrice, a Walloon research project run between 2023 and 2026 and funded by the Walloon Region's Win2Wal programme. It is led by the University of Liège, through its BEMS laboratory, and by the CECOTEPE research centre, in collaboration with citizen energy cooperatives. Development now continues in the open, and outside contributions are welcome."
  - q: "Is OptimCE free?"
    a: "The platform is released under the Apache 2.0 licence: you can deploy it on your own infrastructure free of charge and without restriction. The hosted version, OptimCE Cloud, is currently in alpha and also free. A paid offer will appear as the product matures; alpha users will be told well in advance."
  - q: "Why an open-source platform for energy communities?"
    a: "Because an energy community runs on the trust of its members, and that trust is hard to build on a black box. The allocation key calculation determines how much each member receives and pays: being able to audit it is not a developer's luxury, it is a governance requirement. On top of that there is an economic reality — many communities are small structures for which an annual proprietary licence is out of proportion."
  - q: "Does OptimCE work outside Belgium?"
    a: "The architecture was designed to adapt to distinct regulatory frameworks, which was a necessity from the start: Belgium alone has three different regional regimes. Allocation key families, statuses and billing rules are configurable. Development and validation to date have focused mainly on the Belgian context."
  - q: "How can I contribute to the project?"
    a: "Everything happens in the OptimCE GitHub organisation. The monorepo aggregates the individual services and holds the orchestration configuration that brings the full stack up locally with Docker Compose. Code contributions are welcome, but feedback from community managers is just as valuable — they are the ones who have shaped the product so far."
---

Most software platforms start from a commercial hunch. OptimCE started from a **research project** — and that origin explains nearly everything else about it: the choice of open source, the functional scope, even the way features were prioritised.

## Locomotrice, a Walloon research project

OptimCE is the software output of **Locomotrice**, a research project run in Wallonia between **2023 and 2026** and funded by the Walloon Region's **Win2Wal** programme. That programme funds research led by academic partners with a view to transferring it into the regional economy — research meant, in other words, to leave the laboratory.

Three groups of actors carried the project:

- the **University of Liège**, through its **BEMS** laboratory;
- the **CECOTEPE** research centre;
- **citizen energy cooperatives**, present not as end users to be handed a tool, but as co-design partners.

That last point matters more than it might seem. An energy community is not a pure engineering problem: it is a regulatory, accounting and social object as much as a technical one. The features built were therefore validated in the field, with managers who were already handling members, meters and allocation keys — often in spreadsheets.

## The problem the research exposed

The starting observation is easy to state and painful to live with: **the administrative complexity of an energy community is out of all proportion to its size**.

A community of thirty households has to manage the same objects as an energy supplier — supply points, quarter-hourly readings, allocation keys, invoicing, grid operator reporting — with neither the headcount nor the systems. And the applicable framework is not stable: in Belgium energy is a regional competence, so Wallonia, Brussels and Flanders impose three distinct frameworks, with their own regulators and their own families of keys. The European framework above them is described in our article [“Energy communities in Europe: RED II and IEMD”](/en/news/2026/03/05/energy-communities-europe/).

The available tools were either spreadsheets — flexible but unauditable and quickly unmanageable — or proprietary solutions designed for players of an entirely different size.

## Why open source is not a detail

The decision to publish OptimCE as open source, under the **Apache 2.0** licence, follows directly from the nature of the thing being managed.

An energy community runs on **trust between its members**. The allocation key determines, quarter-hour by quarter-hour, how much energy each member receives and therefore how much they pay. Asking thirty households to trust a black box for that calculation is asking a great deal. Being able to open the code is not a developer comfort here: it is a **governance requirement**.

There is a more prosaic reason as well. Many communities are small, volunteer or semi-volunteer structures for which an annual proprietary licence is wildly out of proportion to the budget. A tool you cannot afford solves no problem at all.

## What the platform does today

OptimCE covers the full management cycle of a community:

- **Member management** — onboarding, roles, links between communities and users;
- **Meter tracking** — centralising supply points and readings;
- **Allocation keys** — configuration, versioned amendments and tracking of member acceptance;
- **Key generation and simulation** — proposing an optimised key from real data, and measuring its performance before it is adopted;
- **Billing** — from the price per kWh through to the PDF and payment tracking;
- **Community life** — a news board and polls, because participatory governance is a regulatory requirement as much as good practice;
- **Multi-community** — a single instance for several communities.

The architecture is **event-driven and modular**, which allows third-party modules to be plugged in without touching the core — a choice inherited directly from regulatory uncertainty: what changes every two years has to be able to change without rewriting the platform.

## Two ways to use it

**Self-hosted**, under the Apache 2.0 licence, free of charge and without restriction. You keep full control of the data, and you take on hosting, updates and availability. The procedure is set out in [“Install OptimCE: quick start guide”](/en/news/2026/03/09/quick-start-guide/).

**Through [OptimCE Cloud](https://app.optimce.be)**, the hosted and managed version, currently in alpha and free. No installation, no maintenance.

The details of the project, its partners and its funding are on the [About](/en/about/) page.

The platform has kept moving since that launch: see the [May 2026 release](/en/news/2026/05/07/release-news/), which introduced the public registry of sharing operations and the user guide.

## FAQ

### Who develops OptimCE?

OptimCE comes out of Locomotrice, a Walloon research project run between 2023 and 2026 and funded by the Walloon Region's Win2Wal programme. It is led by the University of Liège, through its BEMS laboratory, and by the CECOTEPE research centre, in collaboration with citizen energy cooperatives. Development now continues in the open, and outside contributions are welcome.

### Is OptimCE free?

The platform is released under the Apache 2.0 licence: you can deploy it on your own infrastructure free of charge and without restriction. The hosted version, OptimCE Cloud, is currently in alpha and also free. A paid offer will appear as the product matures; alpha users will be told well in advance.

### Why an open-source platform for energy communities?

Because an energy community runs on the trust of its members, and that trust is hard to build on a black box. The allocation key calculation determines how much each member receives and pays: being able to audit it is not a developer's luxury, it is a governance requirement. On top of that there is an economic reality — many communities are small structures for which an annual proprietary licence is out of proportion.

### Does OptimCE work outside Belgium?

The architecture was designed to adapt to distinct regulatory frameworks, which was a necessity from the start: Belgium alone has three different regional regimes. Allocation key families, statuses and billing rules are configurable. Development and validation to date have focused mainly on the Belgian context.

### How can I contribute to the project?

Everything happens in the OptimCE GitHub organisation. The monorepo aggregates the individual services and holds the orchestration configuration that brings the full stack up locally with Docker Compose. Code contributions are welcome, but feedback from community managers is just as valuable — they are the ones who have shaped the product so far.

## Going further

> **[Energy communities in Belgium: CER, CEC, CEL](/en/news/2026/05/11/energy-communities-belgium/)**
>
> The three Belgian statuses, energy sharing, and the role of the regulator and the grid operator.

> **[Install OptimCE: quick start guide](/en/news/2026/03/09/quick-start-guide/)**
>
> Deploy the full stack locally, or start with nothing to install.

<div class="post-cta" markdown="0">
  <h3>Discover OptimCE</h3>
  <p>Create your energy community in minutes on the hosted version, or deploy the platform on your own infrastructure. The code is open and contributions are welcome.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="https://app.optimce.be">Open the OptimCE app</a>
    <a class="btn btn-outline" href="https://github.com/optimce">See the project on GitHub</a>
  </p>
</div>
