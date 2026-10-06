---
layout: page
title: "Functies van het OptimCE-platform"
subtitle: "Wat het platform vandaag doet om een energiegemeenschap te beheren, van de toetreding van leden tot de factuur."
description: "Leden, meters, gegenereerde en gesimuleerde verdeelsleutels, facturatie, CWaPE-documenten, polls: wat OptimCE doet, opensource en gratis tijdens de alfa."
lang: nl
ref: features
permalink: /nl/functies/
last_modified_at: 2026-09-26
feature_list:
  - "Beheer van leden, leveringspunten en meters"
  - "Bewaarde versies van verdeelsleutels, met opvolging van de aanvaarding door de leden"
  - "Automatische generatie van verdeelsleutels (doorlopen van de standaardsleutels, LOGAAS)"
  - "Simulatie van een verdeelsleutel op uw eigen gegevens"
  - "Facturatie van gedeelde energie (eerste versie, Waals kader)"
  - "Vooraf ingevulde administratieve documenten van de CWaPE en opvolging van termijnen"
  - "E-mailmeldingen in vier talen"
  - "Nieuwsbord en polls"
  - "Publiek register van deelacties"
  - "Meerdere gemeenschappen, event-gestuurde integratie, REST-API"
---

OptimCE is een opensourceplatform voor het beheer van energiegemeenschappen. Deze pagina beschrijft
wat het **vandaag** doet, in zijn alfaversie, zonder iets aan te kondigen wat nog niet is
opgeleverd. De [gebruikershandleiding](https://guide.optimce.be) licht daarna elk scherm toe.

## Leden, meters en gemeenschappen

- **Ledenbeheer**: onboarding van nieuwe leden, rollen, koppelingen tussen gebruikers en
  gemeenschappen.
- **Leveringspunten en meters**: de leden, hun leveringspunten, hun installaties en hun meters
  staan op één plek. De deelnemerslijst, één keer bijgehouden, voedt daarna de administratieve
  documenten en de facturatie.
- **Meerdere gemeenschappen, één instantie**: één installatie van OptimCE beheert meerdere
  energiegemeenschappen.

## Verdeelsleutels: instellen, genereren, simuleren

De verdeelsleutel bepaalt, kwartier per kwartier, wie welk deel van de lokale productie krijgt.
OptimCE dekt de hele levenscyclus ervan af.

- **Instelling en aanhangsels**: elke versie van de sleutel wordt bewaard en de aanvaarding door
  de leden wordt opgevolgd.
- **Automatische generatie**: op basis van een CSV-bestand met verbruik en productie per kwartier
  stelt de module een kandidaat-sleutel voor, met de verwachte collectieve zelfverbruiksgraad. Er
  zijn twee algoritmen: het volledig doorlopen van de standaardsleutels van uw regio, en LOGAAS,
  voortgekomen uit het onderzoek van het CeCoTePe binnen het project Locomotrice. Het voorstel gaat
  nooit vanzelf naar de netbeheerder: het volgt de gebruikelijke weg van het aanhangsel.
- **Simulatie**: test een sleutel naar keuze op uw eigen gegevens en lees het zelfverbruik, het
  overschot, de zelfvoorzieningsgraad en de deelgraad af, globaal, per tijdstap en per iteratie,
  zonder de toegepaste sleutel te raken.

Verder lezen: [een optimale verdeelsleutel genereren]({{ "optimce-allocation-key-generator" | ref_url }})
en [een sleutel op uw gegevens simuleren]({{ "optimce-allocation-key-simulation" | ref_url }}).

## Facturatie van gedeelde energie

De eerste versie van de facturatiemodule is ontworpen voor het Waalse kader.

- U legt uw prijzen vast in €/kWh: een verkoopprijs voor de gedeelde energie en een
  terugkoopprijs voor de injectie, voor de hele gemeenschap, per klantensegment of per
  leveringspunt, met een geldigheidsperiode.
- Een facturatiecyclus maakt op basis van de geïmporteerde verdeelgegevens een ontwerp per lid.
  Eenmaal uitgereikt krijgt elk document een nummer in een doorlopende nummering en een
  gestructureerde mededeling.
- Er worden drie documenten als pdf aangemaakt: de factuur, de creditnota en de
  vergoedingsafrekening van de producenten.
- De opvolging van de betalingen is ingebouwd, deelbetalingen inbegrepen, en elk lid vindt zijn
  facturen terug in de applicatie.

De details staan in [de aankondiging van de facturatiemodule]({{ "optimce-billing" | ref_url }}).

## Administratieve documenten en termijnen

Voor Waalse gemeenschappen bereidt OptimCE de documenten van de CWaPE voor op basis van de
officiële, ongewijzigde bestanden: elf pakketten invulbare pdf's, Excel-werkmappen en
Word-overeenkomsten, vooraf ingevuld met de gegevens van de gemeenschap. Velden die het platform
niet kan afleiden, blijven bewerkbaar.

- Elk dossier en elk document doorlopen statussen die in een logboek worden vastgelegd: een
  correctie komt erbij, ze wist niets.
- De termijnen worden berekend in werkdagen volgens de Belgische kalender en getoond op het
  dashboard van de beheerder.
- E-mails, in het Frans, Nederlands, Duits en Engels, melden uitnodigingen, facturen en
  administratieve termijnen.
- Elk lid kan inzien wat er over hem of haar aan de regulator is gemeld.

OptimCE dient niets in en ondertekent niets in uw plaats: het indienen blijft uw zaak. Zie
[de CWaPE-documenten en termijnen]({{ "cwape-administrative-documents" | ref_url }}).

## De gemeenschap levend houden

Een nieuwsbord informeert de leden, polls raadplegen hen. Er zijn drie modi voor de zichtbaarheid
van de resultaten: anoniem, transparant, of resultaten pas bij de afsluiting. Een geavanceerde
modus regelt apart wat de beheerder en wat de leden zien. Zie
[leden van een energiegemeenschap betrekken]({{ "engage-energy-community" | ref_url }}).

## Publiek register van deelacties

Een beheerder kan zijn deelactie publiceren in een publiek register dat in de applicatie is
ingebouwd. Iedereen kan het doorzoeken om een deelactie te vinden die openstaat voor nieuwe leden.

## Een open platform

- **Opensource**: alle code is gepubliceerd onder de licentie Apache 2.0.
- **Zelf hosten**: u kunt OptimCE gratis en zonder beperking op uw eigen infrastructuur
  installeren. De stappen staan in [de installatiegids]({{ "quick-start-guide" | ref_url }}).
- **OptimCE Cloud**: de gehoste versie is gratis gedurende de hele alfafase. Later kan er een
  betalend aanbod komen; de alfagebruikers worden ruim vooraf verwittigd, en zelf hosten blijft
  gratis.
- **Integraties**: een event-gestuurde architectuur (NATS) maakt het mogelijk tools van derden aan
  te sluiten, zoals een energiebeheersysteem, en met een REST-API integreert u OptimCE in uw eigen
  tools.
- **Meertalig**: de interface bestaat in het Frans, Engels, Nederlands en Duits.

## Wat het platform niet doet

OptimCE werkt met de verdeelgegevens die de netbeheerder doorstuurt en met de bestanden die u
importeert: het toont geen realtimegegevens. Het dient uw documenten niet in bij de CWaPE en
ondertekent uw overeenkomsten niet. De facturatie dekt voorlopig alleen het Waalse kader.

<div class="post-cta" markdown="0">
  <h2>Een gemeenschap beheren of oprichten met OptimCE</h2>
  <p>De applicatie is gratis tijdens de alfa. Maak uw gemeenschap aan, nodig uw leden uit en stel
  uw verdeelsleutel in; de gebruikershandleiding begeleidt u scherm per scherm.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="{{ site.cta.app_url }}">De applicatie openen</a>
    <a class="btn btn-outline" href="https://guide.optimce.be">De gebruikershandleiding lezen</a>
    <a class="btn btn-outline" href="https://github.com/{{ site.github_username }}">De code op GitHub bekijken</a>
  </p>
</div>
