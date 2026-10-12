---
layout: page
title: "Energy community billing software"
breadcrumb_title: "Billing"
subtitle: "From the price per kWh to the payment received: your members' invoices, calculated on the allocation sent by the grid operator."
description: "Bill your energy community's members without a spreadsheet: price per kWh, drafts, continuous numbering, PDFs and payment tracking. Walloon framework."
lang: en
ref: product-billing
permalink: /en/features/billing/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Where does the billing data come from?"
    a: "From the allocation sent by the grid operator: the quarter-hourly shared volumes, which you import for the operation and the period to bill. When the billing run starts, OptimCE freezes a snapshot of these volumes; amounts are calculated on that frozen data, which can be traced back."
  - q: "Can different members be charged different prices?"
    a: "Yes. Each price applies to the whole operation, to a customer segment (residential, professional, industrial) or to a specific supply point (EAN), for a validity period. When several rules target the same member, the most specific one wins: an EAN's price takes precedence over its segment's, which takes precedence over the global price."
  - q: "How do you correct an invoice that has already been issued?"
    a: "An issued invoice has received a number in a continuous sequence: it can no longer be modified or deleted. To correct it, you issue a credit note that cancels it, then invoice again. While a document is still a draft, on the other hand, you can delete or recalculate it."
  - q: "Does OptimCE handle VAT?"
    a: "[À VÉRIFIER : traitement de la TVA par le module de facturation.] The community's VAT regime (whether it is liable, and the rates that apply to each member) is decided with an accountant before the first invoice."
---

Every period, the manager of an energy community turns the shared volumes into one invoice per
member: apply the right price, number without gaps, add a structured payment reference, then check
who has paid. In a spreadsheet, each of these steps is redone by hand, and every mistake is
corrected by hand. OptimCE's billing module takes over this work from the allocation sent by the
grid operator, within the Walloon framework.

## How OptimCE handles it

The module follows the whole cycle, from tariff to payment. Tariffs and invoices are always
attached to a sharing operation: a community that runs several operations bills them separately.

### You set two prices

The community decides its own prices, in €/kWh. The **selling price** applies to the shared energy
consumed by members; the **buyback price** pays for the injection that producers share with the
community.

Each price applies to the whole operation, to a customer segment (residential, professional,
industrial) or to a specific supply point, and carries a validity period. When several rules
target the same member, the most specific one wins. A reduced tariff for a school or a household
therefore does not call for a second operation: a price on its EAN is enough.

{% include product-shot.html name="billing-tariffs" alt="The “Tariffs” tab of the Billing module: a consumer selling price of €0.12/kWh and a producer buyback price of €0.05/kWh, both with global scope and valid from 1 January 2025." caption="The two prices of a sharing operation, as shown in the step-by-step guide (test data)." %}

### You launch a billing run for a period

You choose the operation and the period to bill: a month or a quarter, at the community's own
pace. Billing relies on the quarter-hourly readings that the grid operator sends for the
operation. At launch, OptimCE freezes a snapshot of these volumes: amounts are calculated on
frozen data, which can be traced back if a member asks a question.

The calculation runs in the background. It produces a **draft per member**, downloadable as a PDF
with a “proforma” watermark. A draft can be reviewed, deleted or recalculated freely: nothing is
final until you issue it.

### You issue the documents

On issue, each document receives a number in a continuous sequence, a structured payment reference
and a due date. OptimCE generates three documents as PDFs, each with its own series:

- the **invoice** (F-…), for the shared energy consumed by a member;
- the **credit note** (NC-…), to cancel an invoice that has already been issued;
- the **remuneration statement** (DP-…), for a producer's shared injection.

A member who is both a consumer and a producer receives two separate documents. An issued invoice
can no longer be modified: a mistake is corrected with a credit note, then a new invoice, and the
history stays complete.

### You track payments

Members pay by bank transfer, quoting the structured payment reference. You record each payment
received; the amount is prefilled with the document's total, and partial payments are accepted.
The invoice switches to “paid” once the total is reached, and invoices past their due date show
as overdue.

For their part, members find their own documents in the application, with their number, amount,
status and structured payment reference. Each member sees only their own.

{% include product-shot.html name="billing-member" alt="A member's “My invoices” area: remuneration statement DP-2025-00001, status “Issued”, €36.69, with its structured payment reference, labelled “Structured communication” in the interface." caption="What a member sees: their documents and the structured payment reference to quote in their transfer (test data)." %}

## What it does not do

**Brussels and Flanders: planned, not yet available.** The billing module is currently designed
for Walloon communities, under the supervision of the CWaPE. The Flemish and Brussels frameworks
are planned, but not yet implemented.

**Shared energy only.** The community's invoice values the shared energy at the internal price,
excluding network fees and taxes. The energy that sharing did not cover is still billed by each
member's supplier, at their contract rate.

**No payment collection.** OptimCE debits nothing and receives no payments: members pay by
transfer into the community's account, and you record what has arrived.

**Documents in French.** The PDFs are generated in French, whatever the interface language.

**VAT is decided with an accountant.**
[À VÉRIFIER : traitement de la TVA par le module de facturation.] The community's regime, whether
it is liable for VAT and at which rates depending on the member, is settled before the first
invoice: our guide to invoicing shared electricity sets out the cases.

## Frequently asked questions {#faq}

### Where does the billing data come from?

From the allocation sent by the grid operator: the quarter-hourly shared volumes, which you import
for the operation and the period to bill. When the billing run starts, OptimCE freezes a snapshot
of these volumes; amounts are calculated on that frozen data, which can be traced back.

### Can different members be charged different prices?

Yes. Each price applies to the whole operation, to a customer segment (residential, professional,
industrial) or to a specific supply point (EAN), for a validity period. When several rules target
the same member, the most specific one wins: an EAN's price takes precedence over its segment's,
which takes precedence over the global price.

### How do you correct an invoice that has already been issued?

An issued invoice has received a number in a continuous sequence: it can no longer be modified or
deleted. To correct it, you issue a credit note that cancels it, then invoice again. While a
document is still a draft, on the other hand, you can delete or recalculate it.

### Does OptimCE handle VAT?

[À VÉRIFIER : traitement de la TVA par le module de facturation.] The community's VAT regime
(whether it is liable, and the rates that apply to each member) is decided with an accountant
before the first invoice.

## Further reading

- [Invoicing shared electricity in Belgium]({{ "invoice-shared-electricity" | ref_url }}):
  who invoices what, VAT and the mandatory invoice details.
- [Internal transfer price in an energy community]({{ "internal-price-shared-energy" | ref_url }}):
  how to set a price you can defend before the general meeting.
- [Billing in an energy community]({{ "optimce-billing" | ref_url }}): the module announcement,
  with the details of the documents and their life cycle.

{% include product-cta.html page_key="billing" guide="billing-tarification-pay" title="Bill your community with OptimCE" %}
