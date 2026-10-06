---
layout: page
title: "Funktionen der Plattform OptimCE"
subtitle: "Was die Plattform heute leistet, um eine Energiegemeinschaft zu führen – vom Beitritt der Mitglieder bis zur Rechnung."
description: "Mitglieder, Zähler, Aufteilungsschlüssel, Abrechnung, CWaPE-Dokumente und Abstimmungen: was OptimCE heute kann, Open Source und in der Alpha kostenlos."
lang: de
ref: features
permalink: /de/funktionen/
last_modified_at: 2026-09-26
feature_list:
  - "Verwaltung von Mitgliedern, Lieferstellen und Zählern"
  - "Archivierte Aufteilungsschlüssel mit Nachverfolgung der Zustimmung der Mitglieder"
  - "Automatische Generierung von Aufteilungsschlüsseln (Durchlauf der Standardschlüssel, LOGAAS)"
  - "Simulation eines Aufteilungsschlüssels auf den eigenen Daten"
  - "Abrechnung der geteilten Energie (erste Version, wallonischer Rahmen)"
  - "Vorausgefüllte CWaPE-Verwaltungsdokumente und Fristenverfolgung"
  - "E-Mail-Benachrichtigungen in vier Sprachen"
  - "Nachrichtenboard und Abstimmungen"
  - "Öffentliches Register der Teilungsoperationen"
  - "Mehrere Gemeinschaften, ereignisgesteuerte Integration, REST-API"
---

OptimCE ist eine Open-Source-Plattform zur Verwaltung von Energiegemeinschaften. Diese Seite
beschreibt, was sie **heute** in ihrer Alphaversion leistet, ohne etwas anzukündigen, das noch
nicht ausgeliefert ist. Das [Benutzerhandbuch](https://guide.optimce.be) erläutert anschließend
jeden Bildschirm.

## Mitglieder, Zähler und Gemeinschaften

- **Mitgliederverwaltung**: Aufnahme neuer Mitglieder, Rollen, Verknüpfungen zwischen Nutzern und
  Gemeinschaften.
- **Lieferstellen und Zähler**: die Mitglieder, ihre Lieferstellen, ihre Anlagen und ihre Zähler
  werden an einem Ort geführt. Die einmal gepflegte Teilnehmerliste speist anschließend die
  Verwaltungsdokumente und die Abrechnung.
- **Mehrere Gemeinschaften, eine Instanz**: eine einzige OptimCE-Installation verwaltet mehrere
  Energiegemeinschaften.

## Aufteilungsschlüssel: konfigurieren, generieren, simulieren

Der Aufteilungsschlüssel legt Viertelstunde für Viertelstunde fest, wer welchen Anteil der lokalen
Erzeugung erhält. OptimCE deckt seinen gesamten Lebenszyklus ab.

- **Konfiguration und Nachträge**: jede Version des Schlüssels wird archiviert, und die Zustimmung
  der Mitglieder wird nachverfolgt.
- **Automatische Generierung**: aus einer CSV-Datei mit Verbrauch und Erzeugung je Viertelstunde
  schlägt das Modul einen Kandidatenschlüssel mit der erwarteten kollektiven Eigenverbrauchsquote
  vor. Zwei Algorithmen stehen zur Verfügung: ein vollständiger Durchlauf der Standardschlüssel
  Ihrer Region und LOGAAS, hervorgegangen aus der Forschung des CeCoTePe im Projekt Locomotrice. Der
  Vorschlag geht nie von selbst an den Netzbetreiber: er folgt dem üblichen Weg des Nachtrags.
- **Simulation**: testen Sie einen Schlüssel Ihrer Wahl auf Ihren eigenen Daten und lesen Sie
  Eigenverbrauch, Überschuss, Autarkiegrad und Teilungsquote ab, insgesamt, je Zeitschritt und je
  Iteration, ohne den angewandten Schlüssel zu berühren.

Weiterlesen: [einen optimalen Aufteilungsschlüssel generieren]({{ "optimce-allocation-key-generator" | ref_url }})
und [einen Schlüssel auf den eigenen Daten simulieren]({{ "optimce-allocation-key-simulation" | ref_url }}).

## Abrechnung der geteilten Energie

Die erste Version des Abrechnungsmoduls ist auf den wallonischen Rahmen ausgelegt.

- Sie legen Ihre Preise in €/kWh fest: einen Verkaufspreis für die geteilte Energie und einen
  Rückkaufpreis für die Einspeisung, für die ganze Gemeinschaft, je Kundensegment oder je
  Lieferstelle, mit einer Gültigkeitsdauer.
- Ein Abrechnungszyklus erstellt aus den importierten Aufteilungsdaten einen Entwurf je Mitglied.
  Nach der Ausstellung erhält jedes Dokument eine Nummer in einer lückenlosen Nummerierung und
  eine strukturierte Mitteilung.
- Drei Dokumente werden als PDF erzeugt: die Rechnung, die Gutschrift und die
  Vergütungsabrechnung der Erzeuger.
- Die Zahlungsverfolgung ist integriert, Teilzahlungen inbegriffen, und jedes Mitglied findet
  seine Rechnungen in der Anwendung.

Die Einzelheiten stehen in [der Ankündigung des Abrechnungsmoduls]({{ "optimce-billing" | ref_url }}).

## Verwaltungsdokumente und Fristen

Für wallonische Gemeinschaften bereitet OptimCE die Dokumente der CWaPE aus den offiziellen,
unveränderten Dateien vor: elf Pakete aus ausfüllbaren PDFs, Excel-Arbeitsmappen und
Word-Vereinbarungen, vorausgefüllt mit den Daten der Gemeinschaft. Felder, die die Plattform nicht
ableiten kann, bleiben bearbeitbar.

- Jede Akte und jedes Dokument durchlaufen Status, die in einem Protokoll festgehalten werden:
  eine Korrektur kommt hinzu, sie löscht nichts.
- Die Fristen werden in Werktagen nach dem belgischen Kalender berechnet und im Dashboard des
  Verwalters angezeigt.
- E-Mails auf Französisch, Niederländisch, Deutsch und Englisch melden Einladungen, Rechnungen und
  Verwaltungsfristen.
- Jedes Mitglied kann einsehen, was über es an die Regulierungsbehörde gemeldet wurde.

OptimCE reicht nichts ein und unterschreibt nichts an Ihrer Stelle: die Einreichung bleibt Ihre
Sache. Siehe [CWaPE-Dokumente und Fristen]({{ "cwape-administrative-documents" | ref_url }}).

## Die Gemeinschaft beleben

Ein Nachrichtenboard informiert die Mitglieder, Abstimmungen befragen sie. Drei Modi für die
Sichtbarkeit der Ergebnisse sind vorgesehen: anonym, transparent oder Ergebnisse erst beim
Abschluss. Ein erweiterter Modus regelt getrennt, was der Verwalter und was die Mitglieder sehen.
Siehe [Mitglieder einer Energiegemeinschaft einbinden]({{ "engage-energy-community" | ref_url }}).

## Öffentliches Register der Teilungsoperationen

Ein Verwalter kann seine Teilungsoperation in einem öffentlichen Register veröffentlichen, das in
die Anwendung integriert ist. Jeder kann es durchsuchen, um eine für neue Mitglieder offene
Operation zu finden.

## Eine offene Plattform

- **Open Source**: der gesamte Code ist unter der Lizenz Apache 2.0 veröffentlicht.
- **Selbst-Hosting**: Sie können OptimCE kostenlos und ohne Einschränkung auf Ihrer eigenen
  Infrastruktur installieren. Die Schritte beschreibt [die Installationsanleitung]({{ "quick-start-guide" | ref_url }}).
- **OptimCE Cloud**: die gehostete Version ist während der gesamten Alphaphase kostenlos. Ein
  kostenpflichtiges Angebot kann später entstehen; die Alphanutzer werden rechtzeitig informiert,
  und das Selbst-Hosting bleibt kostenlos.
- **Integrationen**: eine ereignisgesteuerte Architektur (NATS) erlaubt es, Werkzeuge von
  Drittanbietern anzuschließen, etwa ein Energiemanagementsystem, und eine REST-API bindet OptimCE
  in Ihre eigenen Werkzeuge ein.
- **Mehrsprachig**: die Oberfläche gibt es auf Französisch, Englisch, Niederländisch und Deutsch.

## Was die Plattform nicht tut

OptimCE arbeitet mit den vom Netzbetreiber übermittelten Aufteilungsdaten und mit den Dateien, die
Sie importieren: es zeigt keine Echtzeitdaten an. Es reicht Ihre Dokumente nicht bei der CWaPE ein
und unterschreibt Ihre Vereinbarungen nicht. Seine Abrechnung deckt vorerst nur den wallonischen
Rahmen ab.

<div class="post-cta" markdown="0">
  <h2>Eine Gemeinschaft mit OptimCE verwalten oder gründen</h2>
  <p>Die Anwendung ist während der Alpha kostenlos. Legen Sie Ihre Gemeinschaft an, laden Sie Ihre
  Mitglieder ein und konfigurieren Sie Ihren Aufteilungsschlüssel; das Benutzerhandbuch begleitet
  Sie Bildschirm für Bildschirm.</p>
  <p class="post-cta__actions">
    <a class="btn btn-primary btn--lg" href="{{ site.cta.app_url }}">Anwendung öffnen</a>
    <a class="btn btn-outline" href="https://guide.optimce.be">Benutzerhandbuch lesen</a>
    <a class="btn btn-outline" href="https://github.com/{{ site.github_username }}">Code auf GitHub ansehen</a>
  </p>
</div>
