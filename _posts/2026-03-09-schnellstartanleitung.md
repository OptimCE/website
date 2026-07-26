---
layout: post
title: "OptimCE installieren: Schnellstart"
date: 2026-03-09 14:00:00 +0100
last_modified_at: 2026-07-26 10:00:00 +0200
author: "OptimCE-Team"
excerpt: "Zwei Wege zum Start mit OptimCE: die gehostete Version ohne jede Installation oder das lokale Deployment der gesamten Stack mit Docker Compose. Voraussetzungen, Klonen mit Submodulen, Umgebungsvariablen und erster Start — Schritt für Schritt."
description: "Voraussetzungen, Repository klonen, Umgebungsvariablen und erster Start: OptimCE lokal installieren, Schritt für Schritt."
tags: [app, guide]
lang: de
ref: quick-start-guide
permalink: /de/aktuelles/2026/03/09/schnellstartanleitung/
faq:
  - q: "Muss ich OptimCE installieren, um es zu nutzen?"
    a: "Nein. OptimCE Cloud ist die gehostete und verwaltete Version: Sie legen ein Konto an und starten — ohne Installation, ohne Wartung. Die lokale Installation richtet sich an Teams, die die Plattform auf eigener Infrastruktur betreiben, die volle Kontrolle über ihre Daten behalten oder zum Code beitragen wollen. Beide Wege bieten denselben Funktionsumfang."
  - q: "Was brauche ich für die lokale Installation von OptimCE?"
    a: "Nur drei Dinge: Docker, Docker Compose und Git. Die gesamte Stack — Anwendungen, PostgreSQL-Datenbanken, Keycloak, API-Gateway, Objektspeicher und Messaging — wird über Docker Compose aus dem Monorepo orchestriert. Node.js, Python oder PostgreSQL müssen Sie nicht separat auf Ihrem Rechner installieren."
  - q: "Warum muss mit --recurse-submodules geklont werden?"
    a: "Weil das OptimCE-Monorepo die einzelnen Dienste als Git-Submodule zusammenfasst: CRM-Frontend und -Backend, Generierung und Simulation von Aufteilungsschlüsseln, Abrechnung, Dokumentenerzeugung und Nachrichtenboard. Ohne --recurse-submodules erhalten Sie zwar die Orchestrierungskonfiguration, aber keinen Anwendungscode. Wurde bereits ohne geklont, hilft git submodule update --init --recursive."
  - q: "Bleiben die Daten der Entwicklungs-Stack erhalten?"
    a: "Nein. In der Entwicklungskonfiguration sind die Datenbanken nicht persistent: Beim Neustart der Container werden die Daten zurückgesetzt. Das ist beabsichtigt und garantiert für jeden Test eine saubere Umgebung. Ein dauerhaftes Deployment erfordert persistente Volumes und eine Sicherungsstrategie."
  - q: "Unter welcher Lizenz steht OptimCE?"
    a: "Unter der Apache-2.0-Lizenz. Sie dürfen die Plattform kostenlos und uneingeschränkt auf eigener Infrastruktur betreiben, auch im professionellen Umfeld. Im Gegenzug bedeutet Self-Hosting, dass Sie Betrieb, Updates und Verfügbarkeit selbst verantworten: Auf diesem Weg wird keine Servicegarantie gegeben."
---

Es gibt zwei Wege, mit OptimCE zu starten, und welcher richtig ist, hängt vor allem davon ab, wer Sie sind.

Wenn Sie eine Energiegemeinschaft verwalten und einfach das Werkzeug brauchen, ist **[OptimCE Cloud](https://app.optimce.be)** die gehostete Version: keine Installation, keine Wartung, und in der Alpha-Phase derzeit kostenlos. Gehen Sie direkt zum [Benutzerhandbuch](https://guide.optimce.be).

Wenn Sie ein technisches Team sind, das die Plattform selbst betreiben, die volle Datenhoheit behalten oder zum Code beitragen will, ist diese Anleitung für Sie. Sie beschreibt das lokale Deployment der gesamten Stack.

## Was Sie deployen werden

OptimCE ist keine monolithische Anwendung, sondern ein **Ökosystem aus Microservices**, das aus einem zentralen Repository heraus orchestriert wird — dem [Monorepo](https://github.com/optimce/monorepo). Der Start bringt Folgendes hoch:

- **sieben Anwendungen** — CRM-Frontend und -Backend, Generierung von Aufteilungsschlüsseln, Schlüsselsimulation, Abrechnung, Dokumentenerzeugung und Nachrichtenboard;
- **sechs PostgreSQL-Datenbanken**, eine je Fachdomäne;
- die **Plattformdienste**: Keycloak für die Authentifizierung, KrakenD als API-Gateway, Nginx als Reverse Proxy, MinIO für Objektspeicher, NATS für Messaging und Jaeger für Tracing.

Diese Architektur erklärt die Werkzeugwahl im nächsten Abschnitt: Sie installieren die Komponenten nicht einzeln, sondern überlassen das Docker Compose.

## Voraussetzungen

Drei Werkzeuge, sonst nichts:

- **Docker**
- **Docker Compose**
- **Git**

Node.js, Python oder PostgreSQL brauchen Sie auf Ihrem Rechner nicht: Jeder Dienst bringt seine eigene Laufzeitumgebung im Container mit.

## 1. Repository klonen

Das Monorepo fasst die Dienste als **Git-Submodule** zusammen. `--recurse-submodules` ist daher nicht optional:

```bash
git clone --recurse-submodules https://github.com/OptimCE/monorepo.git
cd monorepo
```

Wurde bereits ohne Submodule geklont, haben Sie die Orchestrierungskonfiguration, aber keinen Anwendungscode. Nachholen mit:

```bash
git submodule update --init --recursive
```

## 2. Umgebungsvariablen konfigurieren

Setzen Sie vor dem ersten Start die Passwörter in der Datei `.env.dev`:

```
DB_PASSWORD=changeme_db_password
KEYCLOAK_DB_PASSWORD=changeme_keycloak_db_password
KEYCLOAK_ADMIN_PASSWORD=changeme_keycloak_admin_password
```

Ändern Sie diese Werte — auch lokal. Ein stehen gelassenes Demo-Passwort ist der banalste Weg, eine Instanz offenzulegen, die privat bleiben sollte.

Die CRM-Datenbank initialisiert sich beim ersten Start automatisch über das Skript `crm-backend/database_script/init.sql`.

## 3. Stack starten

Der empfohlene Weg führt über das mitgelieferte Skript:

```bash
chmod +x ./docker-stack.sh
./docker-stack.sh start
```

Wer Docker Compose lieber direkt steuert:

```bash
docker compose --env-file .env.dev -f docker-compose.dev.yml --profile dev up -d
```

Und um die Images vorher neu zu bauen:

```bash
docker compose --env-file .env.dev -f docker-compose.dev.yml --profile dev up --build
```

> **Achtung — die Daten sind nicht persistent.** In der Entwicklungskonfiguration werden die Datenbanken beim Neustart der Container zurückgesetzt. Das ist eine bewusste Entscheidung und sichert für jeden Test eine saubere Umgebung. Ein dauerhaftes Deployment verlangt persistente Volumes und eine Sicherungsstrategie.

## 4. Erste Gemeinschaft anlegen

Sobald die Stack läuft, melden Sie sich an der Verwaltungsoberfläche an. Die Authentifizierung läuft über **Keycloak**: Nutzen Sie das Administratorkonto, dessen Passwort Sie in Schritt 2 gesetzt haben.

Die Reihenfolge der Inbetriebnahme entspricht danach der gehosteten Version:

1. Gemeinschaft anlegen und ihre rechtlichen Angaben erfassen;
2. Mitglieder hinzufügen und ihre **Lieferstellen** (EAN) zuordnen;
3. den **Aufteilungsschlüssel** der Teilungsoperation festlegen;
4. die Berechnung über einen Testzeitraum prüfen, bevor sie an den Netzbetreiber übermittelt wird.

Die fachlichen Details jedes Schritts behandelt das [Benutzerhandbuch](https://guide.optimce.be), das die aktuelle Referenz für die Nutzung der Anwendung bleibt.

## Weiterführend

Wenn Ihnen das Thema neu ist und nicht das Werkzeug, beginnen Sie beim Rahmen:

> **[Energiegemeinschaften in Belgien: CER, CEC, CEL](/de/aktuelles/2026/05/11/energiegemeinschaften-belgien/)**
>
> Die drei Status, die Energieteilung und die Rolle von Regulator und Netzbetreiber.

> **[Aufteilungsschlüssel automatisch generieren](/de/aktuelles/2026/05/26/automatische-verteilungsschluessel-generierung/)**
>
> Wie das Generierungsmodul aus Ihren realen Daten einen Schlüssel vorschlägt.

## FAQ

### Muss ich OptimCE installieren, um es zu nutzen?

Nein. OptimCE Cloud ist die gehostete und verwaltete Version: Sie legen ein Konto an und starten — ohne Installation, ohne Wartung. Die lokale Installation richtet sich an Teams, die die Plattform auf eigener Infrastruktur betreiben, die volle Kontrolle über ihre Daten behalten oder zum Code beitragen wollen. Beide Wege bieten denselben Funktionsumfang.

### Was brauche ich für die lokale Installation von OptimCE?

Nur drei Dinge: Docker, Docker Compose und Git. Die gesamte Stack — Anwendungen, PostgreSQL-Datenbanken, Keycloak, API-Gateway, Objektspeicher und Messaging — wird über Docker Compose aus dem Monorepo orchestriert. Node.js, Python oder PostgreSQL müssen Sie nicht separat auf Ihrem Rechner installieren.

### Warum muss mit `--recurse-submodules` geklont werden?

Weil das OptimCE-Monorepo die einzelnen Dienste als Git-Submodule zusammenfasst: CRM-Frontend und -Backend, Generierung und Simulation von Aufteilungsschlüsseln, Abrechnung, Dokumentenerzeugung und Nachrichtenboard. Ohne `--recurse-submodules` erhalten Sie zwar die Orchestrierungskonfiguration, aber keinen Anwendungscode. Wurde bereits ohne geklont, hilft `git submodule update --init --recursive`.

### Bleiben die Daten der Entwicklungs-Stack erhalten?

Nein. In der Entwicklungskonfiguration sind die Datenbanken nicht persistent: Beim Neustart der Container werden die Daten zurückgesetzt. Das ist beabsichtigt und garantiert für jeden Test eine saubere Umgebung. Ein dauerhaftes Deployment erfordert persistente Volumes und eine Sicherungsstrategie.

### Unter welcher Lizenz steht OptimCE?

Unter der Apache-2.0-Lizenz. Sie dürfen die Plattform kostenlos und uneingeschränkt auf eigener Infrastruktur betreiben, auch im professionellen Umfeld. Im Gegenzug bedeutet Self-Hosting, dass Sie Betrieb, Updates und Verfügbarkeit selbst verantworten: Auf diesem Weg wird keine Servicegarantie gegeben.

<div class="post-cta" markdown="0">
  <h3>Keine Lust auf Installation? Nutzen Sie OptimCE Cloud</h3>
  <p>Die gehostete Version ist während der Alpha kostenlos: keine Installation, keine Wartung, derselbe Funktionsumfang. Legen Sie Ihre Gemeinschaft in wenigen Minuten an oder durchsuchen Sie die offenen Teilungsoperationen.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="https://app.optimce.be">OptimCE-Anwendung öffnen</a>
    <a class="btn btn-outline" href="https://github.com/optimce/monorepo">Monorepo auf GitHub ansehen</a>
  </p>
</div>

## Quellen

- [OptimCE — Monorepo](https://github.com/optimce/monorepo) — Orchestrierungskonfiguration, Skript `docker-stack.sh` und maßgebliche Installationsanweisungen.
- [OptimCE — GitHub-Organisation](https://github.com/optimce) — sämtliche Dienste und ihre jeweiligen Repositories.
- [OptimCE-Benutzerhandbuch](https://guide.optimce.be) — aktuelle fachliche Referenz für die Nutzung der Anwendung.
