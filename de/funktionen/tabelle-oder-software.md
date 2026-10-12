---
layout: page
title: "Tabelle oder Software für Ihre Gemeinschaft?"
breadcrumb_title: "Tabelle oder Software"
subtitle: "Ein ehrlicher Vergleich: wann eine Tabelle für die Verwaltung einer Energiegemeinschaft genügt und wo sie an Grenzen stößt."
description: "Reicht Excel für eine Energiegemeinschaft? Wann eine Tabelle genügt, wo sie an Grenzen stößt (Viertelstunden, Schlüssel, Rechnungen, CWaPE), was Software tut."
lang: de
ref: product-vs-spreadsheet
permalink: /de/funktionen/tabelle-oder-software/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Genügt eine Tabelle für eine kleine Energiegemeinschaft?"
    a: "Oft ja. Mit einer Handvoll Mitgliedern, einer einzigen Teilungsoperation und einem Standardschlüssel, der sich nicht ändert, reicht eine sorgfältig geführte Tabelle aus. Anfällig wird sie, wenn sich der Schlüssel weiterentwickelt, wenn sich die Rechnungen häufen oder wenn mehrere Personen daran arbeiten müssen."
  - q: "Warum ist von 35 040 Werten pro Zähler und Jahr die Rede?"
    a: "Weil das Teilen je Viertelstunde berechnet wird: 96 Viertelstunden pro Tag ergeben über ein Jahr mit 365 Tagen 35 040 Werte pro Zähler. Die Tage der Zeitumstellung haben 92 oder 100 Viertelstunden, und die Jahressumme bleibt gleich."
  - q: "Ersetzt OptimCE die Buchhaltung der Gemeinschaft?"
    a: "Nein. OptimCE rechnet die geteilte Energie ab und verfolgt die Zahlung dieser Rechnungen. Die allgemeine Buchhaltung der Gemeinschaft ist weiterhin getrennt zu führen."
  - q: "Was kostet OptimCE im Vergleich zu einer Tabelle?"
    a: "OptimCE Cloud ist während der gesamten Alphaphase kostenlos, und das Selbst-Hosting ist für immer kostenlos. Für die gehostete Version kann später ein kostenpflichtiges Angebot entstehen; die Alphanutzer werden frühzeitig informiert."
---

Die meisten Energiegemeinschaften starten mit einer Tabellenkalkulation, und oft ist das die
richtige Wahl: Sie ist schon installiert, jeder kann sie öffnen, und eine kleine Gemeinschaft
braucht nicht mehr. Aber eine Tabelle hat kein Gedächtnis. Sie weiß nicht, welche Version des
Aufteilungsschlüssels im März galt, welche Rechnungsnummer als Nächstes kommt und was wann bei der
CWaPE eingereicht wurde. Diese Seite vergleicht beides ehrlich, ohne Sie früher als nötig zu einem
Wechsel des Werkzeugs drängen zu wollen.

## Wann eine Tabelle genügt

Eine sorgfältig geführte Tabelle reicht aus, solange die Gemeinschaft einfach bleibt:

- eine Handvoll Mitglieder und eine einzige Teilungsoperation;
- ein Standard-Aufteilungsschlüssel, der sich von Jahr zu Jahr nicht ändert;
- wenige Dokumente: einige Rechnungen pro Periode, ein bereits eingereichtes CWaPE-Dossier;
- eine einzige Person, die die Datei führt und sie sauber weitergibt, wenn sie die Aufgabe abgibt.

Wenn Ihre Gemeinschaft so aussieht, behalten Sie Ihre Tabelle. Sobald sich einer dieser Punkte
ändert, betrifft Sie der Rest dieser Seite.

## So übernimmt OptimCE das

Hier sind die fünf Stellen, an denen eine Tabelle an Grenzen stößt, und was OptimCE stattdessen tut.

### Die Viertelstundendaten

In Belgien wird das Teilen je Viertelstunde berechnet: 96 Werte pro Tag und Zähler, also 35 040
über ein Jahr mit 365 Tagen. Mit einer Zeile je Zähler und Viertelstunde ergeben die Daten eines
Jahres für 30 Zähler 1 051 200 Zeilen: mehr als die 1 048 576 Zeilen eines Excel-Arbeitsblatts
([Microsoft](https://support.microsoft.com/de-de/excel/excel-specifications-and-limits)). Lange
vor dieser Grenze lässt sich die Arbeitsmappe nur noch mühsam öffnen und neu berechnen.

In OptimCE werden die Viertelstundenwerte je Operation und Periode importiert. Die Abrechnung sowie
die Generierung und die Simulation des Schlüssels arbeiten direkt damit.

### Die Versionen des Schlüssels

Ein Aufteilungsschlüssel ändert sich mit jedem Beitritt und jedem Austritt eines Mitglieds. In
einer Tabelle überschreibt die Version vom März die vom Januar, oder sie überlebt in einer Datei
„Schluessel_v3_final.xlsx“, von der niemand mehr weiß, ob ihr zugestimmt wurde.

In OptimCE wird jede Version des Schlüssels archiviert, und die Zustimmung der Mitglieder wird
nachverfolgt. Die Einzelheiten stehen auf der Seite zum
[Aufteilungsschlüssel]({{ "product-allocation-key" | ref_url }}).

### Die Nummerierung der Rechnungen

Rechnungen werden in einer fortlaufenden Serie ohne Lücken nummeriert, und eine ausgestellte
Rechnung wird nicht mehr geändert: Man korrigiert sie mit einer Gutschrift. In einer Tabelle hindert
nichts daran, eine Zeile zu überschreiben, eine Nummer zu überspringen oder eine falsche
strukturierte Mitteilung abzuschreiben.

In OptimCE werden Nummer und strukturierte Mitteilung bei der Ausstellung vergeben, eine Korrektur
läuft über eine Gutschrift, und die Historie bleibt vollständig. Siehe die
[Abrechnungssoftware]({{ "product-billing" | ref_url }}).

{% include product-shot.html name="billing-member" alt="Bereich „My invoices“ eines Mitglieds in der englischen Oberfläche: eine Vergütungsabrechnung DP-2025-00001 mit dem Status „Issued“ (ausgestellt) über 36,69 €, mit ihrer strukturierten Mitteilung." caption="Jedes Mitglied sieht seine eigenen Dokumente, mit der strukturierten Mitteilung für seine Überweisung (Testdaten, englische Oberfläche)." %}

### Die CWaPE-Dossiers

Dieselben Daten (Mitglieder, Lieferstellen, Anlagen) werden in mehrere Formulare der CWaPE
abgeschrieben, und jede Änderung der Gemeinschaft zieht neue nach sich, mit Fristen in Werktagen.
Eine Tabelle weiß nicht, dass ein Dossier gerade seinen Status gewechselt hat, und auch nicht,
welche Version eines Formulars verschickt wurde.

In OptimCE werden die amtlichen Formulare aus der Mitgliederliste vorausgefüllt, jede Version wird
aufbewahrt, und die Fristen werden in Werktagen berechnet. Siehe die
[CWaPE-Unterlagen]({{ "product-cwape" | ref_url }}).

{% include product-shot.html name="cwape-deadlines" alt="Reiter „Deadlines“ der Verwaltungsdokumente („Administrative documents“) in der englischen Oberfläche: eine Vollständigkeitsprüfung („Completeness check“), fällig am 15.09.2026 für Dossier Nr. 1, mit dem Status „Open“." caption="Die offenen Fristen aller Dossiers, berechnet aus den Statuswechseln (Testdaten, englische Oberfläche)." %}

### Zugang der Mitglieder und Übergabe

Um jedem Mitglied seine Rechnung zu zeigen oder das, was über es gemeldet wurde, muss man mit einer
Tabelle für jede Person eine Datei herausziehen und verschicken: Die ganze Arbeitsmappe zu teilen,
würde die Daten aller offenlegen. Außerdem hängt die Datei an der Person, die sie führt: Geht sie,
verschwindet die Historie oft mit ihrem E-Mail-Postfach.

In OptimCE sieht jedes Mitglied seine eigenen Rechnungen und das, was über es gemeldet wurde, und
sonst nichts. Mehrere Personen können die Gemeinschaft verwalten, jede mit ihrer Rolle, und die
Historie bleibt in der Anwendung.

## Was es nicht leistet

**OptimCE ersetzt nicht Ihre Buchhaltung.** Es rechnet die geteilte Energie ab und verfolgt die
Zahlung dieser Rechnungen. Die allgemeine Buchhaltung der Gemeinschaft ist weiterhin getrennt zu
führen.

**Keine Echtzeit.** Wie Ihre Tabelle arbeitet OptimCE mit den vom Netzbetreiber übermittelten
Messwerten und mit den Dateien, die Sie importieren: Es zeigt keine Echtzeitdaten an.

**Es korrigiert keine falschen Daten.** Eine Software vermeidet Übertragungsfehler, keine
Eingabefehler. Eine falsche Adresse oder EAN bleibt falsch, in einer Tabelle genauso wie in
OptimCE.

## Häufige Fragen {#faq}

### Genügt eine Tabelle für eine kleine Energiegemeinschaft?

Oft ja. Mit einer Handvoll Mitgliedern, einer einzigen Teilungsoperation und einem
Standardschlüssel, der sich nicht ändert, reicht eine sorgfältig geführte Tabelle aus. Anfällig
wird sie, wenn sich der Schlüssel weiterentwickelt, wenn sich die Rechnungen häufen oder wenn
mehrere Personen daran arbeiten müssen.

### Warum ist von 35 040 Werten pro Zähler und Jahr die Rede?

Weil das Teilen je Viertelstunde berechnet wird: 96 Viertelstunden pro Tag ergeben über ein Jahr
mit 365 Tagen 35 040 Werte pro Zähler. Die Tage der Zeitumstellung haben 92 oder 100
Viertelstunden, und die Jahressumme bleibt gleich.

### Ersetzt OptimCE die Buchhaltung der Gemeinschaft?

Nein. OptimCE rechnet die geteilte Energie ab und verfolgt die Zahlung dieser Rechnungen. Die
allgemeine Buchhaltung der Gemeinschaft ist weiterhin getrennt zu führen.

### Was kostet OptimCE im Vergleich zu einer Tabelle?

OptimCE Cloud ist während der gesamten Alphaphase kostenlos, und das Selbst-Hosting ist für immer
kostenlos. Für die gehostete Version kann später ein kostenpflichtiges Angebot entstehen; die
Alphanutzer werden frühzeitig informiert.

## Weiterlesen

- [Energiegemeinschaft: CWaPE-Dokumente und Fristen]({{ "cwape-administrative-documents" | ref_url }}):
  jedes Formular, seine Fristen und wo Sie anfangen, wenn schon alles in Tabellen steht.
- [Geteilten Strom in Belgien abrechnen]({{ "invoice-shared-electricity" | ref_url }}):
  wer was abrechnet, die MwSt. und die Pflichtangaben.
- [Aufteilungsschlüssel in Belgien: 3 Regionen]({{ "allocation-key-belgium" | ref_url }}):
  die Standardschlüssel und die Regeln jeder Region.

{% include product-cta.html page_key="vs-spreadsheet" guide="getting-started" title="Von der Tabelle zu OptimCE" %}
