---
layout: post
title: "Automatische generatie van verdeelsleutels met OptimCE"
date: 2026-05-26 00:00:00 +0200
author: "OptimCE-team"
excerpt: "De module voor automatische verdeelsleutel-generatie van OptimCE is live. Hij stelt geoptimaliseerde verdeelsleutels voor op basis van de reële productie- en verbruiksdata van de gemeenschap, met twee algoritmes — brute force op standaardsleutels en LOGAAS, een onderzoeksresultaat van CeCoTePe uit het Locomotrice-project."
tags: [allocation-key, app, guide]
lang: nl
ref: optimce-allocation-key-generator
permalink: /nl/nieuws/2026/05/26/automatische-verdeelsleutel-generatie/
---

De **verdeelsleutel** kiezen die het meest haalt uit de lokale productie van een gemeenschap is moeilijker dan het lijkt. Het vocabulaire wordt door de regulator bepaald, de standaardsleutels staan in een document van CWaPE of Fluvius — en toch hangt de *juiste* keuze af van wat geen van die teksten u kan vertellen: de reële kwartierprofielen van uw leden. Een woonwijk met één school gedraagt zich heel anders dan een bedrijventerrein met basislast, en dezelfde sleutel kan in de ene gemeenschap 70 % van de beschikbare productie terugwinnen en in een andere amper 50 %.

De **module voor automatische generatie van verdeelsleutels** van OptimCE is nu beschikbaar om die beslissing uit het buikgevoel te halen. Geef hem een CSV met de reële productie- en verbruiksdata van de gemeenschap, en hij geeft een kandidaat-sleutel terug met een verwachte collectieve zelfverbruiksgraad — berekend op uw eigen data, niet op een handboekvoorbeeld. Vandaag worden twee **onafhankelijke** algoritmes uitgeleverd, die allebei dezelfde CSV verwerken: een **brute force** die de regionaal goedgekeurde standaardsleutels afzoekt, en **LOGAAS**, een hybride aanpak met lineaire optimalisatie en genetisch algoritme, ontwikkeld door [**CeCoTePe**](https://cecotepe.be/) voor het **Locomotrice**-project. Later kunnen meer algoritmes worden toegevoegd.

Als u het regelgevend landschap nog in kaart brengt — wat CWaPE, BRUGEL en VREG als geldige sleutel aanvaarden — begin dan met ons referentieartikel [„Verdeelsleutel in België: Wallonië, Brussel en Vlaanderen vergeleken"](/nl/nieuws/2026/05/19/verdeelsleutel-energiegemeenschap-belgie/).

## Waarom een verdeelsleutel datagedreven hoort te zijn

De Belgische kaders zijn het over één ding eens: de verdeelsleutel wordt **per kwartier** toegepast op de werkelijke meetgegevens van de slimme meters. Zijn prestatie — de **collectieve zelfverbruiksgraad**, het **aandeel van de geïnjecteerde energie dat daadwerkelijk door leden wordt verbruikt** — hangt dus volledig af van hoe het profiel van elk lid aansluit bij de productiecurve.

Een paar patronen verklaren waarom een handmatige keuze vaker onderpresteert dan men denkt:

- **De profieldiversiteit groeit snel.** Een gemeenschap die start met vijf gelijkaardige gezinnen laat zich goed bedienen met een egalitaire vaste sleutel. Voeg één tertiaire verbruiker toe (school, kmo, openbaar gebouw) en de egalitaire verdeling laat onmiddellijk volumes liggen tijdens kantooruren, terwijl de grote verbruiker ze had kunnen opnemen.
- **De productie verandert.** Een dakuitbreiding, een omvormer-upgrade, een nieuwe WKK-eenheid: elke wijziging verschuift de curve. De vorig jaar optimale sleutel kan vandaag suboptimaal zijn.
- **Standaardsleutels zijn niet inwisselbaar.** De drie Waalse families (egalitair vast, specifiek vast, dynamisch) dekken een breed scala af, maar welke van de drie voor een specifieke gemeenschap *het best* is, is zonder simulatie niet evident. Hetzelfde geldt voor de Brusselse methodes (vast, prorata, hybride) en de Vlaamse *verdeelsleutels* (vaste, relatieve, optimale).

Handmatige selectie maakt daardoor vaak onvoldoende gebruik van de beschikbare productie. Het punt van een automatische generatiemodule is niet het menselijk oordeel over governance te vervangen — het is de **simulatiekost** uit de keuze halen. Zodra een kandidaat is voorgesteld, kan de gemeenschap nog steeds stemmen, aanpassen en verfijnen.

## Wat de OptimCE-module doet

De module zit binnen de bestaande **module Verdeelsleutels** in de open-source kern van OptimCE. De workflow is rechttoe rechtaan:

1. **Input** — kwartierverbruiksdata per lid, kwartierproductiedata per producent, lijst van deelnemers aan de sharing-operatie en de regio (Wallonië / Brussel / Vlaanderen) zodat het algoritme de juiste standaardfamilies respecteert.
2. **Algoritme kiezen** — brute force of LOGAAS.
3. **Uitvoeren** — de module simuleert het gekozen algoritme op de reële data en geeft een **kandidaat-sleutel** terug, samen met de **verwachte collectieve zelfverbruiksgraad**, het **aandeel gedeelde energie per lid** en de **verdeling van de residuele injectie**.
4. **Beoordelen** — de gemeenschapsbeheerder kan kandidaten vergelijken, percentages aanpassen en valideren.
5. **Toepassen** — de gevalideerde sleutel komt als een nieuw addendum in de module Verdeelsleutels, met volledige historiek en opvolging van de aanvaardingsstatus van de leden.

De module duwt **geen** nieuwe sleutel autonoom naar de DSO. Hij produceert een voorstel; de bestaande workflow — addendum, handtekeningen, transmissie — blijft van kracht, inclusief de regulatorgoedkeuring voor niet-standaardsleutels in Wallonië.

## Algoritme 1 — Brute force op standaardsleutels

Het eerste algoritme is bewust eenvoudig, en precies dat is zijn kracht.

Het bouwt een **kandidaatset** op uit alle standaardsleutels die in de regio van de gemeenschap zijn toegestaan:

- In **Wallonië**: egalitaire vaste sleutel, specifieke vaste sleutel (percentages gewogen naar de inbreng van leden), dynamische sleutel op basis van verbruik.
- In **Brussel**: vaste methode (single-round en multi-round), prorata-methode, hybride methode.
- In **Vlaanderen**: *vaste verdeelsleutel*, *relatieve verdeelsleutel*, *optimale verdeelsleutel*.

Voor elke kandidaat **herspeelt het algoritme de reële kwartierdata** van de gemeenschap door de overeenkomstige verdelingsregel en berekent het de resulterende collectieve zelfverbruiksgraad, het aandeel dat elk lid zou hebben ontvangen en de residuele injectie. De best presterende kandidaat — standaard de hoogste collectieve zelfverbruiksgraad — wint, en de module geeft de eerstvolgenden terug, zodat de gemeenschap desgewenst enkele procentpunten prestatie kan ruilen tegen eenvoudiger governance.

De brute-force-aanpak heeft twee grote voordelen:

- **Regulatorconform door constructie.** De output is altijd één van de standaardsleutels, dus hij volgt het gewone DSO-aanvaardingsspoor — geen extra CWaPE-toestemming in Wallonië nodig.
- **Verklaarbaar.** Het resultaat is een gekende sleutelfamilie met gekende eigenschappen. U kunt het verdedigen voor een algemene vergadering zonder optimalisatietheorie te moeten oproepen.

De beperking is de catalogus zelf. Als de profielen van een gemeenschap atypisch zijn — sterk asymmetrisch, sterk seizoensgebonden, met één dominante verbruiker — kan de beste standaardsleutel nog steeds merkbare prestaties laten liggen. Daar komt het tweede algoritme tussen.

## Algoritme 2 — LOGAAS

**LOGAAS** staat voor *Linear Optimization with Genetic Algorithm with Atypical Speciation*. Het is het resultaat van onderzoek van [CeCoTePe](https://cecotepe.be/) voor het Locomotrice-project, formeel beschreven in de preprint *Paque, E. & Hiard, S. (2025), „LOGAAS: A hybrid algorithmic approach to ex-post electricity allocation for energy communities"*.

Waar brute force begrensd is door de standaardcatalogus, doorzoekt LOGAAS een **bredere ruimte van kandidaat-sleutels** — inclusief niet-standaard combinaties — door **lineaire optimalisatie** (vindt de beste ex-post allocatie voor één iteratie) te combineren met een **genetisch algoritme** met **atypische soortvorming** (vindt de beste combinatie van percentages over de maximaal drie toegestane iteraties en behoudt daarbij de diversiteit van de populatie). Praktisch betekent dat: hij kan extra prestaties uit cases halen waar de standaardfamilies niet zuiver bij de profielen passen — sterk heterogene ledengroepen, seizoensgebonden industriële verbruikers samen met gezinnen, of grote overschotsproducenten die anders het grootste deel van hun productie naar het openbaar net zouden terugsturen.

LOGAAS levert een **niet-standaard kandidaat-sleutel** op. In Wallonië betekent dat dat de gemeenschap het **CWaPE-toestemmingsspoor** doorloopt voordat de DSO hem kan toepassen — zie het [artikel over de verdeelsleutel in België](/nl/nieuws/2026/05/19/verdeelsleutel-energiegemeenschap-belgie/) voor de procedure. In Brussel en Vlaanderen is de ruimte voor niet-standaardsleutels kleiner; daar wordt de LOGAAS-output meestal gebruikt als **prestatie-referentie** — hoe zou de best haalbare prestatie eruitzien — waartegen de gekozen standaardsleutel wordt afgewogen.

Gebruik LOGAAS wanneer het brute-force-resultaat dichtbij is maar niet voldoende, wanneer de projecteconomie afhangt van de laatste procentpunten collectief zelfverbruik, of wanneer u een gekwantificeerde bovengrens wilt om een investeringsbeslissing te onderbouwen.

## Vergelijking in één oogopslag

| Criterium | Handmatige keuze | Brute force | LOGAAS |
|---|---|---|---|
| Vereiste data | Ledenlijst, regionaal kader | Ledenlijst + 15-min profielen | Ledenlijst + 15-min profielen |
| Zoekruimte | Eén vooraf gekozen sleutel | Alle regionale standaardsleutels | Standaard + niet-standaard combinaties |
| Looptijd | Onmiddellijk (geen berekening) | Seconden | Minuten |
| Regulatorconform uit de doos | Ja (indien standaard) | Ja — altijd binnen de standaardcatalogus | Wallonië: CWaPE-toestemming nodig. Brussel / Vlaanderen: meestal als referentie. |
| Verklaarbaarheid van het resultaat | Hoog | Hoog — benoemde sleutelfamilie | Lager — numeriek resultaat |
| Geschikt voor | Homogene gemeenschap, governance-georiënteerde projecten | De meeste projecten — nieuwe standaardkeuze | Heterogene profielen, prestatiekritische projecten |

De twee algoritmes zijn **twee onafhankelijke manieren** om een sleutel te genereren uit dezelfde CSV — geen pipeline-stappen. Brute force is de veilige standaardkeuze voor de meeste projecten; LOGAAS is de optie wanneer de standaardcatalogus prestaties laat liggen en een niet-standaardsleutel bespreekbaar is.

## Hoe de module gebruiken

De module is vandaag beschikbaar in de OptimCE-toepassing:

1. Open de module **Verdeelsleutels** voor de sharing-operatie die u wilt optimaliseren.
2. Klik op **Genereer een sleutel**. Upload een CSV met de kwartierverbruiksdata (per lid) en kwartierproductiedata (per producent).
3. Kies een algoritme — brute force of LOGAAS. Beide draaien onafhankelijk op dezelfde CSV; u kunt hun resultaten naast elkaar vergelijken.
4. Start. Bekijk de kandidaat-sleutel, de verwachte collectieve zelfverbruiksgraad en de tabel met aandelen per lid.
5. Valideer de kandidaat om de addendumworkflow te starten: leden ondertekenen, de vertegenwoordiger bezorgt aan de DSO, en de nieuwe sleutel treedt in werking op de afgesproken datum.

De volledige cyclus, van data-upload tot addendum, leeft binnen OptimCE — geen gegoochel meer tussen simulatie-spreadsheets, governance en rapportering.

## Wat komt er nu?

De module is opgebouwd rond een pluggable algoritme-interface, zodat nieuwe benaderingen kunnen worden toegevoegd zonder aan de kern te raken. Plausibele volgende toevoegingen: **multi-objective optimalisatie** (collectief zelfverbruik tegenover billijkheid per lid), **billijkheidsbeperkte varianten** (de kloof tussen best en slechtst bediende leden begrenzen) en **scenario-gebaseerde simulatie** (een sleutel testen tegen verwachte ledenverloop of productiegroei). Elke toevoeging wordt aangekondigd bij uitlevering.

> ### Genereer uw verdeelsleutel met OptimCE
>
> Een open-source platform gebouwd voor Belgische energiegemeenschappen: datagedreven sleutelgeneratie, historiek van sharing-operaties, opvolging van ledenaanvaarding en voorbereiding van regulatorrapportering — alles in één toepassing.
>
> **[Aan de slag op app.optimce.be →](https://app.optimce.be)**

## FAQ — Automatische generatie van verdeelsleutels

### Welke data heeft de module nodig?

**Verbruiksdata** per lid per kwartier, **productiedata** per producent per kwartier, de deelnemerslijst en de regio. Enkele weken data volstaan voor een bruikbaar signaal; een volledig jaar legt seizoenseffecten betrouwbaarder vast.

### Welk algoritme moet ik kiezen?

Standaard **brute force**: snel, volledig verklaarbaar en blijft binnen de standaardcatalogus die automatisch door de DSO wordt aanvaard. Kies **LOGAAS** wanneer u doelbewust verder dan de standaardcatalogus wilt kijken — heterogene profielen, krappe projecteconomie, of de wens te weten hoeveel prestatie de standaardcatalogus laat liggen. Beide draaien onafhankelijk op dezelfde CSV; niets weerhoudt u om ze allebei te draaien en te vergelijken.

### Zal de gegenereerde sleutel regulatorconform zijn?

De brute-force-output is altijd één van de regionale standaardsleutels — rechtstreeks aanvaard door de DSO, zonder extra toestemming. De LOGAAS-output is een niet-standaardsleutel; in Wallonië gaat hij via het **CWaPE-toestemmingsspoor** voordat de DSO hem toepast. In Brussel en Vlaanderen zijn niet-standaardsleutels niet de gebruikelijke weg; daar wordt de LOGAAS-output meestal als prestatie-referentie gebruikt.

### Kan ik het voorstel aanpassen voordat ik het toepas?

Ja. De module geeft een **kandidaat** terug — geen bindende beslissing. U kunt percentages aanpassen, van sleutelfamilie wisselen, of de keuze van het algoritme volledig overrulen voordat u de sleutel doorduwt naar de addendumworkflow.

### Vervangt de module het oordeel van een expert?

Neen. De module kwantificeert de afwegingen; hij beslist niet of uw gemeenschap eerlijkheid boven prestatie, voorspelbaarheid boven optimalisatie of eenvoud boven het laatste procentpunt zelfverbruik plaatst. Dat zijn governance-vragen. De module verkort de technische lus zodat de vergadering haar tijd aan de governance-vraag kan besteden in plaats van aan de berekening.

### Hoe vaak moet ik het algoritme opnieuw draaien?

Een goed ritme is **jaarlijks**, idealiter vóór de algemene vergadering die de addenda van de sharing-operatie goedkeurt. Draai eerder opnieuw wanneer de gemeenschap groeit, een producent wordt toegevoegd of verwijderd, of een lid zijn verbruiksprofiel significant verandert (installatie van een warmtepomp, verkoop van een industriële site…).

## Belangrijkste inzichten

De module voor automatische generatie maakt van de verdeelsleutelkeuze een datagedreven beslissing in plaats van een handboekoefening. **Brute force** vindt de beste standaardsleutel voor de reële profielen van de gemeenschap — snel, verklaarbaar, regulatorconform. **LOGAAS** verkent verder dan de standaardcatalogus wanneer de projecteconomie elke procentpunt nodig heeft. Samen geven ze gemeenschapsbeheerders een instrument om hun sleutelkeuze te verdedigen voor de algemene vergadering, de DSO en de regulator — onderbouwd door cijfers uit de eigen data van de gemeenschap.

Om verder te gaan, lees onze begeleidende gidsen:

> **[Verdeelsleutel in België: Wallonië, Brussel en Vlaanderen vergeleken](/nl/nieuws/2026/05/19/verdeelsleutel-energiegemeenschap-belgie/)**
>
> De regulatoire primer — wat CWaPE, BRUGEL en VREG aanvaarden, de drie regionale vocabulaires en hoe u een sleutelfamilie kiest voordat u OptimCE erbinnen laat optimaliseren.

> **[Hoe een energiegemeenschap oprichten in Wallonië: stapsgewijze gids](/nl/nieuws/2026/05/11/energiegemeenschap-oprichten-wallonie/)**
>
> Het project kaderen, kiezen tussen CER en CEC, de CWaPE op de hoogte brengen en de sharing lanceren — en waar de verdeelsleutel in het dossier past.

> **[Hoe aansluiten bij een energiegemeenschap in Wallonië: praktische gids](/nl/nieuws/2026/05/11/energiegemeenschap-aansluiten-wallonie/)**
>
> Waar een open operatie vinden, aansluitstappen en controlepunten voor het ondertekenen van de sharingovereenkomst.

## Bronnen

- Paque, E. & Hiard, S. (2025). *LOGAAS: A hybrid algorithmic approach to ex-post electricity allocation for energy communities*. CeCoTePe preprint — formele beschrijving van het algoritme, zijn objectieffunctie en simulatieresultaten op synthetische data van energiegemeenschappen.
- [CeCoTePe](https://cecotepe.be/) — onderzoekscentrum achter het LOGAAS-algoritme, partner in het Locomotrice-project.
- [CWaPE — Lijst van standaard verdeelsleutels](https://www.cwape.be/publications/document/5382) — voorstel CD-23d27-CWaPE-0928 van 27 april 2023, canonieke lijst van Waalse standaardsleutels.
- [Sibelga — Verdelingsmethodes voor energiedelen](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methodes-de-repartition) — vaste, prorata en hybride methodes in Brussel.
- [Fluvius — Protocol energiedelen, persoon-aan-persoonverkoop](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf) — Vlaams technisch protocol (v3.x, juli 2024).
