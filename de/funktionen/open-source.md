---
layout: page
title: "Open Source und Selbst-Hosting"
breadcrumb_title: "Open Source"
subtitle: "Der gesamte Code unter Apache-2.0-Lizenz: Hosten Sie OptimCE selbst, verbinden Sie es mit Ihren Werkzeugen, oder lassen Sie es von uns hosten."
description: "OptimCE ist Open-Source-Software für Energiegemeinschaften unter Apache-2.0-Lizenz: kostenloses Selbst-Hosting, REST-API, NATS-Ereignisse, vier Sprachen."
lang: de
ref: product-open-source
permalink: /de/funktionen/open-source/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Ist OptimCE wirklich Open Source?"
    a: "Ja. Der gesamte Code ist unter der Apache-2.0-Lizenz in der GitHub-Organisation optimce veröffentlicht: keine abgespeckte Version, kein proprietärer Kern. Die gehostete Version und die Version, die Sie selbst installieren, bieten dieselben Funktionen."
  - q: "Darf ich OptimCE beruflich nutzen?"
    a: "Ja. Die Apache-2.0-Lizenz erlaubt es, die Software zu nutzen, zu ändern und weiterzugeben, auch im beruflichen Umfeld, sofern die Lizenz- und Urheberrechtshinweise erhalten bleiben."
  - q: "Was ist der Unterschied zwischen OptimCE Cloud und Selbst-Hosting?"
    a: "Wer die Anwendung hostet. OptimCE Cloud läuft auf unseren Servern, ohne Installation und ohne Wartung, und ist während der Alpha kostenlos. Beim Selbst-Hosting läuft OptimCE auf Ihrer Infrastruktur, kostenlos und ohne Einschränkung, aber Betrieb, Updates und Verfügbarkeit stellen Sie selbst sicher."
  - q: "Wie verbinde ich OptimCE mit meinen anderen Werkzeugen?"
    a: "Über seine Ereignisse oder über seine API. Eine ereignisgesteuerte Architektur (NATS) erlaubt es, Werkzeuge von Drittanbietern anzuschließen, etwa ein Energiemanagementsystem, und eine REST-API bindet OptimCE in Ihre eigenen Werkzeuge ein."
---

Eine Energiegemeinschaft vertraut ihrer Software die Liste ihrer Mitglieder an, deren Zähler, ihre
Rechnungen und ihre Dossiers für die Regulierungsbehörde. Sie muss diese Software behalten können,
wenn der Anbieter den Kurs ändert, selbst wählen können, wo sie gehostet wird, und sie mit ihren
anderen Werkzeugen verbinden können. OptimCE ist Open-Source-Software: Der gesamte Code ist unter
der Apache-2.0-Lizenz veröffentlicht, und dieselbe Anwendung läuft auf unseren Servern oder auf
Ihren.

## So übernimmt OptimCE das

### Der gesamte Code unter Apache-2.0-Lizenz

Es gibt weder eine abgespeckte Version noch einen proprietären Kern: Der gesamte Code von OptimCE
ist unter der Apache-2.0-Lizenz in der GitHub-Organisation [optimce](https://github.com/optimce)
veröffentlicht. Diese Lizenz erlaubt es, die Software zu nutzen, zu ändern und weiterzugeben, auch
im beruflichen Umfeld. Im Gegenzug verlangt sie, die Lizenz- und Urheberrechtshinweise zu erhalten
und geänderte Dateien zu kennzeichnen.

Für eine Gemeinschaft heißt das: Sie ist an niemanden gebunden. Passt OptimCE Cloud nicht mehr zu
ihr, kann sie dieselbe Anwendung anderswo betreiben.

### Bei uns oder bei Ihnen

Dieselbe Software lässt sich auf zwei Arten nutzen.

- **OptimCE Cloud** ist die gehostete Version unter app.optimce.be: nichts zu installieren, nichts
  zu warten. Sie ist während der gesamten Alphaphase kostenlos.
- Beim **Selbst-Hosting** installieren Sie OptimCE auf Ihrer eigenen Infrastruktur, kostenlos und
  ohne Einschränkung, für immer. Die Installationsanleitung beschreibt das lokale Deployment des
  gesamten Stacks mit Docker Compose.

Beide Wege bieten dieselben Funktionen. Die Wahl hängt vor allem davon ab, wer Sie sind: Eine
Gemeinschaft, die einfach das Werkzeug braucht, muss nichts installieren, während ein technisches
Team die Plattform selbst betreiben, die volle Datenhoheit behalten oder zum Code beitragen kann.
Was kostenlos ist, und wie lange, steht auf der Seite [Preise]({{ "pricing" | ref_url }}).

### Eine Installation, mehrere Gemeinschaften

Eine einzige OptimCE-Installation verwaltet mehrere Energiegemeinschaften. Ein Konto kann zu
mehreren Gemeinschaften gehören und unter „Meine Gemeinschaften“ zwischen ihnen wechseln. Wer
mehrere Projekte begleitet oder OptimCE für andere hostet, braucht also nicht für jede Gemeinschaft
eine eigene Installation.

### Ihre Werkzeuge anbinden

Eine ereignisgesteuerte Architektur (NATS) erlaubt es, Werkzeuge von Drittanbietern an OptimCE
anzuschließen, etwa ein Energiemanagementsystem. Eine REST-API bindet OptimCE in Ihre eigenen
Werkzeuge ein. Ein Werkzeug, das die Gemeinschaft bereits nutzt, kann so Daten mit OptimCE
austauschen, statt sie erneut erfassen zu lassen. Das erfordert allerdings Integrationsarbeit.

### Eine Oberfläche in vier Sprachen

Die Oberfläche gibt es auf Französisch, Englisch, Niederländisch und Deutsch, was in einem Land mit
drei Amtssprachen zählt. Auch die E-Mails, die die Plattform verschickt, gibt es in diesen vier
Sprachen.

### Mitwirken

Die Installationsanleitung richtet sich auch an Teams, die zum Code beitragen möchten: Der gesamte
Stack lässt sich lokal mit Docker Compose starten. Übersetzungen der Oberfläche werden gemeinsam
auf [Weblate](https://hosted.weblate.org/engage/optimce/) vorgeschlagen, ohne den Code anzufassen.

## Was es nicht leistet

**Keine Servicegarantie beim Selbst-Hosting.** Auf Ihren Servern stellen Sie Betrieb, Updates und
Verfügbarkeit selbst sicher: Auf diesem Weg wird keine Servicegarantie gegeben.

**Die Installationsanleitung beschreibt einen Entwicklungs-Stack.** Seine Datenbanken sind nicht
persistent: Beim Neustart der Container werden die Daten zurückgesetzt. Für ein Deployment, das
Bestand haben soll, müssen Sie selbst persistente Volumes und eine Sicherungsstrategie einrichten.

**Open Source nimmt Ihnen die Arbeit nicht ab.** Wer eine Software hostet, die Mitgliederdaten
verwaltet, braucht jemanden, der sie administriert. Ohne diese Person bleibt OptimCE Cloud der
einfachste Weg.

## Häufige Fragen {#faq}

### Ist OptimCE wirklich Open Source?

Ja. Der gesamte Code ist unter der Apache-2.0-Lizenz in der GitHub-Organisation optimce
veröffentlicht: keine abgespeckte Version, kein proprietärer Kern. Die gehostete Version und die
Version, die Sie selbst installieren, bieten dieselben Funktionen.

### Darf ich OptimCE beruflich nutzen?

Ja. Die Apache-2.0-Lizenz erlaubt es, die Software zu nutzen, zu ändern und weiterzugeben, auch im
beruflichen Umfeld, sofern die Lizenz- und Urheberrechtshinweise erhalten bleiben.

### Was ist der Unterschied zwischen OptimCE Cloud und Selbst-Hosting?

Wer die Anwendung hostet. OptimCE Cloud läuft auf unseren Servern, ohne Installation und ohne
Wartung, und ist während der Alpha kostenlos. Beim Selbst-Hosting läuft OptimCE auf Ihrer
Infrastruktur, kostenlos und ohne Einschränkung, aber Betrieb, Updates und Verfügbarkeit stellen
Sie selbst sicher.

### Wie verbinde ich OptimCE mit meinen anderen Werkzeugen?

Über seine Ereignisse oder über seine API. Eine ereignisgesteuerte Architektur (NATS) erlaubt es,
Werkzeuge von Drittanbietern anzuschließen, etwa ein Energiemanagementsystem, und eine REST-API
bindet OptimCE in Ihre eigenen Werkzeuge ein.

## Weiterlesen

- [OptimCE installieren: Schnellstart]({{ "quick-start-guide" | ref_url }}): die Voraussetzungen,
  das Klonen des Repositorys und der erste Start, Schritt für Schritt.
- [Preise von OptimCE]({{ "pricing" | ref_url }}): was heute kostenlos ist und was sich ändern
  könnte.
- [Software für Energiegemeinschaften]({{ "features" | ref_url }}): alles, was OptimCE heute
  leistet.

{% include product-cta.html page_key="open-source" guide="getting-started" title="OptimCE ohne Installation ausprobieren" %}
