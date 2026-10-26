---
layout: page
title: "Rekenblad of software voor uw gemeenschap?"
breadcrumb_title: "Rekenblad of software"
subtitle: "Een eerlijke vergelijking: wanneer een rekenblad volstaat om een energiegemeenschap te beheren, en waar het begint te breken."
description: "Volstaat Excel voor een energiegemeenschap? Wanneer een rekenblad volstaat, waar het breekt (kwartieren, sleutels, facturen, CWaPE) en wat software doet."
lang: nl
ref: product-vs-spreadsheet
permalink: /nl/functies/rekenblad-of-software/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Volstaat een rekenblad voor een kleine energiegemeenschap?"
    a: "Vaak wel. Met een handvol leden, één deelactie en een standaardsleutel die niet verandert, volstaat een goed bijgehouden rekenblad. Het wordt kwetsbaar wanneer de sleutel evolueert, wanneer de facturen zich opstapelen of wanneer meerdere mensen erin moeten werken."
  - q: "Waarom gaat het om 35 040 waarden per meter per jaar?"
    a: "Omdat het delen per kwartier wordt berekend: 96 kwartieren per dag, over een jaar van 365 dagen, geeft 35 040 waarden per meter. De dagen waarop de klok wordt verzet, tellen 92 of 100 kwartieren, en het jaartotaal blijft hetzelfde."
  - q: "Vervangt OptimCE de boekhouding van de gemeenschap?"
    a: "Nee. OptimCE factureert de gedeelde energie en volgt de betaling van die facturen op. De algemene boekhouding van de gemeenschap houdt u apart bij."
  - q: "Wat kost OptimCE in vergelijking met een rekenblad?"
    a: "OptimCE Cloud is gratis gedurende de hele alfafase, en zelf hosten is voor altijd gratis. Later kan er een betalend aanbod komen voor de gehoste versie; de alfagebruikers worden ruim vooraf verwittigd."
---

De meeste energiegemeenschappen beginnen met een rekenblad, en dat is vaak de juiste keuze: het is
al geïnstalleerd, iedereen kan het openen, en een kleine gemeenschap heeft niet meer nodig. Maar
een rekenblad heeft geen geheugen. Het weet niet welke versie van de verdeelsleutel in maart gold,
welk factuurnummer het volgende is, en ook niet wat er bij de CWaPE is ingediend en wanneer. Deze
pagina vergelijkt beide eerlijk, zonder u te willen laten overstappen voordat het nodig is.

## Wanneer een rekenblad volstaat

Een goed bijgehouden rekenblad volstaat zolang de gemeenschap eenvoudig blijft:

- een handvol leden en één deelactie;
- een standaardverdeelsleutel, die niet van jaar tot jaar verandert;
- weinig documenten om op te stellen: enkele facturen per periode, een CWaPE-dossier dat al is
  ingediend;
- één persoon die het bestand bijhoudt, en het netjes doorgeeft wanneer ze het stokje overdraagt.

Lijkt uw gemeenschap daarop, houd dan uw rekenblad. Verandert een van die punten, dan gaat de rest
van deze pagina over u.

## Hoe OptimCE het aanpakt

Dit zijn de vijf plekken waar een rekenblad begint te breken, en wat OptimCE in de plaats doet.

### De kwartierdata

In België wordt het delen per kwartier berekend: 96 waarden per dag en per meter, of 35 040 over
een jaar van 365 dagen. Met één rij per meter en per kwartier vormen de gegevens van één jaar voor
30 meters 1 051 200 rijen: meer dan de 1 048 576 rijen van een Excel-werkblad
([Microsoft](https://support.microsoft.com/nl-nl/excel/excel-specifications-and-limits)). Lang vóór
die grens wordt de werkmap traag om te openen en te herberekenen.

In OptimCE importeert u de kwartierdata per deelactie en per periode. De facturatie en de
generatie en simulatie van sleutels werken er rechtstreeks mee.

### De versies van de sleutel

Een verdeelsleutel verandert telkens wanneer een lid toetreedt of vertrekt. In een rekenblad
overschrijft de versie van maart die van januari, of ze overleeft in een bestand
“sleutel_v3_definitief.xlsx” waarvan niemand nog weet of het werd aanvaard.

In OptimCE wordt elke versie van de sleutel bewaard en wordt de aanvaarding door de leden
opgevolgd. Alles daarover staat op de pagina over de
[verdeelsleutel]({{ "product-allocation-key" | ref_url }}).

### De nummering van de facturen

Facturen worden genummerd in een doorlopende reeks, zonder gaten, en een uitgereikte factuur wordt
niet meer gewijzigd: u corrigeert ze met een creditnota. In een rekenblad belet niets u om een rij
te overschrijven, een nummer over te slaan of een foute gestructureerde mededeling over te nemen.

In OptimCE worden het nummer en de gestructureerde mededeling bij de uitreiking toegekend, loopt
een correctie via een creditnota en blijft de historiek volledig. Zie de
[facturatiesoftware]({{ "product-billing" | ref_url }}).

{% include product-shot.html name="billing-member" alt="Overzicht “Mijn facturen” van een lid: een vergoedingsafrekening DP-2025-00001 met de status “Uitgereikt”, van 36,69 €, met haar gestructureerde mededeling." caption="Elk lid ziet zijn eigen documenten, met de gestructureerde mededeling die het bij zijn overschrijving vermeldt (testgegevens)." %}

### De CWaPE-dossiers

Dezelfde gegevens (leden, leveringspunten, installaties) worden overgenomen in meerdere formulieren
van de CWaPE, en elke wijziging in de gemeenschap vraagt nieuwe formulieren, met termijnen in
werkdagen. Een rekenblad weet niet dat een dossier net van status is veranderd, en ook niet welke
versie van een formulier is vertrokken.

In OptimCE worden de officiële formulieren vooraf ingevuld op basis van de ledenlijst, wordt elke
versie bewaard en worden de termijnen in werkdagen berekend. Zie het
[CWaPE-dossier]({{ "product-cwape" | ref_url }}).

{% include product-shot.html name="cwape-deadlines" alt="Tabblad “Termijnen” van de “Administratieve documenten”: een “Volledigheidscontrole” met vervaldatum 06/11/2026 voor dossier nr. 1, met de status “Open”." caption="De openstaande termijnen van alle dossiers, berekend op basis van de statuswijzigingen (testgegevens)." %}

### Toegang voor de leden en de overdracht

Om elk lid zijn factuur te tonen, of wat er over hem is ingediend, moet u met een rekenblad per
persoon een apart bestand maken en versturen: de hele werkmap delen zou de gegevens van iedereen
blootgeven. En het bestand hangt af van wie het bijhoudt: als die persoon vertrekt, verdwijnt de
historiek vaak mee met haar mailbox.

In OptimCE ziet elk lid zijn eigen facturen en wat er over hem is ingediend, en niets anders.
Meerdere personen kunnen de gemeenschap beheren, elk met een eigen rol, en de historiek blijft in
de applicatie.

## Wat het niet doet

**OptimCE vervangt uw boekhouding niet.** Het factureert de gedeelde energie en volgt de betaling
van die facturen op. De algemene boekhouding van de gemeenschap houdt u apart bij.

**Geen realtime.** Net als uw rekenblad werkt OptimCE met de meetgegevens die de netbeheerder
doorstuurt en met de bestanden die u importeert: het toont geen realtimegegevens.

**Het corrigeert geen foute gegevens.** Software voorkomt kopieerfouten, geen invoerfouten. Een
verkeerd adres of een verkeerde EAN-code blijft fout, in een rekenblad net zo goed als in OptimCE.

## Veelgestelde vragen {#faq}

### Volstaat een rekenblad voor een kleine energiegemeenschap?

Vaak wel. Met een handvol leden, één deelactie en een standaardsleutel die niet verandert, volstaat
een goed bijgehouden rekenblad. Het wordt kwetsbaar wanneer de sleutel evolueert, wanneer de
facturen zich opstapelen of wanneer meerdere mensen erin moeten werken.

### Waarom gaat het om 35 040 waarden per meter per jaar?

Omdat het delen per kwartier wordt berekend: 96 kwartieren per dag, over een jaar van 365 dagen,
geeft 35 040 waarden per meter. De dagen waarop de klok wordt verzet, tellen 92 of 100 kwartieren,
en het jaartotaal blijft hetzelfde.

### Vervangt OptimCE de boekhouding van de gemeenschap?

Nee. OptimCE factureert de gedeelde energie en volgt de betaling van die facturen op. De algemene
boekhouding van de gemeenschap houdt u apart bij.

### Wat kost OptimCE in vergelijking met een rekenblad?

OptimCE Cloud is gratis gedurende de hele alfafase, en zelf hosten is voor altijd gratis. Later kan
er een betalend aanbod komen voor de gehoste versie; de alfagebruikers worden ruim vooraf
verwittigd.

## Verder lezen

- [Energiegemeenschap: CWaPE-documenten en termijnen]({{ "cwape-administrative-documents" | ref_url }}):
  elk formulier, de termijnen, en waar u begint als alles al in rekenbladen staat.
- [Gedeelde elektriciteit factureren in België]({{ "invoice-shared-electricity" | ref_url }}):
  wie wat factureert, de btw en de verplichte vermeldingen.
- [Verdeelsleutel in België: de 3 regio's]({{ "allocation-key-belgium" | ref_url }}):
  de standaardsleutels en de regels van elk gewest.

{% include product-cta.html page_key="vs-spreadsheet" guide="getting-started" title="Van rekenblad naar OptimCE" %}
