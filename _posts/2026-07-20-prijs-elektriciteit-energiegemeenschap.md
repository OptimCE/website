---
layout: post
title: "Interne overdrachtsprijs in een gemeenschap"
date: 2026-07-20 10:00:00 +0200
author: "OptimCE-team"
excerpt: "Welke prijs per kWh voor de elektriciteit die tussen leden gedeeld wordt? Wat de interne prijs echt dekt, de verdedigbare bandbreedte tussen injectietarief en energiecomponent, vijf rekenmethodes, een doorgerekend Belgisch praktijkgeval en de regels in Wallonië, Brussel en Vlaanderen."
description: "Wat de interne prijs dekt, de verdedigbare bandbreedte tussen injectietarief en energiecomponent, en vijf manieren om hem te berekenen."
tags: [community, administrative, guide]
lang: nl
ref: internal-price-shared-energy
permalink: /nl/nieuws/2026/07/20/prijs-elektriciteit-energiegemeenschap/
last_modified_at: 2026-07-25 10:00:00 +0200
faq:
  - q: "Wie bepaalt de prijs van de gedeelde elektriciteit in een energiegemeenschap?"
    a: "In Wallonië en Brussel: de deelnemers zelf. De CWaPE schrijft dat “de prijs van de gedeelde elektriciteit vrij wordt bepaald tussen de deelnemers aan het delen, in de overeenkomst die hun rechten en plichten vastlegt”. Geen enkele Belgische regulator publiceert een plafond of een rekenmethode. In Vlaanderen stelt de vraag zich anders: energiedelen binnen een energiegemeenschap moet kosteloos gebeuren."
  - q: "Vervangt de interne prijs mijn elektriciteitsfactuur?"
    a: "Nee. Hij vervangt alleen de energiecomponent, goed voor ongeveer 38 % van een Belgische residentiële factuur volgens de CREG-boordtabel van juni 2026. De netkosten, de accijnzen, de gewestelijke toeslagen en de btw blijven verschuldigd op de gedeelde kWh, en de energie die het delen niet dekt, wordt nog altijd door uw gewone leverancier gefactureerd."
  - q: "Tussen welke waarden is een interne overdrachtsprijs verdedigbaar?"
    a: "Tussen het injectietarief dat de producent elders zou krijgen — van 0,94 tot 4,90 c€/kWh volgens de contracten die Test Aankoop in mei 2026 vergeleek — en de energiecomponent die de verbruiker aan zijn leverancier betaalt, in de orde van 14 c€/kWh. Onder die ondergrens verliest de producent bij het delen; boven die bovengrens verliest de verbruiker bij lokaal verbruik."
  - q: "Mag elektriciteit gratis gedeeld worden?"
    a: "Ja in Wallonië en Brussel, waar de prijs een contractuele parameter is die nul mag zijn. In Vlaanderen is het zelfs verplicht binnen een energiegemeenschap: de Vlaamse Nutsregulator geeft aan dat u er energie enkel zonder tegenprestatie kunt delen, en dat verkoop via andere regelingen verloopt."
  - q: "Is een leveringsvergunning nodig om de gedeelde energie aan de leden te verkopen?"
    a: "Nee, binnen de perimeter van het delen. In Wallonië preciseert de SPW dat de gedeelde elektriciteit niet als een leveringsverrichting wordt beschouwd. In Brussel bepaalt de ordonnantie uitdrukkelijk dat de gemeenschap “niet onderworpen is aan de verplichtingen die op de leveranciers rusten voor de elektriciteit die binnen haar wordt gedeeld”. De vrijstelling stopt bij de kring van deelnemers: daarbuiten verkopen valt onder het vergunningsregime."
  - q: "Welke btw geldt op gedeelde elektriciteit?"
    a: "6 % voor particuliere leden en 21 % voor professionele leden: een gemeenschap met gemengde leden factureert dus tegen twee tarieven. Onder 25.000 € omzet excl. btw per jaar kan de vrijstellingsregeling voor kleine ondernemingen gelden. Laat uw situatie nakijken bij de FOD Financiën of bij uw boekhouder."
  - q: "Hoe vaak moet de prijs herzien worden?"
    a: "Minstens één keer per jaar, op de algemene vergadering — dat is de praktijk van de Brusselse gemeenschap Énergie Solidaire du Balai. Een prijs die vastligt terwijl de markt beweegt, benadeelt uiteindelijk altijd iemand: de producenten wanneer de prijzen stijgen, of de verbruikers wanneer ze instorten."
---

Een eigenaar van zonnepanelen verkoopt zijn overschot vandaag tussen **0,94 en 4,90 c€/kWh**, afhankelijk van zijn contract ([Test Aankoop](https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee), mei 2026). Diezelfde dag koopt zijn buur elektriciteit aan **36,94 c€/kWh** alles inbegrepen ([CREG](https://www.creg.be/fr/professionnels/fonctionnement-et-monitoring-du-marche/tableau-de-bord), juni 2026). Tussen die twee cijfers zit een factor elf — en precies in die ruimte nestelt zich een energiegemeenschap.

Blijft de vraag die elke projectdrager uiteindelijk stelt, vaak te laat: **welke prijs schrijft u in de overeenkomst?** Geen enkele Belgische regulator publiceert een antwoord. Noch de CWaPE, noch BRUGEL, noch de Vlaamse Nutsregulator verspreidt een rekenmethode of een referentietarief. Dit artikel vult die leemte: wat de interne prijs werkelijk dekt, tussen welke grenzen hij moet vallen, vijf methodes om hem op te bouwen, een volledig doorgerekend Belgisch praktijkgeval, en wat het kader in elk gewest toelaat.

Is de mechaniek van het delen u nog vreemd, begin dan bij ons referentieartikel [“Verdeelsleutel in België: de 3 regio's”](/nl/nieuws/2026/05/19/verdeelsleutel-energiegemeenschap-belgie/): de sleutel bepaalt *hoeveel kWh* elk lid krijgt, de prijs bepaalt *hoeveel euro*.

## De interne overdrachtsprijs vervangt maar een derde van de factuur

Dat is fout nummer één, en ze vergiftigt algemene vergaderingen: denken dat een interne prijs van 14 c€/kWh de leden 14 c€/kWh zal doen betalen. Zo werkt het niet.

Een Belgische elektriciteitsfactuur valt uiteen in vier blokken. Dit is hun werkelijke gewicht, volgens de maandelijkse boordtabel van de CREG voor **juni 2026** (typisch residentieel profiel, 3.500 kWh/jaar, enkelvoudig tarief):

| Component | België | Vlaanderen | Brussel | Wallonië |
|---|---|---|---|---|
| **Energie** (de commodity) | 38,5 % | 39,3 % | 39,7 % | 37,2 % |
| Net (transmissie + distributie) | 29,7 % | 28,7 % | 24,6 % | 32,7 % |
| Taksen, accijnzen en toeslagen | 26,1 % | 26,4 % | 30,1 % | 24,5 % |
| Btw | 5,7 % | 5,7 % | 5,7 % | 5,7 % |
| **Totale prijs** | **36,94 c€/kWh** | 35,31 | 39,04 | 38,64 |

De interne overdrachtsprijs concurreert alleen met de **eerste regel**: ongeveer **14 c€/kWh** in absolute waarde. Al de rest blijft doorlopen op de gedeelde kWh, want die kWh lopen wel degelijk over het openbare net. De CWaPE formuleert het zonder omwegen: “aangezien de elektriciteit via het net wordt getransporteerd, zijn alle netkosten (transmissie en distributie) en de daarmee verbonden taksen en toeslagen verschuldigd op de gedeelde elektriciteit” ([CWaPE](https://www.cwape.be/node/6062)).

Twee praktische gevolgen:

- **Kondig de besparing altijd aan op de energiecomponent, nooit op de factuur.** De energieprijs halveren halveert de factuur niet: het haalt er ongeveer 19 % af.
- **Het gewicht van het net verschilt sterk van gewest tot gewest** — 32,7 % in Wallonië tegenover 24,6 % in Brussel. Eenzelfde interne prijs geeft dus niet overal hetzelfde gevoelde effect.

### Wat de vertegenwoordiger bovenop de prijs factureert

Bij de afgesproken prijs komen, op de factuur van de gemeenschap zelf, “de btw, de accijnzen en de openbaredienstverplichting tot inlevering van groenestroomcertificaten” ([CWaPE](https://www.cwape.be/node/6063)). Wie deze factuur opstelt en welke vermeldingen ze moet dragen, is het onderwerp van onze gids [“Gedeelde elektriciteit factureren in België”](/nl/nieuws/2026/07/23/gedeelde-elektriciteit-factureren-belgie/). Twee preciseringen waarover veel projecten struikelen:

- **De btw is niet uniform.** Het verlaagde tarief van **6 % geldt voor de levering van elektriciteit aan een particuliere klant**, tegenover **21 % voor een professionele klant**: een gemeenschap met gemengde leden moet er dus op rekenen tegen twee tarieven te factureren. Onder 25.000 € omzet excl. btw per jaar kan de [vrijstellingsregeling voor kleine ondernemingen](https://finances.belgium.be/fr/entreprises/tva/assujettissement-tva/regime-franchise-taxe) van toepassing zijn. Geen enkele circulaire behandelt het energiedelen specifiek: laat uw situatie door uw boekhouder valideren vóór de eerste factuur.
- **De federale bijdrage bestaat niet meer.** Ze werd op 31 december 2021 afgeschaft en opgeslorpt door de bijzondere accijns ([CREG](https://www.creg.be/fr/a-z-index/cotisation-federale)). Veel documenten die nog circuleren, vermelden ze nog altijd: neem ze niet op in uw simulaties.

## De netkosten dalen bijna nooit

Het idee dat een energiegemeenschap van verlaagde nettarieven geniet, is wijdverspreid. Het is vooral **onjuist in het meest voorkomende geval**. We ontleden elders, blok per blok, [waarom een Belgische elektriciteitsfactuur hoog blijft ondanks dalende prijzen](/nl/nieuws/2026/07/25/waarom-elektriciteitsfactuur-hoog-blijft-belgie/) — nettarieven, taksen en leveranciersmarge inbegrepen. Het detail per gewest:

| Gewest | Verlaging van de nettarieven op de gedeelde kWh |
|---|---|
| **Wallonië** | 80 % op de proportionele termen, **uitsluitend binnen eenzelfde gebouw**. Voor een energiegemeenschap: geen enkele verlaging. De CWaPE schrijft het zwart op wit — “er bestaat geen tariefkorting voor het delen binnen een energiegemeenschap”. |
| **Brussel** | Het enige echte gunstregime. Naargelang de nabijheid van de deelnemers: type A (zelfde gebouw) → proportionele tarieven **verlaagd tot 0 €**; type B (zelfde laagspanningscabine) → **gehalveerd**; types C en D → ongewijzigd. Bevestigd tot minstens 2027 door de tariefmethodologie 2025-2029 van BRUGEL. |
| **Vlaanderen** | Geen. “Energiedelen en persoon-aan-persoonverkoop hebben enkel een effect op de energiecomponent van de elektriciteitsfactuur, maar niet op de netkosten, heffingen en taksen” (Fluvius). Ook het capaciteitstarief, dat op de gemeten piek van de digitale meter steunt, wordt niet verlicht. |

Reken daar nog een post bij die bijna niemand ziet aankomen: **uw leverancier mag kosten aanrekenen voor uw deelname aan het delen**. De CWaPE bevestigt dat niets dat verbiedt ([CWaPE](https://www.cwape.be/node/6060)), en de vastgestelde bedragen lopen van nul tot ongeveer 150 € per jaar en per toegangspunt. Op een kleine hoeveelheid gedeelde energie wissen die kosten de winst zonder meer uit — het is de belangrijkste stille moordenaar van de rendabiliteit van een project.

## Wie mag een prijs bepalen? De drie gewesten antwoorden niet hetzelfde

Dit is het punt dat de meeste gidsen onvermeld laten, en het is beslissend: **in Vlaanderen stelt de prijsvraag zich niet**, omdat verkopen binnen een energiegemeenschap er niet toegelaten is.

| | Wallonië | Brussel | Vlaanderen |
|---|---|---|---|
| **Prijs binnen een gemeenschap** | Vrij | Vrij | **Verboden — het delen moet kosteloos zijn** |
| Wat het kader zegt | “De prijs van de gedeelde elektriciteit wordt vrij bepaald tussen de deelnemers aan het delen” (CWaPE) | Geen plafond of referentieprijs in de ordonnantie; verplichting van “billijke, transparante en niet-discriminerende” regels | “In een energiegemeenschap kan u enkel energie delen. Energie verkopen in een energiegemeenschap is niet mogelijk.” (Vlaamse Nutsregulator) |
| Officiële modelovereenkomst | Geen voor de overeenkomst tussen deelnemers | Ja, gepubliceerd door Leefmilieu Brussel | Model gepubliceerd voor de persoon-aan-persoonverkoop |
| Leveringsvergunning | Niet vereist: “de gedeelde elektriciteit wordt niet beschouwd als een leveringsverrichting” (SPW Energie) | Nee: de gemeenschap “is niet onderworpen aan de verplichtingen die op de leveranciers rusten voor de elektriciteit die binnen haar wordt gedeeld” | Niet van toepassing op het delen; de verkoop binnen een gebouw is uitdrukkelijk vrijgesteld |

### Wallonië: volledige vrijheid, en een blanco blad

De prijs is vrij, en de overeenkomst tussen deelnemers moet “de verdeelsleutel, de kostprijs van de gedeelde elektriciteit” bevatten — maar **er bestaat geen enkel modeldocument** ([CWaPE](https://www.cwape.be/node/6064)). U vertrekt van een blanco blad. Nog dit: de Waalse persoon-aan-persoonverkoop is **nog niet operationeel**, bij gebrek aan uitvoeringsbesluit ([CWaPE](https://www.cwape.be/node/6080)). De enige wegen om een prijs toe te passen zijn dus het delen binnen eenzelfde gebouw en het delen binnen een toegelaten gemeenschap.

### Brussel: de vorm omkaderd, het bedrag vrij

De Brusselse ordonnantie bevat **noch het woord “prijs” noch het woord “redelijk”** in haar hoofdstuk over energiegemeenschappen. Wat ze wel oplegt, is een procedurele omkadering: de overeenkomst moet “de billijke, transparante en niet-discriminerende regels voor het delen” vastleggen, opgesteld zijn “in duidelijke en begrijpelijke taal” en mag geen “discriminatie tussen deelnemers” creëren. Het niveau van de prijs blijft volledig onderhandeld — de officiële modelovereenkomst bevat trouwens een in te vullen veld: *“De verkoopprijs van de gedeelde elektriciteit wordt vastgesteld op ….. c€/kWh excl. btw”*.

De hulp bij het rekenwerk komt niet van de regulator maar van **Leefmilieu Brussel**, dat een economische simulatietool en een gratis facilitator ter beschikking stelt.

### Vlaanderen: kosteloos per definitie

*Energiedelen* is in het Vlaamse **Energiedecreet** gedefinieerd als het **“kosteloos”** toewijzen van zelf geproduceerde energie. De regulator is categoriek: “In een energiegemeenschap kan u enkel energie delen. Energie verkopen in een energiegemeenschap is niet mogelijk.” Een prijs blijft mogelijk, maar via andere deuren: de **persoon-aan-persoonverkoop** — “U bepaalt zelf de prijs en regelt de eventuele betaling onderling.” — en de verkoop binnen een gebouw door de **vereniging van mede-eigenaars (VME)**. Let op de valkuil: de meervoudige persoon-aan-persoonverkoop loopt van *meerdere verkopers naar één koper* — ze laat een gemeenschap dus niet toe al haar leden te factureren.

**Duidelijk gezegd: een Vlaams project dat zijn producenten wil vergoeden, moet een andere juridische constructie kiezen dan de energiegemeenschap.** Dat ontdekt u beter vóór de oprichting dan tegenover de regulator.

## De vork: ondergrens producent, bovengrens verbruiker

Heel de discussie over de prijs komt neer op één eenvoudige redenering: **elke partij heeft een alternatief, en de prijs moet voor beide beter zijn dan dat alternatief.**

- **De ondergrens is wat de producent zonder de gemeenschap zou krijgen**: zijn injectietarief. Er bestaat in België geen gereguleerd injectietarief — het is een commerciële prijs. Vaststelling van mei 2026: van **0,94 tot 4,90 c€/kWh** in Vlaanderen en Wallonië, van 1,40 tot 4,81 c€/kWh in Brussel ([Test Aankoop](https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee)). En die ondergrens kan negatief worden: bijna **29.000 Vlaamse prosumenten** kregen in 2025 gedurende minstens één maand een negatief terugkooptarief — ze moesten *betalen* om te injecteren.
- **De bovengrens is wat de verbruiker vandaag al betaalt** voor alleen de energiecomponent van zijn contract: in de orde van **14 c€/kWh**.

Tussen 3 en 14 c€/kWh wint iedereen. Daaronder heeft de producent er belang bij de gemeenschap te verlaten. Daarboven de verbruiker. **De interne overdrachtsprijs is dus geen morele kwestie: het is een verdeling van surplus, en de enige echte vraag is in welke verhouding.**

Eén detail versterkt dat argument en wordt zelden geciteerd: op de Belgische groothandelsmarkt zakte in mei 2026 de prijs van de **piekuren (69,78 €/MWh) onder die van de daluren (103,03 €/MWh)** ([BELIX](https://www.elexys.be/en/insights/belix-average-day-ahead-spot-be)). Zonne-elektriciteit van midden op de dag wordt steeds minder waard op de markt — en steeds meer waard voor wie ze op datzelfde ogenblik lokaal verbruikt. De kloof tussen ondergrens en bovengrens sluit niet: hij wordt breder.

## Vijf methodes om de prijs op te bouwen

Geen enkele is *dé* juiste. Ze beantwoorden aan verschillende prioriteiten.

### 1. De vaste prijs, gestemd op de algemene vergadering

Eén getal, één stemming, één herzieningsdatum. Veruit het meest verspreid, en het is de praktijk van de Brusselse gemeenschap Énergie Solidaire du Balai, waarvan de prijs “elk jaar op de algemene vergadering wordt herzien”.

*Voor wie:* alle gemeenschappen die van start gaan. *Risico:* de prijs drijft weg van de markt als de herziening vergeten wordt.

### 2. Het verschil delen

U berekent uitdrukkelijk de ondergrens en de bovengrens en gaat er in het midden tussen zitten — of op 40/60 als u de producent die geïnvesteerd heeft, wilt bevoordelen. Met een injectietarief van 3 c€ en een energiecomponent van 14 c€ valt het midden op **8,5 c€/kWh**: de producent verdrievoudigt zijn opbrengst, de verbruiker bespaart 40 % op zijn energiecomponent.

*Voor wie:* gemeenschappen die hun prijs willen kunnen **verantwoorden** tegenover een ontevreden lid. *Sterkte:* het is de enige methode die een becijferde, symmetrische en verifieerbare argumentatie oplevert.

### 3. De kostprijs van de installatie

U deelt de investering plus de uitbatingskosten door de kWh die over de levensduur geproduceerd worden. De prijs wordt een afschrijvingsdoelstelling in plaats van een marktafweging.

*Voor wie:* gemeenschappen die hun installatie zelf bezitten. *Risico:* een fotovoltaïsche kostprijs ligt zeer laag, wat een lage producentenprijs geeft — te combineren met een expliciete marge (zie verder).

### 4. De procentuele korting op het leverancierstarief

De prijs volgt de energiecomponent van de leverancier, min X %. Hij blijft automatisch in lijn met de markt.

*Voor wie:* gemeenschappen waarvan de leden voortdurend met hun eigen contract vergelijken. *Let op:* de korting moet slaan op de **energiecomponent**, niet op de all-inprijs, anders belooft u een besparing die u niet kunt waarmaken.

### 5. De indexering op een marktindex

De prijs volgt een gepubliceerde index — bijvoorbeeld het maandgemiddelde van de Belgische day-aheadmarkt. Economisch het correctst, en op een algemene vergadering het moeilijkst uit te leggen.

*Voor wie:* gemeenschappen met een professionele component, vertrouwd met geïndexeerde contracten. *Risico:* u haalt de volatiliteit waarvoor de leden net kwamen vluchten, opnieuw binnen. Nochtans is de stabiliteit van de prijs vaak het meest gewaardeerde argument, nog vóór de besparing.

| Methode | Inspanning | Stabiliteit voor het lid | Verantwoordbaar |
|---|---|---|---|
| Vaste prijs gestemd op de AV | Laag | Zeer hoog | Matig |
| Het verschil delen | Gemiddeld | Hoog | Zeer goed |
| Kostprijs | Gemiddeld | Hoog | Goed |
| Korting in % | Laag | Gemiddeld | Goed |
| Indexering | Hoog | Laag | Zeer goed |

## Een volledig doorgerekend Belgisch praktijkgeval

De Brusselse gemeenschap **Énergie Solidaire du Balai** publiceert haar tarieven — een zeldzaamheid. Dit is haar structuur van 2024, zoals gedocumenteerd door de [Gids Duurzame Gebouwen van Leefmilieu Brussel](https://guidebatimentdurable.brussels/partage-delectricite-sein-dune-communaute-denergie-energie-solidaire-balai/partage-delectricite):

| Post | Bedrag |
|---|---|
| Prijs betaald aan de producent | **6 c€/kWh** |
| Marge behouden door de gemeenschap | **8 c€/kWh** |
| **Prijs van de lokale energie gefactureerd aan de verbruiker** | **14 c€/kWh** |
| + netkosten | 9,575 c€/kWh excl. btw |
| + federale taksen | 4,94 c€/kWh excl. btw |
| **Totaal betaald door de verbruiker** | **≈ 32 c€/kWh incl. btw** |

Drie lessen, waarvan één die de bron opneemt met een eerlijkheid die men vaker zou willen zien:

1. **De producentenprijs (6 c€) ligt duidelijk boven het injectietarief** (1 tot 5 c€): delen blijft interessanter dan injecteren. Dezelfde grootteorde vindt u terug bij [Renouvelle](https://www.renouvelle.be/fr/exemples-calculs-de-rentabilite-economique-dun-partage-delectricite-en-wallonie/), dat een interne deelprijs van 6 c€/kWh documenteert en een collectief injectiecontract aan 3 c€/kWh, tien jaar gegarandeerd.
2. **De marge van 8 c€/kWh is geen winst**: ze financiert de werking van de gemeenschap — administratie, facturatie, verzekering, tools.
3. **De leden, schrijft de bron, “doen geen grote besparingen”.** Ze betalen een stabiele prijs, licht onder de markt, en sluiten zich in de eerste plaats aan voor het project. Iets anders beloven, is vertrekkers voorbereiden.

## De fouten die een gemeenschap breken

- **De werkingsmarge vergeten.** Een prijs die tot op de cent op de productiekost is afgestemd, laat niets over voor boekhouding, verzekering of platform. De gemeenschap leeft één jaar en roept dan dringend bijdragen op.
- **De prijs vastzetten zonder herzieningsdatum.** De Belgische groothandelsprijzen schommelden in het eerste halfjaar van 2026 alleen al tussen 78,94 en 112,13 €/MWh. Een prijs die “voor eens en altijd” wordt vastgelegd, benadeelt uiteindelijk iemand.
- **Een besparing op de factuur aankondigen in plaats van op de energiecomponent.** Het lid rekent na, vindt het niet terug, en het vertrouwen stort in.
- **De bijkomende kosten van de leverancier negeren.** Tot 150 €/jaar en per toegangspunt: op 500 gedeelde kWh overtreft dat de winst.
- **Vergeten dat de prosument de jaarlijkse compensatie verliest** door deel te nemen aan het delen ([CWaPE](https://www.cwape.be/node/6075)), en dat het sociaal tarief niet geldt voor de gedeelde volumes. Die twee effecten horen thuis in de simulatie, niet in de ontdekking achteraf.
- **Het lid dat tegelijk producent en verbruiker is, identiek behandelen.** Het krijgt twee afzonderlijke stromen: een vergoeding voor zijn gedeelde injectie, en een factuur voor de gedeelde energie die het verbruikt. Twee prijzen, twee documenten.

## De prijs laten leven: herziening, transparantie, traceerbaarheid

Een interne overdrachtsprijs is geen beslissing, het is een proces. Drie gewoontes volstaan:

- **Een jaarlijkse herziening op de agenda van de algemene vergadering**, telkens met een vergelijkingspunt: het injectietarief van het moment, de gemiddelde energiecomponent, het resultaat van het afgelopen boekjaar.
- **Een geschreven regel in plaats van een getal.** “De producentenprijs wordt vastgelegd op het dubbele van het vastgestelde gemiddelde injectietarief, geplafonneerd op de helft van de energiecomponent” verdedigt zich beter dan een “6 c€” zonder verhaal — en werkt zichzelf bij.
- **Een bewaarde historiek.** Wanneer een lid een factuur van vorig jaar betwist, moet u kunnen tonen welke prijs op die datum gold, en op beslissing van welke vergadering.

Die transparantie-eis is niet cosmetisch: in Brussel staat ze uitdrukkelijk in de tekst — de regels moeten “billijk, transparant en niet-discriminerend” zijn en opgesteld “in duidelijke en begrijpelijke taal”. Niets legt daarentegen een **identieke** prijs voor iedereen op: de verplichting slaat op de *regels*, niet op de uniformiteit van de bedragen. Een differentiatie tussen objectieve categorieën — investerende leden, gezinnen, ondernemingen — blijft verdedigbaar als ze geschreven, gemotiveerd en uniform toegepast is. Twijfelt u over een gedifferentieerde tariefstructuur, laat ze dan valideren door de gewestelijke facilitator vóór u ze invoert.

## Uw prijs toepassen in OptimCE

Eenmaal de prijs beslist, moet hij op facturen belanden. Dat is precies wat de [facturatiemodule van OptimCE](/nl/nieuws/2026/07/16/facturatie-energiegemeenschap-optimce/) doet, beschikbaar sinds juli 2026.

U definieert **twee prijzen in €/kWh**, onafhankelijk van elkaar — de verkoopprijs van de gedeelde energie aan de verbruikers en de terugkoopprijs van de injectie die aan de producenten wordt betaald. Elke prijs kan globaal gelden, per klantsegment (residentieel, professioneel, industrieel) of voor één specifiek toegangspunt, met een **geldigheidsperiode**: de meest specifieke regel wint, en een globale prijs blijft altijd vereist als vangnet. De prijzen worden op zes decimalen bewaard, zodat afrondingen pas gebeuren op het te betalen bedrag.

Zo dekt u de twee behoeften die hierboven beschreven zijn: de **differentiatie per objectieve categorie** en de **historiek van de herzieningen**. Van prijs veranderen vervangt niets: u voegt vanaf een bepaalde datum een nieuwe regel toe, en de oude blijft raadpleegbaar — precies wat u nodig hebt op de dag dat een lid een factuur van het vorige boekjaar betwist.

Vanaf daar neemt OptimCE de officiële verdelingsvolumes over die al geïmporteerd zijn, past de juiste prijs op elk profiel toe en genereert de facturen, de creditnota's en de vergoedingsafrekeningen als pdf, met wettelijke nummering, gestructureerde mededeling en opvolging van de betalingen. De prijs die u op de algemene vergadering onderhandeld hebt, wordt een tegenstelbaar document, zonder tussentijds rekenblad.

## Conclusie

De prijs van de gedeelde elektriciteit bepalen is geen technische en evenmin een morele kwestie: het is een **verdeling van surplus tussen twee partijen die elk een alternatief hebben**. De producent kan injecteren aan 3 c€/kWh, de verbruiker kan zijn energiecomponent kopen aan 14 c€/kWh. Elke prijs daartussen creëert waarde; de enige beslissing die overblijft, is die van de verdeling — en ze behoort toe aan de algemene vergadering, niet aan de regulator.

Blijft nakijken of uw gewest wel toelaat wat u zich voorstelt: volledige vrijheid in Wallonië en Brussel, opgelegde kosteloosheid binnen de Vlaamse energiegemeenschappen. Daarna de regel schrijven, haar herziening plannen, en haar op elke factuur zonder afrondingsfout toepassen.

> ### Factureer de gedeelde energie tegen de juiste prijs met OptimCE
>
> Opensourceplatform voor Belgische energiegemeenschappen: bepaal uw verkoop- en terugkoopprijzen, per segment of per toegangspunt, met geldigheidsperiode — en genereer facturen en afrekeningen als pdf op basis van uw officiële verdelingsdata.
>
> **[Aan de slag op app.optimce.be →](https://app.optimce.be)**

## FAQ

### Wie bepaalt de prijs van de gedeelde elektriciteit in een energiegemeenschap?

In **Wallonië en Brussel: de deelnemers zelf**. De CWaPE schrijft dat “de prijs van de gedeelde elektriciteit vrij wordt bepaald tussen de deelnemers aan het delen, in de overeenkomst die hun rechten en plichten vastlegt”. Geen enkele Belgische regulator publiceert een plafond of een rekenmethode. In **Vlaanderen** stelt de vraag zich anders: energiedelen binnen een energiegemeenschap moet kosteloos gebeuren.

### Vervangt de interne prijs mijn elektriciteitsfactuur?

Nee. Hij vervangt alleen de **energiecomponent**, goed voor ongeveer 38 % van een Belgische residentiële factuur volgens de CREG-boordtabel van juni 2026. De netkosten, de accijnzen, de gewestelijke toeslagen en de btw blijven verschuldigd op de gedeelde kWh, en de energie die het delen niet dekt, wordt nog altijd door uw gewone leverancier gefactureerd.

### Tussen welke waarden is een interne overdrachtsprijs verdedigbaar?

Tussen het **injectietarief** dat de producent elders zou krijgen — van 0,94 tot 4,90 c€/kWh volgens de contracten die Test Aankoop in mei 2026 vergeleek — en de **energiecomponent** die de verbruiker aan zijn leverancier betaalt, in de orde van 14 c€/kWh. Onder die ondergrens verliest de producent bij het delen; boven die bovengrens verliest de verbruiker bij lokaal verbruik.

### Mag elektriciteit gratis gedeeld worden?

Ja in Wallonië en Brussel, waar de prijs een contractuele parameter is die nul mag zijn. In **Vlaanderen is het zelfs verplicht** binnen een energiegemeenschap: de Vlaamse Nutsregulator geeft aan dat u er energie enkel zonder tegenprestatie kunt delen, en dat verkoop via andere regelingen verloopt.

### Is een leveringsvergunning nodig om de gedeelde energie aan de leden te verkopen?

Nee, **binnen de perimeter van het delen**. In Wallonië preciseert de SPW dat de gedeelde elektriciteit niet als een leveringsverrichting wordt beschouwd. In Brussel bepaalt de ordonnantie uitdrukkelijk dat de gemeenschap “niet onderworpen is aan de verplichtingen die op de leveranciers rusten voor de elektriciteit die binnen haar wordt gedeeld”. De vrijstelling stopt bij de kring van deelnemers: daarbuiten verkopen valt onder het vergunningsregime.

### Welke btw geldt op gedeelde elektriciteit?

**6 % voor particuliere leden en 21 % voor professionele leden**: een gemeenschap met gemengde leden factureert dus tegen twee tarieven. Onder 25.000 € omzet excl. btw per jaar kan de vrijstellingsregeling voor kleine ondernemingen gelden. Laat uw situatie nakijken bij de FOD Financiën of bij uw boekhouder.

### Hoe vaak moet de prijs herzien worden?

**Minstens één keer per jaar, op de algemene vergadering** — dat is de praktijk van de Brusselse gemeenschap Énergie Solidaire du Balai. Een prijs die vastligt terwijl de markt beweegt, benadeelt uiteindelijk altijd iemand: de producenten wanneer de prijzen stijgen, of de verbruikers wanneer ze instorten.

## Bronnen

- [CREG — Maandelijkse boordtabel elektriciteit en aardgas](https://www.creg.be/fr/professionnels/fonctionnement-et-monitoring-du-marche/tableau-de-bord) — all-inprijzen en opsplitsing per component en per gewest (editie juni 2026).
- [CREG — Hoe is de energieprijs samengesteld?](https://www.creg.be/fr/consommateurs/le-marche-de-lenergie/comment-est-compose-le-prix-de-lenergie) — structuur van de factuur en toepasselijke btw-tarieven.
- [CREG — Federale bijdrage](https://www.creg.be/fr/a-z-index/cotisation-federale) — afschaffing op 31 december 2021.
- [CWaPE — Wat kost de gedeelde elektriciteit?](https://www.cwape.be/node/6063) — vrijheid van prijszetting en elementen die bijkomend gefactureerd worden.
- [CWaPE — Netkosten op de gedeelde elektriciteit](https://www.cwape.be/node/6062) — verschuldigde tarieven, korting van 80 % beperkt tot het delen binnen een gebouw.
- [CWaPE — Deelovereenkomsten](https://www.cwape.be/node/6064) — minimale inhoud, geen modelovereenkomst tussen deelnemers.
- [SPW Energie — Energiegemeenschappen en energiedelen](https://energie.wallonie.be/home/les-marches-et-les-acteurs/communautes-d-energie/communautes-d-energie-et-partage-d-energie-au-sein-d-un-meme-batiment-electricite.html) — het delen is geen leveringsverrichting.
- [BRUGEL — Energiedelen: nettarieven](https://energysharing.brugel.brussels/energysharing/tarifs-de-reseau-409) — types A tot D en de kortingen op de lokale volumes.
- [Vlaamse Nutsregulator — Energiedelen en energie verkopen](https://www.vlaamsenutsregulator.be/elektriciteit-en-aardgas/energieprijzen-en-facturen/energiedelen-en-energie-verkopen) — kosteloosheid van het delen in een gemeenschap en vrije prijszetting bij persoon-aan-persoonverkoop.
- [Leefmilieu Brussel — Elektriciteitsdelen: Énergie Solidaire du Balai](https://guidebatimentdurable.brussels/partage-delectricite-sein-dune-communaute-denergie-energie-solidaire-balai/partage-delectricite) — volledige prijsstructuur van een Brusselse gemeenschap (tarieven 2024).
- [Renouvelle — Rekenvoorbeelden van de rendabiliteit van elektriciteitsdelen in Wallonië](https://www.renouvelle.be/fr/exemples-calculs-de-rentabilite-economique-dun-partage-delectricite-en-wallonie/) — toegepaste interne prijzen en impact van de leverancierskosten.
- [Test Aankoop — Wat de op het net geïnjecteerde zonne-elektriciteit opbrengt](https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee) — vork van de injectietarieven in België, mei 2026.
- [Elexys — BELIX, maandgemiddelde van de Belgische day-aheadmarkt](https://www.elexys.be/en/insights/belix-average-day-ahead-spot-be) — groothandelsprijzen base, piek en dal.
- [FOD Financiën — Vrijstellingsregeling van belasting](https://finances.belgium.be/fr/entreprises/tva/assujettissement-tva/regime-franchise-taxe) — drempel van 25.000 € voor kleine ondernemingen.
</content>
