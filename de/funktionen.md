---
layout: page
title: "Software für Energiegemeinschaften"
subtitle: "Was die Software OptimCE heute leistet, um eine Energiegemeinschaft zu führen – vom Beitritt der Mitglieder bis zur Rechnung."
description: "Open-Source-Software für Energiegemeinschaften: Mitglieder, Aufteilungsschlüssel, Abrechnung, CWaPE-Verfahren, Abstimmungen. In der Alpha kostenlos."
lang: de
ref: features
permalink: /de/funktionen/
last_modified_at: 2026-11-13
feature_list:
  - "Verwaltung von Mitgliedern, Lieferstellen und Zählern"
  - "Archivierte Aufteilungsschlüssel mit Nachverfolgung der Zustimmung der Mitglieder"
  - "Automatische Generierung von Aufteilungsschlüsseln (Durchlauf der Standardschlüssel, LOGAAS)"
  - "Simulation eines Aufteilungsschlüssels auf den eigenen Daten"
  - "Abrechnung der geteilten Energie (erste Version, wallonischer Rahmen)"
  - "CWaPE-Verfahren, vorausgefüllte Dokumente, Fristen und Unterzeichnung der Anlage 8"
  - "E-Mail-Benachrichtigungen in vier Sprachen"
  - "Nachrichtenboard und Abstimmungen"
  - "Gemeinschaftsverzeichnis, einsehbar mit einem OptimCE-Konto"
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

Um eine Gemeinschaft der Reihe nach einzurichten, vom Anlegen bis zur ersten Rechnung, folgen Sie
den [ersten Schritten mit OptimCE]({{ "product-getting-started" | ref_url }}).

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
und [einen Schlüssel auf den eigenen Daten simulieren]({{ "optimce-allocation-key-simulation" | ref_url }}). Den vollständigen
Ablauf zeigt die Seite [Aufteilungsschlüssel: berechnen, testen, verfolgen]({{ "product-allocation-key" | ref_url }}).

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

Die Einzelheiten stehen in [der Ankündigung des Abrechnungsmoduls]({{ "optimce-billing" | ref_url }}). Das Modul wird
auf der Seite [Abrechnungssoftware für Energiegemeinschaften]({{ "product-billing" | ref_url }}) vorgestellt.

## Verwaltungsdokumente und Fristen

Für wallonische Gemeinschaften bereitet OptimCE die Dokumente der CWaPE aus den offiziellen,
unveränderten Dateien vor: elf Pakete aus ausfüllbaren PDFs, Excel-Arbeitsmappen und
Word-Vereinbarungen, vorausgefüllt mit den Daten der Gemeinschaft. Felder, die die Plattform nicht
ableiten kann, bleiben bearbeitbar.

- Die Arbeit ist in Verfahren gegliedert: Änderungen im CRM fließen in den Entwurf des passenden
  Verfahrens, den Sie senden, wann Sie es entscheiden. Sobald der Versand erfasst ist, ist das
  Verfahren festgeschrieben.
- Die Fristen werden in Werktagen gezählt, ohne die belgischen Feiertage. Die Erinnerungen
  erscheinen in der Anwendung 14, 7 und 2 Tage vorher und dann bei Überschreitung der Frist.
- E-Mails auf Französisch, Niederländisch, Deutsch und Englisch melden Einladungen, Rechnungen und
  Unterschriftsanfragen. Die Verwaltungsfristen laufen über eine Zusammenfassung per E-Mail, die
  standardmäßig deaktiviert ist.
- Die Anlage 8, die ehrenwörtliche Erklärung der an der Teilung Beteiligten, wird in der Anwendung
  unterschrieben: eine einfache elektronische Signatur im Sinne der eIDAS-Verordnung.
- Jedes Mitglied kann einsehen, was über es an die Regulierungsbehörde gemeldet wurde.

OptimCE reicht nichts an Ihrer Stelle ein: die Einreichung bleibt Ihre
Sache. Siehe [CWaPE-Dokumente und Fristen]({{ "cwape-administrative-documents" | ref_url }}). Das Modul wird auf
der Seite [CWaPE-Verfahren Ihrer Energiegemeinschaft]({{ "product-cwape" | ref_url }}) vorgestellt.

## Die Gemeinschaft beleben

Ein Nachrichtenboard informiert die Mitglieder, Abstimmungen befragen sie. Drei Modi für die
Sichtbarkeit der Ergebnisse sind vorgesehen: anonym, transparent oder Ergebnisse erst beim
Abschluss. Ein erweiterter Modus regelt getrennt, was der Verwalter und was die Mitglieder sehen.
Siehe [Mitglieder einer Energiegemeinschaft einbinden]({{ "engage-energy-community" | ref_url }}).

## Gemeinschaftsverzeichnis

Ein Verwalter kann eine Teilungsoperation öffentlich machen, sobald für sie mindestens eine Gemeinde
angegeben ist. Seine Gemeinschaft erscheint dann im Gemeinschaftsverzeichnis der Anwendung, mit
Beschreibung, Website, Sitz und ihren öffentlichen Operationen. Das Verzeichnis ist mit einem
OptimCE-Konto einsehbar und lässt sich nach Gemeinde oder Regulierungsbehörde filtern, als Liste
oder auf einer Karte.

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

Die Einzelheiten stehen auf der Seite [Open Source und Selbst-Hosting]({{ "product-open-source" | ref_url }});
was kostenlos ist, und wie lange, steht auf der Seite [Preise]({{ "pricing" | ref_url }}).

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
