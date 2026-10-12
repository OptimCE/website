---
layout: page
title: "CWaPE filing for your energy community"
breadcrumb_title: "CWaPE filing"
subtitle: "The official forms prefilled, plus each dossier's statuses and deadlines, gathered in one place and kept on record."
description: "Prepare your energy community's CWaPE filing: official forms prefilled, every version kept, statuses and deadlines in Belgian working days."
lang: en
ref: product-cwape
permalink: /en/features/cwape-filing/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Does OptimCE file the dossier with the CWaPE?"
    a: "No. OptimCE prepares the documents, but filing remains your responsibility, through your usual channels. You then record in the platform that the dossier was filed, and on what date: that date starts the clock on the deadlines. OptimCE does not sign anything either."
  - q: "Are the forms the CWaPE's official versions?"
    a: "Yes. OptimCE starts from the official, unmodified files: eleven sets of fillable PDFs, Excel workbooks and Word agreements. It prefills them with the community's data; the fields it cannot derive remain editable."
  - q: "How are the deadlines calculated?"
    a: "From the dossier type, the region and the filing date you recorded. Deadlines in working days follow the Belgian calendar. They are surfaced on the manager's dashboard and flagged by email."
  - q: "Can members see what has been declared about them?"
    a: "Yes. Each member has a “What has been filed about me” page: there they see the documents in which they appear and the values transmitted, as they stood on the filing date. These values do not change if their details are corrected afterwards."
---

Creating or changing an energy community in Wallonia means filling in the CWaPE's forms and the
grid operator's agreements, then meeting deadlines counted in working days. The same data passes
from one file to the next (members, supply points, installations), and months later you need to be
able to say what was filed and when. OptimCE prepares these documents from the community's data
and keeps a record of every step.

## How OptimCE handles it

### One dossier per sharing operation

Each dossier concerns a single sharing operation: a community that runs several operations opens
one dossier per operation. Its type, for example a creation notification, determines the
regulatory deadlines that will be calculated later on. You give it a title of your choice and the
reference assigned by the authority, which you can change later.

While the dossier is “in preparation”, it remains editable and no deadline runs. Its page brings
together its documents, its deadlines and the history of its statuses, and offers only the status
changes allowed at that stage. The module is enabled community by community.

{% include product-shot.html name="cwape-dossier" alt="A “Creation notification” dossier with status “In preparation”: sharing operation, file reference CWAPE-2026-0042, region “Wallonia (CWaPE)”, “Submitted” and “Lapsed” buttons, and “Documents”, “Deadlines” and “History” tabs." caption="A dossier's page just after it was created, in the step-by-step guide (test data)." %}

### The official forms, prefilled

OptimCE starts from the CWaPE's official files, **unmodified**: eleven sets of fillable PDFs,
Excel workbooks and Word agreements. It prefills them with the community's data. The list of
members, supply points and meters is kept once, then feeds every document that asks for it.

Before generating a document, you review the data carried over and correct a value if needed, for
that document only. Fields the platform cannot derive remain editable. Each generation adds a new
version, and a saved file is never replaced: you can find what was produced, when and by whom. A
document you already have in hand is attached to the dossier in the same way.

### Statuses and a log that erases nothing

You file the dossier through your usual channels, then record in OptimCE that the filing took
place, on its actual date. The dossier then moves to “submitted”; after that, it can be declared
complete, be corrected, or lapse.

Every status change is recorded in a log. A correction is added after the entry it corrects and
erases nothing: the question “what did we transmit, and when?” always has an answer.

### Deadlines calculated, not typed in

You never enter a deadline by hand. OptimCE calculates it from the dossier type, the region and the
date you recorded, in working days on the Belgian calendar. The “Deadlines” tab brings together
the deadlines of every dossier, and the manager's dashboard surfaces them. Emails, in French,
Dutch, German or English, flag administrative deadlines.

When an obligation has been met, you mark the deadline as met: it leaves the list of open
deadlines, but the dossier's history keeps a record of it.

{% include product-shot.html name="cwape-deadlines" alt="The “Deadlines” tab of “Administrative documents”: a “Completeness check” due on 15/09/2026 for dossier #1, with status “Open”." caption="The table of open deadlines, calculated from the recorded status changes (test data)." %}

### What each member can check

A participant appears by name in the documents sent to the regulator. OptimCE gives them a “What
has been filed about me” page, with the documents in which they appear and the values
transmitted, frozen at the filing date.

## What it does not do

**OptimCE files nothing.** No document goes automatically to the CWaPE or to the grid operator.
Filing remains your responsibility; the platform prepares the document, records the date it was
sent and keeps the exact version that went out.

**OptimCE signs nothing.** Agreements remain contracts that the parties read and sign. A prefilled
document is ready to be signed; it is not signed in the application.

**Brussels and Flanders: planned, not yet available.** The module currently prepares the CWaPE's
documents. Brussels and Flanders require their own documents: support for them is planned, but not
yet implemented.

**It does not check the substance for you.** A form prefilled from wrong data is still wrong.
Re-read what you file, and keep the CWaPE's guides to hand.

## Frequently asked questions {#faq}

### Does OptimCE file the dossier with the CWaPE?

No. OptimCE prepares the documents, but filing remains your responsibility, through your usual
channels. You then record in the platform that the dossier was filed, and on what date: that date
starts the clock on the deadlines. OptimCE does not sign anything either.

### Are the forms the CWaPE's official versions?

Yes. OptimCE starts from the official, unmodified files: eleven sets of fillable PDFs, Excel
workbooks and Word agreements. It prefills them with the community's data; the fields it cannot
derive remain editable.

### How are the deadlines calculated?

From the dossier type, the region and the filing date you recorded. Deadlines in working days
follow the Belgian calendar. They are surfaced on the manager's dashboard and flagged by email.

### Can members see what has been declared about them?

Yes. Each member has a “What has been filed about me” page: there they see the documents in
which they appear and the values transmitted, as they stood on the filing date. These values do
not change if their details are corrected afterwards.

## Further reading

- [Energy community: CWaPE documents and deadlines]({{ "cwape-administrative-documents" | ref_url }}):
  each form, who files it, where and within what deadline.
- [Create an energy community in Wallonia]({{ "create-energy-community-wallonia" | ref_url }}):
  the steps, from the legal form to the notification.

{% include product-cta.html page_key="cwape" guide="admin-doc-dossier-create" title="Prepare your CWaPE filing with OptimCE" %}
