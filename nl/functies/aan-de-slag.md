---
layout: page
title: "Een gemeenschap starten op OptimCE"
breadcrumb_title: "Aan de slag"
subtitle: "Zes stappen, van het aanmaken van de gemeenschap tot de eerste factuur, elk met een eigen stapsgewijze handleiding."
description: "Gemeenschap aanmaken, leden en meters toevoegen, deelactie openen, sleutel vastleggen, factureren: starten op OptimCE in zes stappen."
lang: nl
ref: product-getting-started
permalink: /nl/functies/aan-de-slag/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Moet u OptimCE installeren om te starten?"
    a: "Nee. OptimCE Cloud, op app.optimce.be, vraagt geen installatie: u maakt een account aan, daarna uw gemeenschap. Zelf hosten is een andere weg, voor teams die het platform zelf willen hosten."
  - q: "Wat kost OptimCE?"
    a: "OptimCE Cloud is gratis gedurende de hele alfafase, en zelf hosten is voor altijd gratis. Later kan er een betalend aanbod komen voor de gehoste versie; de alfagebruikers worden ruim vooraf verwittigd."
  - q: "In welke volgorde doorloopt u de stappen?"
    a: "In de volgorde van deze pagina, die de afhankelijkheden tussen de modules volgt: meters zijn gekoppeld aan leden, tarieven en facturen aan een deelactie, en de facturatie past de verdeling van die deelactie toe."
  - q: "Kunt u meerdere gemeenschappen beheren met hetzelfde account?"
    a: "Ja. Eén installatie van OptimCE beheert meerdere gemeenschappen, en een account kan tot meerdere ervan behoren. U schakelt van de ene naar de andere over vanuit “Mijn gemeenschappen”."
---

Een energiegemeenschap in software opstarten draait vooral om de juiste volgorde. Deze pagina volgt
de volgorde waarin een beheerder een Waalse gemeenschap in OptimCE instelt, van het aanmaken tot de
eerste factuur. Voor een gemeenschap in Vlaanderen of in Brussel geldt dit traject nog niet (zie
onderaan). Elke stap verwijst naar zijn stapsgewijze handleiding, die elk scherm toont met
testgegevens, en naar de pagina die de module in detail beschrijft.

## Wat u bij de hand moet hebben

- **Voor de gemeenschap**: haar officiële naam, haar btw-nummer, het adres van haar zetel, haar
  IBAN en de rekeninghouder.
- **Voor elk lid**: zijn status (particulier of bedrijf), zijn naam, zijn e-mailadres, zijn
  telefoonnummer, zijn adres en zijn IBAN; voor een particulier ook zijn rijksregisternummer.
- **Voor elke meter**: het installatieadres, de EAN-code, het meternummer, de technische
  kenmerken (fasen, uitleesfrequentie, vermogen) en de netbeheerder.

Niets verplicht u om alles al op de eerste dag te hebben: het dashboard toont wat nog ontbreekt.

## Het traject, stap voor stap

### 1. De gemeenschap aanmaken

Vanuit “Mijn gemeenschappen” maakt u de gemeenschap aan: een naam en haar regulator, voor
Wallonië vooraf ingesteld op de CWaPE. U wordt er beheerder van; daarna moet u ze nog activeren om
ze in te stellen.

Handleiding:
[een gemeenschap aanmaken](https://guide.optimce.be/community-create/nl.html). Voor het overzicht:
[beheersoftware voor energiegemeenschappen]({{ "features" | ref_url }}).

{% include product-shot.html name="start-dashboard" alt="Dashboard van een nieuwe gemeenschap: “Aandachtspunten” somt vijf ontbrekende gegevens op (btw-nummer, juridische naam, IBAN, rekeninghouder, adres van de zetel), en er bestaat nog geen enkele deelbewerking." caption="Het dashboard van een pas aangemaakte gemeenschap: wat er nog moet worden aangevuld (testgegevens)." %}

### 2. De leden toevoegen

Een wizard in vier stappen registreert elk lid: zijn status, zijn persoonlijke gegevens, zijn
adressen en zijn bankgegevens. Daarna stelt een venster voor om meteen zijn meter toe te voegen;
dat kunt u ook later doen vanuit zijn fiche. U kunt leden ook via een uitnodiging toevoegen.

Handleiding: [een lid aanmaken](https://guide.optimce.be/member-create/nl.html). Module:
[leden, meters en gemeenschappen]({{ "features" | ref_url }}).

{% include product-shot.html name="start-member" alt="Eerste stap van de wizard “Lid toevoegen”: de keuze van de status, “Particulier” of “Bedrijf”, gevolgd door de stappen “Persoonlijke informatie”, “Adressen” en “Bankgegevens”." caption="De wizard om een lid aan te maken, bij de eerste stap (testgegevens)." %}

### 3. De meters toevoegen

Vul voor elke meter de locatie en de EAN-code in, de kenmerken, de netbeheerder, het lid op wiens
naam hij staat en de activeringsdatum. De energiewaarden van de meter, zoals het afnamevermogen en
de productiecapaciteit, voeden de verdeelberekeningen. Vóór zijn activeringsdatum telt de meter in
geen enkele berekening mee.

Handleiding: [een meter aanmaken](https://guide.optimce.be/meter-create/nl.html). Module:
[leden, meters en gemeenschappen]({{ "features" | ref_url }}).

### 4. De deelactie aanmaken

Geef ze een naam, een type (binnen een gebouw, hernieuwbare-energiegemeenschap of
burgerenergiegemeenschap) en de gemeenten die ze dekt. De tarieven, de facturen en de
administratieve dossiers worden daarna aan deze deelactie gekoppeld.

Handleiding: [een deelactie aanmaken](https://guide.optimce.be/sharing-op-create/nl.html).
Module: [het CWaPE-dossier van de deelactie]({{ "product-cwape" | ref_url }}).

### 5. De verdeelsleutel vastleggen

Geef met de wizard het aantal verbruikers en hun namen op, en daarna de iteraties, die elk een
percentage van de energie verdelen, tot 100 %. U kunt ook een sleutel laten voorstellen op basis
van uw gegevens, en hem simuleren voordat u hem aanneemt.

Handleiding: [een sleutel aanmaken met de wizard](https://guide.optimce.be/key-create-wizard/nl.html).
Module: [verdeelsleutel: genereren, simuleren, opvolgen]({{ "product-allocation-key" | ref_url }}).

### 6. Factureren

Leg de verkoopprijs van de gedeelde energie en de terugkoopprijs van de injectie vast, importeer
de meetgegevens van de periode, genereer een ontwerp per lid, reik de documenten uit en volg daarna
de betalingen op.

Handleiding: [een deelactie factureren, van het tarief tot de ontvangen betaling](https://guide.optimce.be/billing-tarification-pay/nl.html).
Module: [de facturatiesoftware]({{ "product-billing" | ref_url }}).

### En daarna

Elk lid vindt zijn facturen terug in de applicatie en kan inzien wat er over hem bij de regulator
is ingediend. Voor de stappen bij de CWaPE bereidt de module voor administratieve documenten de
officiële formulieren van de deelactie voor en berekent ze de termijnen in werkdagen.

## Wat het niet doet

**OptimCE richt de rechtspersoon niet op.** De rechtsvorm van de gemeenschap, haar statuten en
haar algemene vergadering regelt u buiten de applicatie.

**OptimCE dient niets in uw plaats in.** De kennisgevingen aan de CWaPE en de overeenkomsten met
de netbeheerder blijven uw zaak; OptimCE bereidt de documenten voor en volgt de termijnen op.

**Brussel en Vlaanderen: gepland, nog niet beschikbaar.** De regulator kiest u bij het aanmaken,
maar de facturatie en de administratieve documenten dekken vandaag het Waalse kader. Brussel en
Vlaanderen zijn gepland, maar nog niet geïmplementeerd. Het traject op deze pagina geldt dus nog
niet voor een gemeenschap in Vlaanderen of in Brussel.

## Veelgestelde vragen {#faq}

### Moet u OptimCE installeren om te starten?

Nee. OptimCE Cloud, op app.optimce.be, vraagt geen installatie: u maakt een account aan, daarna uw
gemeenschap. Zelf hosten is een andere weg, voor teams die het platform zelf willen hosten.

### Wat kost OptimCE?

OptimCE Cloud is gratis gedurende de hele alfafase, en zelf hosten is voor altijd gratis. Later kan
er een betalend aanbod komen voor de gehoste versie; de alfagebruikers worden ruim vooraf
verwittigd.

### In welke volgorde doorloopt u de stappen?

In de volgorde van deze pagina, die de afhankelijkheden tussen de modules volgt: meters zijn
gekoppeld aan leden, tarieven en facturen aan een deelactie, en de facturatie past de verdeling van
die deelactie toe.

### Kunt u meerdere gemeenschappen beheren met hetzelfde account?

Ja. Eén installatie van OptimCE beheert meerdere gemeenschappen, en een account kan tot meerdere
ervan behoren. U schakelt van de ene naar de andere over vanuit “Mijn gemeenschappen”.

## Verder lezen

- [Energiegemeenschap oprichten in Wallonië]({{ "create-energy-community-wallonia" | ref_url }}):
  de stappen, van de rechtsvorm tot de kennisgeving.
- [Energiegemeenschap: CWaPE-documenten en termijnen]({{ "cwape-administrative-documents" | ref_url }}):
  wat u moet indienen, waar en binnen welke termijn.
- [Rekenblad of software voor uw gemeenschap?]({{ "product-vs-spreadsheet" | ref_url }}):
  wanneer een rekenblad nog volstaat, en waar het begint te breken.

{% include product-cta.html page_key="getting-started" guide="getting-started" title="Uw gemeenschap aanmaken op OptimCE" %}
