---
layout: page
title: "Spreadsheet or software to run a community?"
breadcrumb_title: "Spreadsheet or software"
subtitle: "An honest comparison: when a spreadsheet is enough to run an energy community, and where it starts to break."
description: "Is Excel enough to run an energy community? When a spreadsheet holds, where it breaks (quarter-hours, keys, invoices, CWaPE) and what software does."
lang: en
ref: product-vs-spreadsheet
permalink: /en/features/spreadsheet-or-software/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Is a spreadsheet enough for a small energy community?"
    a: "Often, yes. With a handful of members, a single sharing operation and a standard key that does not change, a well-kept spreadsheet does the job. It becomes fragile when the key evolves, when invoices multiply or when several people need to work on it."
  - q: "Why do people talk about 35,040 values per meter per year?"
    a: "Because sharing is calculated per quarter-hour: 96 quarter-hours a day, over a 365-day year, make 35,040 values per meter. Days when the clocks change have 92 or 100 quarter-hours, and the yearly total stays the same."
  - q: "Does OptimCE replace the community's accounting?"
    a: "No. OptimCE invoices the shared energy and tracks the payment of those invoices. The community's general accounts still have to be kept separately."
  - q: "How much does OptimCE cost compared with a spreadsheet?"
    a: "OptimCE Cloud is free throughout the alpha phase, and self-hosting is free for good. A paid offer may come later for the hosted version; alpha users will be told well in advance."
---

Most energy communities start on a spreadsheet, and it is often the right choice: it is already
installed, everyone knows how to open it, and a small community needs nothing more. But a
spreadsheet has no memory. It does not know which version of the allocation key applied in March,
which invoice number comes next, or what was filed with the CWaPE and when. This page compares the
two honestly, without trying to make you switch tools sooner than you need to.

## When a spreadsheet is enough

A well-kept spreadsheet does the job as long as the community stays simple:

- a handful of members and a single sharing operation;
- a standard allocation key that does not change from one year to the next;
- few documents to produce: a few invoices per period, a CWaPE dossier already filed;
- one person who keeps the file, and who hands it over properly when they step down.

If your community looks like this, keep your spreadsheet. The day one of these points changes,
the rest of this page is for you.

## How OptimCE handles it

Here are the five places where a spreadsheet starts to break, and what OptimCE does instead.

### Quarter-hourly data

In Belgium, sharing is calculated per quarter-hour: 96 values per day and per meter, or 35,040
over a 365-day year. Stored at one row per meter and per quarter-hour, a year's data for 30
meters comes to 1,051,200 rows: more than the 1,048,576 rows of an Excel worksheet
([Microsoft](https://support.microsoft.com/en-us/excel/excel-specifications-and-limits)).
Well before that limit, the workbook becomes slow to open and to recalculate.

In OptimCE, quarter-hourly readings are imported per operation and per period. Billing, key
generation and key simulation work directly on them.

### Key versions

An allocation key changes every time a member joins or leaves. In a spreadsheet, the March
version overwrites the January one, or lives on in a file called “key_v3_final.xlsx”, and no one
remembers any more whether it was ever accepted.

In OptimCE, every version of the key is recorded and members' acceptance is tracked. The details
are on the [allocation key]({{ "product-allocation-key" | ref_url }}) page.

### Invoice numbering

Invoices are numbered in a continuous sequence, with no gaps, and an issued invoice can no longer
be modified: it is corrected with a credit note. In a spreadsheet, nothing stops you from
overwriting a row, skipping a number or copying a wrong structured payment reference.

In OptimCE, the number and the structured payment reference are assigned on issue, a correction
goes through a credit note, and the history stays complete. See the
[billing software]({{ "product-billing" | ref_url }}) page.

{% include product-shot.html name="billing-member" alt="A member's “My invoices” area: remuneration statement DP-2025-00001, status “Issued”, €36.69, with its structured payment reference, labelled “Structured communication” in the interface." caption="Each member sees their own documents, with the structured payment reference to quote in their transfer (test data)." %}

### CWaPE dossiers

The same data (members, supply points, installations) is copied into several CWaPE forms, and
every change to the community calls for new ones, with deadlines in working days. A spreadsheet
does not know that a dossier has just changed status, or which version of a form went out.

In OptimCE, the official forms are prefilled from the list of members, every version is kept and
deadlines are calculated in working days. See the [CWaPE filing]({{ "product-cwape" | ref_url }})
page.

{% include product-shot.html name="cwape-deadlines" alt="The “Deadlines” tab of “Administrative documents”: a “Completeness check” due on 15/09/2026 for dossier #1, with status “Open”." caption="The open deadlines of every dossier, calculated from the status changes (test data)." %}

### Member access and handover

To show each member their invoice, or what has been declared about them, a spreadsheet forces you
to extract and send one file per person: sharing the whole workbook would expose everyone's data.
And the file depends on the person who keeps it: when they leave, the history often goes with
their mailbox.

In OptimCE, each member sees their own invoices and what has been declared about them, and nothing
else. Several people can manage the community, each with their own role, and the history stays in
the application.

## What it does not do

**OptimCE does not replace your accounting.** It invoices the shared energy and tracks the payment
of those invoices. The community's general accounts still have to be kept separately.

**No real time.** Like your spreadsheet, OptimCE works on the readings sent by the grid operator
and on the files you import: it does not display real-time data.

**It does not fix wrong data.** Software avoids copying errors, not input errors. A wrong address
or EAN stays wrong, whether in a spreadsheet or in OptimCE.

## Frequently asked questions {#faq}

### Is a spreadsheet enough for a small energy community?

Often, yes. With a handful of members, a single sharing operation and a standard key that does not
change, a well-kept spreadsheet does the job. It becomes fragile when the key evolves, when
invoices multiply or when several people need to work on it.

### Why do people talk about 35,040 values per meter per year?

Because sharing is calculated per quarter-hour: 96 quarter-hours a day, over a 365-day year, make
35,040 values per meter. Days when the clocks change have 92 or 100 quarter-hours, and the yearly
total stays the same.

### Does OptimCE replace the community's accounting?

No. OptimCE invoices the shared energy and tracks the payment of those invoices. The community's
general accounts still have to be kept separately.

### How much does OptimCE cost compared with a spreadsheet?

OptimCE Cloud is free throughout the alpha phase, and self-hosting is free for good. A paid offer
may come later for the hosted version; alpha users will be told well in advance.

## Further reading

- [Energy community: CWaPE documents and deadlines]({{ "cwape-administrative-documents" | ref_url }}):
  each form, its deadlines, and where to start when everything is already in spreadsheets.
- [Invoicing shared electricity in Belgium]({{ "invoice-shared-electricity" | ref_url }}):
  who invoices what, VAT and the mandatory invoice details.
- [Allocation key in Belgium: the 3 regions]({{ "allocation-key-belgium" | ref_url }}):
  the standard keys and the rules of each region.

{% include product-cta.html page_key="vs-spreadsheet" guide="getting-started" title="Move from your spreadsheet to OptimCE" %}
