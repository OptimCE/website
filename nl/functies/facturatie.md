---
layout: page
title: "Facturatiesoftware voor energiegemeenschappen"
breadcrumb_title: "Facturatie"
subtitle: "Van de prijs per kWh tot de ontvangen betaling: de facturen van uw leden, berekend op de verdeling die de netbeheerder doorstuurt."
description: "Factureer de leden van uw energiegemeenschap zonder rekenblad: prijs per kWh, ontwerpen, doorlopende nummering, gestructureerde mededeling, betalingen."
lang: nl
ref: product-billing
permalink: /nl/functies/facturatie/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Waar komen de gegevens voor de facturatie vandaan?"
    a: "Uit de verdeling die de netbeheerder doorstuurt: de gedeelde volumes per kwartier, die u importeert voor de deelactie en de periode die u factureert. Bij de start van de cyclus bevriest OptimCE een momentopname van die volumes; de bedragen worden berekend op die bevroren gegevens, die u kunt natrekken."
  - q: "Kunt u verschillende prijzen toepassen naargelang het lid?"
    a: "Ja. Elke prijs geldt voor de hele deelactie, voor een klantsegment (residentieel, professioneel, industrieel) of voor één specifiek leveringspunt (EAN), met een geldigheidsperiode. Als meerdere regels hetzelfde lid betreffen, wint de meest specifieke: de prijs van een EAN gaat voor op die van zijn segment, en die gaat voor op de globale prijs."
  - q: "Hoe corrigeert u een factuur die al is uitgereikt?"
    a: "Een uitgereikte factuur heeft een nummer gekregen in een doorlopende nummering: ze kan niet meer worden gewijzigd of verwijderd. Om ze te corrigeren, reikt u een creditnota uit die haar annuleert, en factureert u opnieuw. Zolang een document nog een ontwerp is, kunt u het daarentegen wel verwijderen of herberekenen."
  - q: "Regelt OptimCE de btw?"
    a: "Gedeeltelijk. De module berekent de btw, maar met één tarief van 21 % voor alle documenten: tarieven die per lid verschillen en de vrijstellingsregeling voor kleine ondernemingen worden nog niet ondersteund. De btw-regeling van de gemeenschap (btw-plichtig of niet, de tarieven voor elk lid) legt u vóór de eerste factuur vast met een boekhouder."
---

Elke periode zet de beheerder van een energiegemeenschap de gedeelde volumes om in één factuur
per lid: de juiste prijs toepassen, zonder gaten nummeren, een gestructureerde mededeling
toevoegen en daarna nagaan wie betaald heeft. In een rekenblad doet u elk van die stappen opnieuw
met de hand, en elke fout corrigeert u ook met de hand. De facturatiemodule van OptimCE neemt dat
werk over op basis van de verdeling die de distributienetbeheerder doorstuurt, binnen het Waalse
kader van de CWaPE.

## Hoe OptimCE het aanpakt

De module volgt de volledige cyclus, van het tarief tot de ontvangen betaling. Tarieven en
facturen zijn altijd gekoppeld aan een deelactie: een gemeenschap met meerdere deelacties
factureert ze afzonderlijk.

### U legt twee prijzen vast

De gemeenschap bepaalt zelf haar prijzen, in €/kWh. De **verkoopprijs** geldt voor de gedeelde
energie die de leden verbruiken; de **terugkoopprijs** vergoedt de injectie die de producenten met
de gemeenschap delen.

Elke prijs geldt voor de hele deelactie, voor een klantsegment (residentieel, professioneel,
industrieel) of voor één specifiek leveringspunt, en heeft een geldigheidsperiode. Als meerdere
regels hetzelfde lid betreffen, wint de meest specifieke. Een verlaagd tarief voor een school of
voor een gezin vraagt dus geen tweede deelactie: een prijs op het leveringspunt (EAN) van dat lid
volstaat.

{% include product-shot.html name="billing-tariffs" alt="Tabblad “Tarieven” van de module “Facturatie”: een “Verkoopprijs voor verbruiker” van 0,12 €/kWh en een “Terugkoopprijs voor producent” van 0,05 €/kWh, allebei met reikwijdte “Globaal” en geldig vanaf 1 januari 2025." caption="De twee prijzen van een deelactie, zoals de stapsgewijze handleiding ze toont (testgegevens)." %}

### U start een cyclus voor een periode

U kiest de deelactie en de periode die u wilt factureren: een maand, een kwartaal, op het ritme
van de gemeenschap. De facturatie steunt op de kwartierdata die de netbeheerder voor de deelactie
doorstuurt. Bij de start bevriest OptimCE een momentopname van die volumes: de bedragen worden
berekend op bevroren gegevens, die u kunt natrekken als een lid een vraag stelt.

De berekening loopt op de achtergrond. Ze levert een **ontwerp per lid** op, dat u als pdf
downloadt met een “proforma”-watermerk. Een ontwerp kunt u vrij nalezen, verwijderen of
herberekenen: niets is definitief zolang u niet hebt uitgereikt.

### U reikt de documenten uit

Bij de uitreiking krijgt elk document een nummer in een doorlopende nummering, een gestructureerde
mededeling en een vervaldatum. OptimCE genereert drie documenten als pdf, elk met een eigen reeks:

- de **factuur** (F-…), voor de gedeelde energie die een lid verbruikt;
- de **creditnota** (NC-…), om een al uitgereikte factuur te annuleren;
- de **vergoedingsafrekening** (DP-…), voor de gedeelde injectie van een producent.

Een lid dat tegelijk verbruiker en producent is, ontvangt twee afzonderlijke documenten. Een
uitgereikte factuur kan niet meer worden gewijzigd: een fout corrigeert u met een creditnota en
daarna met een nieuwe factuur, en de historiek blijft volledig.

### U volgt de betalingen op

De leden betalen per overschrijving, met vermelding van de gestructureerde mededeling. U
registreert elke ontvangen betaling; het bedrag is vooraf ingevuld met het totaal van het document,
en deelbetalingen worden aanvaard. De factuur krijgt de status “betaald” zodra het totaal bereikt
is, en facturen waarvan de vervaldatum verstreken is, verschijnen als achterstallig.

Elk lid vindt op zijn beurt zijn eigen documenten terug in de applicatie, met hun nummer, bedrag,
status en gestructureerde mededeling. De documenten van de andere leden ziet het niet.

{% include product-shot.html name="billing-member" alt="Overzicht “Mijn facturen” van een lid: een vergoedingsafrekening DP-2025-00001 met de status “Uitgereikt”, van 36,69 €, met haar “Gestructureerde mededeling” +++000/0000/00202+++." caption="Wat een lid ziet: zijn documenten en de gestructureerde mededeling die het bij zijn overschrijving vermeldt (testgegevens)." %}

## Wat het niet doet

**Brussel en Vlaanderen: gepland, nog niet beschikbaar.** De facturatiemodule is vandaag ontworpen
voor Waalse gemeenschappen, onder toezicht van de CWaPE. Het Vlaamse en het Brusselse kader zijn
gepland, maar nog niet geïmplementeerd. Wat op deze pagina staat, geldt dus nog niet voor een
gemeenschap in Vlaanderen of in Brussel.

**Alleen de gedeelde energie.** De factuur van de gemeenschap waardeert de gedeelde energie tegen
de interne prijs, exclusief netkosten en taksen. De energie die het delen niet heeft gedekt, wordt
nog altijd gefactureerd door de leverancier van elk lid, tegen zijn contracttarief.

**Geen inning.** OptimCE int niets en ontvangt geen enkele betaling: de leden betalen per
overschrijving op de rekening van de gemeenschap, en u registreert wat er is binnengekomen.

**Documenten in het Frans.** De pdf's worden in het Frans gegenereerd, ongeacht de taal van de
interface.

**Voorlopig één btw-tarief.** De module past vandaag een tarief van 21 % toe op alle documenten.
Gedifferentieerde tarieven, zoals het verlaagde tarief van 6 % op de elektriciteit van een gezin, en
de vrijstellingsregeling voor kleine ondernemingen worden nog niet ondersteund. De regeling van de
gemeenschap, btw-plichtig of niet en tegen welke tarieven per lid, legt u vast vóór de eerste
factuur met een boekhouder: onze gids over het factureren van gedeelde elektriciteit zet de gevallen
op een rij.

## Veelgestelde vragen {#faq}

### Waar komen de gegevens voor de facturatie vandaan?

Uit de verdeling die de netbeheerder doorstuurt: de gedeelde volumes per kwartier, die u importeert
voor de deelactie en de periode die u factureert. Bij de start van de cyclus bevriest OptimCE een
momentopname van die volumes; de bedragen worden berekend op die bevroren gegevens, die u kunt
natrekken.

### Kunt u verschillende prijzen toepassen naargelang het lid?

Ja. Elke prijs geldt voor de hele deelactie, voor een klantsegment (residentieel, professioneel,
industrieel) of voor één specifiek leveringspunt (EAN), met een geldigheidsperiode. Als meerdere
regels hetzelfde lid betreffen, wint de meest specifieke: de prijs van een EAN gaat voor op die van
zijn segment, en die gaat voor op de globale prijs.

### Hoe corrigeert u een factuur die al is uitgereikt?

Een uitgereikte factuur heeft een nummer gekregen in een doorlopende nummering: ze kan niet meer
worden gewijzigd of verwijderd. Om ze te corrigeren, reikt u een creditnota uit die haar annuleert,
en factureert u opnieuw. Zolang een document nog een ontwerp is, kunt u het daarentegen wel
verwijderen of herberekenen.

### Regelt OptimCE de btw?

Gedeeltelijk. De module berekent de btw, maar met één tarief van 21 % voor alle documenten: tarieven
die per lid verschillen en de vrijstellingsregeling voor kleine ondernemingen worden nog niet
ondersteund. De btw-regeling van de gemeenschap (btw-plichtig of niet, de tarieven voor elk lid)
legt u vóór de eerste factuur vast met een boekhouder.

## Verder lezen

- [Gedeelde elektriciteit factureren in België]({{ "invoice-shared-electricity" | ref_url }}):
  wie wat factureert, de btw en de verplichte vermeldingen.
- [Interne overdrachtsprijs in een gemeenschap]({{ "internal-price-shared-energy" | ref_url }}):
  hoe u een prijs bepaalt die u voor de algemene vergadering kunt verdedigen.
- [Facturatie in een energiegemeenschap]({{ "optimce-billing" | ref_url }}): de aankondiging van de
  module, met de details van de documenten en hun levenscyclus.

{% include product-cta.html page_key="billing" guide="billing-tarification-pay" title="Uw gemeenschap factureren met OptimCE" %}
