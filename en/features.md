---
layout: page
title: "Features of the OptimCE platform"
subtitle: "What the platform does today to run an energy community, from members joining to the invoice."
description: "Members, meters, allocation keys generated and simulated, billing, CWaPE documents, polls: what OptimCE does, open source and free during the alpha."
lang: en
ref: features
permalink: /en/features/
last_modified_at: 2026-09-26
feature_list:
  - "Management of members, supply points and meters"
  - "Versioned allocation keys, with members' acceptance tracked"
  - "Automatic allocation key generation (search over standard keys, LOGAAS)"
  - "Allocation key simulation on your own data"
  - "Billing of shared energy (first version, Walloon framework)"
  - "Pre-filled CWaPE administrative documents and deadline tracking"
  - "Email notifications in four languages"
  - "News board and polls"
  - "Public registry of sharing operations"
  - "Multi-community, event-driven integration, REST API"
---

OptimCE is an open-source platform for managing energy communities. This page describes what it
does **today**, in its alpha version, without announcing anything that has not shipped yet. The
[user guide](https://guide.optimce.be) then walks through every screen.

## Members, meters and communities

- **Member management**: onboarding new members, roles, links between users and communities.
- **Supply points and meters**: members, their supply points, their installations and their meters
  are held in one place. The list of participants, kept once, then feeds the administrative
  documents and billing.
- **Several communities, one instance**: a single OptimCE installation runs several energy
  communities.

## Allocation keys: configure, generate, simulate

The allocation key decides, quarter-hour by quarter-hour, who receives which share of local
generation. OptimCE covers its whole life cycle.

- **Configuration and amendments**: every version of the key is recorded and members' acceptance
  is tracked.
- **Automatic generation**: from a CSV file of quarter-hourly consumption and generation, the
  module proposes a candidate key with the expected collective self-consumption rate. Two
  algorithms are available: an exhaustive search over your region's standard keys, and LOGAAS,
  which comes out of CeCoTePe's research in the Locomotrice project. The proposal never goes to the
  grid operator on its own: it follows the usual amendment workflow.
- **Simulation**: test a key of your choice on your own data and read self-consumption, surplus,
  self-sufficiency rate and sharing rate, overall, per time step and per iteration, without
  touching the key in force.

Further reading: [generate an optimal allocation key]({{ "optimce-allocation-key-generator" | ref_url }})
and [simulate a key on your data]({{ "optimce-allocation-key-simulation" | ref_url }}).

## Billing of shared energy

The first version of the billing module is built for the Walloon framework.

- You set your prices in €/kWh: a selling price for shared energy and a buyback price for
  injection, for the whole community, per customer segment or per supply point, with a validity
  period.
- A billing cycle produces a draft per member from the imported allocation data. Once issued,
  each document receives a number in a continuous sequence and a structured payment reference.
- Three documents are generated as PDF: the invoice, the credit note and the producers'
  remuneration statement.
- Payment tracking is built in, partial payments included, and each member finds their invoices
  in the application.

The details are in [the billing module announcement]({{ "optimce-billing" | ref_url }}).

## Administrative documents and deadlines

For Walloon communities, OptimCE prepares the CWaPE documents from the official, unmodified
files: eleven sets of fillable PDFs, Excel workbooks and Word agreements, pre-filled with the
community's data. Fields the platform cannot derive remain editable.

- Every file and every document goes through statuses recorded in a log: a correction is added,
  it erases nothing.
- Deadlines are calculated in working days on the Belgian calendar and surfaced on the manager's
  dashboard.
- Emails, in French, Dutch, German and English, report invitations, invoices and administrative
  deadlines.
- Each member can see what has been declared about them to the regulator.

OptimCE files nothing and signs nothing on your behalf: filing remains your responsibility. See
[CWaPE documents and deadlines]({{ "cwape-administrative-documents" | ref_url }}).

## Engaging the community

A news board keeps members informed; polls consult them. Three result-visibility modes are
available: anonymous, transparent, or results revealed at closing. An advanced mode sets
separately what the manager and the members see. See
[engaging energy community members]({{ "engage-energy-community" | ref_url }}).

## Public registry of sharing operations

A manager can publish their sharing operation in a public registry built into the application.
Anyone can browse it to find an operation open to new members.

## An open platform

- **Open source**: all the code is published under the Apache 2.0 licence.
- **Self-hosting**: you can install OptimCE on your own infrastructure, free of charge and without
  restriction. The steps are described in [the installation guide]({{ "quick-start-guide" | ref_url }}).
- **OptimCE Cloud**: the hosted version is free throughout the alpha phase. A paid offer may come
  later; alpha users will be told well in advance, and self-hosting will remain free.
- **Integrations**: an event-driven architecture (NATS) lets you plug in third-party tools such as
  an energy management system, and a REST API lets you integrate OptimCE into your own tools.
- **Multilingual**: the interface is available in French, English, Dutch and German.

## What the platform does not do

OptimCE works on the allocation data sent by the grid operator and on the files you import: it
does not display real-time data. It does not file your documents with the CWaPE and does not sign
your agreements. Its billing covers, for now, the Walloon framework only.

<div class="post-cta" markdown="0">
  <h2>Run or create a community with OptimCE</h2>
  <p>The application is free during the alpha. Create your community, invite your members and set
  up your allocation key; the user guide takes you through it screen by screen.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="{{ site.cta.app_url }}">Open the application</a>
    <a class="btn btn-outline" href="https://guide.optimce.be">Read the user guide</a>
    <a class="btn btn-outline" href="https://github.com/{{ site.github_username }}">View the code on GitHub</a>
  </p>
</div>
