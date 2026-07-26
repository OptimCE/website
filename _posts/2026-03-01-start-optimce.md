---
layout: post
title: "Start von OptimCE: die Ursprünge des Projekts"
date: 2026-03-01 10:00:00 +0100
last_modified_at: 2026-07-26 10:00:00 +0200
author: "OptimCE-Team"
excerpt: "OptimCE ist nicht in einem Inkubator entstanden, sondern in einem Labor. Ein Rückblick auf Locomotrice, das wallonische Forschungsprojekt hinter der Plattform, auf die beteiligten Partner und auf die Gründe für die Veröffentlichung als Open Source."
description: "Woher OptimCE kommt: das Forschungsprojekt Locomotrice, die Partner Universität Lüttich und CECOTEPE, und warum es quelloffen ist."
tags: [app, announcement]
lang: de
ref: launch-optimce
permalink: /de/aktuelles/2026/03/01/start-optimce/
faq:
  - q: "Wer entwickelt OptimCE?"
    a: "OptimCE ging aus Locomotrice hervor, einem wallonischen Forschungsprojekt der Jahre 2023 bis 2026, gefördert durch das Programm Win2Wal der Wallonischen Region. Getragen wird es von der Universität Lüttich mit ihrem BEMS-Labor und vom Forschungszentrum CECOTEPE, in Zusammenarbeit mit Bürgerenergiegenossenschaften. Die Entwicklung läuft heute quelloffen weiter und steht externen Beiträgen offen."
  - q: "Ist OptimCE kostenlos?"
    a: "Die Plattform steht unter der Apache-2.0-Lizenz: Sie können sie kostenlos und uneingeschränkt auf eigener Infrastruktur betreiben. Die gehostete Version OptimCE Cloud befindet sich derzeit in der Alpha-Phase und ist ebenfalls kostenlos. Ein kostenpflichtiges Angebot entsteht mit der Reife des Produkts; Alpha-Nutzer werden rechtzeitig informiert."
  - q: "Warum eine Open-Source-Plattform für Energiegemeinschaften?"
    a: "Weil eine Energiegemeinschaft auf dem Vertrauen ihrer Mitglieder beruht und sich dieses Vertrauen schwer auf einer Blackbox aufbauen lässt. Die Berechnung des Aufteilungsschlüssels bestimmt, wie viel jedes Mitglied erhält und zahlt: Sie prüfen zu können, ist kein Entwicklerluxus, sondern eine Governance-Voraussetzung. Hinzu kommt die wirtschaftliche Realität — viele Gemeinschaften sind kleine Strukturen, für die eine jährliche proprietäre Lizenz unverhältnismäßig ist."
  - q: "Funktioniert OptimCE auch außerhalb Belgiens?"
    a: "Die Architektur wurde von Anfang an für unterschiedliche Regulierungsrahmen ausgelegt — schon deshalb, weil Belgien allein drei regionale Regime kennt. Schlüsselfamilien, Status und Abrechnungsregeln sind konfigurierbar. Entwicklung und Validierung konzentrieren sich bislang vor allem auf den belgischen Kontext."
  - q: "Wie kann ich zum Projekt beitragen?"
    a: "Alles läuft über die GitHub-Organisation OptimCE. Das Monorepo bündelt die einzelnen Dienste und enthält die Orchestrierungskonfiguration, mit der sich die gesamte Stack lokal per Docker Compose starten lässt. Code-Beiträge sind willkommen, Rückmeldungen von Gemeinschaftsverwaltern aus der Praxis aber ebenso — sie haben das Produkt bisher geprägt."
---

Die meisten Softwareplattformen entstehen aus einer geschäftlichen Intuition. OptimCE entstand aus einem **Forschungsprojekt** — und dieser Ursprung erklärt fast alles Weitere: die Entscheidung für Open Source, den Funktionsumfang und sogar die Priorisierung der Features.

## Locomotrice, ein wallonisches Forschungsprojekt

OptimCE ist das Softwareergebnis von **Locomotrice**, einem Forschungsprojekt, das zwischen **2023 und 2026** in der Wallonie durchgeführt und über das Programm **Win2Wal** der Wallonischen Region gefördert wurde. Dieses Programm finanziert Forschung akademischer Akteure mit dem Ziel des Transfers in die regionale Wirtschaft — Forschung also, die das Labor verlassen soll.

Drei Gruppen von Akteuren trugen das Projekt:

- die **Universität Lüttich** mit ihrem Labor **BEMS**;
- das Forschungszentrum **CECOTEPE**;
- **Bürgerenergiegenossenschaften** — nicht als Endnutzer, denen ein fertiges Werkzeug übergeben wird, sondern als Partner der Mitgestaltung.

Dieser letzte Punkt wiegt schwerer, als er zunächst wirkt. Eine Energiegemeinschaft ist kein reines Ingenieurproblem: Sie ist ebenso ein regulatorisches, buchhalterisches und soziales Objekt wie ein technisches. Die entwickelten Funktionen wurden daher im Feld validiert — mit Verwaltern, die Mitglieder, Zähler und Aufteilungsschlüssel bereits handhabten, meist in Tabellenkalkulationen.

## Das Problem, das die Forschung sichtbar machte

Die Ausgangsbeobachtung ist schnell gesagt und mühsam zu leben: **Der Verwaltungsaufwand einer Energiegemeinschaft steht in keinem Verhältnis zu ihrer Größe.**

Eine Gemeinschaft aus dreißig Haushalten muss dieselben Objekte verwalten wie ein Energieversorger — Lieferstellen, viertelstündliche Messwerte, Aufteilungsschlüssel, Abrechnung, Reporting an den Netzbetreiber — ohne dessen Personal und ohne dessen Systeme. Und der geltende Rahmen ist nicht stabil: In Belgien ist Energie eine regionale Zuständigkeit, sodass Wallonie, Brüssel und Flandern drei unterschiedliche Rahmen mit eigenen Regulierungsbehörden und eigenen Schlüsselfamilien vorgeben. Den darüber liegenden europäischen Rahmen beschreibt unser Artikel [„Energiegemeinschaften in Europa: RED II und IEMD“](/de/aktuelles/2026/03/05/energiegemeinschaften-europa/).

Die verfügbaren Werkzeuge waren entweder Tabellenkalkulationen — flexibel, aber nicht prüfbar und rasch unbeherrschbar — oder proprietäre Lösungen, die für Akteure ganz anderer Größenordnung gebaut waren.

## Warum Open Source kein Detail ist

Die Entscheidung, OptimCE unter der **Apache-2.0-Lizenz** quelloffen zu veröffentlichen, folgt unmittelbar aus der Natur des verwalteten Gegenstands.

Eine Energiegemeinschaft lebt vom **Vertrauen zwischen ihren Mitgliedern**. Der Aufteilungsschlüssel bestimmt viertelstundengenau, wie viel Energie jedes Mitglied erhält und damit wie viel es zahlt. Dreißig Haushalte zu bitten, einer Blackbox bei dieser Berechnung zu vertrauen, ist viel verlangt. Den Code öffnen zu können, ist hier kein Entwicklerkomfort, sondern eine **Governance-Voraussetzung**.

Hinzu kommt ein nüchternerer Grund. Viele Gemeinschaften sind kleine, ehrenamtlich oder halb ehrenamtlich getragene Strukturen, für die eine jährliche proprietäre Lizenz jedes Budget sprengt. Ein Werkzeug, das man sich nicht leisten kann, löst kein Problem.

## Was die Plattform heute leistet

OptimCE deckt den vollständigen Verwaltungszyklus einer Gemeinschaft ab:

- **Mitgliederverwaltung** — Onboarding, Rollen, Verknüpfung von Gemeinschaften und Nutzern;
- **Zählerverwaltung** — Bündelung der Lieferstellen und Messwerte;
- **Aufteilungsschlüssel** — Konfiguration, Historisierung der Nachträge und Nachverfolgung der Zustimmung der Mitglieder;
- **Schlüsselgenerierung und -simulation** — Vorschlag eines optimierten Schlüssels aus realen Daten und Messung seiner Leistung vor der Freigabe;
- **Abrechnung** — vom Preis pro kWh bis zum PDF und zur Zahlungsverfolgung;
- **Gemeinschaftsleben** — Nachrichtenboard und Abstimmungen, denn partizipative Governance ist ebenso regulatorische Anforderung wie gute Praxis;
- **Mehrere Gemeinschaften** — eine Instanz für mehrere Gemeinschaften.

Die Architektur ist **ereignisgesteuert und modular**, sodass sich Module Dritter einbinden lassen, ohne den Kern anzutasten — eine Entscheidung, die direkt aus der regulatorischen Unsicherheit folgt: Was sich alle zwei Jahre ändert, muss sich ändern lassen, ohne die Plattform neu zu schreiben.

## Zwei Nutzungswege

**Self-Hosting** unter der Apache-2.0-Lizenz, kostenlos und uneingeschränkt. Sie behalten die volle Datenhoheit und verantworten Betrieb, Updates und Verfügbarkeit selbst. Das Vorgehen beschreibt [„OptimCE installieren: Schnellstart“](/de/aktuelles/2026/03/09/schnellstartanleitung/).

**Über [OptimCE Cloud](https://app.optimce.be)**, die gehostete und verwaltete Version, derzeit in der Alpha-Phase und kostenlos. Keine Installation, keine Wartung.

Einzelheiten zum Projekt, zu den Partnern und zur Förderung finden sich auf der Seite [Über uns](/de/about/).

Seit diesem Start hat sich die Plattform weiterentwickelt: siehe die [Version Mai 2026](/de/aktuelles/2026/05/07/release-neuigkeiten/), die das öffentliche Register der Teilungsoperationen und das Benutzerhandbuch eingeführt hat.

## FAQ

### Wer entwickelt OptimCE?

OptimCE ging aus Locomotrice hervor, einem wallonischen Forschungsprojekt der Jahre 2023 bis 2026, gefördert durch das Programm Win2Wal der Wallonischen Region. Getragen wird es von der Universität Lüttich mit ihrem BEMS-Labor und vom Forschungszentrum CECOTEPE, in Zusammenarbeit mit Bürgerenergiegenossenschaften. Die Entwicklung läuft heute quelloffen weiter und steht externen Beiträgen offen.

### Ist OptimCE kostenlos?

Die Plattform steht unter der Apache-2.0-Lizenz: Sie können sie kostenlos und uneingeschränkt auf eigener Infrastruktur betreiben. Die gehostete Version OptimCE Cloud befindet sich derzeit in der Alpha-Phase und ist ebenfalls kostenlos. Ein kostenpflichtiges Angebot entsteht mit der Reife des Produkts; Alpha-Nutzer werden rechtzeitig informiert.

### Warum eine Open-Source-Plattform für Energiegemeinschaften?

Weil eine Energiegemeinschaft auf dem Vertrauen ihrer Mitglieder beruht und sich dieses Vertrauen schwer auf einer Blackbox aufbauen lässt. Die Berechnung des Aufteilungsschlüssels bestimmt, wie viel jedes Mitglied erhält und zahlt: Sie prüfen zu können, ist kein Entwicklerluxus, sondern eine Governance-Voraussetzung. Hinzu kommt die wirtschaftliche Realität — viele Gemeinschaften sind kleine Strukturen, für die eine jährliche proprietäre Lizenz unverhältnismäßig ist.

### Funktioniert OptimCE auch außerhalb Belgiens?

Die Architektur wurde von Anfang an für unterschiedliche Regulierungsrahmen ausgelegt — schon deshalb, weil Belgien allein drei regionale Regime kennt. Schlüsselfamilien, Status und Abrechnungsregeln sind konfigurierbar. Entwicklung und Validierung konzentrieren sich bislang vor allem auf den belgischen Kontext.

### Wie kann ich zum Projekt beitragen?

Alles läuft über die GitHub-Organisation OptimCE. Das Monorepo bündelt die einzelnen Dienste und enthält die Orchestrierungskonfiguration, mit der sich die gesamte Stack lokal per Docker Compose starten lässt. Code-Beiträge sind willkommen, Rückmeldungen von Gemeinschaftsverwaltern aus der Praxis aber ebenso — sie haben das Produkt bisher geprägt.

## Weiterführend

> **[Energiegemeinschaften in Belgien: CER, CEC, CEL](/de/aktuelles/2026/05/11/energiegemeinschaften-belgien/)**
>
> Die drei belgischen Status, die Energieteilung und die Rolle von Regulator und Netzbetreiber.

> **[OptimCE installieren: Schnellstart](/de/aktuelles/2026/03/09/schnellstartanleitung/)**
>
> Die gesamte Stack lokal ausrollen — oder ganz ohne Installation starten.

<div class="post-cta" markdown="0">
  <h3>Entdecken Sie OptimCE</h3>
  <p>Legen Sie Ihre Energiegemeinschaft in wenigen Minuten auf der gehosteten Version an, oder betreiben Sie die Plattform auf eigener Infrastruktur. Der Code ist offen, Beiträge sind willkommen.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="https://app.optimce.be">OptimCE-Anwendung öffnen</a>
    <a class="btn btn-outline" href="https://github.com/optimce">Projekt auf GitHub ansehen</a>
  </p>
</div>
