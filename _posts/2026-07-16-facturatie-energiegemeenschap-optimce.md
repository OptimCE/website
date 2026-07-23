---
layout: post
title: "Facturatie in een energiegemeenschap: OptimCE genereert uw facturen"
date: 2026-07-16 10:00:00 +0200
author: "OptimCE-team"
excerpt: "Nieuwe OptimCE-functie: genereer automatisch de facturen van uw energiegemeenschap, van de prijs per kWh tot de pdf en de opvolging van de betalingen."
tags: [administrative, app, news]
lang: nl
ref: optimce-billing
last_modified_at: 2026-07-23 10:00:00 +0200
permalink: /nl/nieuws/2026/07/16/facturatie-energiegemeenschap-optimce/
faq:
  - q: "Waar komen de gegevens voor de facturatie vandaan?"
    a: "Uit de officiële verdelingsdata die de netbeheerder aanlevert en die al in OptimCE geïmporteerd zijn: verbruikte gedeelde energie en gedeelde injectie, per EAN en per periode. Bij het starten van een facturatiecyclus bevriest OptimCE een momentopname van die volumes: de bedragen worden berekend op bevroren, traceerbare data."
  - q: "Wie bepaalt de prijzen van de gedeelde energie?"
    a: "De gemeenschap zelf. U definieert vrij twee prijzen in €/kWh: de verkoopprijs van de gedeelde energie aan de verbruikers en de terugkoopprijs die aan de producenten wordt betaald voor hun injectie. Elke prijs kan globaal gelden, per klantsegment (residentieel, professioneel, industrieel) of voor één EAN, met een geldigheidsperiode — de meest specifieke regel wint."
  - q: "Welke documenten genereert OptimCE?"
    a: "Drie documenten, elk met een eigen nummerreeks: de factuur (F-…) voor de gedeelde energie die een lid verbruikte, de creditnota (NC-…) om een uitgereikte factuur te corrigeren, en de vergoedingsafrekening (DP-…) voor de gedeelde injectie van een producent. Alle worden als pdf gegenereerd; ontwerpen dragen een watermerk 'proforma'."
  - q: "Wat dekt de factuur van een energiegemeenschap?"
    a: "Alleen de gedeelde energie, gewaardeerd tegen de interne prijs van de gemeenschap, exclusief netkosten en taksen. De residuele energie — wat het delen niet dekte — wordt nog altijd door de leverancier van elk lid gefactureerd tegen zijn contracttarief."
  - q: "Kan een uitgereikte factuur gecorrigeerd worden?"
    a: "Niet rechtstreeks: eenmaal uitgereikt krijgt een factuur een wettelijk nummer in een doorlopende reeks zonder gaten en kan ze niet meer gewijzigd of verwijderd worden. Om te corrigeren reikt u een creditnota uit die haar annuleert, en factureert u opnieuw. Een ontwerp daarentegen kan vrij verwijderd of herberekend worden."
  - q: "Hoe krijgen de leden toegang tot hun facturen?"
    a: "Elk lid vindt zijn eigen facturen in de applicatie en downloadt de pdf wanneer hij wil. Aan beheerderskant is de betalingsopvolging ingebouwd: u registreert betalingen — ook gedeeltelijke —, de factuur springt automatisch op 'betaald' en achterstallige facturen worden na de vervaldatum gemarkeerd."
---

Een werkende energiegemeenschap produceert twee dingen: gedeelde kWh … en bedragen om te factureren. Elke periode wijst de officiële verdeling elk lid zijn aandeel van de lokaal geproduceerde energie toe — en dan moet iemand die volumes omzetten in euro's: berekenen wat elke verbruiker verschuldigd is en wat elke producent ontvangt, conforme documenten opstellen, betalingen innen en opvolgen. Tot nu toe gebeurde dat werk meestal met de hand, tussen een rekenblad en een zelfgemaakt factuursjabloon. Dat is voorbij: OptimCE bevat voortaan een **facturatiemodule**, waarvan de eerste versie operationeel is.

Het principe is eenvoudig: u legt uw prijzen vast, u kiest een periode, en OptimCE **genereert de facturen van alle leden** op basis van de verdelingsdata die al in het platform zitten — met pdf, wettelijke nummering, gestructureerde mededeling en opvolging van de betalingen.

Is de mechaniek van de verdeling nog onduidelijk voor u, begin dan met ons referentieartikel [„Verdeelsleutel in België: Wallonië, Brussel, Vlaanderen"](/nl/nieuws/2026/05/19/verdeelsleutel-energiegemeenschap-belgie/) — de facturatie is er het rechtstreekse vervolg van.

## Waarom de interne facturatie de kritieke schakel is

Bij energiedelen rekent en bezorgt de netbeheerder, maar **hij factureert niet**: hij past de verdeelsleutel kwartier per kwartier toe en deelt de volumes mee. De waardering van die volumes — tegen welke prijs de verbruiker de gedeelde energie betaalt, tegen welke prijs de producent voor zijn injectie wordt vergoed — is de zaak van de gemeenschap zelf.

Concreet komt die last op de schouders van de beheerder van de gemeenschap terecht. Voor elke periode moet u:

- **de exacte volumes** per aansluitingspunt (EAN) overnemen;
- **de juiste prijs** op elk profiel toepassen, zonder reken- of afrondingsfouten;
- **een conform document** opstellen: [btw, verplichte vermeldingen](/nl/nieuws/2026/07/23/gedeelde-elektriciteit-factureren-belgie/), doorlopende nummering;
- **een betalingsreferentie** toevoegen en de binnenkomende overschrijvingen afpunten;
- **de vragen van de leden** over hun afrekening beantwoorden.

Met tien leden is dat vervelend; met vijftig onhoudbaar. En de inzet gaat verder dan administratie: een heldere, regelmatige facturatie is de eerste voorwaarde voor het **vertrouwen van de leden** — zij maakt het economische voordeel van het delen zwart op wit zichtbaar. We schreven het al in onze [gids voor het oprichten van een energiegemeenschap in Wallonië](/nl/nieuws/2026/05/11/energiegemeenschap-oprichten-wallonie/): het is in de uitbatingsfase dat een beheertool onmisbaar wordt.

## Hoe het werkt: van gedeeld volume tot factuur

De module is geïntegreerd met de rest van het platform en volgt een traject in vier stappen.

1. **De data zijn er al.** De facturatie steunt op de officiële verdelingsdata die al in OptimCE geïmporteerd zijn: verbruikte gedeelde energie en gedeelde injectie, per EAN en per periode. Niets opnieuw invoeren, niets exporteren — de facturatie leest dezelfde volumes als uw dashboards.
2. **U definieert uw prijzen.** Twee prijzen, in €/kWh, vrij bepaald door de gemeenschap: de **verkoopprijs** van de gedeelde energie aan de verbruikers en de **terugkoopprijs** die aan de producenten wordt betaald voor hun injectie. Elke prijs kan globaal gelden, per klantsegment (residentieel, professioneel, industrieel) of voor één specifieke EAN — de meest specifieke regel wint — en draagt een geldigheidsperiode. Welke bedragen u invult, is een andere vraag: onze gids [« Prijs van elektriciteit in een energiegemeenschap: de interne overdrachtsprijs bepalen »](/nl/nieuws/2026/07/20/prijs-elektriciteit-energiegemeenschap/) beschrijft de verdedigbare marge en vijf rekenmethodes.
3. **U start een facturatiecyclus.** U kiest de periode — maandelijks, driemaandelijks, zoals het u past — en OptimCE controleert vóór de berekening of alles in orde is: verbruiksdata aanwezig, bankgegevens en officiële naam van de gemeenschap, toepasselijk tarief, geen dubbels in de data. Daarna **bevriest het een momentopname** van de verdeling: de bedragen worden berekend op bevroren, traceerbare volumes.
4. **U leest na, dan reikt u uit.** De cyclus produceert een **ontwerp per lid**, te downloaden als pdf met watermerk „proforma". U controleert, dan reikt u uit: de factuur krijgt haar wettelijk nummer, haar gestructureerde mededeling en haar vervaldatum.

Samengevat — dit geeft u op en dit krijgt u:

| U definieert | OptimCE genereert |
|---|---|
| De verkoopprijs voor verbruikers (€/kWh) | Eén factuur per verbruikend lid |
| De terugkoopprijs voor producenten (€/kWh) | Eén vergoedingsafrekening per producent |
| De te factureren periode | De totalen exclusief btw, de btw en het te betalen bedrag |
| | De verzendklare pdf met IBAN en gestructureerde mededeling |

## Drie documenten, een nummering zonder gaten

De module onderscheidt drie documenten, elk met een eigen reeks:

| Document | Reeks | Rol |
|---|---|---|
| **Factuur** | F-2026-00001 | De gedeelde energie die een lid verbruikte, tegen de interne prijs |
| **Creditnota** | NC-2026-00001 | De correctie van een al uitgereikte factuur |
| **Vergoedingsafrekening** | DP-2026-00001 | De gedeelde injectie van een producent, tegen de terugkoopprijs |

Elk document detailleert, regel per regel en EAN per EAN, de kWh vermenigvuldigd met de eenheidsprijs, daarna het totaal exclusief btw, de btw en het te betalen bedrag. U vindt er de uitreiker (de gemeenschap, als vertegenwoordiger van het delen), de bestemmeling, de IBAN van de gemeenschap, een Belgische **gestructureerde mededeling** om overschrijvingen ondubbelzinnig af te punten, de uitreikings- en vervaldatum, en de wettelijke vermeldingen — waaronder de precisering dat de factuur de gedeelde energie dekt **exclusief netkosten en taksen**.

Een lid dat tegelijk verbruikt en produceert, ontvangt twee afzonderlijke documenten: zijn factuur voor gedeelde energie en zijn vergoedingsafrekening.

De nummering is **doorlopend en zonder gaten**, zoals de facturatieregels vereisen: een uitgereikte factuur kan niet meer gewijzigd of verwijderd worden. Een fout? U reikt een **creditnota** uit die haar annuleert, en factureert daarna correct opnieuw — de historiek blijft intact en controleerbaar.

## Van ontwerp tot betaling: de levenscyclus

Elke factuur volgt een expliciete levenscyclus, in één oogopslag zichtbaar:

| Status | Wat het betekent |
|---|---|
| **Ontwerp** | Berekend voorstel, aanpasbaar en verwijderbaar — proforma-pdf met watermerk |
| **Uitgereikt** | Wettelijk nummer toegekend, definitief document, vervaldatum vastgelegd |
| **Verzonden** | Aan het lid bezorgd |
| **Betaald** | Betalingen geregistreerd tot het volledige bedrag |
| **Achterstallig** | Vervaldatum overschreden zonder volledige betaling |

De betalingsopvolging is ingebouwd: u registreert elke overschrijving — ook **gedeeltelijke betalingen** — en de factuur springt automatisch op „betaald" zodra het volledige bedrag bereikt is. Facturen waarvan de vervaldatum verstreken is, worden als **achterstallig** gemarkeerd, zodat u herinneringen gericht kunt versturen zonder rekeninguittreksels uit te pluizen.

## Aan ledenkant: transparantie via het document

Elk lid vindt **zijn eigen facturen** in de applicatie en downloadt de pdf wanneer hij wil. Niet langer wachten op een e-mail van de beheerder of vragen om een overzicht: het referentiedocument staat voor iedereen op dezelfde plaats klaar.

Even het toepassingsgebied in herinnering brengen: de factuur van de gemeenschap dekt de **gedeelde energie**, gewaardeerd tegen de interne prijs. De residuele energie — wat het delen niet dekte — wordt nog altijd door de leverancier van elk lid gefactureerd, tegen zijn contracttarief. Het zijn de twee documenten samen die het verhaal van de besparing vertellen; ons artikel over [het verlagen van de elektriciteitsfactuur dankzij energiedelen](/nl/nieuws/2026/06/03/energiegemeenschap-elektriciteitsfactuur-verlagen/) legt dat mechanisme uit.

## Een eerste versie op maat van Wallonië — en wat volgt

Deze eerste versie is ontworpen voor het **Waalse kader** (CWaPE): aangepaste wettelijke vermeldingen en automatische toepassing van de btw op de facturen. De documenten worden in het Frans gegenereerd; de generatieketen is al klaar voor meertaligheid, die zal volgen.

Op het programma van de volgende versies: de **automatische verzending van facturen per e-mail**, de ondersteuning van het **Vlaamse en Brusselse kader**, en rijkere tariefstructuren. Trouw aan de aanpak van OptimCE: vroeg leveren, op het terrein bewijzen, itereren met de gemeenschappen.

De module is nu beschikbaar op [app.optimce.be](https://app.optimce.be) — gratis, zoals het hele platform tijdens de alfafase.

## Conclusie

Met de facturatie sluit OptimCE de lus: import van de data, [keuze en simulatie van de verdeelsleutel](/nl/nieuws/2026/06/09/verdeelsleutel-simuleren-optimce/), deelacties, en voortaan de facturen — de laatste stap die elk kwartaal nog in een rekenbladkarwei veranderde. Volumes worden conforme documenten, betalingen volgt u in één oogopslag op, en elk lid ziet duidelijk wat het delen hem oplevert.

> ### Factureer uw energiegemeenschap met OptimCE
>
> Opensourceplatform gebouwd voor Belgische energiegemeenschappen: importeer uw verdelingsdata, definieer uw prijzen, genereer facturen en afrekeningen als pdf en volg de betalingen op — alles in één applicatie.
>
> **[Aan de slag op app.optimce.be →](https://app.optimce.be)**

## FAQ

### Waar komen de gegevens voor de facturatie vandaan?

Uit de officiële verdelingsdata die de netbeheerder aanlevert en die **al in OptimCE geïmporteerd** zijn: verbruikte gedeelde energie en gedeelde injectie, per EAN en per periode. Bij het starten van een facturatiecyclus bevriest OptimCE een momentopname van die volumes: de bedragen worden berekend op bevroren, traceerbare data.

### Wie bepaalt de prijzen van de gedeelde energie?

**De gemeenschap zelf.** U definieert vrij twee prijzen in €/kWh: de verkoopprijs van de gedeelde energie aan de verbruikers en de terugkoopprijs die aan de producenten wordt betaald voor hun injectie. Elke prijs kan globaal gelden, per klantsegment (residentieel, professioneel, industrieel) of voor één EAN, met een geldigheidsperiode — de meest specifieke regel wint.

### Welke documenten genereert OptimCE?

Drie documenten, elk met een eigen nummerreeks: de **factuur** (F-…) voor de gedeelde energie die een lid verbruikte, de **creditnota** (NC-…) om een uitgereikte factuur te corrigeren, en de **vergoedingsafrekening** (DP-…) voor de gedeelde injectie van een producent. Alle worden als pdf gegenereerd; ontwerpen dragen een watermerk „proforma".

### Wat dekt de factuur van een energiegemeenschap?

Alleen de **gedeelde energie**, gewaardeerd tegen de interne prijs van de gemeenschap, exclusief netkosten en taksen. De residuele energie — wat het delen niet dekte — wordt nog altijd door de leverancier van elk lid gefactureerd tegen zijn contracttarief.

### Kan een uitgereikte factuur gecorrigeerd worden?

Niet rechtstreeks: eenmaal uitgereikt krijgt een factuur een wettelijk nummer in een **doorlopende reeks zonder gaten** en kan ze niet meer gewijzigd of verwijderd worden. Om te corrigeren reikt u een **creditnota** uit die haar annuleert, en factureert u opnieuw. Een ontwerp daarentegen kan vrij verwijderd of herberekend worden.

### Hoe krijgen de leden toegang tot hun facturen?

Elk lid vindt **zijn eigen facturen** in de applicatie en downloadt de pdf wanneer hij wil. Aan beheerderskant is de betalingsopvolging ingebouwd: u registreert betalingen — ook gedeeltelijke —, de factuur springt automatisch op „betaald" en achterstallige facturen worden na de vervaldatum gemarkeerd.

## Bronnen

- [CWaPE — Energiegemeenschappen](https://www.cwape.be/node/158) — het Waalse kader voor energiegemeenschappen: types, rechtsgrondslagen, melding en jaarlijkse rapportering.
- [CWaPE — Energiegemeenschappen en energiedelen](https://www.cwape.be/secteur/communautes-partage-energie) — het algemene Waalse kader van het energiedelen.
- [FOD Financiën — Btw](https://finances.belgium.be/fr/entreprises/tva) — facturatie-, boekhoud- en btw-verplichtingen voor Belgische ondernemingen en rechtspersonen.
- [Pricing and sharing rules for energy communities](https://econpapers.repec.org/article/eeejuipol/v_3a96_3ay_3a2025_3ai_3ac_3as0957178725001109.htm) — onderzoek naar deelregels en interne prijszetting in energiegemeenschappen.
