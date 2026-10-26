---
layout: page
title: "Abrechnungssoftware für Energiegemeinschaften"
breadcrumb_title: "Abrechnung"
subtitle: "Vom Preis pro kWh bis zur eingegangenen Zahlung: die Rechnungen Ihrer Mitglieder, berechnet auf Grundlage der vom Netzbetreiber übermittelten Aufteilung."
description: "Rechnungen für die Mitglieder Ihrer Energiegemeinschaft ohne Tabelle: Preis pro kWh, Entwürfe, lückenlose Nummerierung, PDF und Zahlungsverfolgung."
lang: de
ref: product-billing
permalink: /de/funktionen/abrechnung/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Woher stammen die Daten für die Abrechnung?"
    a: "Aus der vom Netzbetreiber übermittelten Aufteilung: den geteilten Mengen je Viertelstunde, die Sie für die abzurechnende Operation und Periode importieren. Beim Start des Abrechnungslaufs friert OptimCE einen Schnappschuss dieser Mengen ein; die Beträge werden auf diesen eingefrorenen Daten berechnet, die sich nachvollziehen lassen."
  - q: "Kann man je nach Mitglied unterschiedliche Preise anwenden?"
    a: "Ja. Jeder Preis gilt für die ganze Operation, für ein Kundensegment (Haushalte, Gewerbe, Industrie) oder für eine bestimmte Lieferstelle (EAN), jeweils für einen Gültigkeitszeitraum. Betreffen mehrere Regeln dasselbe Mitglied, gewinnt die genaueste: Der Preis einer EAN geht dem Preis ihres Segments vor, und dieser dem globalen Preis."
  - q: "Wie korrigiert man eine bereits ausgestellte Rechnung?"
    a: "Eine ausgestellte Rechnung hat eine Nummer in einer lückenlosen Nummerierung erhalten: Sie lässt sich weder ändern noch löschen. Zur Korrektur stellen Sie eine Gutschrift aus, die sie annulliert, und rechnen dann neu ab. Solange ein Dokument noch ein Entwurf ist, können Sie es dagegen löschen oder neu berechnen."
  - q: "Wie geht OptimCE mit der MwSt. um?"
    a: "Teilweise. Das Modul berechnet die MwSt., aber mit einem einheitlichen Satz von 21 % für alle Dokumente: je nach Mitglied unterschiedliche Sätze und die Mehrwertsteuerbefreiung für Kleinunternehmen werden noch nicht unterstützt. Die MwSt.-Regelung der Gemeinschaft (MwSt.-Pflicht, für jedes Mitglied geltende Sätze) wird vor der ersten Rechnung mit einem Buchhalter festgelegt."
---

In jeder Periode verwandelt der Verwalter einer Energiegemeinschaft die geteilten Mengen in eine
Rechnung je Mitglied: den richtigen Preis anwenden, lückenlos nummerieren, eine strukturierte
Mitteilung hinzufügen und anschließend prüfen, wer bezahlt hat. In einer Tabellenkalkulation wird
jeder dieser Schritte von Hand wiederholt, und jeder Fehler wird von Hand korrigiert. Das
Abrechnungsmodul von OptimCE übernimmt diese Arbeit auf Grundlage der vom Netzbetreiber
übermittelten Aufteilung, im wallonischen Rahmen.

## So funktioniert die Abrechnung mit OptimCE

Das Modul begleitet den gesamten Zyklus, vom Tarif bis zum Zahlungseingang. Tarife und Rechnungen
sind immer einer Teilungsoperation zugeordnet: Eine Gemeinschaft, die mehrere Operationen betreibt,
rechnet sie getrennt ab.

### Sie legen zwei Preise fest

Die Gemeinschaft bestimmt ihre Preise selbst, in €/kWh. Der **Verkaufspreis** gilt für die geteilte
Energie, die die Mitglieder verbrauchen; der **Rückkaufpreis** vergütet die Einspeisung, die die
Erzeuger mit der Gemeinschaft teilen.

Jeder Preis gilt für die ganze Operation, für ein Kundensegment (Haushalte, Gewerbe, Industrie)
oder für eine bestimmte Lieferstelle und hat einen Gültigkeitszeitraum. Betreffen mehrere Regeln
dasselbe Mitglied, gewinnt die genaueste. Ein ermäßigter Tarif für eine Schule oder einen Haushalt
erfordert also keine zweite Operation: Ein Preis auf der betreffenden EAN genügt.

{% include product-shot.html name="billing-tariffs" alt="Reiter „Tarife“ des Moduls „Abrechnung“: ein „Verkaufspreis für Verbraucher“ von 0,12 €/kWh und ein „Rückkaufpreis für Erzeuger“ von 0,05 €/kWh, beide mit dem Geltungsbereich „Global“ und gültig ab dem 1. Januar 2025." caption="Die beiden Preise einer Teilungsoperation, wie sie die Schritt-für-Schritt-Anleitung zeigt (Testdaten)." %}

### Sie starten einen Abrechnungslauf für eine Periode

Sie wählen die Operation und die abzurechnende Periode: einen Monat, ein Quartal, ganz im Rhythmus
der Gemeinschaft. Die Abrechnung stützt sich auf die Viertelstundenwerte, die der Netzbetreiber für
die Operation übermittelt. Beim Start friert OptimCE einen Schnappschuss dieser Mengen ein: Die
Beträge werden auf eingefrorenen Daten berechnet, die sich nachvollziehen lassen, wenn ein Mitglied
eine Frage stellt.

Die Berechnung läuft im Hintergrund. Sie erzeugt einen **Entwurf je Mitglied**, als PDF mit
„Proforma“-Wasserzeichen herunterladbar. Einen Entwurf können Sie frei prüfen, löschen oder neu
berechnen: Nichts ist endgültig, solange Sie nicht ausgestellt haben.

### Sie stellen die Dokumente aus

Bei der Ausstellung erhält jedes Dokument eine Nummer in einer lückenlosen Nummerierung, eine
strukturierte Mitteilung und ein Fälligkeitsdatum. OptimCE erzeugt drei Dokumente als PDF, jedes
mit seiner eigenen Serie:

- die **Rechnung** (F-…) für die geteilte Energie, die ein Mitglied verbraucht hat;
- die **Gutschrift** (NC-…), um eine bereits ausgestellte Rechnung zu annullieren;
- die **Vergütungsabrechnung** (DP-…) für die geteilte Einspeisung eines Erzeugers.

Ein Mitglied, das zugleich verbraucht und erzeugt, erhält zwei getrennte Dokumente. Eine
ausgestellte Rechnung lässt sich nicht mehr ändern: Ein Fehler wird durch eine Gutschrift und
anschließend eine neue Rechnung korrigiert, und die Historie bleibt vollständig.

### Sie verfolgen die Zahlungen

Die Mitglieder zahlen per Überweisung und geben dabei die strukturierte Mitteilung an. Sie erfassen
jede eingegangene Zahlung; der Betrag ist mit der Summe des Dokuments vorausgefüllt, und
Teilzahlungen sind möglich. Die Rechnung wechselt auf den Status „bezahlt“, sobald die Summe
erreicht ist, und Rechnungen mit überschrittener Fälligkeit erscheinen als überfällig.

Jedes Mitglied findet seinerseits seine eigenen Dokumente in der Anwendung, mit Nummer, Betrag,
Status und strukturierter Mitteilung. Es sieht nur seine eigenen.

{% include product-shot.html name="billing-member" alt="Bereich „Meine Rechnungen“ eines Mitglieds: eine Vergütungsabrechnung DP-2025-00001 mit dem Status „Ausgestellt“ über 36,69 €, mit ihrer strukturierten Mitteilung." caption="Was ein Mitglied sieht: seine Dokumente und die strukturierte Mitteilung, die es bei seiner Überweisung angibt (Testdaten)." %}

## Was es nicht leistet

**Brüssel und Flandern: geplant, noch nicht verfügbar.** Das Abrechnungsmodul ist heute auf
wallonische Gemeinschaften unter der Aufsicht der CWaPE ausgelegt. Der flämische und der Brüsseler
Rahmen sind geplant, aber noch nicht umgesetzt.

**Nur die geteilte Energie.** Die Rechnung der Gemeinschaft bewertet die geteilte Energie zum
internen Preis, ohne Netzentgelte und Steuern. Die Energie, die das Teilen nicht gedeckt hat,
stellt weiterhin der Lieferant jedes Mitglieds zu dessen Vertragstarif in Rechnung.

**Kein Zahlungseinzug.** OptimCE bucht nichts ab und nimmt keine Zahlung entgegen: Die Mitglieder
überweisen auf das Konto der Gemeinschaft, und Sie erfassen, was eingegangen ist.

**Dokumente auf Französisch.** Die PDF werden auf Französisch erzeugt, unabhängig von der Sprache
der Oberfläche.

**Vorerst ein einheitlicher MwSt.-Satz.** Das Modul wendet derzeit auf alle Dokumente einen Satz von
21 % an. Unterschiedliche Sätze, etwa der ermäßigte Satz von 6 % auf den Strom eines Haushalts, und
die Mehrwertsteuerbefreiung für Kleinunternehmen werden noch nicht unterstützt. Die Regelung der
Gemeinschaft, ob mehrwertsteuerpflichtig oder nicht und zu welchen Sätzen je nach Mitglied, wird vor
der ersten Rechnung mit einem Buchhalter entschieden: Unser Leitfaden zur Abrechnung von geteiltem
Strom stellt die Fälle vor.

## Häufige Fragen {#faq}

### Woher stammen die Daten für die Abrechnung?

Aus der vom Netzbetreiber übermittelten Aufteilung: den geteilten Mengen je Viertelstunde, die Sie
für die abzurechnende Operation und Periode importieren. Beim Start des Abrechnungslaufs friert
OptimCE einen Schnappschuss dieser Mengen ein; die Beträge werden auf diesen eingefrorenen Daten
berechnet, die sich nachvollziehen lassen.

### Kann man je nach Mitglied unterschiedliche Preise anwenden?

Ja. Jeder Preis gilt für die ganze Operation, für ein Kundensegment (Haushalte, Gewerbe, Industrie)
oder für eine bestimmte Lieferstelle (EAN), jeweils für einen Gültigkeitszeitraum. Betreffen
mehrere Regeln dasselbe Mitglied, gewinnt die genaueste: Der Preis einer EAN geht dem Preis ihres
Segments vor, und dieser dem globalen Preis.

### Wie korrigiert man eine bereits ausgestellte Rechnung?

Eine ausgestellte Rechnung hat eine Nummer in einer lückenlosen Nummerierung erhalten: Sie lässt
sich weder ändern noch löschen. Zur Korrektur stellen Sie eine Gutschrift aus, die sie annulliert,
und rechnen dann neu ab. Solange ein Dokument noch ein Entwurf ist, können Sie es dagegen löschen
oder neu berechnen.

### Wie geht OptimCE mit der MwSt. um?

Teilweise. Das Modul berechnet die MwSt., aber mit einem einheitlichen Satz von 21 % für alle
Dokumente: je nach Mitglied unterschiedliche Sätze und die Mehrwertsteuerbefreiung für
Kleinunternehmen werden noch nicht unterstützt. Die MwSt.-Regelung der Gemeinschaft (MwSt.-Pflicht,
für jedes Mitglied geltende Sätze) wird vor der ersten Rechnung mit einem Buchhalter festgelegt.

## Weiterlesen

- [Geteilten Strom in Belgien abrechnen]({{ "invoice-shared-electricity" | ref_url }}):
  wer was abrechnet, die MwSt. und die Pflichtangaben.
- [Interner Verrechnungspreis für geteilten Strom]({{ "internal-price-shared-energy" | ref_url }}):
  wie Sie einen Preis festlegen, der sich vor der Generalversammlung vertreten lässt.
- [Abrechnung in der Energiegemeinschaft]({{ "optimce-billing" | ref_url }}): die Ankündigung des
  Moduls, mit den Einzelheiten der Dokumente und ihres Lebenszyklus.

{% include product-cta.html page_key="billing" guide="billing-tarification-pay" title="Ihre Gemeinschaft mit OptimCE abrechnen" %}
