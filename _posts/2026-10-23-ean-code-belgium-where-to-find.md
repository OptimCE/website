---
layout: post
title: "Belgian EAN code: where to find it, what it's for"
date: 2026-10-23 06:00:00 +0200
author: "Eric from OptimCE"
excerpt: "Eighteen digits starting with 54, printed on every bill since 2022, instalment invoices included. The EAN code identifies neither your meter nor your contract but the point where electricity enters your home, which is why you are asked for it to switch supplier, move house, declare solar panels or join an energy community. Where to find it when the bill is missing, how many codes you really have, and why ORES treats it as confidential."
description: "Your electricity EAN code identifies your supply point, not your meter. Where to find it, when to give it, who can retrieve it, and who should not get it."
tags: [guide]
lang: en
ref: ean-code-belgium
pillar: facture-electricite
permalink: /en/guides/ean-code-belgium-where-to-find/
faq:
  - q: "Where can I find my electricity EAN code?"
    a: "First on any recent energy bill: since 1 January 2022, the royal decree of 9 December 2021 requires suppliers to print the unique identification code of your supply point on the annual and closing statement, and also on the plain instalment invoice. If you have no bill to hand, look in your supplier's customer area, in your grid operator's portal (myORES, MyRESA), on the operator's meter-reading letter or visit notice, or on the energy takeover form signed when you moved in. As a last resort, ask the grid operator: it finds the code from your exact address and your meter number, which you read on the meter itself. ORES sends it by text message, AIEG and REW by e-mail. OptimCE's “Find your DSO” tool tells you, from your postcode, which operator to contact."
  - q: "Does the EAN code change when I move house or get a new meter?"
    a: "No, in both cases. The EAN code belongs to the home, not to the occupant: when you move, you leave yours behind and take over the one at your new address. When the grid operator replaces the meter, the device gets a new meter number but the EAN code stays the same, as AIEG and Sibelga both state. It does not change when you switch supplier either. Two exceptions are documented in Wallonia. When AIESH took over ORES's network in Couvin on 1 January 2024, residents received a new code specific to AIESH while keeping their supply contract. And ORES replaces the meter and creates a new code for supply points that have remained blocked in the market systems since November 2021. When moving into a flat, check the code you are given: the Walloon regulator CWaPE finds that the code passed on by a landlord or building manager is often the neighbour's."
  - q: "Does gas have a different EAN code from electricity?"
    a: "Yes. There is one EAN code per energy: a home connected to both electricity and gas has two 18-digit codes, both starting with 54. ORES says so in its technical fact sheets, CWaPE in its mediation reports, and the energy takeover form used when moving house has a box for each. The two look similar enough to be confused: CWaPE warns against mixing up the electricity code and the gas code on its GreenCheck page. So check which one you pass on, especially for a form that concerns electricity only, such as a solar panel declaration or joining an energy community. In Wallonia only ORES and RESA distribute gas, so one of those two will retrieve your gas code if you have lost it."
  - q: "Why does my EAN code start with 54?"
    a: "Because the EAN code of a supply point is an identifier from the international GS1 system, where prefixes 540 to 549 are managed by GS1 Belgium & Luxembourg. The Walloon technical regulation calls it an “EAN-GSRN” code identifying an access point. Every Belgian code therefore has 18 digits and starts with 54, and the following digits depend on the organisation that created the code: 5414489 for every Brussels supply point according to the Brussels regulator Brugel, 5414557 at REW in Wavre, 5414 at AIEG. The prefix does not reliably tell you who runs your network today, though: AIEG mentions codes starting with 541449 in Gesves, like the example published by ORES. To find your current operator, start from your municipality, not from your code."
  - q: "Can someone switch my supplier with just my EAN code?"
    a: "The risk exists, and ORES says so: with your EAN code, an ill-intentioned person could change your energy contract. That is why the grid operator treats it as confidential, to be given only to the occupant or the owner. In practice, the federal Energy Ombudsman attributes most unjustified takeovers to mistakes: it received 852 reports of them in 2023, usually caused by an error in recording the EAN code. One published case also shows a door-to-door seller who had used another customer's codes. Since 1 January 2024, a doorstep seller may only leave a no-obligation offer, which you can confirm after three days at the earliest, and any energy contract can be cancelled free of charge within 14 days. Give your code to the supplier you have chosen, not to a canvasser. If a takeover you did not ask for happens, write to the supplier concerned, then refer the matter to the Energy Ombudsman."
  - q: "Do I need my EAN code to join an energy community in Wallonia?"
    a: "Yes: it is what identifies you in the sharing scheme. The community's manager enters your offtake EAN code, your meter number, your grid operator and your address in Annex 6 of CWaPE's energy-sharing form. You sign the sworn statement as the holder of the access point, that is, the person who signed the contract with the supplier, and you copy your offtake code onto it and, if you have one, your injection code. The grid operator then checks, code by code, that the smart meter's communication function is active and that net metering (compensation) has been given up. One rule follows from this: the Walloon decree provides that an access point may take part in only one energy-sharing activity. You therefore cannot combine sharing within your building and an energy community with the same code."
---

Your electricity EAN code is an 18-digit number that starts with 54. It identifies neither your meter, nor your contract, nor you: it identifies the **access point to the grid**, the place where electricity enters your home. Since 1 January 2022, a royal decree has required suppliers to print it on their bills, instalment invoices included.

Sooner or later you will be asked for it: to switch supplier, move house, declare solar panels, join an energy community. And that is usually the day it cannot be found.

This article does not repeat what is already on this site. [“Read your Belgian electricity bill line by line”](/en/guides/read-electricity-bill-belgium/) shows where the code sits on the bill; [“Join an energy community in Wallonia”](/en/guides/join-energy-community-wallonia/) walks through the joining process; [“Energy community: CWaPE documents and deadlines”](/en/guides/energy-community-administrative-documents-wallonia/) lists the forms in which the codes are entered; [“Which electricity tariff to choose in Belgium?”](/en/guides/choose-electricity-tariff-belgium/) compares the options before a contract change.

**The question here is a practical one: what exactly does this code designate, where can you find it, how many do you have, who asks for it, and who should not get it?** The article covers Wallonia and its five distribution system operators (DSOs): ORES, RESA, AIEG, AIESH and REW. Brussels and Flanders are summarised at the end.

## What an EAN code designates

“EAN” stands for *European Article Numbering*. The Walloon technical regulation, in the version adopted by the regulator CWaPE in August 2026, defines it as a “unique numeric field” identifying “either an access point (EAN-GSRN code […]) or one of the market players (EAN-GLN code […])”. The one on your bill is the first kind.

RESA puts it in one sentence: the EAN number “is neither the meter number nor the customer number”. It “stays attached to the connection point, whoever the supplier or the customer”. ORES adds that there is “one EAN code per energy supplied”.

### EAN code or meter number?

Three numbers sit side by side on your documents:

- **the EAN code**, 18 digits, assigned by the grid operator to the access point;
- **the meter number**, written on the device. A replacement meter gets a new number, “while the EAN code remains the same” (Sibelga);
- **the customer number**, assigned by your supplier, which changes with it; AIEG points out that it does not know it.

The meter number still matters: together with your address, it is what grid operators ask for to retrieve your EAN code. Take a photo of it once and for all.

### Why the code starts with 54

A supply point's code is a *Global Service Relation Number*, a GS1 key whose uses explicitly include “the metering points of an electricity company”. Such a code begins with the prefix of the organisation that created it, and prefixes 540 to 549 belong to GS1 Belgium & Luxembourg. What follows varies:

- in Brussels, every code starts with **5414489** (Brugel);
- at REW, in Wavre, the code “always starts with 5414557”;
- at AIEG, with **5414**, and “in rare cases” with **541449**, in Gesves;
- the example ORES publishes starts with **541449**.

So the start of the code does not reliably tell you who runs your network today. Start from your municipality instead: the [“Find your DSO”](/en/tools/find-my-dso/) tool gives it from your postcode, for electricity and for gas.

### What changes, what stays

| What happens | Does the EAN code change? | Source |
|---|---|---|
| You switch supplier | No | RESA |
| The operator replaces your meter | No | AIEG: “the EAN code will remain identical” |
| A new occupant moves in | No | AIEG: the code belongs “to an address and not to a household” |
| Your municipality changes grid operator | Not always | Couvin, 2024: new AIESH codes, supply contract kept; Gesves: AIEG runs codes starting with 541449 |
| Your supply point has stayed blocked in the market systems | Yes, at ORES | New meter, new code; the old one “will be destroyed” |

*Assumptions: situations documented by Walloon grid operators as of 23 October 2026. We found no published general rule on what happens to codes when a network changes hands. The blocking affects supply points left in error since the Atrias market platform went live in November 2021.*

## Where to find your EAN code

### On your bills, instalment invoices included

The royal decree of 9 December 2021 requires “the switching code or the unique identification code of the final customer for their supply point” on the annual and closing statement (article 3, § 2, 9°), and the same code on the instalment invoice (article 5, 11°). That is the legal place of the EAN code, which the federal regulator CREG defines as “unique to your supply point”. The label varies by supplier; our [bill-reading guide](/en/guides/read-electricity-bill-belgium/) shows where it sits.

### Beyond the bill

| Where | What to know |
|---|---|
| Your supplier's customer area | ORES lists it among the places to find the code |
| myORES | Log in with itsme, eID or MyGov; shows the EAN; a code can only be linked to one account |
| MyRESA | Reserved for residential supply contracts; sign up with the same details as on the contract |
| Letters from the grid operator | Meter-reading letter (ORES, RESA), visit notice, text or e-mail inviting you to submit your readings (RESA), quotation for works (ORES) |
| Energy takeover form | Filled in when moving: one box for the electricity EAN, one for the gas EAN |
| The meter | Sometimes a label: REW sticks one “systematically” on smart meters; but CWaPE writes that the code “is not displayed on the meter” |

*Assumptions: channels described on the websites of ORES, RESA, AIEG and REW as of 23 October 2026; AIESH describes none. CWaPE's sentence comes from its 2020 mediation report.*

## Several EAN codes in one home

| What you have | How many EAN codes |
|---|---|
| Electricity and gas | Two, one per energy (ORES) |
| An exclusive night meter, at ORES | No extra code: it “is linked to the same EAN as the main meter” |
| A second electricity meter, for example for a charging point | One more: at ORES it “will have its own EAN code”, and can have its own supplier |
| Solar panels | One, sometimes two: the declaration form has an “injection EAN” field for bidirectional meters with two codes |
| A prepayment meter | The same code; to top up, you are asked for its last 13 digits (ORES) |

*Assumptions: the exclusive night meter rule is ORES's; we did not find it at the other four Walloon operators. CWaPE's energy takeover form points the same way: it lists the exclusive night meter under the home's single electricity EAN.*

For solar panels, CWaPE wrote in 2020 that most prosumers had “a bidirectional meter with a single EAN code”. Since 2024, a new installation requires a smart meter, and ORES lets you sign with two suppliers, “one for the energy drawn and the other for the energy sold”. Your bills or your grid operator will tell you whether you have one code or two; declaration and sharing forms ask for both when both exist.

## When you are asked for your EAN code

### To switch supplier

The new supplier does the work. The law of 29 April 1999 presumes it is “mandated” to end the old contract, with notice of “a maximum of three weeks” and no termination fee (article 18, § 2/3). It needs your code to identify the right supply point. Check that it is correct on the contract confirmation: according to the federal Energy Ombudsman, the cause of an unjustified supplier switch is “generally an error in recording the EAN code(s)”.

### To move house

The code belongs to the home; your contract follows you. In Wallonia, supply “continues at the customer's new address under the same conditions”, with exceptions such as termination or a move to another region (Walloon Government order of 30 March 2006, article 3*bis*).

The **energy takeover form** drawn up by CWaPE records the meter readings at the change of occupant: EAN codes, readings for each meter, two copies signed by both parties. It “is not equivalent to a contract”: tell your supplier “as soon as possible”.

In a block of flats, check the code you are given. CWaPE finds that errors are “often” swaps: “a new occupant is given their neighbour's EAN code, for example by their landlord or a building manager”. The reliable check is the meter number, read by yourself.

If nobody takes over the supply point, the grid operator writes to the new occupant within five working days and, failing a response, visits within fifteen working days with a regularisation form; without a contract, it may suspend supply (ministerial order of 3 March 2008).

Two decisions made on a code stay with the home. Participation in a sharing scheme, as our [guide for tenants](/en/guides/tenant-solar-without-roof-guide/) explains. And **giving up compensation**, which sharing requires: it is final, and the right “cannot be reactivated for the new producer (new owner or tenant)” either, CWaPE specifies. If you take over a house with solar panels, ask whether the previous occupant gave it up.

### To declare an installation

Solar panels, a battery, a plug-and-play kit: the declaration to the grid operator goes through the UP10 form, whose version 2.00 of 14 November 2025 asks for the “offtake EAN” and, if there is one, the “injection EAN”. According to AIEG's procedure, the applicant is the final customer “attached to the EAN code concerned”, and the form must arrive within 45 calendar days of the electrical safety inspection (RGIE). For a battery, that declaration has a consequence detailed in [“Home battery: the price and the alternative”](/en/guides/home-battery-price-vs-energy-sharing/).

### To join an energy community

Your EAN code is the identity document of your participation:

- **the community's manager enters it** in Annex 6 of CWaPE's sharing form, together with your meter number, your grid operator, your address and your status, residential or not. Each production installation appears there by its injection EAN, which the producer must hold;
- **you sign** the sworn statement (Annex 8) as “holder of the access point”, meaning the person who signed the contract with the supplier, and you copy your offtake code onto it and, where relevant, your injection code;
- **the grid operator checks**, code by code, that the meter's communication function is active and that compensation has been given up.

One rule follows: “an access point may take part in only one energy-sharing activity” (Walloon electricity decree, article 35*quaterdecies*, § 1, 4°). So no combining sharing within your building with an energy community: the grid operator checks it.

For a renewable energy community, the perimeter is also checked by code: no public database links EAN codes to transformer stations, but the grid operator can issue a certificate. And participants do not need the same operator: the application is filed with “the grid operator or operators” concerned. In OptimCE, each meter of a community is recorded with its EAN, its number and its operator ([Getting started with OptimCE](/en/features/getting-started/)).

### Two lesser-known uses

CWaPE's **GreenCheck** shows, from your electricity code, “the percentage of green electricity you consume each month”, for Walloon contracts; our analysis of [green electricity](/en/guides/green-electricity-belgium-really-green/) explains what that figure proves. And the new technical regulation, still to be published in the Belgian Official Gazette, gives you free access to your offtake and injection data “upon communication of [your] EAN code”.

## I can't find my EAN code

The grid operator can retrieve it: it is the one that assigns it. The [“Find your DSO”](/en/tools/find-my-dso/) tool tells you which one to contact; for gas, in Wallonia, it will be ORES or RESA, the only two that distribute it.

Have your **exact address** ready, box number included, and your **meter number**, read on the device. AIEG and REW only send the code “if there is a good match” between the two. The new technical regulation adopted by CWaPE provides for a reply within ten days at most, based on those two pieces of information.

| Operator | How to ask | How the code arrives |
|---|---|---|
| ORES | “Connaître mon code EAN” form on demandes.ores.be (also in Dutch and German): address, then the last four digits of the meter number; chat 8 am to 8 pm on weekdays; 078/15.78.01 | By text message, to the mobile number ORES or your supplier holds; otherwise an adviser searches: 48 hours by text, or three working days by post |
| RESA | Customer service on 04/220 12 11, Monday to Friday 8 am to 6 pm, contact form or chat; MyRESA | No published deadline |
| AIEG | “Demande de code EAN” form (address, meter number, signature) sent back via the website; 085/27.49.00 | By e-mail, if address and meter number match |
| AIESH | No published procedure: 060/45.91.60 or clients@aiesh.be | Not specified |
| REW | “Demande de code EAN” form on rew.be; 010/22.26.53 | By e-mail, if address and meter number match |

*Assumptions: procedures published by the operators, checked on 23 October 2026. ORES's form sends every code at the address, electricity and gas, and limits the number of requests.*

ORES's form warns from the outset that any abusive attempt to obtain an EAN code, for instance during door-to-door selling, may lead to legal proceedings. For a simple phone call, on the other hand, the code is not needed.

## Should you keep your EAN code to yourself?

Yes, without treating it as a state secret. ORES calls it “confidential data that is only given to the occupant or the owner of the building”, because “an ill-intentioned person could change your energy contract”.

The documented risk is mainly administrative. The federal Energy Ombudsman received **852 reports of unjustified takeovers in 2023**, against 1,042 in 2022 and 182 in 2021. Usually, the origin is a supplier linking a new customer's name to an EAN code tied to someone else's address. Its 2025 report also counts **359 “mystery switches”**, against 386 in 2024; the two series come from different publications and cannot be compared. Fraud happens too: one published case shows a door-to-door seller who had used another customer's EAN codes.

Three protections work in your favour:

- since 1 January 2024, a doorstep seller may only leave “a no-obligation offer and not an energy supply contract”, to be confirmed “after a period of at least three days” (royal decree of 12 November 2023);
- any energy contract can be cancelled free of charge within 14 calendar days, “however you concluded the contract” (FPS Economy);
- it is up to the supplier that took you over wrongly to cancel the takeover.

One rule has changed to your disadvantage: under the MIG6 market protocol, the supplier whose customer was taken can bill the consumption for that period. The Ombudsman is asking for a return to the old rule, under which neither supplier could.

**Give your code** to the supplier you chose, to the manager of the community you join, to your installer, to whoever takes over your home. **Not** to a canvasser while you have decided nothing. The usual sign of a takeover you did not ask for, according to the Ombudsman: a meter-reading card from the grid operator, then a supplier's letter, with no action on your part. Write to the supplier concerned and keep a copy, then, if that fails, refer the matter to the Energy Ombudsman, which handles contracts and abusive selling; CWaPE's regional mediation service handles meter readings and meters.

## Brussels and Flanders

**In Brussels**, every code starts with 5414489. Sibelga retrieves it online from the address and meter number, or on 02 549 41 00.

**In Flanders**, Fluvius says the code “always starts with the digit 54”, is printed on the bill, on a Fluvius quotation or on the meter's sticker, and answers its request form within five working days; someone else's code requires a power of attorney. For energy sharing, each participant is registered by their code in Mijn Fluvius, and each access point can join only one energy community.

## Key takeaways

1. **The EAN code designates the access point**, not the meter, the contract or you: it survives a change of supplier, meter and occupant.
2. **Eighteen digits, always 54 first**; the rest is not enough to identify your current operator.
3. **It is on your bills since 2022, instalments included**, and in myORES, MyRESA or the meter-reading letter.
4. **One code per energy, sometimes more**: a second meter or a separate injection point has its own.
5. **One access point, one sharing activity**: your code is what registers you in an energy community.
6. **Lost it? The grid operator retrieves it** from your address and meter number.
7. **Keep it for the steps you have chosen**: unjustified takeovers mostly stem from code errors.

## FAQ

### Where can I find my electricity EAN code?

On any recent bill, instalment invoices included: the law has required it since 2022. Otherwise in your supplier's customer area, myORES or MyRESA, on the meter-reading letter or the takeover form. As a last resort, the grid operator retrieves it from your exact address and meter number.

### Does the EAN code change when I move house or get a new meter?

No: it belongs to the home, and a replaced meter keeps the same code. Documented exceptions: AIESH taking over the Couvin network in 2024, and supply points blocked at ORES. In a block of flats, check the code you are given: according to CWaPE, it is often the neighbour's.

### Does gas have a different EAN code from electricity?

Yes, one code per energy, both 18 digits starting with 54. CWaPE warns against mixing them up: check which one you pass on, especially for a step that concerns electricity only.

### Why does my EAN code start with 54?

Because it is a GS1 identifier, and prefixes 540 to 549 belong to GS1 Belgium & Luxembourg. The rest depends on the organisation that created the code (5414489 in Brussels, 5414557 at REW, 5414 at AIEG), not necessarily on your current operator.

### Can someone switch my supplier with just my EAN code?

The risk exists, according to ORES, but unjustified takeovers mostly stem from code errors: 852 reports in 2023. Since 2024, no contract can be signed on the doorstep, and any contract can be cancelled within 14 days. If an unrequested takeover happens, write to the supplier, then to the Energy Ombudsman.

### Do I need my EAN code to join an energy community in Wallonia?

Yes: it identifies you in Annex 6 of the sharing form and in the statement you sign as holder of the access point. The same access point may take part in only one sharing activity.

## Sources

- [Belgian Official Gazette — Royal decree of 9 December 2021 setting further minimum requirements for gas and electricity bills and billing information](https://www.ejustice.just.fgov.be/eli/arrete/2021/12/09/2021022724/justel) (in French) — article 3, § 2, 9° (unique identification code of the supply point on the annual and closing statement) and article 5, 11° (same code on the instalment invoice); in force since 1 January 2022. Accessed 23 October 2026.
- [CWaPE — Decision CD-26h27-CWaPE-1284 approving the technical regulation for the management of electricity distribution networks in Wallonia](https://www.cwape.be/sites/default/files/cwape-documents/CD-26h27-CWaPE-1284-D%C3%A9cision%20d%27approbation%20du%20RTDE%20%26%20annexes_site.pdf) (in French) — decision of 27 August 2026 adopting the new technical regulation, to be published in the Official Gazette after translation and applicable ten days after publication; the regulation in force remains the one approved by the Walloon Government order of 27 May 2021. Source of the definition of the EAN code (EAN-GSRN for an access point, EAN-GLN for a market player), of the rule that the operator gives the code within ten days based on meter number and address (article IV.22, § 2) and of free access to metering data upon communication of the code (article V.74). Accessed 23 October 2026.
- [GS1 — Global Service Relation Number (GSRN)](https://www.gs1.org/standards/id-keys/gsrn) and [GS1 — GS1 Company Prefix](https://www.gs1.org/standards/id-keys/company-prefix) — use of the GSRN for the metering points of an electricity company; prefixes 540 to 549 managed by GS1 Belgium & Luxembourg. Accessed 23 October 2026.
- [CREG — EAN code](https://www.creg.be/fr/a-z-index/code-ean) (in French) — 18-digit code, unique to the supply point, shown on the bill and needed to take out a new contract. Accessed 23 October 2026.
- [ORES — EAN code](https://www.ores.be/particulier/code-ean) (in French) — where to find the code, its confidential nature and the risk of a contract change by an ill-intentioned person. Accessed 23 October 2026.
- [ORES — Fact sheet E-01 “Démarches administratives”, version 06, September 2025](https://media.ores.be/ores-cms/efqhbfq3/ores_fiche_e-01_demarches_administratives_fr_web.pdf) (in French) — example code (541449060016048579), one code per energy supplied, permanently linked to the access point and not to the customer. Accessed 23 October 2026.
- [ORES — Connaître mon code EAN](https://demandes.ores.be/code-ean) (in French; Dutch and German versions available) — online form: address, last four digits of the meter number, text message to the known number, search by an adviser (48 hours by text or three working days by post), all codes at the address sent, request limit, warning against abusive attempts. Accessed 23 October 2026.
- [ORES — Readings and consumption FAQ](https://www.ores.be/faq/releves-et-consommation) (in French) — code on the bill, meter-reading letter or myORES; calls to 078/15.78.01 without an EAN code; old code destroyed after unblocking. Accessed 23 October 2026.
- [ORES — Meters FAQ](https://www.ores.be/faq/les-compteurs) and [ORES — Exclusive night meter](https://www.ores.be/comprendre-ma-facture/exclusif-de-nuit) (in French) — exclusive night meter linked to the same EAN as the main meter; a second electricity meter with its own EAN code. Accessed 23 October 2026.
- [ORES — myORES FAQ](https://www.ores.be/faq/myores) (in French) — login with itsme, eID or MyGov, EAN shown, one code linked to one account. Accessed 23 October 2026.
- [ORES — Prepayment meter FAQ](https://www.ores.be/faq/compteur-a-fonction-de-prepaiement) (in French) — last 13 digits of the EAN code to top up or check the balance. Accessed 23 October 2026.
- [ORES — Blocked data](https://www.ores.be/blocage-donnees-que-faire-avant-et-apres-la-reception-du-code-ean) (in French) — blockages since Atrias went live in November 2021, new meter and new EAN code. Accessed 23 October 2026.
- [ORES — Prosumers from 2024](https://www.ores.be/particulier/prosumer-a-partir-de-2024) (in French) — smart meter mandatory, two suppliers possible for energy drawn and energy sold. Accessed 23 October 2026.
- [RESA — My EAN number](https://www.resa.be/fr/ma-situation/mon-numero-ean/), [RESA — Where can I find my EAN code and meter number?](https://www.resa.be/fr/aide-et-contact/index/transmettre-index/ou-puis-je-trouver-mon-code-ean-et-mon-numero-de-compteur/) and [RESA — MyRESA](https://www.resa.be/fr/my-resa-votre-espace-personnel/) (in French) — code distinct from meter and customer numbers, attached to the connection point; meter-reading letter, visit notice, invitation text or e-mail, MyRESA for residential contracts. Customer-service details taken from the site footer. Accessed 23 October 2026.
- [AIEG — Finding my EAN code](https://www.aieg.be/trouver-mon-code-ean/), [AIEG — Requesting my EAN code](https://www.aieg.be/je-demande-mon-code-ean/) and [“Demande de code EAN” form](https://www.aieg.be/app/uploads/2025/10/Demande-Code-EAN.pdf) (in French) — 5414 prefix and the Gesves case (541449), code unchanged after meter replacement, sent by e-mail when address and meter number match, customer number unknown to AIEG. Accessed 23 October 2026.
- [AIEG — Commissioning notification procedure, UP10 form, version 1.02](https://www.aieg.be/app/uploads/2025/02/Procedure-de-notification-de-mise-en-service_PV_-UP10_Fr-1_02.pdf) (in French) — applicant attached to the EAN code concerned, 45 calendar days after the RGIE inspection. Accessed 23 October 2026.
- [UP10 form, version 2.00 of 14 November 2025](https://cms.resa.be/app/uploads/2025/03/formulaire-unique-up-10-kva-version1-07.pdf) (in French) — “EAN prélèvement” and “EAN injection” fields, the latter only for a bidirectional meter with two EAN codes. Accessed 23 October 2026.
- [AIESH — FAQ on the takeover of the Couvin network](https://aiesh.be/static/docs/couvin_FAQ_V1.pdf) (in French) — new AIESH-specific EAN code on 1 January 2024, supply contract kept. Contact details from the [contact page](https://www.aiesh.be/contact/). Accessed 23 October 2026.
- [REW — Finding your EAN code](https://www.rew.be/recherche-de-votre-code-ean) (in French) — 5414557 prefix, label systematically placed on smart meters, request form and reply by e-mail. Contact details from the [contact page](https://www.rew.be/contactus). Accessed 23 October 2026.
- [CWaPE — 2020 annual report of the regional energy mediation service](https://www.cwape.be/sites/default/files/cwape-documents/2021.06.30-Rapport%20annuel%20sp%C3%A9cifique%20SRME%202020.pdf) (in French) — one code per electricity and gas connection, code not displayed on the meter, frequent code swaps between neighbours in the same building, prosumers with a bidirectional meter and a single EAN code. Accessed 23 October 2026.
- [CWaPE — Energy takeover form, production installation](https://www.cwape.be/documents/download/3058) (in French) — electricity EAN and gas EAN boxes, two copies signed by both parties, not equivalent to a contract. Accessed 23 October 2026.
- [CWaPE — Explanatory guide to the electricity-sharing form in Wallonia, July 2025](https://www.cwape.be/documents/download/5610) (in French) — content of Annex 6, holder of the injection EAN, exclusivity of the sharing activity, no public database linking EANs to transformer stations, final renunciation of compensation. Accessed 23 October 2026.
- [CWaPE — Annex 8, sworn statement of the persons taking part in sharing, version of 12 October 2023](https://www.cwape.be/documents/download/5612) (in French) — signature as holder of the access point, offtake and injection EAN codes. Accessed 23 October 2026.
- [CWaPE — GreenCheck](https://www.cwape.be/conso/greencheck) (in French) — monthly percentage of green electricity from the EAN code, for Walloon contracts; warning against confusing electricity and gas codes. Accessed 23 October 2026.
- [CWaPE — Mediation](https://www.cwape.be/srme/mediation) (in French) — division of competences between the regional service and the federal Energy Ombudsman, prior written complaint. Accessed 23 October 2026.
- [Wallex — Decree of 12 April 2001 on the organisation of the regional electricity market](https://wallex.wallonie.be/eli/loi-decret/2001/04/12/2001027238) (in French) — article 35*quaterdecies*, § 1, 4° (one access point, one sharing activity) and § 3 (application to the grid operator or operators). Accessed 23 October 2026.
- [Wallex — Walloon Government order of 30 March 2006 on public service obligations in the electricity market](https://wallex.wallonie.be/eli/arrete/2006/03/30/2006201391) (in French) — article 3*bis* (supply continues at the new address) and article 22*bis* (grid operator contacts the new occupant within five working days). Accessed 23 October 2026.
- [Wallex — Ministerial order of 3 March 2008 on the regularisation procedure](https://wallex.wallonie.be/eli/arrete/2008/03/03/2008200847) (in French) — visit within fifteen working days, regularisation form, possible suspension. Accessed 23 October 2026.
- [Justel — Law of 29 April 1999 on the organisation of the electricity market](https://www.ejustice.just.fgov.be/eli/loi/1999/04/29/1999011160/justel) (in French) — article 18, § 2/3: notice of at most three weeks, supplier presumed mandated, no termination fee. Accessed 23 October 2026.
- [Justel — Royal decree of 12 November 2023 on unsolicited visits to consumers' homes](https://www.ejustice.just.fgov.be/eli/arrete/2023/11/12/2023047098/justel) (in French) — no-obligation offer, confirmation after at least three days, in force since 1 January 2024. Accessed 23 October 2026.
- [FPS Economy, ConsumerConnect — Right of withdrawal](https://consumerconnect.be/fr/themes/energie/gaz-electricite/contrat/droit-de-retractation) (in French) — 14 calendar days, free of charge, however the contract was concluded. Accessed 23 October 2026.
- [Energy Ombudsman — 2024 memorandum](https://www.mediateurenergie.be/sites/default/files/content/download/files/memorandum2024_0.pdf) (in French) — 852 reports of unjustified takeovers in 2023, 1,042 in 2022, 182 in 2021; usual cause in the recording of the EAN code; cancellation up to the supplier that took over the point; usual warning sign. Accessed 23 October 2026.
- [Energy Ombudsman — Press release of 28 April 2026 on the 2025 activity report](https://www.mediateurenergie.be/fr/actualites/communique-de-presse-rapport-dactivites-2025-du-service-federal-de-mediation-de-lenergie) (in French) — 359 “mystery switches” in 2025 against 386 in 2024, billing of the hijacked period allowed by MIG6. Accessed 23 October 2026.
- [Energy Ombudsman — “Mystery Switch” case](https://www.mediateurenergie.be/fr/exemples/mystery-switch) (in French) — door-to-door seller who used another customer's EAN codes, return to the original supplier and cancelled invoices. Accessed 23 October 2026.
- [Brugel — Understanding my bill](https://brugel.brussels/themes/consommateurs-7/comprendre-ma-facture-13) and [Sibelga — EAN code search](https://www.sibelga.be/fr/raccordements-compteurs/mon-raccordement/recherche-du-code-ean) (in French) — Brussels prefix 5414489, online search and customer-service number, code unchanged when the meter is replaced. Accessed 23 October 2026.
- [Fluvius — Requesting an EAN code](https://www.fluvius.be/nl/contact/contactformulier/ean-code) and [Fluvius — Energy sharing in an energy community](https://www.fluvius.be/nl/groene-energie/energiedelen/in-een-energiegemeenschap) (in Dutch) — 18-digit code starting with 54, meter sticker, reply within five working days, power of attorney for a third party; participants registered by EAN code, one access point per community. Accessed 23 October 2026.
