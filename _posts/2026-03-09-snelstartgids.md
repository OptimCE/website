---
layout: post
title: "OptimCE installeren: snelstartgids"
date: 2026-03-09 14:00:00 +0100
last_modified_at: 2026-07-26 10:00:00 +0200
author: "OptimCE-team"
excerpt: "Twee manieren om met OptimCE te starten: de gehoste versie, zonder iets te installeren, of een lokale uitrol van de volledige stack met Docker Compose. Vereisten, klonen met submodules, omgevingsvariabelen en eerste start, stap voor stap."
description: "Vereisten, repository klonen, omgevingsvariabelen en eerste start: OptimCE lokaal installeren, stap voor stap."
tags: [app, guide]
lang: nl
ref: quick-start-guide
permalink: /nl/nieuws/2026/03/09/snelstartgids/
faq:
  - q: "Moet ik OptimCE installeren om het te gebruiken?"
    a: "Nee. OptimCE Cloud is de gehoste en beheerde versie: u maakt een account aan en gaat van start, zonder installatie en zonder onderhoud. De lokale installatie is bedoeld voor teams die het platform op hun eigen infrastructuur willen draaien, de volledige controle over hun data willen houden of aan de code willen bijdragen. Beide bieden dezelfde functionaliteit."
  - q: "Wat heb ik nodig om OptimCE lokaal te installeren?"
    a: "Slechts drie dingen: Docker, Docker Compose en Git. De volledige stack — applicaties, PostgreSQL-databanken, Keycloak, API-gateway, objectopslag en messaging — wordt via Docker Compose vanuit de monorepo georkestreerd. U hoeft Node.js, Python of PostgreSQL niet apart op uw machine te installeren."
  - q: "Waarom moet ik klonen met --recurse-submodules?"
    a: "Omdat de OptimCE-monorepo de afzonderlijke diensten bundelt als Git-submodules: CRM-frontend en -backend, generatie en simulatie van verdeelsleutels, facturatie, documentgeneratie en het nieuwsbord. Zonder --recurse-submodules krijgt u de orkestratieconfiguratie maar geen applicatiecode. Hebt u al zonder gekloond, dan lost git submodule update --init --recursive het op."
  - q: "Blijven de gegevens van de ontwikkelstack bewaard?"
    a: "Nee. In de ontwikkelconfiguratie zijn de databanken niet persistent: bij het herstarten van de containers worden de gegevens gewist. Dat is bewust zo — het garandeert een schone omgeving bij elke test. Een uitrol die moet blijven draaien vereist persistente volumes en een back-upstrategie."
  - q: "Onder welke licentie staat OptimCE?"
    a: "Onder de Apache 2.0-licentie. U mag het platform gratis en zonder beperking op uw eigen infrastructuur uitrollen, ook in een professionele context. Als tegenprestatie voor die vrijheid betekent zelf hosten dat u zelf instaat voor hosting, updates en beschikbaarheid: op dat pad wordt geen dienstgarantie geboden."
---

Er zijn twee manieren om met OptimCE te starten, en welke de juiste is hangt vooral af van wie u bent.

Beheert u een energiegemeenschap en wilt u gewoon het gereedschap, dan is **[OptimCE Cloud](https://app.optimce.be)** de gehoste versie: geen installatie, geen onderhoud, en tijdens de alpha momenteel gratis. Ga meteen naar de [gebruikersgids](https://guide.optimce.be).

Bent u een technisch team dat het platform zelf wil draaien, de volledige controle over de data wil houden of aan de code wil bijdragen, dan is deze gids voor u. Hij beschrijft de lokale uitrol van de volledige stack.

## Wat u gaat uitrollen

OptimCE is geen monolithische applicatie maar een **ecosysteem van microservices**, georkestreerd vanuit één centrale repository: de [monorepo](https://github.com/optimce/monorepo). Bij het opstarten komen omhoog:

- **zeven applicaties** — CRM-frontend en -backend, generatie van verdeelsleutels, sleutelsimulatie, facturatie, documentgeneratie en het nieuwsbord;
- **zes PostgreSQL-databanken**, één per functioneel domein;
- de **platformdiensten**: Keycloak voor authenticatie, KrakenD als API-gateway, Nginx als reverse proxy, MinIO voor objectopslag, NATS voor messaging en Jaeger voor tracing.

Die architectuur verklaart de gereedschapskeuze in de volgende sectie: u installeert de componenten niet één voor één, u laat Docker Compose het werk doen.

## Vereisten

Drie tools, en verder niets:

- **Docker**
- **Docker Compose**
- **Git**

Node.js, Python of PostgreSQL hoeft u niet op uw machine te installeren: elke dienst brengt zijn eigen runtime mee in zijn container.

## 1. De repository klonen

De monorepo bundelt de diensten als **Git-submodules**. `--recurse-submodules` is dus niet optioneel:

```bash
git clone --recurse-submodules https://github.com/OptimCE/monorepo.git
cd monorepo
```

Hebt u al zonder submodules gekloond, dan hebt u de orkestratieconfiguratie maar geen applicatiecode. Herstel met:

```bash
git submodule update --init --recursive
```

## 2. De omgevingsvariabelen instellen

Stel vóór de eerste start de wachtwoorden in het bestand `.env.dev` in:

```
DB_PASSWORD=changeme_db_password
KEYCLOAK_DB_PASSWORD=changeme_keycloak_db_password
KEYCLOAK_ADMIN_PASSWORD=changeme_keycloak_admin_password
```

Wijzig deze waarden, ook lokaal. Een demowachtwoord dat blijft staan is de meest banale manier om een instantie bloot te leggen die privé had moeten blijven.

De CRM-databank initialiseert zich bij de eerste start automatisch via het script `crm-backend/database_script/init.sql`.

## 3. De stack starten

De aanbevolen weg loopt via het meegeleverde script:

```bash
chmod +x ./docker-stack.sh
./docker-stack.sh start
```

Wie Docker Compose liever rechtstreeks aanstuurt:

```bash
docker compose --env-file .env.dev -f docker-compose.dev.yml --profile dev up -d
```

En om de images eerst te herbouwen:

```bash
docker compose --env-file .env.dev -f docker-compose.dev.yml --profile dev up --build
```

> **Let op — de gegevens zijn niet persistent.** In de ontwikkelconfiguratie worden de databanken bij het herstarten van de containers gewist. Dat is een bewuste keuze die bij elke test een schone omgeving waarborgt. Een blijvende uitrol vereist persistente volumes en een back-upstrategie.

## 4. Uw eerste gemeenschap aanmaken

Zodra de stack draait, meldt u zich aan op de beheerinterface. De authenticatie verloopt via **Keycloak**: gebruik het beheerdersaccount waarvan u in stap 2 het wachtwoord hebt ingesteld.

De volgorde van ingebruikname is daarna dezelfde als op de gehoste versie:

1. de gemeenschap aanmaken en haar juridische gegevens invullen;
2. de leden toevoegen en hun **leveringspunten** (EAN) koppelen;
3. de **verdeelsleutel** van de deelactie vastleggen;
4. de berekening over een testperiode nakijken voordat ze naar de netbeheerder gaat.

De functionele details van elke stap staan in de [gebruikersgids](https://guide.optimce.be), die de actuele referentie blijft voor het gebruik van de applicatie.

## Verder lezen

Is het onderwerp nieuw voor u in plaats van het gereedschap, begin dan bij het kader:

> **[Energiegemeenschappen in België: CER, CEC, CEL](/nl/nieuws/2026/05/11/energiegemeenschappen-belgie/)**
>
> De drie statuten, energiedelen, en de rol van de regulator en de netbeheerder.

> **[Verdeelsleutel automatisch genereren](/nl/nieuws/2026/05/26/automatische-verdeelsleutel-generatie/)**
>
> Hoe de generatiemodule op basis van uw echte data een sleutel voorstelt.

## FAQ

### Moet ik OptimCE installeren om het te gebruiken?

Nee. OptimCE Cloud is de gehoste en beheerde versie: u maakt een account aan en gaat van start, zonder installatie en zonder onderhoud. De lokale installatie is bedoeld voor teams die het platform op hun eigen infrastructuur willen draaien, de volledige controle over hun data willen houden of aan de code willen bijdragen. Beide bieden dezelfde functionaliteit.

### Wat heb ik nodig om OptimCE lokaal te installeren?

Slechts drie dingen: Docker, Docker Compose en Git. De volledige stack — applicaties, PostgreSQL-databanken, Keycloak, API-gateway, objectopslag en messaging — wordt via Docker Compose vanuit de monorepo georkestreerd. U hoeft Node.js, Python of PostgreSQL niet apart op uw machine te installeren.

### Waarom moet ik klonen met `--recurse-submodules`?

Omdat de OptimCE-monorepo de afzonderlijke diensten bundelt als Git-submodules: CRM-frontend en -backend, generatie en simulatie van verdeelsleutels, facturatie, documentgeneratie en het nieuwsbord. Zonder `--recurse-submodules` krijgt u de orkestratieconfiguratie maar geen applicatiecode. Hebt u al zonder gekloond, dan lost `git submodule update --init --recursive` het op.

### Blijven de gegevens van de ontwikkelstack bewaard?

Nee. In de ontwikkelconfiguratie zijn de databanken niet persistent: bij het herstarten van de containers worden de gegevens gewist. Dat is bewust zo — het garandeert een schone omgeving bij elke test. Een uitrol die moet blijven draaien vereist persistente volumes en een back-upstrategie.

### Onder welke licentie staat OptimCE?

Onder de Apache 2.0-licentie. U mag het platform gratis en zonder beperking op uw eigen infrastructuur uitrollen, ook in een professionele context. Als tegenprestatie voor die vrijheid betekent zelf hosten dat u zelf instaat voor hosting, updates en beschikbaarheid: op dat pad wordt geen dienstgarantie geboden.

<div class="post-cta" markdown="0">
  <h3>Liever niet installeren? Gebruik OptimCE Cloud</h3>
  <p>De gehoste versie is gratis tijdens de alpha: geen installatie, geen onderhoud, dezelfde functionaliteit. Maakt u gemeenschap aan in enkele minuten of doorblader de open deelacties.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="https://app.optimce.be">Open de OptimCE-app</a>
    <a class="btn btn-outline" href="https://github.com/optimce/monorepo">Bekijk de monorepo op GitHub</a>
  </p>
</div>

## Bronnen

- [OptimCE — monorepo](https://github.com/optimce/monorepo) — orkestratieconfiguratie, het script `docker-stack.sh` en de gezaghebbende installatie-instructies.
- [OptimCE — GitHub-organisatie](https://github.com/optimce) — alle diensten en hun respectieve repositories.
- [OptimCE-gebruikersgids](https://guide.optimce.be) — actuele functionele referentie voor het gebruik van de applicatie.
