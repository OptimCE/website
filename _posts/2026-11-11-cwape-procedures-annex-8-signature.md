---
layout: post
title: "CWaPE procedures and signing annex 8"
date: 2026-11-11 06:00:00 +0100
author: "Eric from OptimCE"
excerpt: "OptimCE's administrative area is now organised into procedures, fed by the changes made in the CRM, and the CWaPE's annex 8 can be signed in the application. OptimCE still sends nothing: you do the sending."
description: "CWaPE procedures arising from the CRM, deadlines, documents and simple electronic signature of annex 8: what OptimCE's new administrative area changes."
tags: [app, announcement, news]
lang: en
ref: admin-procedures-annex-8
permalink: /en/news/2026/11/11/cwape-procedures-annex-8-signature/
faq:
  - q: "Does OptimCE send the procedures to the DSO or to the CWaPE?"
    a: "No. The “Send” window prepares the message and the documents, but you send them yourself, from your email account or from the online form. There is no interface between OptimCE and the DSO or the CWaPE."
  - q: "What is the legal value of the annex 8 signature?"
    a: "It is a simple electronic signature within the meaning of the eIDAS Regulation, neither advanced nor qualified. It cannot be rejected as evidence solely on the grounds that it is electronic, but it does not automatically have the value of a handwritten signature, nor the weight of a qualified signature such as the one itsme provides. OptimCE uses neither eID nor itsme today; itsme integration is planned, with no date announced yet."
  - q: "Who can sign annex 8 for a member?"
    a: "Any OptimCE account linked to the member; the first signature closes the slot. A company's representative, or another linked account, signs for the member, and the PDF, the consent and the evidence say so."
  - q: "What happens to dossiers created before the redesign?"
    a: "They are converted into procedures. When the module is first activated, the manager confirms a starting state, and the history is not replayed."
---

As of 11 November 2026, OptimCE's administrative area is organised into procedures. The CWaPE's annex 8, the sworn declaration of persons taking part in the sharing, can now be signed in the application. One thing does not change: OptimCE sends nothing to the network operator or to the CWaPE. You do the sending.

## From documents to procedures

The 11 CWaPE documents generated from the official files, the retention of transmitted versions, the deadlines and the “What has been filed about me” page already existed: our guide [“Energy community: CWaPE documents and deadlines”](/en/guides/energy-community-administrative-documents-wallonia/) presents them. What changes is the organisation.

A procedure is a form, a recipient (the reference DSO or the CWaPE) and an effective date. The Walloon catalogue has seven types of procedure:

- sharing modification, simple route (DSO only);
- sharing modification, authorisation route (DSO then CWaPE);
- authorisation of a new operation;
- end of sharing;
- notification of the community's creation;
- update of the community's information;
- annual report.

Procedures arise from changes made in the CRM: a meter added to or removed from an operation, a new allocation key, an operation created or deleted, a new representative, new articles of association or new internal rules. The change joins the draft of the right procedure. Several changes feed a single draft, which you send when you decide to. The annual report opens by itself every year from 1<sup>st</sup> June, for the 1<sup>st</sup> September deadline.

When the module is first activated, you confirm a “starting state”: what has already been notified, what remains to be done, what has been sent. The history is not replayed. Former dossiers are converted into procedures.

## The course of a procedure

### Deadlines and reminders

A list of the procedures to be done, sorted by deadline, gives the next action and its date. It includes third-party deadlines: the date by which the DSO or the CWaPE must have replied. Lapse occurs at six months. Time limits are counted in working days, excluding Belgian public holidays.

Reminders appear in the application 14, 7 and 2 days before the deadline, then once it has passed. An email summary, disabled by default, can be added to them: a community administrator enables it and chooses the frequency and the recipients.

### The documents

A generated document first comes out marked “BROUILLON” (draft). “Generate the final versions” produces the unmarked versions, and sending is refused as long as a document supplied is not final. When the CRM cannot fill in a document, generation is refused, with the reason and a link to what needs correcting.

New document: the description of the allocation key, drawn from the operation's latest approved key. For the CWaPE's two community forms, which are filled in online, an “Entry sheet” gives each value to copy.

### Sending, by you

The “Send” window prepares the recipient, the subject, with an [OPT-…] reference to keep in replies, the text and the documents. You send from your own email account or from the online form, then you enter the date and the channel. The procedure is then frozen. Afterwards, you record the replies in the procedure, which keeps the whole thread: acknowledgment of completeness, request for additional information, decision, amendment…

### What the procedure changes in the CRM

Each meter and each key of an operation carries a regulatory status: to be notified, awaiting the DSO or the regulator, authorised, active, left, refused, removed. It is shown as a badge, and a banner on the operation's page gives the number of changes not yet notified. When the module is active, the procedure drives this status.

The effective date falls on the 20<sup>th</sup> working day after the signed amendment, or on the requested date if that is later. On that day, the platform switches incoming meters to “Active”, closes outgoing meters as of the day before and replaces the old key. After a refusal, the procedure offers “Remove from the operation” or “Correct and refile”.

## Signing annex 8

Only one document can be signed in the application: annex 8.

### On the manager's side

The “Request signature” button sits on the document, within the procedure. A pill then shows its status, with “Follow” and “Evidence”. A tracking page, reserved for managers, shows the signatories and the history; from there you can send a reminder, once every 24 hours, or cancel.

### On the participant's side

A notification arrives in the application and by email. The “To sign” menu entry shows a counter. The signing screen shows the exact PDF to be signed: the participant fills in “Signed at” and the date, types or draws their signature, then ticks the consent box. They can also decline, giving a reason.

Any account linked to the member can sign; the first signature closes the slot. A company's representative, or another linked account, signs for the member, and the PDF, the consent and the evidence say so. The signed PDF becomes the final version of the document, which moves to “Signed”. It replaces printing, signing by hand and scanning.

### The technical safeguards

- The PDF is certified by OptimCE; the prefilled values are frozen before signing.
- Each signature is timestamped.
- The final file is in PAdES format, the European standard for PDF signatures.
- A chained evidence log accompanies the request: altering a past event breaks the chain.
- A sealed evidence report contains, among other things, the consent sentence that was ticked, the values entered, the IP address and the browser.

### What the signature is worth

It is a **simple** electronic signature within the meaning of the eIDAS Regulation, neither advanced nor qualified. The cryptographic key is the platform's; the signatory's identity rests on their authentication and on the evidence log. A simple signature cannot be rejected as evidence solely on the grounds that it is electronic, but it does not automatically have the value of a handwritten signature. So it does not carry the weight of a qualified signature, the only category the regulation treats as equivalent to a handwritten signature, and the one that itsme, for example, provides. OptimCE uses neither eID nor itsme today; itsme integration is planned, with no date announced yet.

## What it does not do

- **No sending.** OptimCE sends nothing to the DSO or to the CWaPE.
- **Annex 8 only.** Not the agreements with the DSO, nor amendments, nor membership forms.
- **No detection of production installations.** For a change of installation, the procedure is created by hand.
- **Wallonia only.** Neither Brugel nor the VREG.
- **No proofreading for you.** A form prefilled with wrong data is still wrong.

## Availability and activation

Both new features are available on app.optimce.be as of 11 November 2026. The administrative module is optional and is enabled per community. Signing is a separate module, enabled per community and disabled by default. During the alpha, the platform is free (see [pricing](/en/pricing/)). The [CWaPE procedures](/en/features/cwape-filing/) page presents the module.

> ### Prepare your CWaPE procedures with OptimCE
>
> Your CWaPE procedures in one place, and annex 8 signed in the application. Free during the alpha.
>
> **[Get started on app.optimce.be →](https://app.optimce.be)**

## FAQ

### Does OptimCE send the procedures to the DSO or to the CWaPE?

No. The “Send” window prepares the message and the documents, but you send them yourself, from your email account or from the online form. There is no interface between OptimCE and the DSO or the CWaPE.

### What is the legal value of the annex 8 signature?

It is a simple electronic signature within the meaning of the eIDAS Regulation, neither advanced nor qualified. It cannot be rejected as evidence solely on the grounds that it is electronic, but it does not automatically have the value of a handwritten signature, nor the weight of a qualified signature such as the one itsme provides. OptimCE uses neither eID nor itsme today; itsme integration is planned, with no date announced yet.

### Who can sign annex 8 for a member?

Any OptimCE account linked to the member; the first signature closes the slot. A company's representative, or another linked account, signs for the member, and the PDF, the consent and the evidence say so.

### What happens to dossiers created before the redesign?

They are converted into procedures. When the module is first activated, the manager confirms a starting state, and the history is not replayed.

## Sources

- [CWaPE — Partage d'énergie](https://www.cwape.be/node/5618) (in French) — the electricity sharing form and its “Annexe 8 - Déclaration sur l'honneur des personnes prenant part au partage” (document 5612). Accessed on 11 November 2026.
- [Regulation (EU) No 910/2014 (eIDAS), consolidated version of 18 October 2024](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0910-20241018) — article 3, points 10 to 12: definitions of the electronic signature, the advanced electronic signature and the qualified electronic signature. Article 25: an electronic signature shall not be denied legal effect and admissibility as evidence in legal proceedings solely on the grounds that it is in an electronic form; only a qualified electronic signature has the equivalent legal effect of a handwritten signature. Accessed on 11 November 2026.
- [itsme — Qualified Electronic Signature](https://www.itsme-id.com/business/services/sign) — itsme Sign, presented by its provider as a qualified electronic signature under the eIDAS Regulation, with the same legal value as a handwritten signature. Accessed on 13 November 2026.
