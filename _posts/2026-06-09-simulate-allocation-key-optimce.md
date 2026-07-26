---
layout: post
title: "Simulate an allocation key: test your scenarios"
date: 2026-06-09 10:00:00 +0200
author: "OptimCE Team"
excerpt: "New OptimCE feature: simulate an allocation key on your own data and measure self-consumption, surplus, self-sufficiency and the sharing rate."
description: "Simulate a key on your own data and measure self-consumption, surplus, self-sufficiency and the sharing rate before you commit."
tags: [allocation-key, app, news]
lang: en
ref: optimce-allocation-key-simulation
permalink: /en/news/2026/06/09/simulate-allocation-key-optimce/
faq:
  - q: "What does it mean to simulate an allocation key?"
    a: "It means replaying real production and consumption data through a chosen allocation key, without applying it in production, to measure its indicators in advance: collective self-consumption, surplus, self-sufficiency rate and sharing rate. It is a 'what-if' test before you decide."
  - q: "What is the difference between simulating and generating an allocation key?"
    a: "Automatic generation proposes the best key from your data (brute force over standard keys or the LOGAAS algorithm). Simulation tests a key you have chosen on a given dataset and shows its indicators. The two are complementary: you generate to find a good candidate, and you simulate to understand and compare scenarios."
  - q: "What is the difference between self-consumption rate, self-sufficiency rate and sharing rate?"
    a: "The self-consumption rate is measured on the production side: the share of locally produced energy consumed by members. The self-sufficiency rate is measured on the consumption side: the share of members' consumption covered by local production. The sharing rate shows how much of the injection was actually distributed to members through the key."
  - q: "What do the 'per iteration' results mean?"
    a: "Many keys distribute energy in several rounds (iterations): a first round allocates according to the rule, then energy left unconsumed is redistributed in the next round. The simulation shows the result globally, per time step and per iteration, so you can see how sharing progresses round after round."
  - q: "What data do I need to import to run a simulation?"
    a: "A CSV file containing each member's consumption per time step (often quarter-hourly) and each producer's production for the sharing operation. Each row corresponds to one time step. A few weeks of data already give a usable signal; a full year better captures seasonality."
  - q: "Does the simulation change my live allocation key?"
    a: "No. The simulation is an 'out-of-production' calculation: it touches neither the key applied by the grid operator nor your real data. You can test as many scenarios as you want with no effect on the ongoing sharing operation."
---

Choosing an **allocation key** means deciding, quarter-hour by quarter-hour, who receives which share of the energy produced locally. But how do you know, *before* putting it in place, whether a given key will actually improve your community's self-consumption — or let production slip onto the grid? OptimCE's new feature answers exactly that question: **simulate an allocation key** on your own data and read its performance indicators immediately.

The idea is simple: you import a dataset, you choose a key, and the simulation replays each time step through that key to return **self-consumption**, **surplus**, the **self-sufficiency rate** and the **sharing rate** — globally, per time step and per iteration. You test a scenario without applying it, risk-free, and you decide on figures rather than on gut feel.

If allocation keys are a new concept for you, start with our reference article [“Allocation key in Belgium: the 3 regions”](/en/news/2026/05/19/allocation-key-belgium/) — it sets out the vocabulary used here.

## Why simulate an allocation key?

An allocation key is not neutral: depending on the community's consumption and production profiles, **the same key can create a lot of value in one project and destroy it in another**. A fixed egalitarian key is perfect for ten households with similar profiles, but leaves volumes unused as soon as a large consumer — a school, an SME, a public building — joins the group. A dynamic key, on the other hand, recovers that lost production, at the cost of a share that varies from month to month.

The problem is that **arbitrating on gut feel is risky**. Solar production curves and consumption profiles cross in non-trivial ways at the 15-minute step; by eye, it is impossible to predict whether key A will beat key B over a full year. And the stakes are concrete: every point of self-consumption gained is surplus no longer injected at a low price, so more value kept inside the community.

Simulating is precisely about **taking that decision out of gut-feel territory**. You measure the real effect of a key on the indicators that matter — self-consumption, surplus, self-sufficiency, sharing rate — before committing to anything. To understand why these indicators are central to a community's value, see our article [“Energy self-consumption in Belgium”](/en/news/2026/06/05/energy-self-consumption-belgium/).

## What the simulation lets you do

The feature is built into the **"Allocation keys" module** of OptimCE's open-source core. The user flow takes just a few steps:

1. **Import a CSV** with consumption data per time step (often quarter-hourly) for each member and production data for each producer in the sharing operation. Each row of the file corresponds to one time step.
2. **Choose an allocation key** to test — a standard key for your region, an existing community key, or a scenario you want to explore.
3. **Run the simulation.** OptimCE replays each time step through the key and its various iterations, then aggregates the results.
4. **Read the indicators** returned, at three levels of granularity: **global** (over the whole period), **per time step** (quarter-hour by quarter-hour) and **per iteration** (round after round of distribution).

Here is, at a glance, what you provide and what you get:

| You import | You get |
|---|---|
| Consumption per time step, per member | Simulated collective self-consumption rate |
| Production per time step, per producer | Simulated surplus (injected energy not shared) |
| The allocation key to test | Self-sufficiency rate and sharing rate |
| | Breakdown: global, per time step and per iteration |

The result is not a theoretical estimate drawn from a textbook example: it is computed **on your own data**. That is what makes the simulation useful for deciding.

## Reading the indicators

Four indicators summarise a key's performance. They are simple once clearly distinguished — and that is often where confusion arises.

### The self-consumption rate

The **collective self-consumption rate** is measured **on the production side**: the share of locally produced energy that members actually consume, rather than inject onto the grid. The higher it is, the better the local production is valued within the community.

### Surplus

**Surplus** is the other side of self-consumption: it is the energy injected by producers that **no one in the community consumed**, and which therefore flows back onto the public grid, usually resold at low value. The link is direct: **the more local consumption absorbs production, the lower the surplus**. A good key reduces surplus by steering energy toward the members who need it at the right moment.

### The self-sufficiency rate

The **self-sufficiency rate** is measured **on the consumption side**: the share of members' consumption covered by shared local production, rather than bought from the supplier. It mirrors self-consumption, seen from the members' bill rather than from the panels.

### The sharing rate and the per-iteration view

The **sharing rate** shows how much of the available injection was actually **distributed to members through the key**. This is where the **per-iteration** view comes in. Many keys distribute over several rounds: a first round allocates energy according to the rule, then the energy a member did not consume is **redistributed in the next round** among those still in demand (this is the principle of "multi-round", relative or optimal keys). The simulation shows how the sharing rate **progresses at each iteration**, until the shareable injection is exhausted — you see exactly what the successive rounds add.

To avoid any confusion, this table summarises where each indicator sits:

| Indicator | Measured… | Answers the question |
|---|---|---|
| Self-consumption rate | on the **production** side | What share of production is consumed locally? |
| Surplus | on the **production** side | What share of production goes onto the grid? |
| Self-sufficiency rate | on the **consumption** side | What share of consumption is covered locally? |
| Sharing rate | the **key**'s mechanics | What share of injection was distributed, round by round? |

## When to use the simulation

The simulation is useful at every stage of an energy community's life.

- **Before launch.** You compare several candidate keys on historical or estimated data and choose the one that best serves the project's goals, with full knowledge.
- **During design.** You explicitly arbitrate between **fairness** (a readable, predictable key for members) and **overall performance** (a key that maximises collective self-consumption), with figures to back it up.
- **During day-to-day operation.** You measure the effect of a **new dataset** or a **change in profiles** (one member installs a heat pump, another a charging point) on the indicators — without breaking anything in the ongoing operation.
- **When updating the key.** When a **member joins or leaves** the community, you simulate the recalculated key before submitting it, to check it stays performant. Our article on the [allocation key in Belgium](/en/news/2026/05/19/allocation-key-belgium/) details the procedure for changing a key after start-up, and the [guide to creating a community in Wallonia](/en/news/2026/05/11/create-energy-community-wallonia/) places that step within the regulator file.

## The value for communities

For a community manager, a facilitator or a project developer, simulation changes how decisions are made:

- **A faster, more rational decision.** No more juggling simulation spreadsheets and rough estimates: the indicators appear directly in the tool that already manages the community.
- **Pedagogy.** By seeing *why* one key works better than another on real data, members understand and adopt the choice more easily. The simulation turns an abstract technical discussion into a concrete demonstration.
- **A solid argument.** Before a general assembly, a grid operator or a regulator, defending a key with figures — drawn from the community's own data — carries far more weight than a recommendation in principle.

It is also a lever for valuing local production, and therefore for [reducing members' electricity bills](/en/news/2026/06/03/energy-community-reduce-electricity-bill/): every point of surplus avoided is value kept inside the community.

## Simulation and automatic generation: two complementary tools

OptimCE already offers an **automatic generation module** that *proposes* the best key from the data — via a **brute force** over regional standard keys and via **LOGAAS**, an algorithm from CeCoTePe research for the Locomotrice project. The simulation, in contrast, *tests* a key that **you** have chosen.

These are two complementary uses, not competing ones:

| | Simulation | Automatic generation |
|---|---|---|
| Question asked | "What does *this* key give on this data?" | "*Which* key is best for this data?" |
| Input | A chosen key + a CSV | A CSV |
| Output | The KPIs of the tested key | One (or more) optimised candidate key(s) |
| Typical use | Compare scenarios, understand, justify | Find a good starting point |

In practice, you generate to find a solid candidate, then simulate to understand its behaviour, compare variants and defend it. For the algorithm details, see [“Automatic allocation key generation”](/en/news/2026/05/26/automatic-allocation-key-generation/).

## Energy communities in Belgium, in brief

An **energy community** brings together producers and consumers who locally share renewable production. Sharing is administrative: smart meters are read at a **15-minute** step, and the **distribution system operator (DSO)** applies the chosen allocation key to assign each member a share of the injected energy. Belgium recognises several forms — REC, CEC and, in Brussels, LEC — overseen by regional regulators ([Brugel](https://energysharing.brugel.brussels) in Brussels, with [Sibelga](https://www.sibelga.be/en/connections-meters/renewable-energy/energy-sharing) as grid operator).

In this landscape, the allocation key is the central parameter of a community's performance — and the simulation meets a real need: **to structure and understand energy sharing** before committing to it. For the full picture of legal forms, see [“Energy communities in Belgium: CER, CEC, CEL”](/en/news/2026/05/11/energy-communities-belgium/).

## Conclusion

Allocation key simulation brings one simple but decisive thing: **the ability to test before deploying**. Rather than choosing a key on gut feel and discovering its effects afterwards, you measure self-consumption, surplus, self-sufficiency and the sharing rate in advance on your own data — globally and round by round. That means less risk, more pedagogy, and governance decisions backed by figures.

> ### Simulate your allocation key with OptimCE
>
> Open-source platform built for Belgian energy communities: simulate a key on your data, compare scenarios, generate an optimal key, keep a history of sharing operations and prepare regulator reporting — all in a single application.
>
> **[Get started on app.optimce.be →](https://app.optimce.be)**

## FAQ

### What does it mean to simulate an allocation key?

It means replaying real production and consumption data through a chosen allocation key, **without applying it in production**, to measure its indicators in advance: collective self-consumption, surplus, self-sufficiency rate and sharing rate. It is a "what-if" test before you decide.

### What is the difference between simulating and generating an allocation key?

**Automatic generation** proposes the best key from your data (brute force over standard keys or the LOGAAS algorithm). **Simulation** tests a key you have chosen on a given dataset and shows its indicators. The two are complementary: you generate to find a good candidate, and you simulate to understand and compare scenarios.

### What is the difference between self-consumption rate, self-sufficiency rate and sharing rate?

The **self-consumption rate** is measured on the production side: the share of locally produced energy consumed by members. The **self-sufficiency rate** is measured on the consumption side: the share of members' consumption covered by local production. The **sharing rate** shows how much of the injection was actually distributed to members through the key.

### What do the "per iteration" results mean?

Many keys distribute energy in several rounds (iterations): a first round allocates according to the rule, then energy left unconsumed is redistributed in the next round. The simulation shows the result **globally**, **per time step** and **per iteration**, so you can see how sharing progresses round after round.

### What data do I need to import to run a simulation?

A **CSV** file containing each member's consumption per time step (often quarter-hourly) and each producer's production for the sharing operation. Each row corresponds to one time step. A few weeks of data already give a usable signal; a full year better captures seasonality.

### Does the simulation change my live allocation key?

No. The simulation is an "out-of-production" calculation: it touches neither the key applied by the grid operator nor your real data. You can test as many scenarios as you want with no effect on the ongoing sharing operation.

## Sources

- [Brugel — Energy Sharing](https://energysharing.brugel.brussels) — the Brussels regulator's official portal on energy sharing and the energy community framework.
- [Brugel — Energy communities](https://energysharing.brugel.brussels/blog/energy-sharing-18/communautes-d-energie-406) — authorisation, validity period and regulatory framework in Brussels.
- [Sibelga — Sharing energy in a community](https://www.sibelga.be/en/connections-meters/renewable-energy/energy-sharing/sharing-energy-in-an-energy-communitiy) — conditions, actors and principles of sharing in Brussels.
- [IÖW — Self-consumption and self-sufficiency in energy sharing communities](https://www.ioew.de/en/publication/self_consumption_and_self_sufficiency_in_energy_sharing_communities_in_germany) — methodological reference on self-consumption and self-sufficiency indicators.
- [KPMG — Energy sharing in Belgium: overview and policy recommendations](https://kpmg.com/be/en/insights/industries/energy-natural-resources-insights/energy-sharing-in-belgium-overview-and-policy-recom.html) — overview of energy sharing in Belgium.
- [Pricing and sharing rules for energy communities](https://econpapers.repec.org/article/eeejuipol/v_3a96_3ay_3a2025_3ai_3ac_3as0957178725001109.htm) — research on sharing rules and internal pricing, which justifies the value of a simulation.
