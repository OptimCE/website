---
layout: page
title: "Opensource en zelf hosten"
breadcrumb_title: "Opensource"
subtitle: "Alle code onder de Apache 2.0-licentie: host OptimCE zelf, koppel het aan uw tools, of laat het door ons hosten."
description: "OptimCE is opensourcesoftware voor energiegemeenschappen onder de Apache 2.0-licentie: gratis zelf hosten, REST-API, NATS-events en vier talen."
lang: nl
ref: product-open-source
permalink: /nl/functies/open-source/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Is OptimCE echt opensource?"
    a: "Ja. Alle code is gepubliceerd onder de Apache 2.0-licentie, in de GitHub-organisatie optimce: geen afgeslankte versie, geen propriëtaire kern. De gehoste versie en de versie die u zelf installeert, geven toegang tot dezelfde functies."
  - q: "Mag u OptimCE in een professionele context gebruiken?"
    a: "Ja. De Apache 2.0-licentie staat toe de software te gebruiken, te wijzigen en te verspreiden, ook in een professionele context, op voorwaarde dat u de licentie- en auteursrechtvermeldingen behoudt."
  - q: "Wat is het verschil tussen OptimCE Cloud en zelf hosten?"
    a: "Wie de applicatie host. OptimCE Cloud draait op onze servers, zonder installatie of onderhoud, en is gratis tijdens de alfa. Als u zelf host, draait OptimCE op uw infrastructuur, gratis en zonder beperking, maar staat u zelf in voor de hosting, de updates en de beschikbaarheid."
  - q: "Hoe koppelt u OptimCE aan uw andere tools?"
    a: "Via zijn events of via zijn API. Een event-gestuurde architectuur (NATS) maakt het mogelijk tools van derden aan te sluiten, zoals een energiebeheersysteem, en met een REST-API integreert u OptimCE in uw eigen tools."
---

Een energiegemeenschap vertrouwt haar software heel wat toe: de lijst van haar leden, hun meters,
haar facturen en haar dossiers bij de regulator. Ze moet die software kunnen blijven gebruiken als de
leverancier van koers verandert, zelf kunnen kiezen waar ze wordt gehost en ze kunnen koppelen aan
haar andere tools. OptimCE is opensourcesoftware: alle code is gepubliceerd onder de Apache
2.0-licentie, en dezelfde applicatie draait op onze servers of op de uwe.

## Hoe OptimCE het aanpakt

### Alle code, onder de Apache 2.0-licentie

Er is geen afgeslankte versie en geen propriëtaire kern: alle code van OptimCE is gepubliceerd
onder de Apache 2.0-licentie, in de GitHub-organisatie [optimce](https://github.com/optimce). Die
licentie staat toe de software te gebruiken, te wijzigen en te verspreiden, ook in een
professionele context. In ruil vraagt ze dat u de licentie- en auteursrechtvermeldingen behoudt en
aangeeft welke bestanden u hebt gewijzigd.

Voor een gemeenschap betekent dat: ze is aan niemand gebonden. Bevalt OptimCE Cloud haar niet
meer, dan kan ze dezelfde applicatie elders laten draaien.

### Bij ons of bij u

Dezelfde software kunt u op twee manieren gebruiken.

- **OptimCE Cloud** is de gehoste versie, op app.optimce.be: niets te installeren, niets te
  onderhouden. Ze is gratis gedurende de hele alfafase.
- **Zelf hosten** betekent dat u OptimCE op uw eigen infrastructuur installeert, gratis en zonder
  beperking, voor altijd. De installatiegids beschrijft de lokale uitrol van de volledige stack met
  Docker Compose.

Beide wegen geven toegang tot dezelfde functies. De keuze hangt vooral af van wie u bent: een
gemeenschap die gewoon de tool wil, hoeft niets te installeren, terwijl een technisch team het
platform zelf kan hosten, de volledige controle over de gegevens kan houden of aan de code kan
bijdragen. Wat gratis is, en voor hoelang, staat op de pagina [prijzen]({{ "pricing" | ref_url }}).

### Eén installatie, meerdere gemeenschappen

Eén installatie van OptimCE beheert meerdere energiegemeenschappen. Een account kan tot meerdere
gemeenschappen behoren en van de ene naar de andere overschakelen vanuit “Mijn gemeenschappen”.
Een organisatie die meerdere projecten begeleidt, of die OptimCE voor anderen wil hosten, heeft dus
geen aparte installatie per gemeenschap nodig.

### Uw tools koppelen

Een event-gestuurde architectuur (NATS) maakt het mogelijk tools van derden op OptimCE aan te
sluiten, zoals een energiebeheersysteem. Met een REST-API integreert u OptimCE in uw eigen tools.
Een tool die de gemeenschap al gebruikt, kan zo gegevens uitwisselen met OptimCE in plaats van ze
opnieuw te laten invoeren, al vraagt dat wel integratiewerk.

### Een interface in vier talen

De interface bestaat in het Frans, Engels, Nederlands en Duits, wat belangrijk is in een land met
drie officiële talen. De e-mails die het platform verstuurt, bestaan in dezelfde vier talen.

### Bijdragen

De installatiegids richt zich ook tot teams die aan de code willen bijdragen: de volledige stack
start lokaal met Docker Compose. Vertalingen van de interface kunt u samen met anderen voorstellen
op [Weblate](https://hosted.weblate.org/engage/optimce/), zonder de code aan te raken.

## Wat het niet doet

**Geen dienstgarantie bij zelf hosten.** Op uw eigen servers staat u zelf in voor de hosting, de
updates en de beschikbaarheid: op dat pad wordt geen dienstgarantie geboden.

**De installatiegids beschrijft een ontwikkelstack.** De databanken ervan zijn niet persistent: de
gegevens worden gewist wanneer de containers herstarten. Voor een uitrol die moet blijven draaien,
configureert u zelf persistente volumes en een back-upstrategie.

**Opensource doet het werk niet in uw plaats.** Wie software host die ledengegevens verwerkt, heeft
iemand nodig die de installatie beheert. Zonder die persoon blijft OptimCE Cloud de eenvoudigste weg.

## Veelgestelde vragen {#faq}

### Is OptimCE echt opensource?

Ja. Alle code is gepubliceerd onder de Apache 2.0-licentie, in de GitHub-organisatie optimce: geen
afgeslankte versie, geen propriëtaire kern. De gehoste versie en de versie die u zelf installeert,
geven toegang tot dezelfde functies.

### Mag u OptimCE in een professionele context gebruiken?

Ja. De Apache 2.0-licentie staat toe de software te gebruiken, te wijzigen en te verspreiden, ook
in een professionele context, op voorwaarde dat u de licentie- en auteursrechtvermeldingen behoudt.

### Wat is het verschil tussen OptimCE Cloud en zelf hosten?

Wie de applicatie host. OptimCE Cloud draait op onze servers, zonder installatie of onderhoud, en
is gratis tijdens de alfa. Als u zelf host, draait OptimCE op uw infrastructuur, gratis en zonder
beperking, maar staat u zelf in voor de hosting, de updates en de beschikbaarheid.

### Hoe koppelt u OptimCE aan uw andere tools?

Via zijn events of via zijn API. Een event-gestuurde architectuur (NATS) maakt het mogelijk tools
van derden aan te sluiten, zoals een energiebeheersysteem, en met een REST-API integreert u OptimCE
in uw eigen tools.

## Verder lezen

- [OptimCE installeren: snelstartgids]({{ "quick-start-guide" | ref_url }}): de vereisten, het
  klonen van de repository en de eerste start, stap voor stap.
- [Prijzen van OptimCE]({{ "pricing" | ref_url }}): wat vandaag gratis is, en wat kan veranderen.
- [Beheersoftware voor energiegemeenschappen]({{ "features" | ref_url }}): alles wat OptimCE
  vandaag doet.

{% include product-cta.html page_key="open-source" guide="getting-started" title="OptimCE uitproberen zonder iets te installeren" %}
