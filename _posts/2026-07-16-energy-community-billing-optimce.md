---
layout: post
title: "Energy community billing: OptimCE generates your invoices"
date: 2026-07-16 10:00:00 +0200
author: "OptimCE Team"
excerpt: "New OptimCE feature: automatically generate your energy community's invoices, from the price per kWh to the PDF and payment tracking."
tags: [administrative, app, news]
lang: en
ref: optimce-billing
last_modified_at: 2026-07-23 10:00:00 +0200
permalink: /en/news/2026/07/16/energy-community-billing-optimce/
faq:
  - q: "Where does the billing data come from?"
    a: "From the official settlement data transmitted by the grid operator and already imported into OptimCE: shared energy consumed and shared injection, per EAN and per period. When you launch a billing run, OptimCE freezes a snapshot of those volumes: amounts are computed on frozen, traceable data."
  - q: "Who sets the prices for shared energy?"
    a: "The community itself. You freely define two prices in €/kWh: the selling price of shared energy to consumers and the buyback price paid to producers for their injection. Each price can apply globally, per customer segment (residential, professional, industrial) or to a single EAN, with a validity period — the most specific rule wins."
  - q: "Which documents does OptimCE generate?"
    a: "Three documents, each with its own numbering series: the invoice (F-…) for the shared energy consumed by a member, the credit note (NC-…) to correct an issued invoice, and the remuneration statement (DP-…) for a producer's shared injection. All are generated as PDFs; drafts carry a 'proforma' watermark."
  - q: "What does an energy community invoice cover?"
    a: "Only the shared energy, valued at the community's internal price, excluding network fees and taxes. The residual energy — what sharing did not cover — is still billed by each member's supplier at their contract rate."
  - q: "Can an issued invoice be corrected?"
    a: "Not directly: once issued, an invoice receives a legal number in a gapless sequence and can no longer be modified or deleted. To correct it, you issue a credit note that cancels it, then re-invoice. A draft, on the other hand, can be freely deleted or recomputed."
  - q: "How do members access their invoices?"
    a: "Each member finds their own invoices in the application and downloads the PDF whenever they want. On the manager's side, payment tracking is built in: you record payments — even partial ones —, the invoice automatically switches to 'paid' and overdue invoices are flagged after the due date."
---

A working energy community produces two things: shared kWh… and amounts to invoice. Every period, the official settlement assigns each member their share of the locally produced energy — then someone has to turn those volumes into euros: compute what each consumer owes, what each producer earns, produce compliant documents, collect and track payments. Until now, that work was mostly done by hand, between a spreadsheet and a home-made invoice template. That's over: OptimCE now includes a **billing module**, and its first version is up and running.

The principle is simple: you set your prices, you pick a period, and OptimCE **generates every member's invoice** from the settlement data already in the platform — with PDFs, legal numbering, a structured payment reference and payment tracking.

If the settlement mechanics are still fuzzy for you, start with our reference article ["Allocation key in Belgium: Wallonia, Brussels and Flanders compared"](/en/news/2026/05/19/allocation-key-belgium/) — billing is its direct continuation.

## Why internal billing is the critical link

In energy sharing, the grid operator computes and forwards, but **does not invoice**: it applies the allocation key quarter-hour by quarter-hour and communicates the volumes. Valuing those volumes — the price consumers pay for shared energy, the price producers receive for their injection — is up to the community itself.

In practice, that burden falls on the community manager. For every period, you have to:

- **retrieve the exact volumes** per connection point (EAN);
- **apply the right price** to each profile, without calculation or rounding errors;
- **produce a compliant document**: [VAT, mandatory mentions](/en/news/2026/07/23/who-invoices-shared-electricity-belgium/), sequential numbering;
- **attach a payment reference** and reconcile incoming transfers;
- **answer members' questions** about their statement.

With ten members it's tedious; with fifty, unmanageable. And the stakes go beyond paperwork: clear, regular billing is the first condition of **member trust** — it is what makes the economic benefit of sharing visible, in black and white. We already wrote it in our [guide to creating an energy community in Wallonia](/en/news/2026/05/11/create-energy-community-wallonia/): it is in the operational phase that a management tool becomes essential.

## How it works: from shared volume to invoice

The module is integrated with the rest of the platform and follows a four-step flow.

1. **The data is already there.** Billing relies on the official settlement data already imported into OptimCE: shared energy consumed and shared injection, per EAN and per period. Nothing to re-enter, nothing to export — billing reads the same volumes as your dashboards.
2. **You define your prices.** Two prices, in €/kWh, freely set by the community: the **selling price** of shared energy to consumers and the **buyback price** paid to producers for their injection. Each price can apply globally, per customer segment (residential, professional, industrial) or to a single EAN — the most specific rule wins — and carries a validity period. Deciding which amounts to enter is another matter: our guide ["Electricity price in an energy community: how to set the internal transfer price"](/en/news/2026/07/20/energy-community-electricity-price/) walks through the defensible range and five calculation methods.
3. **You launch a billing run.** You choose the period — monthly, quarterly, whatever suits you — and OptimCE checks that everything is in order before computing: consumption data present, the community's bank details and legal name, an applicable tariff, no duplicates in the data. Then it **freezes a snapshot** of the settlement: amounts are computed on frozen, traceable volumes.
4. **You review, then you issue.** The run produces a **draft per member**, downloadable as a PDF with a "proforma" watermark. You check, then you issue: the invoice then receives its legal number, its structured payment reference and its due date.

In short, here is what you provide and what you get:

| You define | OptimCE generates |
|---|---|
| The selling price for consumers (€/kWh) | One invoice per consuming member |
| The buyback price for producers (€/kWh) | One remuneration statement per producer |
| The period to bill | Net totals, VAT and the amount due |
| | A ready-to-share PDF with IBAN and structured payment reference |

## Three documents, gapless numbering

The module distinguishes three documents, each with its own series:

| Document | Series | Role |
|---|---|---|
| **Invoice** | F-2026-00001 | The shared energy consumed by a member, at the internal price |
| **Credit note** | NC-2026-00001 | The correction of an already issued invoice |
| **Remuneration statement** | DP-2026-00001 | A producer's shared injection, at the buyback price |

Each document details, line by line and EAN by EAN, the kWh multiplied by the unit price, then the net total, the VAT and the amount due. It shows the issuer (the community, as sharing representative), the recipient, the community's IBAN, a Belgian **structured payment reference** to reconcile transfers without ambiguity, the issue date and the due date, plus the legal mentions — including the clarification that the invoice covers shared energy **excluding network fees and taxes**.

A member who both consumes and produces receives two separate documents: their shared-energy invoice and their remuneration statement.

Numbering is **sequential and gapless**, as invoicing rules require: an issued invoice can no longer be modified or deleted. Made a mistake? You issue a **credit note** that cancels it, then re-invoice correctly — the history stays intact and auditable.

## From draft to payment: the lifecycle

Every invoice follows an explicit lifecycle, visible at a glance:

| Status | What it means |
|---|---|
| **Draft** | A computed proposal, editable and deletable — proforma PDF with watermark |
| **Issued** | Legal number assigned, final document, due date set |
| **Sent** | Transmitted to the member |
| **Paid** | Payments recorded up to the full amount |
| **Overdue** | Due date passed without full payment |

Payment tracking is built in: you record each transfer — including **partial payments** — and the invoice automatically switches to "paid" once the full amount is reached. Invoices past their due date are flagged as **overdue**, so you can target reminders without combing through bank statements.

## For members: transparency through the document

Each member finds **their own invoices** in the application and downloads the PDF whenever they want. No more waiting for an email from the manager or asking for a recap: the reference document is available, in the same place, for everyone.

A reminder on scope: the community's invoice covers the **shared energy**, valued at the internal price. The residual energy — what sharing did not cover — is still billed by each member's supplier, at their contract rate. It is the two documents together that tell the story of the savings achieved; our article on [reducing your electricity bill through sharing](/en/news/2026/06/03/energy-community-reduce-electricity-bill/) details that mechanism.

## A first version built for Wallonia — and what's next

This first version is designed for the **Walloon framework** (CWaPE): adapted legal mentions and automatic VAT application on invoices. Documents are generated in French; the rendering pipeline is already multilingual-ready, and more languages will follow.

On the roadmap for the next versions: **automatic email delivery of invoices**, support for the **Flemish and Brussels frameworks**, and richer tariff structures. True to OptimCE's approach: ship early, prove it in the field, iterate with the communities.

The module is available now on [app.optimce.be](https://app.optimce.be) — free, like the whole platform during the alpha phase.

## Conclusion

With billing, OptimCE closes the loop: data import, [choosing and simulating the allocation key](/en/news/2026/06/09/simulate-allocation-key-optimce/), sharing operations, and now the invoices — the last step that still turned every quarter into a spreadsheet chore. Volumes become compliant documents, payments are tracked at a glance, and every member sees clearly what sharing brings them.

> ### Bill your energy community with OptimCE
>
> Open-source platform built for Belgian energy communities: import your settlement data, define your prices, generate invoices and statements as PDFs and track payments — all in a single application.
>
> **[Get started on app.optimce.be →](https://app.optimce.be)**

## FAQ

### Where does the billing data come from?

From the official settlement data transmitted by the grid operator and **already imported into OptimCE**: shared energy consumed and shared injection, per EAN and per period. When you launch a billing run, OptimCE freezes a snapshot of those volumes: amounts are computed on frozen, traceable data.

### Who sets the prices for shared energy?

**The community itself.** You freely define two prices in €/kWh: the selling price of shared energy to consumers and the buyback price paid to producers for their injection. Each price can apply globally, per customer segment (residential, professional, industrial) or to a single EAN, with a validity period — the most specific rule wins.

### Which documents does OptimCE generate?

Three documents, each with its own numbering series: the **invoice** (F-…) for the shared energy consumed by a member, the **credit note** (NC-…) to correct an issued invoice, and the **remuneration statement** (DP-…) for a producer's shared injection. All are generated as PDFs; drafts carry a "proforma" watermark.

### What does an energy community invoice cover?

Only the **shared energy**, valued at the community's internal price, excluding network fees and taxes. The residual energy — what sharing did not cover — is still billed by each member's supplier at their contract rate.

### Can an issued invoice be corrected?

Not directly: once issued, an invoice receives a legal number in a **gapless sequence** and can no longer be modified or deleted. To correct it, you issue a **credit note** that cancels it, then re-invoice. A draft, on the other hand, can be freely deleted or recomputed.

### How do members access their invoices?

Each member finds **their own invoices** in the application and downloads the PDF whenever they want. On the manager's side, payment tracking is built in: you record payments — even partial ones —, the invoice automatically switches to "paid" and overdue invoices are flagged after the due date.

## Sources

- [CWaPE — Energy communities](https://www.cwape.be/node/158) — the Walloon framework for energy communities: types, legal bases, notification and annual reporting.
- [CWaPE — Energy communities and energy sharing](https://www.cwape.be/secteur/communautes-partage-energie) — the general Walloon framework for energy sharing.
- [FPS Finance — VAT](https://finances.belgium.be/fr/entreprises/tva) — invoicing, accounting and VAT obligations for Belgian businesses and legal entities.
- [Pricing and sharing rules for energy communities](https://econpapers.repec.org/article/eeejuipol/v_3a96_3ay_3a2025_3ai_3ac_3as0957178725001109.htm) — research on sharing rules and internal price setting in energy communities.
