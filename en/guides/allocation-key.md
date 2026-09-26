---
layout: pillar
title: "Allocation key: understand, choose, test"
subtitle: "What each region accepts, how to choose a family of keys, then how to test it on your own data."
description: "Allocation keys for Belgian energy communities: what CWaPE, BRUGEL and VREG accept, choosing a key family, then generating and simulating one."
lang: en
ref: pillar-cle-de-repartition
pillar: cle-de-repartition
permalink: /en/guides/allocation-key/
breadcrumb_parent: guides
last_modified_at: 2026-09-26
sections:
  - title: "Understanding the key and what each region accepts"
    refs: [allocation-key-belgium]
  - title: "Generating and simulating your key with OptimCE"
    refs: [optimce-allocation-key-generator, optimce-allocation-key-simulation]
---
In an energy-sharing operation, the **allocation key** is the calculation rule, expressed as percentages, that attributes to each consumer member a share of the energy injected by the producers. There is nothing physical about it: the distribution system operator (DSO) applies it quarter-hour by quarter-hour to the smart-meter readings. Only one key applies per sharing operation, and it decides only the kWh: what they are worth in euros is a matter for the [internal transfer price]({{ "internal-price-shared-energy" | ref_url }}), set separately in the same agreement.

Belgium has three frameworks, and our [comparison of the three regions]({{ "allocation-key-belgium" | ref_url }}) details what each one allows:

- **Wallonia**: three standard keys published by CWaPE — egalitarian fixed, specific fixed, consumption-based dynamic — which DSOs accept automatically; any other key must be authorised by CWaPE.
- **Brussels**: three methods operated by Sibelga and set by BRUGEL — fixed (single-round or multi-round), prorata, hybrid — which can be changed at any time at the request of the single point of contact.
- **Flanders**: no list of “standard” keys published by VREG; the Fluvius protocol, the authoritative source, supports three *verdeelsleutels*: vaste, relatieve and optimale.

Behind these three vocabularies, the same two families recur everywhere: **fixed** keys, egalitarian or weighted by members' contributions, and **dynamic or optimised** keys, which follow actual consumption. Choosing between them is not a technical question but a governance choice: equality between members, recognition of investment, or maximising collective self-consumption. The diversity of profiles matters too — as soon as a school or an SME joins the group, strict equality stops being optimal — as does the financial predictability members expect. Finally, all three regions allow a key to be modified after launch: it is wise to plan an annual review at the general assembly from the outset.

It remains to test these principles against your own profiles, because the same key can recover 70% of the available production in one community and barely 50% in another. OptimCE offers two features for this, both fed by a CSV of your production and consumption data. [Automatic generation]({{ "optimce-allocation-key-generator" | ref_url }}) proposes a candidate key, either by scanning your region's standard keys (brute force) or with the LOGAAS algorithm, whose non-standard key must, in Wallonia, go through the CWaPE authorisation route. [Simulation]({{ "optimce-allocation-key-simulation" | ref_url }}) replays a key you have chosen and returns its self-consumption, surplus, self-sufficiency and sharing rate, without touching the key applied by the grid operator. Neither one submits a key to the DSO: the amendment, the signatures and the submission stay in your hands.

The guides below follow the same order: first the three regional frameworks, then generating and simulating a key on your data.
