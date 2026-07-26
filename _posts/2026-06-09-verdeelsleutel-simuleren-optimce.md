---
layout: post
title: "Verdeelsleutel simuleren: test uw scenario's"
date: 2026-06-09 10:00:00 +0200
author: "OptimCE-team"
excerpt: "Nieuwe OptimCE-functie: simuleer een verdeelsleutel op uw data en meet zelfverbruik, surplus, zelfvoorziening en deelgraad voor uw gemeenschap."
description: "Simuleer een sleutel op uw eigen data en meet zelfverbruik, surplus, zelfvoorziening en deelgraad voordat u hem vastlegt."
tags: [allocation-key, app, news]
lang: nl
ref: optimce-allocation-key-simulation
permalink: /nl/nieuws/2026/06/09/verdeelsleutel-simuleren-optimce/
faq:
  - q: "Wat betekent het om een verdeelsleutel te simuleren?"
    a: "Het betekent reële productie- en verbruiksdata door een gekozen verdeelsleutel spelen, zonder die in productie toe te passen, om de indicatoren vooraf te meten: collectief zelfverbruik, surplus, zelfvoorzieningsgraad en deelgraad. Het is een 'wat-als'-test voordat u beslist."
  - q: "Wat is het verschil tussen een verdeelsleutel simuleren en genereren?"
    a: "Automatische generatie stelt de beste sleutel voor op basis van uw data (brute force op standaardsleutels of het LOGAAS-algoritme). Simulatie test een sleutel die u zelf hebt gekozen op een bepaalde dataset en toont de indicatoren ervan. Beide vullen elkaar aan: u genereert om een goede kandidaat te vinden en u simuleert om scenario's te begrijpen en te vergelijken."
  - q: "Wat is het verschil tussen zelfverbruiksgraad, zelfvoorzieningsgraad en deelgraad?"
    a: "De zelfverbruiksgraad wordt aan de productiezijde gemeten: het aandeel van de lokaal geproduceerde energie dat door de leden wordt verbruikt. De zelfvoorzieningsgraad wordt aan de verbruikszijde gemeten: het aandeel van het verbruik van de leden dat door lokale productie wordt gedekt. De deelgraad toont hoeveel van de injectie via de sleutel effectief onder de leden werd verdeeld."
  - q: "Wat betekenen de resultaten 'per iteratie'?"
    a: "Veel sleutels verdelen energie in meerdere rondes (iteraties): een eerste ronde verdeelt volgens de regel, daarna wordt de niet-verbruikte energie in de volgende ronde herverdeeld. De simulatie toont het resultaat globaal, per tijdstap en per iteratie, zodat u ziet hoe het delen ronde na ronde vordert."
  - q: "Welke data moet ik importeren om een simulatie te starten?"
    a: "Een CSV-bestand met het verbruik per tijdstap (vaak per kwartier) van elk lid en de productie van elke producent van de deeloperatie. Elke regel komt overeen met één tijdstap. Enkele weken data geven al een bruikbaar signaal; een volledig jaar vat de seizoensgebondenheid beter."
  - q: "Verandert de simulatie mijn verdeelsleutel in productie?"
    a: "Nee. De simulatie is een berekening 'buiten productie': ze raakt noch aan de sleutel die de netbeheerder toepast, noch aan uw reële data. U test zoveel scenario's als u wilt zonder enig effect op de lopende deeloperatie."
---

Een **verdeelsleutel** kiezen betekent kwartier per kwartier beslissen wie welk aandeel van de lokaal geproduceerde energie ontvangt. Maar hoe weet u, *voordat* u die invoert, of een bepaalde sleutel het zelfverbruik van uw gemeenschap echt zal verbeteren — of productie naar het net laat wegvloeien? De nieuwe functie van OptimCE beantwoordt net die vraag: **een verdeelsleutel simuleren** op uw eigen data en de prestatie-indicatoren meteen aflezen.

Het idee is eenvoudig: u importeert een dataset, u kiest een sleutel, en de simulatie speelt elke tijdstap door die sleutel om u het **zelfverbruik**, het **surplus**, de **zelfvoorzieningsgraad** en de **deelgraad** terug te geven — globaal, per tijdstap en per iteratie. U test een scenario zonder het toe te passen, zonder risico, en u beslist op basis van cijfers in plaats van buikgevoel.

Is het begrip verdeelsleutel nieuw voor u, begin dan met ons referentieartikel [“Verdeelsleutel in België: de 3 regio's”](/nl/nieuws/2026/05/19/verdeelsleutel-energiegemeenschap-belgie/) — het zet het vocabulaire uiteen dat hier wordt gebruikt.

## Waarom een verdeelsleutel simuleren?

Een verdeelsleutel is niet neutraal: afhankelijk van de verbruiks- en productieprofielen van de gemeenschap kan **dezelfde sleutel in het ene project veel waarde creëren en in het andere vernietigen**. Een vaste egalitaire sleutel is perfect voor tien huishoudens met vergelijkbare profielen, maar laat volumes ongebruikt zodra een grote verbruiker — een school, een kmo, een openbaar gebouw — toetreedt. Een dynamische sleutel daarentegen recupereert die verloren productie, ten koste van een aandeel dat van maand tot maand varieert.

Het probleem is dat **op buikgevoel beslissen riskant is**. Productiecurves van zonne-energie en verbruiksprofielen kruisen elkaar op niet-triviale wijze op de 15-minutenstap; met het blote oog is het onmogelijk te voorspellen of sleutel A het over een volledig jaar van sleutel B wint. En de inzet is concreet: elk punt zelfverbruik dat u wint, is surplus dat niet langer tegen een lage prijs wordt geïnjecteerd, dus meer waarde die in de gemeenschap blijft.

Simuleren betekent net **die beslissing uit het buikgevoel halen**. U meet het reële effect van een sleutel op de indicatoren die ertoe doen — zelfverbruik, surplus, zelfvoorziening, deelgraad — voordat u zich tot iets verbindt. Om te begrijpen waarom die indicatoren centraal staan in de waarde van een gemeenschap, zie ons artikel [“Zelfverbruik van energie in België”](/nl/nieuws/2026/06/05/zelfverbruik-energie-belgie/).

## Wat de simulatie mogelijk maakt

De functie is ingebouwd in de **module "Verdeelsleutels"** van de open-source kern van OptimCE. De gebruikersflow telt slechts enkele stappen:

1. **Importeer een CSV** met verbruiksdata per tijdstap (vaak per kwartier) voor elk lid en productiedata voor elke producent van de deeloperatie. Elke regel van het bestand komt overeen met één tijdstap.
2. **Kies een verdeelsleutel** om te testen — een standaardsleutel voor uw regio, een bestaande sleutel van de gemeenschap, of een scenario dat u wilt verkennen.
3. **Start de simulatie.** OptimCE speelt elke tijdstap door de sleutel en zijn verschillende iteraties en aggregeert vervolgens de resultaten.
4. **Lees de indicatoren** die worden teruggegeven, op drie niveaus van granulariteit: **globaal** (over de hele periode), **per tijdstap** (kwartier per kwartier) en **per iteratie** (ronde na ronde van de verdeling).

Hier ziet u in één oogopslag wat u aanlevert en wat u krijgt:

| U importeert | U krijgt |
|---|---|
| Verbruik per tijdstap, per lid | Gesimuleerde collectieve zelfverbruiksgraad |
| Productie per tijdstap, per producent | Gesimuleerd surplus (geïnjecteerde, niet-gedeelde energie) |
| De te testen verdeelsleutel | Zelfvoorzieningsgraad en deelgraad |
| | Detail: globaal, per tijdstap en per iteratie |

Het resultaat is geen theoretische schatting uit een handboekvoorbeeld: het wordt berekend **op uw eigen data**. Dat maakt de simulatie nuttig om te beslissen.

## De indicatoren lezen

Vier indicatoren vatten de prestatie van een sleutel samen. Ze zijn eenvoudig zodra u ze duidelijk onderscheidt — en net daar ontstaat vaak verwarring.

### De zelfverbruiksgraad

De **collectieve zelfverbruiksgraad** wordt aan de **productiezijde** gemeten: het aandeel van de lokaal geproduceerde energie dat de leden effectief verbruiken in plaats van op het net te injecteren. Hoe hoger, hoe beter de lokale productie binnen de gemeenschap wordt gevaloriseerd.

### Het surplus

Het **surplus** is de keerzijde van zelfverbruik: het is de door de producenten geïnjecteerde energie die **niemand in de gemeenschap heeft verbruikt**, en die dus terug naar het openbare net stroomt, meestal verkocht tegen lage waarde. De link is rechtstreeks: **hoe meer het lokale verbruik de productie opneemt, hoe lager het surplus**. Een goede sleutel verlaagt het surplus door energie te sturen naar de leden die ze op het juiste moment nodig hebben.

### De zelfvoorzieningsgraad

De **zelfvoorzieningsgraad** wordt aan de **verbruikszijde** gemeten: het aandeel van het verbruik van de leden dat door gedeelde lokale productie wordt gedekt in plaats van bij de leverancier te worden aangekocht. Het is de spiegel van het zelfverbruik, bekeken vanuit de factuur van de leden in plaats van vanuit de panelen.

### De deelgraad en de lezing per iteratie

De **deelgraad** toont hoeveel van de beschikbare injectie effectief **via de sleutel onder de leden werd verdeeld**. Hier komt de lezing **per iteratie** van pas. Veel sleutels verdelen in meerdere rondes: een eerste ronde verdeelt de energie volgens de regel, daarna wordt de energie die een lid niet verbruikte **in de volgende ronde herverdeeld** onder wie nog vraag heeft (dat is het principe van "meerdere rondes", relatieve of optimale sleutels). De simulatie toont hoe de deelgraad **bij elke iteratie vordert**, tot de deelbare injectie is uitgeput — u ziet precies wat de opeenvolgende rondes toevoegen.

Om verwarring te vermijden, vat deze tabel samen waar elke indicator zich bevindt:

| Indicator | Gemeten… | Beantwoordt de vraag |
|---|---|---|
| Zelfverbruiksgraad | aan de **productiezijde** | Welk aandeel van de productie wordt lokaal verbruikt? |
| Surplus | aan de **productiezijde** | Welk aandeel van de productie gaat naar het net? |
| Zelfvoorzieningsgraad | aan de **verbruikszijde** | Welk aandeel van het verbruik wordt lokaal gedekt? |
| Deelgraad | de mechaniek van de **sleutel** | Welk aandeel van de injectie werd verdeeld, ronde per ronde? |

## Wanneer de simulatie gebruiken?

De simulatie is nuttig in elke fase van het leven van een energiegemeenschap.

- **Vóór de start.** U vergelijkt meerdere kandidaat-sleutels op historische of geschatte data en kiest die welke de doelstellingen van het project het best dient, met kennis van zaken.
- **Tijdens het ontwerp.** U maakt expliciet de afweging tussen **billijkheid** (een leesbare, voorspelbare sleutel voor de leden) en **globale prestatie** (een sleutel die het collectieve zelfverbruik maximaliseert), met cijfers ter ondersteuning.
- **Tijdens de werking.** U meet het effect van een **nieuwe dataset** of een **wijziging van profielen** (een lid plaatst een warmtepomp, een ander een laadpaal) op de indicatoren — zonder iets te breken in de lopende operatie.
- **Bij het bijwerken van de sleutel.** Wanneer een **lid toetreedt of vertrekt**, simuleert u de herberekende sleutel voordat u ze indient, om te controleren of ze performant blijft. Ons artikel over de [verdeelsleutel in België](/nl/nieuws/2026/05/19/verdeelsleutel-energiegemeenschap-belgie/) beschrijft de procedure om een sleutel na de start te wijzigen, en de [gids om een gemeenschap op te richten in Wallonië](/nl/nieuws/2026/05/11/energiegemeenschap-oprichten-wallonie/) plaatst die stap in het regulatordossier.

## De waarde voor gemeenschappen

Voor een gemeenschapsbeheerder, een facilitator of een projectontwikkelaar verandert simulatie de manier van beslissen:

- **Een snellere, rationelere beslissing.** Geen gejongleer meer tussen simulatierekenbladen en ruwe schattingen: de indicatoren verschijnen rechtstreeks in de tool die de gemeenschap al beheert.
- **Pedagogie.** Door op reële data te zien *waarom* de ene sleutel beter werkt dan de andere, begrijpen en aanvaarden de leden de keuze gemakkelijker. De simulatie maakt van een abstracte technische discussie een concrete demonstratie.
- **Een sterk argument.** Voor een algemene vergadering, een netbeheerder of een regulator weegt een sleutel verdedigen met cijfers — uit de eigen data van de gemeenschap — veel zwaarder dan een principiële aanbeveling.

Het is ook een hefboom om lokale productie te valoriseren, en dus om de [elektriciteitsfactuur van de leden te verlagen](/nl/nieuws/2026/06/03/energiegemeenschap-elektriciteitsfactuur-verlagen/): elk vermeden surpluspunt is waarde die in de gemeenschap blijft.

## Simulatie en automatische generatie: twee complementaire tools

OptimCE biedt al een **module voor automatische generatie** die de beste sleutel *voorstelt* op basis van de data — via een **brute force** op de regionale standaardsleutels en via **LOGAAS**, een algoritme uit het onderzoek van CeCoTePe voor het Locomotrice-project. De simulatie daarentegen *test* een sleutel die **u** hebt gekozen.

Het zijn twee complementaire toepassingen, geen concurrenten:

| | Simulatie | Automatische generatie |
|---|---|---|
| Gestelde vraag | "Wat geeft *deze* sleutel op deze data?" | "*Welke* sleutel is het best voor deze data?" |
| Invoer | Een gekozen sleutel + een CSV | Een CSV |
| Uitvoer | De KPI's van de geteste sleutel | Eén (of meer) geoptimaliseerde kandidaat-sleutel(s) |
| Typisch gebruik | Scenario's vergelijken, begrijpen, verantwoorden | Een goed startpunt vinden |

In de praktijk genereert u om een solide kandidaat te vinden en simuleert u vervolgens om zijn gedrag te begrijpen, varianten te vergelijken en hem te verdedigen. Voor de details van de algoritmes, zie [“Verdeelsleutel automatisch genereren”](/nl/nieuws/2026/05/26/automatische-verdeelsleutel-generatie/).

## Energiegemeenschappen in België, in het kort

Een **energiegemeenschap** brengt producenten en verbruikers samen die lokaal hernieuwbare productie delen. Het delen is administratief: digitale meters worden afgelezen op een **15-minutenstap**, en de **distributienetbeheerder (DNB)** past de gekozen verdeelsleutel toe om elk lid een aandeel van de geïnjecteerde energie toe te wijzen. België erkent verschillende vormen — HEG, BEG en, in Brussel, LEG — onder toezicht van de regionale regulatoren ([Brugel](https://energysharing.brugel.brussels) in Brussel, met [Sibelga](https://www.sibelga.be/nl/aansluitingen-meters/hernieuwbare-energie/energie-delen) als netbeheerder).

In dit landschap is de verdeelsleutel de centrale parameter van de prestatie van een gemeenschap — en de simulatie beantwoordt een reële behoefte: **het delen van energie structureren en begrijpen** voordat men zich ertoe verbindt. Voor het volledige overzicht van de juridische vormen, zie [“Energiegemeenschappen in België: CER, CEC, CEL”](/nl/nieuws/2026/05/11/energiegemeenschappen-belgie/).

## Conclusie

Het simuleren van een verdeelsleutel brengt één eenvoudige maar doorslaggevende zaak: **de mogelijkheid om te testen vóór de uitrol**. In plaats van een sleutel op buikgevoel te kiezen en de effecten achteraf te ontdekken, meet u zelfverbruik, surplus, zelfvoorziening en de deelgraad vooraf op uw eigen data — globaal en ronde na ronde. Dat betekent minder risico, meer pedagogie, en bestuursbeslissingen onderbouwd met cijfers.

> ### Simuleer uw verdeelsleutel met OptimCE
>
> Open-source platform op maat van Belgische energiegemeenschappen: simuleer een sleutel op uw data, vergelijk scenario's, genereer een optimale sleutel, houd een historiek van de deeloperaties bij en bereid de rapportering aan de regulator voor — alles in één applicatie.
>
> **[Start op app.optimce.be →](https://app.optimce.be)**

## FAQ

### Wat betekent het om een verdeelsleutel te simuleren?

Het betekent reële productie- en verbruiksdata door een gekozen verdeelsleutel spelen, **zonder die in productie toe te passen**, om de indicatoren vooraf te meten: collectief zelfverbruik, surplus, zelfvoorzieningsgraad en deelgraad. Het is een "wat-als"-test voordat u beslist.

### Wat is het verschil tussen een verdeelsleutel simuleren en genereren?

**Automatische generatie** stelt de beste sleutel voor op basis van uw data (brute force op standaardsleutels of het LOGAAS-algoritme). **Simulatie** test een sleutel die u zelf hebt gekozen op een bepaalde dataset en toont de indicatoren ervan. Beide vullen elkaar aan: u genereert om een goede kandidaat te vinden en u simuleert om scenario's te begrijpen en te vergelijken.

### Wat is het verschil tussen zelfverbruiksgraad, zelfvoorzieningsgraad en deelgraad?

De **zelfverbruiksgraad** wordt aan de productiezijde gemeten: het aandeel van de lokaal geproduceerde energie dat door de leden wordt verbruikt. De **zelfvoorzieningsgraad** wordt aan de verbruikszijde gemeten: het aandeel van het verbruik van de leden dat door lokale productie wordt gedekt. De **deelgraad** toont hoeveel van de injectie via de sleutel effectief onder de leden werd verdeeld.

### Wat betekenen de resultaten "per iteratie"?

Veel sleutels verdelen energie in meerdere rondes (iteraties): een eerste ronde verdeelt volgens de regel, daarna wordt de niet-verbruikte energie in de volgende ronde herverdeeld. De simulatie toont het resultaat **globaal**, **per tijdstap** en **per iteratie**, zodat u ziet hoe het delen ronde na ronde vordert.

### Welke data moet ik importeren om een simulatie te starten?

Een **CSV**-bestand met het verbruik per tijdstap (vaak per kwartier) van elk lid en de productie van elke producent van de deeloperatie. Elke regel komt overeen met één tijdstap. Enkele weken data geven al een bruikbaar signaal; een volledig jaar vat de seizoensgebondenheid beter.

### Verandert de simulatie mijn verdeelsleutel in productie?

Nee. De simulatie is een berekening "buiten productie": ze raakt noch aan de sleutel die de netbeheerder toepast, noch aan uw reële data. U test zoveel scenario's als u wilt zonder enig effect op de lopende deeloperatie.

## Bronnen

- [Brugel — Energy Sharing](https://energysharing.brugel.brussels) — officieel portaal van de Brusselse regulator over energiedelen en het kader van energiegemeenschappen.
- [Brugel — Energiegemeenschappen](https://energysharing.brugel.brussels/blog/energy-sharing-18/communautes-d-energie-406) — toelating, geldigheidsduur en regelgevend kader in Brussel.
- [Sibelga — Energie delen in een gemeenschap](https://www.sibelga.be/nl/aansluitingen-meters/hernieuwbare-energie/energie-delen) — voorwaarden, actoren en principes van het delen in Brussel.
- [IÖW — Self-consumption and self-sufficiency in energy sharing communities](https://www.ioew.de/en/publication/self_consumption_and_self_sufficiency_in_energy_sharing_communities_in_germany) — methodologische referentie over indicatoren voor zelfverbruik en zelfvoorziening.
- [KPMG — Energy sharing in Belgium: overview and policy recommendations](https://kpmg.com/be/en/insights/industries/energy-natural-resources-insights/energy-sharing-in-belgium-overview-and-policy-recom.html) — overzicht van energiedelen in België.
- [Pricing and sharing rules for energy communities](https://econpapers.repec.org/article/eeejuipol/v_3a96_3ay_3a2025_3ai_3ac_3as0957178725001109.htm) — onderzoek naar deelregels en interne prijzen, dat het nut van een simulatie onderbouwt.
