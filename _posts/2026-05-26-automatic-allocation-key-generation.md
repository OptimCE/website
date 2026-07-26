---
layout: post
title: "Automatic allocation key generation"
date: 2026-05-26 00:00:00 +0200
author: "OptimCE Team"
excerpt: "OptimCE's automatic generation module is now live. It proposes optimised allocation keys from a community's real production and consumption data, with two algorithms — brute force on standard keys and LOGAAS, a CeCoTePe research output from the Locomotrice project."
description: "Two algorithms — brute force over standard keys and LOGAAS — that propose an optimised key from your community's real data."
tags: [allocation-key, app, guide]
lang: en
ref: optimce-allocation-key-generator
permalink: /en/news/2026/05/26/automatic-allocation-key-generation/
---

Picking the **allocation key** that gets the most out of a community's local production is a deceptively hard call. The vocabulary is set by the regulator, the standard keys are listed in a CWaPE or Fluvius document, and yet the *right* choice depends on something none of those texts can tell you: the actual quarter-hourly profiles of your members. A residential neighbourhood with a single school behaves very differently from a business park with a baseload, and the same key can recover 70% of the available production in one community and barely 50% in another.

OptimCE's **automatic allocation key generation module** is now live to take that decision out of gut-feel territory. Feed it a CSV of the community's real production and consumption data, and it returns a candidate key with an expected collective self-consumption rate — computed on your own data, not on a textbook example. Two **independent** algorithms ship today, both consuming the same CSV input: a **brute force** scan over the regionally validated standard keys, and **LOGAAS**, a hybrid linear-optimisation / genetic-algorithm approach developed by [**CeCoTePe**](https://cecotepe.be/) for the **Locomotrice** project. More algorithms can be added later.

If you are still mapping the regional landscape — what CWaPE, BRUGEL and VREG accept as a valid key — start with our reference article [“Allocation key in Belgium: the 3 regions”](/en/news/2026/05/19/allocation-key-belgium/).

<img src="/assets/images/diagrams/allocation-key-flow-en.svg"
     alt="Five-step diagram: quarter-hourly data, generation or simulation, candidate key, member validation, submission to the grid operator."
     width="800" height="330" loading="lazy" decoding="async"
     style="width:100%;height:auto">

## Why an allocation key deserves to be data-driven

The Belgian frameworks all agree on one thing: the allocation key is applied **quarter-hour by quarter-hour** on real smart-meter readings. That means its performance — the **collective self-consumption rate**, the **share of injected energy actually consumed by members** — depends entirely on how each member's profile lines up with the production curve.

A few patterns explain why manual choice underdelivers more often than not:

- **Profile diversity widens fast.** A community that starts as five identical households is easy to serve with an egalitarian fixed key. Add one tertiary consumer (a school, an SME, a public building) and the egalitarian split immediately leaves volumes on the table during business hours, when the large consumer could have absorbed them.
- **Production reshapes over time.** A roof extension, an inverter upgrade, a new cogeneration unit — each change shifts the curve. The key that was optimal last year may be sub-optimal today.
- **Standard keys are not fungible.** The three Walloon standard families (egalitarian fixed, specific fixed, dynamic) cover a wide range of cases, but the *best* of those three for a given community is not obvious without simulation. The same is true for the Brussels methods (fixed, prorata, hybrid) and the Flemish *verdeelsleutels* (vaste, relatieve, optimale).

Manual key selection therefore tends to under-use the available production. The point of an automatic generation module is not to replace human judgement on governance — it is to remove the **simulation cost** from the choice. Once a candidate is proposed, the community can still vote, amend and refine it.

## What the OptimCE module does

The module sits inside the existing **Allocation Keys** module of the open-source OptimCE core. The workflow is straightforward:

1. **Input** — 15-minute consumption data for each member, 15-minute production data for each generator, the list of participants in the sharing operation, and the region (Wallonia / Brussels / Flanders) so the algorithm knows which standard key families to respect.
2. **Choose an algorithm** — brute force or LOGAAS.
3. **Run** — the module simulates the chosen algorithm on the actual data and returns a **candidate key** together with the **expected collective self-consumption rate**, the **per-member share of shared energy**, and the **distribution of the residual injection**.
4. **Review** — the community manager can compare candidates, edit percentages, and validate.
5. **Apply** — the validated key flows into the existing Allocation Keys module as a new amendment, with full history tracking and member-acceptance status.

The module does **not** push a new key to the DSO autonomously. It produces a proposal; the existing amendment, signature and transmission workflow stays in place — including the regulator-authorisation step for non-standard keys in Wallonia.

## Algorithm 1 — Brute force on standard keys

The first algorithm is deliberately simple, and that is precisely its strength.

It builds a **candidate set** made of every standard key allowed in the community's region:

- In **Wallonia**: egalitarian fixed key, specific fixed key (with member-investment-weighted percentages), consumption-based dynamic key.
- In **Brussels**: fixed method (single-round and multi-round), prorata method, hybrid method.
- In **Flanders**: *vaste verdeelsleutel*, *relatieve verdeelsleutel*, *optimale verdeelsleutel*.

For each candidate, the algorithm **replays the community's actual quarter-hourly data** through the corresponding distribution rule and computes the resulting collective self-consumption rate, the share each member would have received and the residual injection. The candidate with the best performance — by default, the highest collective self-consumption — wins, and the module reports the runner-ups so the community can trade a few percentage points of performance for governance simplicity if that is the call.

The brute-force approach has two big advantages:

- **Regulator-compliant by construction.** The output is always one of the standard keys, so it goes through the regular DSO-acceptance route — no CWaPE non-standard authorisation needed in Wallonia.
- **Explainable.** The result is a known key family with known properties. You can defend it in front of a general assembly without invoking optimisation theory.

Its limit is the catalogue itself. If a community's profiles are atypical — strongly asymmetric, heavily seasonal, with one dominant consumer — the best of the standard keys may still leave noticeable performance on the table. That is where the second algorithm steps in.

## Algorithm 2 — LOGAAS

**LOGAAS** stands for *Linear Optimization with Genetic Algorithm with Atypical Speciation*. It is the output of research conducted by [CeCoTePe](https://cecotepe.be/) for the Locomotrice project, formally described in the preprint *Paque, E. & Hiard, S. (2025), "LOGAAS: A hybrid algorithmic approach to ex-post electricity allocation for energy communities"*.

Where brute force is bounded by the standard catalogue, LOGAAS searches a **broader space of candidate keys** — including non-standard combinations — by combining **linear optimisation** (to find the best ex-post allocation for a given iteration) with a **genetic algorithm** featuring **atypical speciation** (to find the best combination of percentages across the up to three allowed iterations, while preserving population diversity). The practical takeaway is that it can squeeze additional performance in cases where the standard families do not fit the profiles cleanly: highly heterogeneous member sets, seasonal industrial consumers paired with residential households, or large surplus producers that would otherwise re-inject most of their output on the public grid.

LOGAAS' output is a candidate **non-standard key**. In Wallonia, that means the community goes through the **CWaPE authorisation route** before the DSO can apply it — see the [Belgium allocation-key article](/en/news/2026/05/19/allocation-key-belgium/) for the procedure. In Brussels and Flanders, the room for non-standard keys is narrower; the LOGAAS output there is typically used as a benchmark — what would the best achievable performance look like — against which the chosen standard key is judged.

Use LOGAAS when the brute-force result feels close but not quite enough, when the project economics depend on the last few percentage points of collective self-consumption, or when you want a quantified upper bound to inform an investment decision.

## At-a-glance comparison

| Criterion | Manual choice | Brute force | LOGAAS |
|---|---|---|---|
| Input needed | Member list, regional framework | Member list + 15-min profiles | Member list + 15-min profiles |
| Search scope | One pre-selected key | All regional standard keys | Standard + non-standard combinations |
| Runtime | Instant (no computation) | Seconds | Minutes |
| Regulator-compliant out of the box | Yes (if standard) | Yes — always within the standard catalogue | Wallonia: needs CWaPE authorisation. Brussels / Flanders: typically used as a benchmark. |
| Result explainability | High | High — named key family | Lower — numerical output |
| Best for | Homogeneous community, governance-first projects | Most projects — the new default | Heterogeneous profiles, performance-critical projects |

The two algorithms are **two independent ways** to generate a key from the same CSV input — not pipeline steps. Brute force is the safer default for most projects; LOGAAS is the option to reach for when the standard catalogue is leaving performance on the table and a non-standard key is on the table.

## How to use the module

The module is available today in the OptimCE application:

1. Open the **Allocation Keys** module for the sharing operation you want to optimise.
2. Click **Generate a key**. Upload a CSV with the community's quarter-hourly consumption (per member) and production (per generator).
3. Pick an algorithm — brute force or LOGAAS. The two run independently on the same CSV; you can compare their outputs side by side.
4. Run. Review the candidate, its expected collective self-consumption rate, and the per-member share table.
5. Validate the candidate to start the amendment workflow: members sign, the representative transmits to the DSO, and the new key takes effect on the agreed date.

The whole loop, from data upload to amendment, lives inside OptimCE — no spreadsheet juggling between simulation, governance and reporting.

## What's coming next

The module is built around a pluggable algorithm interface, so adding new approaches does not require touching the core. Plausible next additions include **multi-objective optimisation** (balancing collective self-consumption against per-member fairness), **fairness-constrained variants** (capping the gap between the best- and worst-served members), and **scenario-based simulation** (testing a key against expected member churn or production growth). Each addition will be announced as it ships.

> ### Generate your allocation key with OptimCE
>
> An open-source platform built for Belgian energy communities: data-driven key generation, history of sharing operations, member-acceptance tracking and regulator reporting — in a single application.
>
> **[Get started on app.optimce.be →](https://app.optimce.be)**

## FAQ — Automatic allocation key generation

### What data does the module need?

Quarter-hourly **consumption** data for each member, quarter-hourly **production** data for each generator in the sharing operation, the list of participants and the region. A few weeks of data is enough to get a usable signal; a full year captures seasonal effects more reliably.

### Which algorithm should I pick?

Default to **brute force**: it is fast, fully explainable and stays within the standard catalogue accepted automatically by the DSO. Pick **LOGAAS** when you specifically want to explore beyond the standard catalogue — heterogeneous profiles, tight project economics, or you want to know how much performance the standard catalogue is leaving on the table. The two run independently on the same CSV; nothing prevents you from running both and comparing.

### Will the generated key be regulator-compliant?

The brute-force output is always one of the regional standard keys — directly accepted by the DSO with no extra authorisation. The LOGAAS output is a non-standard key; in Wallonia it goes through the **CWaPE authorisation route** before the DSO applies it. In Brussels and Flanders, non-standard keys are not the typical path, so the LOGAAS output is more often used as a performance benchmark there.

### Can I edit the suggestion before applying it?

Yes. The module returns a **candidate** — not a binding decision. You can adjust percentages, swap a key family, or override the algorithm's choice entirely before pushing it into the amendment workflow.

### Does the module replace expert judgement?

No. The module quantifies trade-offs; it does not decide whether your community prefers fairness over performance, predictability over optimisation, or simplicity over the last percentage point of self-consumption. Those are governance questions. The module shortens the technical loop so the assembly can spend its meeting on the governance question instead.

### How often should I rerun the algorithm?

A good rhythm is **once a year**, ideally before the annual general assembly that approves the sharing operation's amendments. Rerun sooner if the community grows, a producer is added or removed, or a member changes their consumption profile significantly (e.g., installs a heat pump or sells an industrial site).

## Key takeaways

The automatic generation module turns the allocation-key choice from a textbook exercise into a data-driven decision. **Brute force** finds the best standard key for the community's actual profiles — fast, explainable, regulator-compliant. **LOGAAS** explores beyond the standard catalogue when the project's economics need every percentage point. Together, they give community managers a tool to defend their key choice in front of the general assembly, the DSO and the regulator — backed by numbers from the community's own data.

To go further, see our companion guides:

> **[Allocation key in Belgium: the 3 regions](/en/news/2026/05/19/allocation-key-belgium/)**
>
> The regulatory primer — what CWaPE, BRUGEL and VREG accept, the three regional vocabularies, and how to pick a key family before letting OptimCE optimise inside it.

> **[Create an energy community in Wallonia](/en/news/2026/05/11/create-energy-community-wallonia/)**
>
> Framing the project, choosing between CER and CEC, notifying CWaPE, and launching the sharing — where the allocation key fits in the file.

> **[Join an energy community in Wallonia](/en/news/2026/05/11/join-energy-community-wallonia/)**
>
> Where to find an open operation, enrolment steps and what to check before signing the sharing agreement.

## Sources

- Paque, E. & Hiard, S. (2025). *LOGAAS: A hybrid algorithmic approach to ex-post electricity allocation for energy communities*. CeCoTePe preprint — formal description of the algorithm, its objective function and simulation results on synthetic energy-community data.
- [CeCoTePe](https://cecotepe.be/) — research centre behind the LOGAAS algorithm, partner in the Locomotrice project.
- [CWaPE — List of standard allocation keys](https://www.cwape.be/publications/document/5382) — proposal CD-23d27-CWaPE-0928 of 27 April 2023, the canonical list of Walloon standard keys.
- [Sibelga — Distribution methods for energy sharing](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methodes-de-repartition) — Brussels fixed / prorata / hybrid methods.
- [Fluvius — Protocol energiedelen, persoon-aan-persoonverkoop](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf) — Flemish technical protocol (v3.x, July 2024).
