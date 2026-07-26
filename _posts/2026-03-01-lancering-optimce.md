---
layout: post
title: "Lancering van OptimCE: het ontstaan"
date: 2026-03-01 10:00:00 +0100
last_modified_at: 2026-07-26 10:00:00 +0200
author: "OptimCE-team"
excerpt: "OptimCE is niet ontstaan in een incubator maar in een laboratorium. Een terugblik op Locomotrice, het Waalse onderzoeksproject achter het platform, op de partners die het droegen, en op de redenen om het als opensource te publiceren."
description: "Waar OptimCE vandaan komt: het onderzoeksproject Locomotrice, de partners Universiteit Luik en CECOTEPE, en waarom het opensource is."
tags: [app, announcement]
lang: nl
ref: launch-optimce
permalink: /nl/nieuws/2026/03/01/lancering-optimce/
faq:
  - q: "Wie ontwikkelt OptimCE?"
    a: "OptimCE komt voort uit Locomotrice, een Waals onderzoeksproject dat liep van 2023 tot 2026 en gefinancierd werd door het Win2Wal-programma van het Waalse Gewest. Het wordt gedragen door de Universiteit van Luik, via haar BEMS-laboratorium, en door het onderzoekscentrum CECOTEPE, in samenwerking met burgerenergiecoöperaties. De ontwikkeling loopt vandaag opensource verder en staat open voor externe bijdragen."
  - q: "Is OptimCE gratis?"
    a: "Het platform verschijnt onder de Apache 2.0-licentie: u mag het gratis en zonder beperking op uw eigen infrastructuur uitrollen. De gehoste versie, OptimCE Cloud, zit momenteel in alpha en is eveneens gratis. Er komt een betalend aanbod naarmate het product rijpt; alphagebruikers worden ruim op voorhand verwittigd."
  - q: "Waarom een opensourceplatform voor energiegemeenschappen?"
    a: "Omdat een energiegemeenschap draait op het vertrouwen van haar leden, en dat vertrouwen moeilijk op te bouwen valt op een zwarte doos. De berekening van de verdeelsleutel bepaalt hoeveel elk lid ontvangt en betaalt: die kunnen auditeren is geen luxe voor ontwikkelaars, het is een bestuursvoorwaarde. Daar komt de economische realiteit bij — veel gemeenschappen zijn kleine structuren waarvoor een jaarlijkse propriëtaire licentie buiten verhouding is."
  - q: "Werkt OptimCE ook buiten België?"
    a: "De architectuur is ontworpen om zich aan te passen aan verschillende regelgevende kaders, wat van meet af aan noodzakelijk was: België alleen al telt drie verschillende gewestelijke regimes. Families van verdeelsleutels, statuten en facturatieregels zijn instelbaar. De ontwikkeling en validatie tot nu toe richten zich vooral op de Belgische context."
  - q: "Hoe kan ik bijdragen aan het project?"
    a: "Alles verloopt via de GitHub-organisatie OptimCE. De monorepo bundelt de verschillende diensten en bevat de orkestratieconfiguratie waarmee u de volledige stack lokaal opstart met Docker Compose. Codebijdragen zijn welkom, maar praktijkfeedback van gemeenschapsbeheerders evenzeer — zij hebben het product tot nu toe gevormd."
---

De meeste softwareplatformen ontstaan uit een commerciële intuïtie. OptimCE ontstond uit een **onderzoeksproject** — en die oorsprong verklaart zowat al de rest: de keuze voor opensource, de functionele omvang, en zelfs de manier waarop functies werden geprioriteerd.

## Locomotrice, een Waals onderzoeksproject

OptimCE is het softwareresultaat van **Locomotrice**, een onderzoeksproject dat tussen **2023 en 2026** in Wallonië liep en gefinancierd werd door het **Win2Wal**-programma van het Waalse Gewest. Dat programma financiert onderzoek van academische actoren met het oog op overdracht naar het regionale economische weefsel — onderzoek dus dat het laboratorium moet verlaten.

Drie groepen actoren droegen het project:

- de **Universiteit van Luik**, via haar **BEMS**-laboratorium;
- het onderzoekscentrum **CECOTEPE**;
- **burgerenergiecoöperaties**, aanwezig niet als eindgebruikers aan wie een werktuig wordt geleverd, maar als partners in de co-creatie.

Dat laatste weegt zwaarder dan het lijkt. Een energiegemeenschap is geen zuiver ingenieursprobleem: het is evenzeer een regelgevend, boekhoudkundig en sociaal object als een technisch. De ontwikkelde functies werden dus in het veld gevalideerd, met beheerders die al leden, meters en verdeelsleutels beheerden — meestal in rekenbladen.

## Het probleem dat het onderzoek blootlegde

De beginvaststelling is snel gezegd en lastig te beleven: **de administratieve complexiteit van een energiegemeenschap staat niet in verhouding tot haar omvang**.

Een gemeenschap van dertig gezinnen moet dezelfde objecten beheren als een energieleverancier — leveringspunten, kwartierwaarden, verdeelsleutels, facturatie, rapportering aan de netbeheerder — zonder de mankracht en zonder de systemen. En het toepasselijke kader ligt niet vast: in België is energie een gewestelijke bevoegdheid, waardoor Wallonië, Brussel en Vlaanderen drie verschillende kaders opleggen, met eigen regulatoren en eigen families van sleutels. Het Europese kader daarboven beschrijft ons artikel [“Energiegemeenschappen in Europa: RED II en IEMD”](/nl/nieuws/2026/03/05/energiegemeenschappen-europa/).

De beschikbare werktuigen waren ofwel rekenbladen — soepel maar niet auditeerbaar en snel onbeheersbaar — ofwel propriëtaire oplossingen ontworpen voor spelers van een heel andere schaal.

## Waarom opensource geen detail is

De beslissing om OptimCE opensource te publiceren, onder de **Apache 2.0**-licentie, volgt rechtstreeks uit de aard van wat er beheerd wordt.

Een energiegemeenschap draait op **vertrouwen tussen haar leden**. De verdeelsleutel bepaalt, kwartier na kwartier, hoeveel energie elk lid ontvangt en dus hoeveel het betaalt. Dertig gezinnen vragen om een zwarte doos te vertrouwen voor die berekening is veel gevraagd. De code kunnen openen is hier geen comfort voor ontwikkelaars: het is een **bestuursvoorwaarde**.

Daar komt een prozaïscher reden bij. Veel gemeenschappen zijn kleine, vrijwillige of half-vrijwillige structuren waarvoor een jaarlijkse propriëtaire licentie het budget ver overstijgt. Een werktuig dat u niet kunt betalen, lost geen enkel probleem op.

## Wat het platform vandaag doet

OptimCE dekt de volledige beheerscyclus van een gemeenschap:

- **Ledenbeheer** — onboarding, rollen, koppelingen tussen gemeenschappen en gebruikers;
- **Meteropvolging** — centralisatie van leveringspunten en meetwaarden;
- **Verdeelsleutels** — configuratie, historiek van aanhangsels en opvolging van de aanvaarding door de leden;
- **Sleutelgeneratie en -simulatie** — een geoptimaliseerde sleutel voorstellen op basis van echte data, en de prestatie meten vóór de vastlegging;
- **Facturatie** — van de prijs per kWh tot de pdf en de opvolging van betalingen;
- **Gemeenschapsleven** — nieuwsbord en polls, want participatief bestuur is evenzeer een regelgevende vereiste als goede praktijk;
- **Meerdere gemeenschappen** — één instantie voor verschillende gemeenschappen.

De architectuur is **gebeurtenisgestuurd en modulair**, waardoor modules van derden kunnen worden ingeplugd zonder de kern aan te raken — een keuze die rechtstreeks voortkomt uit de regelgevende onzekerheid: wat om de twee jaar verandert, moet kunnen veranderen zonder het platform te herschrijven.

## Twee manieren om het te gebruiken

**Zelf hosten**, onder de Apache 2.0-licentie, gratis en zonder beperking. U houdt de volledige controle over de data en neemt hosting, updates en beschikbaarheid zelf op. De werkwijze staat in [“OptimCE installeren: snelstartgids”](/nl/nieuws/2026/03/09/snelstartgids/).

**Via [OptimCE Cloud](https://app.optimce.be)**, de gehoste en beheerde versie, momenteel in alpha en gratis. Geen installatie, geen onderhoud.

De details van het project, zijn partners en zijn financiering staan op de pagina [Over ons](/nl/about/).

Sinds die lancering is het platform blijven evolueren: zie de [release van mei 2026](/nl/nieuws/2026/05/07/release-nieuws/), die het publieke register van deelacties en de gebruikersgids introduceerde.

## FAQ

### Wie ontwikkelt OptimCE?

OptimCE komt voort uit Locomotrice, een Waals onderzoeksproject dat liep van 2023 tot 2026 en gefinancierd werd door het Win2Wal-programma van het Waalse Gewest. Het wordt gedragen door de Universiteit van Luik, via haar BEMS-laboratorium, en door het onderzoekscentrum CECOTEPE, in samenwerking met burgerenergiecoöperaties. De ontwikkeling loopt vandaag opensource verder en staat open voor externe bijdragen.

### Is OptimCE gratis?

Het platform verschijnt onder de Apache 2.0-licentie: u mag het gratis en zonder beperking op uw eigen infrastructuur uitrollen. De gehoste versie, OptimCE Cloud, zit momenteel in alpha en is eveneens gratis. Er komt een betalend aanbod naarmate het product rijpt; alphagebruikers worden ruim op voorhand verwittigd.

### Waarom een opensourceplatform voor energiegemeenschappen?

Omdat een energiegemeenschap draait op het vertrouwen van haar leden, en dat vertrouwen moeilijk op te bouwen valt op een zwarte doos. De berekening van de verdeelsleutel bepaalt hoeveel elk lid ontvangt en betaalt: die kunnen auditeren is geen luxe voor ontwikkelaars, het is een bestuursvoorwaarde. Daar komt de economische realiteit bij — veel gemeenschappen zijn kleine structuren waarvoor een jaarlijkse propriëtaire licentie buiten verhouding is.

### Werkt OptimCE ook buiten België?

De architectuur is ontworpen om zich aan te passen aan verschillende regelgevende kaders, wat van meet af aan noodzakelijk was: België alleen al telt drie verschillende gewestelijke regimes. Families van verdeelsleutels, statuten en facturatieregels zijn instelbaar. De ontwikkeling en validatie tot nu toe richten zich vooral op de Belgische context.

### Hoe kan ik bijdragen aan het project?

Alles verloopt via de GitHub-organisatie OptimCE. De monorepo bundelt de verschillende diensten en bevat de orkestratieconfiguratie waarmee u de volledige stack lokaal opstart met Docker Compose. Codebijdragen zijn welkom, maar praktijkfeedback van gemeenschapsbeheerders evenzeer — zij hebben het product tot nu toe gevormd.

## Verder lezen

> **[Energiegemeenschappen in België: CER, CEC, CEL](/nl/nieuws/2026/05/11/energiegemeenschappen-belgie/)**
>
> De drie Belgische statuten, energiedelen, en de rol van de regulator en de netbeheerder.

> **[OptimCE installeren: snelstartgids](/nl/nieuws/2026/03/09/snelstartgids/)**
>
> De volledige stack lokaal uitrollen, of starten zonder iets te installeren.

<div class="post-cta" markdown="0">
  <h3>Ontdek OptimCE</h3>
  <p>Maakt u energiegemeenschap in enkele minuten aan op de gehoste versie, of rol het platform uit op uw eigen infrastructuur. De code is open, bijdragen zijn welkom.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="https://app.optimce.be">Open de OptimCE-app</a>
    <a class="btn btn-outline" href="https://github.com/optimce">Bekijk het project op GitHub</a>
  </p>
</div>
