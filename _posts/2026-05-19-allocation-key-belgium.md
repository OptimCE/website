---
layout: post
title: "Allocation key in Belgium: Wallonia, Brussels and Flanders compared"
date: 2026-05-19 10:00:00 +0200
author: "OptimCE Team"
excerpt: "Allocation key in an energy community — types accepted by CWaPE, BRUGEL and VREG, regional differences across Wallonia, Brussels and Flanders, and practical guidance to choose one."
tags: [allocation-key, administrative]
lang: en
ref: allocation-key-belgium
last_modified_at: 2026-07-20 10:00:00 +0200
permalink: /en/news/2026/05/19/allocation-key-belgium/
---

The **allocation key** is the quiet piece of machinery that turns a local electricity production into a tangible benefit for each member of an energy community. Quarter-hour by quarter-hour, it decides *who gets how much* of the shared energy. And that is precisely where Belgium gets complicated: Wallonia, Brussels and Flanders have not adopted the same grid of standard keys, do not use the same vocabulary, and do not impose the same validation rules.

This article walks through the three regional frameworks — **CWaPE / ORES / RESA / AIEG** in Wallonia, **BRUGEL / Sibelga** in Brussels, **VREG / Fluvius** in Flanders — to compare what is actually allowed in each region and help community managers pick a key that holds over time. If you are new to the very idea of an energy community, start with our article [“Energy communities in Belgium: CER, CEC and CEL explained”](/en/news/2026/05/11/energy-communities-belgium/) — it sets the vocabulary used here.

## Allocation key: a quick refresher

An **allocation key** is the calculation rule, expressed as percentages, that determines how the energy injected on the grid by the producers of a sharing operation is attributed to each consumer member. It is not physical: electrons keep flowing through the public grid. It is administrative and virtual, computed by the **distribution system operator (DSO)** from the smart-meter readings at a **15-minute resolution**.

Concretely, for every quarter-hour:

1. The DSO records the energy **injected** by the producers in the community.
2. It records the energy **withdrawn** by each consumer.
3. It applies the **allocation key** validated by the community to attribute a share of the injected volume to each consumer.
4. The shared volume attributed to each member is passed on to their **energy supplier**, who values it at the community's internal tariff rather than the standard market tariff.

This logic applies to all sharing configurations: **intra-building collective self-consumption**, **CER**, **CEC** and **CEL** (in Brussels). For the detailed administrative mechanics, see [CWaPE's reference page on shared volume distribution](https://www.cwape.be/node/6068).

The strategic role of a key is therefore twofold: **distribute a limited resource fairly** among members and **maximise the local consumption** of a local production. The right balance depends on the project: a residential neighbourhood around a municipal PV roof is not the same as a business park connected to a cogeneration plant.

## The Walloon framework: three standard keys validated by CWaPE

In Wallonia, energy sharing is governed by the 12 April 2001 decree on the regional electricity market (article 35sexdecies, § 2). On that basis, the [CWaPE](https://www.cwape.be/secteur/communautes-partage-energie) — in consultation with the DSOs — published a **list of standard allocation keys** automatically accepted by network operators. The reference document is the [CD-23d27-CWaPE-0928 proposal of 27 April 2023](https://www.cwape.be/publications/document/5382).

### The three Walloon standard keys

| Key | Logic | Best suited for |
|---|---|---|
| **Egalitarian fixed key** (*clé fixe égalitaire*) | Shared volume split equally between all participants. Automatic adjustment when a member joins or leaves. | Citizen-led projects where fairness is the priority. |
| **Specific fixed key** (*clé fixe spécifique*) | Predefined percentages, often aligned with **investment shares** in the production units. | Cooperatives, co-financed business parks, set-ups where some members invested more. |
| **Consumption-based dynamic key** (*clé dynamique*) | Distribution prorated on each member's actual consumption during the quarter-hour. Favours larger consumers when production is high. | Mixed projects aimed at **maximising collective self-consumption**. |

### Non-standard keys

A community can **propose an alternative key**, but it then needs to be **specifically authorised**: ORES, RESA or AIEG forwards it to CWaPE, which validates or asks for adjustments. This route remains a minority case; in practice the three standard keys cover the vast majority of Walloon projects.

### Modifying a key after launch

That is possible. The **community representative** submits the request to the DSO, members sign an **amendment to the sharing agreement**, and the change takes effect on a date agreed with the network operator. The [ORES — Energy sharing in practice](https://www.ores.be/professionnel/en-pratique) page details the operational steps on the DSO side.

For the full creation procedure and where the key fits into the CWaPE notification, see our guide [“How to create an energy community in Wallonia: a step-by-step guide”](/en/news/2026/05/11/create-energy-community-wallonia/).

## The Brussels framework: fixed, prorata and hybrid methods

In Brussels, the regulator is [BRUGEL](https://www.brugel.brussels/themes/energies-renouvelables-11/partage-d-energie-420) and the single DSO is **Sibelga**. The Brussels framework recognises three sharing configurations — **CEL (Local Energy Community)**, **intra-building collective self-consumption** and **peer-to-peer (P2P) sale** — and **three distribution methods** are operated by Sibelga for the first two (P2P does not require an allocation key).

### The three official Brussels methods

| Method | Logic | Brussels-specific feature |
|---|---|---|
| **Fixed method** | A constant percentage attributed to each participant per quarter-hour. **“Single-round”** variant (one distribution pass) or **“multi-round”** (energy not consumed gets redistributed among participants who have not saturated their allocation). | The multi-round variant boosts the collective self-consumption rate. |
| **Prorata method** | Distribution based on individual consumption as a share of the group total. If your consumption is **20% of the group total**, you receive **20% of the available injection**. | Completed in **one round**. |
| **Hybrid method** | Sequential combination: first a **fixed** allocation, then any surplus is redistributed **prorata** among participants still in demand. | A trade-off between predictability (fixed) and optimisation (prorata). |

The textbook example from [Sibelga](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methodes-de-repartition) — 1 producer, 4 consumers, fixed key — gives **25% of the injection to each consumer** per quarter-hour. If one of them consumes less than their share, the multi-round variant redistributes the balance to the other three.

### Modifying and billing

The method can be **changed at any time** at the request of the operation's single point of contact. That same single point of contact also handles **internal billing** to members based on monthly data provided by Sibelga — Sibelga does not arbitrate, it computes and forwards.

That internal billing, precisely, no longer has to be done by hand: OptimCE now offers a [first working version of its billing module](/en/news/2026/07/16/energy-community-billing-optimce/), which generates member invoices from the settlement data — starting with the Walloon framework, other regions to follow.

For the economic context and tariff impact in Brussels, see [Renouvelle's analysis of costs and benefits of electricity sharing in Brussels](https://www.renouvelle.be/fr/quels-couts-avantages-sur-le-partage-delectricite-et-les-communautes-denergie-a-bruxelles/) and the [2024 study on the potential of Brussels energy communities](https://document.environnement.brussels/opac_css/elecfile/RAP_2024_CommunautesEnergie.pdf).

## The Flemish framework: verdeelsleutel under the Fluvius protocol

In Flanders, the regulator is the [VREG](https://www.vlaamsenutsregulator.be) and the DSO is Fluvius. The framework applies to **energy sharing** (*energiedelen*) within a group, **peer-to-peer sale** (*persoon-aan-persoonverkoop*) and **energy communities** (CER and CEC, translated as *hernieuwbare-energiegemeenschap* and *burgerenergiegemeenschap*).

Technically, the 15-minute resolution and the requirement of a **“meetregime 3” digital meter** are mandatory. Three keys — called *verdeelsleutels* — are supported by the [Fluvius protocol](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf).

### The three verdeelsleutels

| Verdeelsleutel | English equivalent | Logic |
|---|---|---|
| **Vaste verdeelsleutel** | Fixed key | A predefined percentage per participant for each quarter-hour. |
| **Relatieve verdeelsleutel** | Relative key | Fixed key **plus a redistribution round**: injected energy not consumed by some is shared prorata among participants who have not saturated their allocation. |
| **Optimale verdeelsleutel** | Optimal key | Starts from the agreed key but **iterates over several rounds** until the injection available for the quarter-hour is fully consumed. Maximises the collective self-consumption rate. |

The group manager picks the key based on the **installed capacity at each participant**, the **number of members**, the **expected production**, the **financial contributions** and any other local criteria. Agreements must be documented and communicated to all members before go-live.

A practical difference with Wallonia: Flanders does **not have a published list of “standard” keys** like the CWaPE — the Fluvius operational protocol is the authoritative source, and each community defines its key within that frame. For Walloon regulatory rulings that also touch Flanders, see the [CWaPE decision on allocation keys between Flanders and Wallonia](https://www.cwape.be/documents-recents/decision-relative-lapprobation-de-la-proposition-de-cles-de-repartition-entre) for cross-border setups.

## At-a-glance comparison of the three regions

| Criterion | Wallonia | Brussels | Flanders |
|---|---|---|---|
| Regulator | **CWaPE** | **BRUGEL** | **VREG** |
| DSO | ORES / RESA / AIEG | **Sibelga** (single) | **Fluvius** (single) |
| Reference document | Proposal CD-23d27-CWaPE-0928 (27/04/2023) | Sibelga “Distribution methods” page | Fluvius protocol v3.x (July 2024) |
| Key #1 — Egalitarian | Egalitarian fixed key | Fixed method (one round, equal shares) | Vaste verdeelsleutel |
| Key #2 — Specific percentages | Specific fixed key | Fixed method (predefined percentages) | Vaste verdeelsleutel (negotiated percentages) |
| Key #3 — “Optimisation” logic | **Dynamic key** (consumption prorata) | **Prorata method** + **hybrid method** | **Relatieve** + **optimale verdeelsleutel** |
| Non-standard keys | Possible with CWaPE authorisation | Method can be changed at any time | Defined within the Fluvius protocol |
| Smart meter | Mandatory | Mandatory | “Meetregime 3” digital meter |
| Calculation step | 15 minutes | 15 minutes | 15 minutes |

Three frameworks, three vocabularies, but a **strong convergence on the substance**: all rely on the quarter-hour and smart meters, and all offer at least one **“fixed”** family and one **“dynamic / optimised”** family. The nuances matter mostly for governance and the financial predictability of members.

## How to choose your allocation key

No key is universally “best”. The right choice depends on the project, the members and the goals. Here are four questions to ask yourself, valid across all three regions.

### 1. What is the political goal of the sharing?

- **Equality and solidarity** — everyone gets the same share regardless of their consumption: **egalitarian fixed key** (Wallonia), **fixed method 25/25/25/25** (Brussels), **vaste verdeelsleutel** (Flanders).
- **Recognising investment** — members who funded the panels get a larger share: **specific fixed key** (Wallonia), **fixed method with negotiated percentages** (Brussels / Flanders).
- **Maximising self-consumption** — making the most of every locally produced kWh: **dynamic key** (Wallonia), **prorata or hybrid method** (Brussels), **relatieve or optimale verdeelsleutel** (Flanders).

### 2. How diverse are the consumption profiles?

A residential neighbourhood with similar profiles (~3,500 kWh/year each) works very well with an **egalitarian fixed key**. But as soon as a large consumer joins — a school, a municipality, an SME — strict equality stops being optimal: the share allocated to the large consumer goes under-used while their neighbours still pay their surplus at market rate. In that case, switching to a **dynamic / prorata / optimal key** recovers what would otherwise be lost.

### 3. How much financial predictability do members expect?

**Fixed** keys offer immediate clarity: “I'm entitled to X% of the share every quarter-hour”. **Dynamic / optimal** keys offer better overall performance but a variable share from one month to the next. If you communicate to households unfamiliar with energy matters, the predictability of a fixed key eases adoption. If your members are sophisticated (a cooperative, a business park), the dynamic key tends to be the better story.

### 4. How much flexibility to evolve the key?

The **three regions allow modifying** a key after launch. In Wallonia, the amendment to the agreement plus the DSO step takes a few weeks; in Brussels and Flanders, the modification is announced by the single point of contact to the DSO. Avoid keys that are too rigid at launch: plan from the start an annual review at the general assembly.

The key decides **how many kWh** each member receives; it says nothing about **how many euros** they are worth. That second decision — the price applied to the shared energy — is taken separately, in the same agreement: see ["Electricity price in an energy community: how to set the internal transfer price"](/en/news/2026/07/20/energy-community-electricity-price/).

### Four typical practical cases

| Community profile | Wallonia | Brussels | Flanders |
|---|---|---|---|
| Residential neighbourhood + 1 municipal PV roof | Egalitarian fixed key | Fixed method | Vaste verdeelsleutel |
| Cooperative with different contributions | Specific fixed key | Fixed method (investment percentages) | Vaste verdeelsleutel (investment percentages) |
| Residential mix + 1 school / SME consumer | Dynamic key | Prorata or hybrid method | Relatieve verdeelsleutel |
| Surplus production to valorise locally | Dynamic key | Hybrid method | Optimale verdeelsleutel |

## Configuring, monitoring and evolving the key: the role of a dedicated tool

An allocation key is not a one-time decision. It lives with the community: a member joins, another leaves, production grows after a new roof is added, the general assembly revises the percentages, the regulator validates a non-standard key. Every change implies an **amendment to the agreement**, a **transmission to the DSO** and a **historical record** that the community must keep for its annual reporting.

That is precisely what **OptimCE** tools at the core of the application. The **Allocation Keys module** of the open-source core lets you:

- **Configure the key** directly on a sharing operation, consistent with the types recognised in your region (CWaPE in Wallonia, Sibelga in Brussels, Fluvius in Flanders).
- **Track the full history** of keys applied over time — useful for amendments, recomputations in case of dispute, and regulator reporting.
- **Track the acceptance status** of each member for a new key: who signed the amendment, who hasn't validated yet, who declined.

The **automatic generation module** is now live: from the **actual production and consumption data** of the members, it proposes optimised candidate keys — through a **brute force** scan over the regional standard keys and through **LOGAAS**, a genetic-algorithm approach developed by **CeCoTePe** during the **Locomotrice** research project. See our dedicated guide: ["Automatic allocation key generation: how OptimCE finds the optimal key"](/en/news/2026/05/26/automatic-allocation-key-generation/).

> ### Manage your allocation keys with OptimCE
>
> An open-source platform built for Belgian energy communities: configure keys, track the history of sharing operations, monitor member acceptance status and prepare your regulator reporting — all in a single application.
>
> **[Get started on app.optimce.be →](https://app.optimce.be)**

## FAQ — Allocation key

### Can the allocation key be changed after launch?

Yes, in all three regions. You sign an **amendment to the sharing agreement** between the affected members, then forward the new key to the DSO via the **representative** (Wallonia) or the **single point of contact** (Brussels, Flanders). The change takes effect on the date agreed with the network operator, typically a few weeks after the request.

### Is the key calculated yearly, monthly or per quarter-hour?

**Per quarter-hour**, in all three regions. The DSO records producer injections and consumer withdrawals on each 15-minute slot, applies the key, and then aggregates the shared volumes monthly for transmission to the suppliers.

### If production exceeds the members' consumption, what happens to the surplus?

The injected energy not consumed by the community is **re-injected on the grid** and sold back via the producer's supplier at the prevailing buy-back tariff. A **dynamic key** (Wallonia), **hybrid** (Brussels) or **optimal** (Flanders) reduces this surplus by maximising local consumption, but does not eliminate it entirely.

### Can several keys be mixed within the same community?

Within a **single sharing operation**, only one key applies. However, a **single energy community** can host **several sharing operations** (e.g., one intra-building operation + one neighbourhood-scale CER), each with its own key. That's one of the strengths of the Belgian legal model.

### Does the key need to be validated by the regulator?

In **Wallonia**, **standard keys** are accepted automatically by the DSO; **non-standard keys** must be authorised by CWaPE. In **Brussels**, the three methods operated by Sibelga are set by BRUGEL and require no additional authorisation. In **Flanders**, the key is defined within the Fluvius protocol and does not require prior VREG validation.

### Which key is recommended for a small neighbourhood community?

For a dozen households with similar profiles around a shared PV roof, the **egalitarian fixed key** (Wallonia) / **fixed method** (Brussels) / **vaste verdeelsleutel** (Flanders) is very often the right starting point. It is easy to read for members, robust to members joining and leaving, and avoids debates over percentages. An annual review will help decide if you should move to a more dynamic key.

### What happens when a new member joins the community?

The key is **recomputed** to include the new member. With an **egalitarian fixed key**, each member's percentage mechanically drops (10% with 5 members → 9.09% with 11 members). With a **specific fixed key**, percentages must be renegotiated. With a **dynamic / optimal key**, integration is automatic since the distribution follows actual consumption. An amendment to the agreement formalises the addition in every case.

## Key takeaways

Three regulators (CWaPE, BRUGEL, VREG), three reference DSOs (ORES/RESA/AIEG, Sibelga, Fluvius), three vocabularies (“key”, “method”, “verdeelsleutel”) — but a shared mechanic at the quarter-hour, dependent on smart meters, and organised around two big families: the **fixed** keys (egalitarian or weighted) and the **dynamic / optimised** keys (prorata, hybrid, optimal).

Choosing a key is not a technical question: it's a governance choice that should reflect the values and constraints of the members. And because no key is set in stone, you need a tool to configure it, historise it, evolve it cleanly — and now to **generate it automatically from real community data**: that's exactly what **OptimCE** provides.

To go further, see our companion guides:

> **[Automatic allocation key generation: how OptimCE finds the optimal key](/en/news/2026/05/26/automatic-allocation-key-generation/)**
>
> The data-driven follow-up — how brute force and LOGAAS find the best allocation key from a community's real production and consumption data.

> **[Energy communities in Belgium: CER, CEC and CEL explained](/en/news/2026/05/11/energy-communities-belgium/)**
>
> The full panorama of legal forms, European directives and operational mechanics of energy sharing in Belgium.

> **[How to create an energy community in Wallonia: a step-by-step guide](/en/news/2026/05/11/create-energy-community-wallonia/)**
>
> Choosing between CER and CEC, framing the project, notifying CWaPE, the acknowledgement and launching the sharing with ORES, RESA or AIEG — including where the allocation key fits in the file.

> **[How to join an energy community in Wallonia: a practical guide](/en/news/2026/05/11/join-energy-community-wallonia/)**
>
> Where to find an open operation, enrolment steps and points to check before signing the sharing agreement.

## Sources

- [CWaPE — List of standard allocation keys for distributing shared volumes](https://www.cwape.be/publications/document/5382) — proposal CD-23d27-CWaPE-0928 of 27 April 2023.
- [CWaPE — How is shared electricity distributed between participants?](https://www.cwape.be/node/6068) — principle of the distribution and role of the allocation key.
- [CWaPE — Energy sharing](https://www.cwape.be/node/5618) — summary on energy sharing in Wallonia.
- [CWaPE — Energy communities and energy sharing](https://www.cwape.be/secteur/communautes-partage-energie) — Walloon general portal.
- [CWaPE — Distribution of shared volumes: list of standard allocation keys](https://www.cwape.be/documents-recents/repartition-des-volumes-partages-liste-des-cles-de-repartition-standards) — short version of the reference document.
- [CWaPE — Decision approving the proposal of allocation keys between Flanders and Wallonia](https://www.cwape.be/documents-recents/decision-relative-lapprobation-de-la-proposition-de-cles-de-repartition-entre) — cross-border case.
- [ORES — Energy sharing in practice](https://www.ores.be/professionnel/en-pratique) — practical explanation of fixed, specific and dynamic keys.
- [BRUGEL — Energy sharing](https://www.brugel.brussels/themes/energies-renouvelables-11/partage-d-energie-420) — Brussels regulatory framework.
- [Sibelga — Renewable energy sharing in Brussels](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie) — Brussels practical page.
- [Sibelga — Distribution methods for energy sharing](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methodes-de-repartition) — fixed, prorata and hybrid methods.
- [Brussels Environment — Study on the potential, development and functioning of energy communities](https://document.environnement.brussels/opac_css/elecfile/RAP_2024_CommunautesEnergie.pdf) — 2024 in-depth study.
- [VREG — Vlaamse Nutsregulator](https://www.vlaamsenutsregulator.be) — Flemish regulator.
- [Fluvius — Protocol energiedelen, persoon-aan-persoonverkoop](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf) — technical protocol v3.x (July 2024).
- [Renouvelle — Costs and benefits of electricity sharing and energy communities in Brussels](https://www.renouvelle.be/fr/quels-couts-avantages-sur-le-partage-delectricite-et-les-communautes-denergie-a-bruxelles/) — economic analysis.
