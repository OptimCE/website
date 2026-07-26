---
layout: post
title: "Internal transfer price in an energy community"
date: 2026-07-20 10:00:00 +0200
author: "OptimCE Team"
excerpt: "What price per kWh should apply to the electricity shared between members? What the internal price really covers, the defensible range between injection tariff and energy component, five calculation methods, a costed Belgian case and the rules in Wallonia, Brussels and Flanders."
description: "What the internal price covers, the defensible range between injection tariff and energy component, and five ways to calculate it."
tags: [community, administrative, guide]
lang: en
ref: internal-price-shared-energy
permalink: /en/news/2026/07/20/energy-community-electricity-price/
last_modified_at: 2026-07-25 10:00:00 +0200
faq:
  - q: "Who sets the price of shared electricity in an energy community?"
    a: "In Wallonia and Brussels, the participants themselves. CWaPE writes that the price of shared electricity is freely determined between the participants in the sharing arrangement, in the agreement setting out their rights and obligations. No Belgian regulator publishes a cap or a calculation method. In Flanders, the question does not arise in the same way: sharing within an energy community must be free of charge."
  - q: "Does the internal price replace my electricity bill?"
    a: "No. It replaces only the energy component, around 38% of a Belgian residential bill according to CREG's June 2026 dashboard. Grid fees, excise duties, regional levies and VAT remain due on the shared kWh, and the energy that sharing does not cover is still billed by your usual supplier."
  - q: "Between which values is an internal transfer price defensible?"
    a: "Between the injection tariff the producer would get elsewhere — 0.94 to 4.90 c€/kWh according to the contracts surveyed by Test-Achats in May 2026 — and the energy component the consumer pays their supplier, in the order of 14 c€/kWh. Below the floor the producer loses by sharing; above the ceiling the consumer loses by consuming locally."
  - q: "Can electricity be shared free of charge?"
    a: "Yes in Wallonia and Brussels, where the price is a contractual parameter that may be set to zero. In Flanders it is even mandatory within an energy community: the Vlaamse Nutsregulator states that energy may only be shared there without consideration, selling going through other arrangements."
  - q: "Do you need a supply licence to sell shared energy to your members?"
    a: "No, within the perimeter of the sharing arrangement. In Wallonia, the SPW specifies that shared electricity is not a supply operation. In Brussels, the ordinance says explicitly that the community is not subject to the obligations imposed on suppliers for the electricity shared within it. The exemption stops at the perimeter of the participants: selling beyond it falls under the licensing regime."
  - q: "Which VAT rate applies to shared electricity?"
    a: "6% for residential members and 21% for business members: a community with mixed membership therefore invoices at two rates. Below €25,000 in annual turnover excluding VAT, the small business exemption scheme may apply. Check your situation with the FPS Finance or your accountant."
  - q: "How often should the price be reviewed?"
    a: "At least once a year, at the general meeting — that is what the Brussels community Énergie Solidaire du Balai does. A price frozen while the market moves always ends up penalising someone: the producers when prices rise, the consumers when they collapse."
---

A solar panel owner today sells their surplus for between **0.94 and 4.90 c€/kWh**, depending on their contract ([Test-Achats](https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee), May 2026). On the same day, their neighbour buys electricity at **36.94 c€/kWh**, all in ([CREG](https://www.creg.be/fr/professionnels/fonctionnement-et-monitoring-du-marche/tableau-de-bord), June 2026). Between those two numbers there is a factor of eleven — and that is exactly the space an energy community occupies.

Which leaves the question every project lead ends up asking, often too late: **what price do you write into the agreement?** No Belgian regulator publishes an answer. Neither CWaPE, nor BRUGEL, nor the Vlaamse Nutsregulator issues a calculation method or a reference tariff. This article fills that gap: what the internal price really covers, the bounds it has to fall between, five methods for building it, a fully costed Belgian case, and what each regional framework allows.

If the mechanics of sharing are still unfamiliar, start with our reference article [“Allocation key in Belgium: the 3 regions”](/en/news/2026/05/19/allocation-key-belgium/): the allocation key decides *how many kWh* each member receives, the price decides *how many euros*.

## The internal transfer price replaces only a third of the bill

This is mistake number one, and it poisons general meetings: believing that an internal price of 14 c€/kWh means members will pay 14 c€/kWh. They will not.

A Belgian electricity bill breaks down into four blocks. Here is their real weight, according to CREG's monthly dashboard for **June 2026** (typical residential profile, 3,500 kWh/year, single-rate meter):

| Component | Belgium | Flanders | Brussels | Wallonia |
|---|---|---|---|---|
| **Energy** (the commodity) | 38.5% | 39.3% | 39.7% | 37.2% |
| Grid (transmission + distribution) | 29.7% | 28.7% | 24.6% | 32.7% |
| Taxes, excise duties and levies | 26.1% | 26.4% | 30.1% | 24.5% |
| VAT | 5.7% | 5.7% | 5.7% | 5.7% |
| **Total price** | **36.94 c€/kWh** | 35.31 | 39.04 | 38.64 |

The internal transfer price competes with the **first line only**: roughly **14 c€/kWh** in absolute terms. Everything else keeps running on the shared kWh, because those kWh do travel across the public grid. CWaPE puts it without ambiguity: since the electricity transits the grid, all grid fees (transmission and distribution), together with the related taxes and levies, are due on shared electricity ([CWaPE](https://www.cwape.be/node/6062)).

Two practical consequences:

- **Always present the saving on the energy component, never on the bill.** Halving the price of energy does not halve the bill: it takes about 19% off it.
- **The weight of grid fees varies sharply from one region to another** — 32.7% in Wallonia against 24.6% in Brussels. The same internal price therefore does not produce the same felt effect everywhere.

### What the representative invoices on top of the price

On the community's own invoice, the agreed price is joined by "VAT, excise duties and the public service obligation to surrender green certificate quotas" ([CWaPE](https://www.cwape.be/node/6063)). Who issues this invoice, and which mentions it must carry, is the subject of our guide [“Invoicing shared electricity in Belgium”](/en/news/2026/07/23/who-invoices-shared-electricity-belgium/). Two details that trip up a lot of projects:

- **VAT is not uniform.** The reduced **6% rate applies to electricity supplied to a residential customer**, against **21% for a business customer**: a community with mixed membership should therefore expect to invoice at two rates. Below €25,000 in annual turnover excluding VAT, the [small business exemption scheme](https://finances.belgium.be/fr/entreprises/tva/assujettissement-tva/regime-franchise-taxe) may apply. No circular deals specifically with energy sharing: have your situation validated by your accountant before the first invoice.
- **The federal levy no longer exists.** It was abolished on 31 December 2021 and absorbed into the special excise duty ([CREG](https://www.creg.be/fr/a-z-index/cotisation-federale)). Plenty of documents still in circulation mention it: leave it out of your simulations.

## Grid fees almost never go down

The idea that an energy community enjoys reduced network charges is widespread. It is above all **wrong in the most common case**. We also take apart, block by block, [why a Belgian electricity bill stays high despite falling prices](/en/news/2026/07/25/why-electricity-bill-still-high-belgium/) — network costs, taxes and supplier margin included. Region by region:

| Region | Reduction in network charges on shared kWh |
|---|---|
| **Wallonia** | 80% on the proportional terms, **within a single building only**. For an energy community: no reduction at all. CWaPE says so in black and white — there is "no tariff reduction for sharing within an energy community". |
| **Brussels** | The only genuinely preferential regime. Depending on how close participants are: type A (same building) → proportional tariffs **cut to €0**; type B (same LV substation) → **halved**; types C and D → unchanged. Confirmed until at least 2027 by BRUGEL's 2025-2029 tariff methodology. |
| **Flanders** | None. "Energiedelen … hebben enkel een effect op de energiecomponent van de elektriciteitsfactuur, maar niet op de netkosten, heffingen en taksen" — energy sharing affects only the energy component of the electricity bill, not grid costs, levies or taxes (Fluvius). The capacity tariff, based on the peak measured at the meter, is not eased either. |

Add to that an item almost nobody anticipates: **your supplier may charge fees for your participation in sharing**. CWaPE confirms that nothing prohibits it ([CWaPE](https://www.cwape.be/node/6060)), and the amounts observed range from zero to around €150 per year per supply point. On a small volume of shared energy, those fees simply wipe out the gain — the single biggest silent killer of a project's economics.

## Who is allowed to set a price? The three regions do not answer the same way

This is the point most guides pass over in silence, and it is decisive: **in Flanders, the price question does not arise**, because selling inside an energy community is not permitted there.

| | Wallonia | Brussels | Flanders |
|---|---|---|---|
| **Price within a community** | Free | Free | **Prohibited — sharing must be free of charge** |
| What the framework says | "The price of shared electricity is freely determined between the participants in the sharing arrangement" (CWaPE) | No cap and no reference price in the ordinance; obligation to apply "fair, transparent and non-discriminatory" rules | "In een energiegemeenschap kan je enkel energie delen. Energie verkopen in een energiegemeenschap is niet mogelijk" — in an energy community you can only share energy; selling it is not possible (Vlaamse Nutsregulator) |
| Official model agreement | None for the agreement between participants | Yes, published by Brussels Environment | Model published for peer-to-peer selling |
| Supply licence | Not required: "shared electricity is not considered a supply operation" (SPW Energy) | No: the community "is not subject to the obligations imposed on suppliers for the electricity shared within it" | Not applicable to sharing; selling within a building is expressly exempt |

### Wallonia: complete freedom, and a blank page

The price is free, and the agreement between participants must contain "the allocation key and the cost of shared electricity" — but **no model template exists** ([CWaPE](https://www.cwape.be/node/6064)). You start from a blank page. Also worth noting: Walloon peer-to-peer is **not yet operational**, for want of an implementing decree ([CWaPE](https://www.cwape.be/node/6080)). The only routes for applying a price are therefore sharing within a single building and sharing within an authorised community.

### Brussels: the form is regulated, the amount is free

The Brussels ordinance contains **neither the word "price" nor the word "reasonable"** in its chapter on energy communities. What it does impose is a procedural framework: the agreement must set "fair, transparent and non-discriminatory sharing rules", be drafted "in clear and comprehensible language" and not "create discrimination between participants". The level of the price itself remains entirely a matter of negotiation — the official model agreement even includes a field to complete: *"The selling price of shared electricity is set at ….. c€/kWh excluding VAT"*.

Help with the numbers comes not from the regulator but from **Brussels Environment**, which provides an economic simulation tool and a free facilitator.

### Flanders: free of charge by definition

*Energiedelen* is defined in the Flemish Energy Decree as the **"kosteloos"** — free of charge — allocation of self-generated energy. The regulator is categorical: within an energy community you may only share, not sell. A price is still possible, but through other doors: **person-to-person selling** (*persoon-aan-persoonverkoop*), where "je bepaalt zelf de prijs" — you set the price yourself — and selling within a building through the owners' association. Watch out for the trap: multiple peer-to-peer selling runs from *several sellers to a single buyer* — so it does not allow a community to invoice all of its members.

**In plain terms: a Flemish project that wants to pay its producers has to choose a legal structure other than the energy community.** Better to discover that before incorporation than in front of the regulator.

## The range: producer floor, consumer ceiling

The whole price discussion comes down to one simple line of reasoning: **each side has an alternative, and the price has to beat that alternative for both of them.**

- **The floor is what the producer would get without the community**: their injection tariff. There is no regulated injection tariff in Belgium — it is a commercial price. May 2026 survey: **0.94 to 4.90 c€/kWh** in Flanders and Wallonia, 1.40 to 4.81 c€/kWh in Brussels ([Test-Achats](https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee)). And that floor can turn negative: nearly **29,000 Flemish prosumers** faced a negative buyback tariff for at least one month in 2025 — they had to *pay* to inject.
- **The ceiling is what the consumer already pays** for the energy component alone of their contract: in the order of **14 c€/kWh**.

Between 3 and 14 c€/kWh, everyone wins. Below that, the producer is better off leaving the community. Above it, so is the consumer. **The internal transfer price is therefore not a moral question: it is a division of surplus, and the only real question is in what proportions.**

One detail that reinforces the argument, and that rarely gets quoted: on the Belgian wholesale market in May 2026, the **peak-hours price (69.78 €/MWh) fell below the off-peak price (103.03 €/MWh)** ([BELIX](https://www.elexys.be/en/insights/belix-average-day-ahead-spot-be)). Midday solar electricity is worth less and less on the market — and more and more to whoever consumes it locally at the same moment. The gap between floor and ceiling is not closing: it is widening.

## Five methods for building the price

None of them is "the right one". They answer different priorities.

### 1. A fixed price voted at the general meeting

One number, one vote, one review date. By far the most common, and it is what the Brussels community Énergie Solidaire du Balai does, whose price "is reviewed every year at the general meeting".

*For whom:* every community starting out. *Risk:* the price drifts away from the market if the review is forgotten.

### 2. Splitting the difference

You explicitly compute the floor and the ceiling, then settle in the middle — or at 40/60 if you want to favour the producer who made the investment. With an injection tariff of 3 c€ and an energy component of 14 c€, the midpoint lands at **8.5 c€/kWh**: the producer triples the value of their energy, the consumer saves 40% on their energy component.

*For whom:* communities that want to be able to **justify** their price to an unhappy member. *Strength:* it is the only method that produces a costed, symmetrical and verifiable argument.

### 3. The cost price of the installation

You divide the investment plus operating costs by the kWh produced over the asset's lifetime. The price becomes a payback target rather than a market trade-off.

*For whom:* communities that own their installation. *Risk:* a solar cost price is very low, which gives a low producer price — to be combined with an explicit margin (see below).

### 4. A percentage discount on the supplier tariff

The price follows the supplier's energy component, minus X%. It stays automatically in line with the market.

*For whom:* communities whose members constantly compare with their own contract. *Careful:* the discount must apply to the **energy component**, not to the all-in price, or you promise a saving you cannot deliver.

### 5. Indexation on a market index

The price follows a published index — the monthly average of the Belgian day-ahead market, for instance. Economically the fairest, and the hardest to explain at a general meeting.

*For whom:* communities with a business membership, used to indexed contracts. *Risk:* you reimport into the community the volatility members joined to escape. And price stability is often the feature they value most, ahead of the saving itself.

| Method | Effort | Stability for the member | Ease of justification |
|---|---|---|---|
| Fixed price voted at the general meeting | Low | Very high | Moderate |
| Splitting the difference | Medium | High | Very good |
| Cost price | Medium | High | Good |
| Percentage discount | Low | Medium | Good |
| Indexation | High | Low | Very good |

## A fully costed Belgian case

The Brussels community **Énergie Solidaire du Balai** publishes its tariffs — a rarity. Here is its 2024 structure, as documented in Brussels Environment's [Sustainable Building Guide](https://guidebatimentdurable.brussels/partage-delectricite-sein-dune-communaute-denergie-energie-solidaire-balai/partage-delectricite):

| Item | Amount |
|---|---|
| Price paid to the producer | **6 c€/kWh** |
| Margin kept by the community | **8 c€/kWh** |
| **Price of local energy invoiced to the consumer** | **14 c€/kWh** |
| + grid fees | 9.575 c€/kWh excl. VAT |
| + federal taxes | 4.94 c€/kWh excl. VAT |
| **Total paid by the consumer** | **≈ 32 c€/kWh incl. VAT** |

Three lessons, one of which the source owns with a candour you wish you saw more often:

1. **The producer price (6 c€) sits well above the injection tariff** (1 to 5 c€): sharing remains more attractive than injecting. The same order of magnitude shows up at [Renouvelle](https://www.renouvelle.be/fr/exemples-calculs-de-rentabilite-economique-dun-partage-delectricite-en-wallonie/), which documents an internal sharing price of 6 c€/kWh and a community injection contract at 3 c€/kWh guaranteed for ten years.
2. **The 8 c€/kWh margin is not profit**: it funds the running of the community — administration, billing, insurance, tools.
3. **Members, the source writes, "do not make big savings".** They pay a stable price, slightly below the market, and join first and foremost for the project. Promising anything else is preparing for departures.

## The mistakes that break a community

- **Forgetting the operating margin.** A price set to the cent on the cost of production leaves nothing for the accounting, the insurance or the platform. The community lives a year, then calls for emergency contributions.
- **Freezing the price with no review date.** Belgian wholesale prices swung between 78.94 and 112.13 €/MWh in the first half of 2026 alone. A price set "once and for all" ends up penalising someone.
- **Presenting a saving on the bill instead of on the energy component.** The member does the maths, cannot make the numbers add up, and trust collapses.
- **Ignoring the supplier's extra fees.** Up to €150/year per supply point: on 500 shared kWh, that exceeds the gain.
- **Forgetting that the prosumer loses annual netting** by taking part in sharing ([CWaPE](https://www.cwape.be/node/6075)), and that the social tariff does not apply to shared volumes. Both effects belong in the simulation, not in an after-the-fact discovery.
- **Treating the producer-consumer member as a single case.** They receive two distinct flows: remuneration for their shared injection, and an invoice for the shared energy they consume. Two prices, two documents.

## Keeping the price alive: review, transparency, traceability

An internal transfer price is not a decision, it is a process. Three habits are enough:

- **An annual review on the general meeting's agenda**, with a benchmark presented every time: the current injection tariff, the average energy component, the result of the past financial year.
- **A written rule rather than a number.** "The producer price is set at twice the average injection tariff observed, capped at half the energy component" defends itself better than a "6 c€" with no story behind it — and it updates itself.
- **A history kept.** When a member disputes an invoice from last year, you have to be able to show which price applied on that date, and by decision of which meeting.

This transparency requirement is not cosmetic: in Brussels it is explicitly in the text — the rules must be "fair, transparent and non-discriminatory" and drafted "in clear and comprehensible language". Nothing, on the other hand, requires an **identical** price for everyone: the constraint bears on the *rules*, not on uniformity of amounts. Differentiation between objective categories — investor members, households, businesses — remains defensible if it is written down, justified and applied consistently. If in doubt about a differentiated tariff structure, have it validated by the regional facilitator before putting it into practice.

## Applying your price in OptimCE

Once the price is decided, it has to land on invoices. That is exactly what [OptimCE's billing module](/en/news/2026/07/16/energy-community-billing-optimce/) does, available since July 2026.

You define **two prices in €/kWh**, independent of each other — the selling price of shared energy to consumers and the buyback price of injection paid to producers. Each can apply globally, per customer segment (residential, professional, industrial) or to a specific supply point, with a **validity period**: the most specific rule wins, and a global price is always required as a safety net. Prices are stored to six decimal places, so that rounding only happens at the level of the amount due.

That covers the two needs described above: **differentiation by objective category** and the **history of revisions**. Changing a price replaces nothing: you add a new rule from a given date, and the old one stays consultable — exactly what you need the day a member disputes an invoice from the previous financial year.

From there, OptimCE takes the official settlement volumes already imported, applies the right price to each profile and generates the invoices, credit notes and remuneration statements as PDFs, with legal numbering, a structured payment reference and payment tracking. The price you negotiated at the general meeting becomes an enforceable document, with no spreadsheet in between.

## Conclusion

Setting the price of shared electricity is neither a technical question nor a moral one: it is a **division of surplus between two parties who each have an alternative**. The producer can inject at 3 c€/kWh, the consumer can buy their energy component at 14 c€/kWh. Any price between the two creates value; the only decision left is how to split it — and that belongs to the general meeting, not to the regulator.

What remains is to check that your region allows what you have in mind: complete freedom in Wallonia and Brussels, mandatory free-of-charge sharing within Flemish communities. Then to write the rule, plan its review, and apply it without a rounding error on every invoice.

> ### Invoice shared energy at the right price with OptimCE
>
> Open-source platform for Belgian energy communities: define your selling and buyback prices, per segment or per supply point, with a validity period — and generate invoices and statements as PDFs from your official settlement data.
>
> **[Get started on app.optimce.be →](https://app.optimce.be)**

## FAQ

### Who sets the price of shared electricity in an energy community?

In **Wallonia and Brussels, the participants themselves**. CWaPE writes that the price of shared electricity is freely determined between the participants in the sharing arrangement, in the agreement setting out their rights and obligations. No Belgian regulator publishes a cap or a calculation method. In **Flanders**, the question does not arise in the same way: sharing within an energy community must be free of charge.

### Does the internal price replace my electricity bill?

No. It replaces only the **energy component**, around 38% of a Belgian residential bill according to CREG's June 2026 dashboard. Grid fees, excise duties, regional levies and VAT remain due on the shared kWh, and the energy that sharing does not cover is still billed by your usual supplier.

### Between which values is an internal transfer price defensible?

Between the **injection tariff** the producer would get elsewhere — 0.94 to 4.90 c€/kWh according to the contracts surveyed by Test-Achats in May 2026 — and the **energy component** the consumer pays their supplier, in the order of 14 c€/kWh. Below the floor the producer loses by sharing; above the ceiling the consumer loses by consuming locally.

### Can electricity be shared free of charge?

Yes in Wallonia and Brussels, where the price is a contractual parameter that may be set to zero. In **Flanders it is even mandatory** within an energy community: the Vlaamse Nutsregulator states that energy may only be shared there without consideration, selling going through other arrangements.

### Do you need a supply licence to sell shared energy to your members?

No, **within the perimeter of the sharing arrangement**. In Wallonia, the SPW specifies that shared electricity is not a supply operation. In Brussels, the ordinance says explicitly that the community "is not subject to the obligations imposed on suppliers for the electricity shared within it". The exemption stops at the perimeter of the participants: selling beyond it falls under the licensing regime.

### Which VAT rate applies to shared electricity?

**6% for residential members and 21% for business members**: a community with mixed membership therefore invoices at two rates. Below €25,000 in annual turnover excluding VAT, the small business exemption scheme may apply. Check your situation with the FPS Finance or your accountant.

### How often should the price be reviewed?

**At least once a year, at the general meeting** — that is what the Brussels community Énergie Solidaire du Balai does. A price frozen while the market moves always ends up penalising someone: the producers when prices rise, the consumers when they collapse.

## Sources

- [CREG — Monthly electricity and natural gas dashboard](https://www.creg.be/fr/professionnels/fonctionnement-et-monitoring-du-marche/tableau-de-bord) — all-in prices and breakdown by component, per region (June 2026 edition).
- [CREG — How is the energy price made up?](https://www.creg.be/fr/consommateurs/le-marche-de-lenergie/comment-est-compose-le-prix-de-lenergie) — structure of the bill and applicable VAT rates.
- [CREG — Federal levy](https://www.creg.be/fr/a-z-index/cotisation-federale) — abolished on 31 December 2021.
- [CWaPE — What does shared electricity cost?](https://www.cwape.be/node/6063) — freedom to set the price and items invoiced on top.
- [CWaPE — Grid fees on shared electricity](https://www.cwape.be/node/6062) — tariffs due, 80% reduction limited to sharing within a building.
- [CWaPE — Sharing agreements](https://www.cwape.be/node/6064) — minimum content, absence of a model template between participants.
- [SPW Energy — Energy communities and energy sharing](https://energie.wallonie.be/home/les-marches-et-les-acteurs/communautes-d-energie/communautes-d-energie-et-partage-d-energie-au-sein-d-un-meme-batiment-electricite.html) — sharing is not a supply operation.
- [BRUGEL — Energy sharing: grid tariffs](https://energysharing.brugel.brussels/energysharing/tarifs-de-reseau-409) — types A to D and the reductions applicable to local volumes.
- [Vlaamse Nutsregulator — Energiedelen en energie verkopen](https://www.vlaamsenutsregulator.be/elektriciteit-en-aardgas/energieprijzen-en-facturen/energiedelen-en-energie-verkopen) — free-of-charge sharing within a community and price freedom in peer-to-peer selling.
- [Brussels Environment — Electricity sharing: Énergie Solidaire du Balai](https://guidebatimentdurable.brussels/partage-delectricite-sein-dune-communaute-denergie-energie-solidaire-balai/partage-delectricite) — full price structure of a Brussels community (2024 tariffs).
- [Renouvelle — Worked examples of the economic viability of electricity sharing in Wallonia](https://www.renouvelle.be/fr/exemples-calculs-de-rentabilite-economique-dun-partage-delectricite-en-wallonie/) — internal prices in practice and the impact of supplier fees.
- [Test-Achats — The cost of solar electricity injected into the grid](https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee) — range of injection tariffs in Belgium, May 2026.
- [Elexys — BELIX, monthly average of the Belgian day-ahead market](https://www.elexys.be/en/insights/belix-average-day-ahead-spot-be) — baseload, peak and off-peak wholesale prices.
- [FPS Finance — VAT exemption scheme](https://finances.belgium.be/fr/entreprises/tva/assujettissement-tva/regime-franchise-taxe) — the €25,000 threshold for small businesses.
