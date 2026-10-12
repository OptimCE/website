---
layout: page
title: "Eine Gemeinschaft mit OptimCE starten"
breadcrumb_title: "Erste Schritte"
subtitle: "Sechs Schritte, vom Anlegen der Gemeinschaft bis zur ersten Rechnung, jeder mit seiner Schritt-für-Schritt-Anleitung."
description: "Gemeinschaft anlegen, Mitglieder und Zähler erfassen, Teilungsoperation eröffnen, Schlüssel festlegen, abrechnen: in sechs Schritten mit OptimCE starten."
lang: de
ref: product-getting-started
permalink: /de/funktionen/erste-schritte/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Muss ich OptimCE installieren, um zu starten?"
    a: "Nein. OptimCE Cloud unter app.optimce.be erfordert keine Installation: Sie legen ein Konto an, dann Ihre Gemeinschaft. Das Selbst-Hosting ist ein anderer Weg, für Teams, die die Plattform selbst hosten möchten."
  - q: "Was kostet OptimCE?"
    a: "OptimCE Cloud ist während der gesamten Alphaphase kostenlos, und das Selbst-Hosting ist für immer kostenlos. Für die gehostete Version kann später ein kostenpflichtiges Angebot entstehen; die Alphanutzer werden frühzeitig informiert."
  - q: "In welcher Reihenfolge erledigt man die Schritte?"
    a: "In der Reihenfolge dieser Seite, die den Abhängigkeiten zwischen den Modulen folgt: Zähler sind Mitgliedern zugeordnet, Tarife und Rechnungen einer Teilungsoperation, und die Abrechnung wendet die Aufteilung dieser Operation an."
  - q: "Kann man mit demselben Konto mehrere Gemeinschaften verwalten?"
    a: "Ja. Eine einzige OptimCE-Installation verwaltet mehrere Gemeinschaften, und ein Konto kann zu mehreren davon gehören. Sie wechseln unter „Meine Gemeinschaften“ zwischen ihnen."
---

Eine Energiegemeinschaft in einer Software zu starten heißt vor allem zu wissen, in welcher
Reihenfolge man vorgeht. Diese Seite folgt der Reihenfolge, in der ein Verwalter eine wallonische
Gemeinschaft in OptimCE einrichtet, vom Anlegen bis zur ersten Rechnung. Jeder Schritt verweist auf
seine Schritt-für-Schritt-Anleitung, die jeden Bildschirm mit Testdaten zeigt, und auf die Seite,
die das Modul im Detail beschreibt.

## Was Sie bereithalten sollten

- **Für die Gemeinschaft**: ihre rechtliche Bezeichnung, ihre MwSt.-Nummer, die Anschrift ihres
  Sitzes, ihre IBAN und den Kontoinhaber.
- **Für jedes Mitglied**: seinen Status (Privatperson oder Unternehmen), Name, E-Mail-Adresse,
  Telefonnummer, Anschrift und IBAN; bei einer Privatperson die Nationalregisternummer.
- **Für jeden Zähler**: die Installationsadresse, die EAN, die Zählernummer, seine technischen
  Merkmale (Phasen, Ablesehäufigkeit, Leistung) und seinen Netzbetreiber.

Sie müssen nicht alles am ersten Tag beisammenhaben: Das Dashboard listet auf, was noch fehlt.

## Der Weg, Schritt für Schritt

### 1. Die Gemeinschaft anlegen

Legen Sie die Gemeinschaft unter „Meine Gemeinschaften“ an: mit einem Namen und ihrer
Regulierungsbehörde, für die Wallonie ist die CWaPE vorausgewählt. Sie werden Administrator der
Gemeinschaft; danach müssen Sie sie noch aktivieren, um sie zu konfigurieren.

Anleitung (auf Englisch): [eine Gemeinschaft erstellen](https://guide.optimce.be/community-create/en.html).
Für den Überblick: [die Software für Energiegemeinschaften]({{ "features" | ref_url }}).

{% include product-shot.html name="start-dashboard" alt="Dashboard einer neuen Gemeinschaft in der englischen Oberfläche: „Things to check“ (zu prüfende Punkte) listet fünf fehlende Angaben auf (MwSt.-Nummer, rechtliche Bezeichnung, IBAN, Kontoinhaber, Anschrift des Sitzes), und es gibt noch keine Teilungsoperation." caption="Das Dashboard einer soeben angelegten Gemeinschaft: was noch zu ergänzen ist (Testdaten, englische Oberfläche)." %}

### 2. Die Mitglieder hinzufügen

Ein Assistent in vier Schritten erfasst jedes Mitglied: seinen Status, seine persönlichen Angaben,
seine Adressen und seine Bankverbindung. Danach bietet ein Fenster an, direkt mit seinem Zähler
weiterzumachen; das können Sie auch später von seiner Detailseite aus tun. Mitglieder lassen sich
auch per Einladung hinzufügen.

Anleitung: [ein Mitglied anlegen](https://guide.optimce.be/member-create/en.html). Modul:
[Mitglieder, Zähler und Gemeinschaften]({{ "features" | ref_url }}).

{% include product-shot.html name="start-member" alt="Erster Schritt des Assistenten „Add a member“ (Mitglied hinzufügen) in der englischen Oberfläche: die Wahl des Status, „Individual“ oder „Company“ (Privatperson oder Unternehmen), gefolgt von den Schritten persönliche Angaben, Adressen und Bankverbindung." caption="Der Assistent zum Anlegen eines Mitglieds, beim ersten Schritt (Testdaten, englische Oberfläche)." %}

### 3. Die Zähler hinzufügen

Geben Sie für jeden Zähler Standort und EAN an, seine Merkmale, seinen Netzbetreiber, das Mitglied,
auf dessen Namen er läuft, und sein Aktivierungsdatum. Seine Energiewerte, etwa die
Entnahmeleistung und die Erzeugungskapazität, fließen in die Aufteilungsberechnungen ein. Vor
seinem Aktivierungsdatum geht der Zähler in keine Berechnung ein.

Anleitung: [einen Zähler anlegen](https://guide.optimce.be/meter-create/en.html). Modul:
[Mitglieder, Zähler und Gemeinschaften]({{ "features" | ref_url }}).

### 4. Die Teilungsoperation anlegen

Geben Sie ihr einen Namen, einen Typ (innerhalb eines Gebäudes, Erneuerbare-Energie-Gemeinschaft
oder Bürgerenergiegemeinschaft) und die Gemeinden, die sie abdeckt. Tarife, Rechnungen und
Verwaltungsdossiers werden anschließend dieser Operation zugeordnet.

Anleitung: [eine Teilungsoperation anlegen](https://guide.optimce.be/sharing-op-create/en.html).
Modul: [die CWaPE-Unterlagen der Operation]({{ "product-cwape" | ref_url }}).

### 5. Den Aufteilungsschlüssel festlegen

Geben Sie im Assistenten die Zahl der Verbraucher und ihre Namen an, dann Iterationen, die jeweils
einen Prozentsatz der Energie verteilen, bis 100 % erreicht sind. Sie können sich auch aus Ihren
Daten einen Schlüssel vorschlagen lassen und ihn simulieren, bevor Sie ihn übernehmen.

Anleitung: [einen Schlüssel mit dem Assistenten anlegen](https://guide.optimce.be/key-create-wizard/en.html).
Modul: [Aufteilungsschlüssel: berechnen, testen, verfolgen]({{ "product-allocation-key" | ref_url }}).

### 6. Abrechnen

Legen Sie den Verkaufspreis der geteilten Energie und den Rückkaufpreis der Einspeisung fest,
importieren Sie die Messwerte der Periode, erzeugen Sie einen Entwurf je Mitglied, stellen Sie die
Dokumente aus und verfolgen Sie dann die Zahlungen.

Anleitung: [eine Operation abrechnen, vom Tarif bis zum Zahlungseingang](https://guide.optimce.be/billing-tarification-pay/en.html).
Modul: [die Abrechnungssoftware]({{ "product-billing" | ref_url }}).

### Und danach

Jedes Mitglied findet seine Rechnungen in der Anwendung und kann einsehen, was über es an die
Regulierungsbehörde gemeldet wurde. Für die Verfahren bei der CWaPE bereitet das Modul der
Verwaltungsdokumente die amtlichen Formulare der Operation vor und berechnet ihre Fristen in
Werktagen.

## Was es nicht leistet

**OptimCE gründet keine juristische Person.** Rechtsform, Statuten und Generalversammlung der
Gemeinschaft werden außerhalb der Anwendung geregelt.

**OptimCE reicht nichts für Sie ein.** Die Meldungen an die CWaPE und die Vereinbarungen mit dem
Netzbetreiber bleiben Ihre Sache; OptimCE bereitet die Dokumente vor und verfolgt die Fristen.

**Brüssel und Flandern: geplant, noch nicht verfügbar.** Die Regulierungsbehörde wird beim Anlegen
gewählt, doch Abrechnung und Verwaltungsdokumente decken heute den wallonischen Rahmen ab. Brüssel
und Flandern sind geplant, aber noch nicht umgesetzt.

## Häufige Fragen {#faq}

### Muss ich OptimCE installieren, um zu starten?

Nein. OptimCE Cloud unter app.optimce.be erfordert keine Installation: Sie legen ein Konto an, dann
Ihre Gemeinschaft. Das Selbst-Hosting ist ein anderer Weg, für Teams, die die Plattform selbst
hosten möchten.

### Was kostet OptimCE?

OptimCE Cloud ist während der gesamten Alphaphase kostenlos, und das Selbst-Hosting ist für immer
kostenlos. Für die gehostete Version kann später ein kostenpflichtiges Angebot entstehen; die
Alphanutzer werden frühzeitig informiert.

### In welcher Reihenfolge erledigt man die Schritte?

In der Reihenfolge dieser Seite, die den Abhängigkeiten zwischen den Modulen folgt: Zähler sind
Mitgliedern zugeordnet, Tarife und Rechnungen einer Teilungsoperation, und die Abrechnung wendet
die Aufteilung dieser Operation an.

### Kann man mit demselben Konto mehrere Gemeinschaften verwalten?

Ja. Eine einzige OptimCE-Installation verwaltet mehrere Gemeinschaften, und ein Konto kann zu
mehreren davon gehören. Sie wechseln unter „Meine Gemeinschaften“ zwischen ihnen.

## Weiterlesen

- [Energiegemeinschaft in der Wallonie gründen]({{ "create-energy-community-wallonia" | ref_url }}):
  die Schritte, von der Rechtsform bis zur Meldung.
- [Energiegemeinschaft: CWaPE-Dokumente und Fristen]({{ "cwape-administrative-documents" | ref_url }}):
  was einzureichen ist, wo und innerhalb welcher Frist.
- [Tabelle oder Software für Ihre Gemeinschaft?]({{ "product-vs-spreadsheet" | ref_url }}):
  wann eine Tabelle noch genügt und wo sie an Grenzen stößt.

{% include product-cta.html page_key="getting-started" guide="getting-started" title="Ihre Gemeinschaft auf OptimCE anlegen" %}
