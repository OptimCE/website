---
layout: post
title: "Abrechnung in der Energiegemeinschaft: OptimCE erstellt Ihre Rechnungen"
date: 2026-07-16 10:00:00 +0200
author: "OptimCE-Team"
excerpt: "Neue OptimCE-Funktion: Erstellen Sie die Rechnungen Ihrer Energiegemeinschaft automatisch — vom Preis pro kWh bis zum PDF und zur Zahlungsverfolgung."
tags: [administrative, app, news]
lang: de
ref: optimce-billing
last_modified_at: 2026-07-23 10:00:00 +0200
permalink: /de/aktuelles/2026/07/16/energiegemeinschaft-abrechnung-optimce/
faq:
  - q: "Woher stammen die Daten für die Abrechnung?"
    a: "Aus den offiziellen Verteilungsdaten, die der Netzbetreiber übermittelt und die bereits in OptimCE importiert sind: verbrauchte geteilte Energie und geteilte Einspeisung, pro EAN und pro Periode. Beim Start eines Abrechnungslaufs friert OptimCE einen Schnappschuss dieser Volumina ein: Die Beträge werden auf eingefrorenen, nachvollziehbaren Daten berechnet."
  - q: "Wer legt die Preise für die geteilte Energie fest?"
    a: "Die Gemeinschaft selbst. Sie definieren frei zwei Preise in €/kWh: den Verkaufspreis der geteilten Energie an die Verbraucher und den Rückkaufpreis, der den Erzeugern für ihre Einspeisung gezahlt wird. Jeder Preis kann global, pro Kundensegment (Haushalte, Gewerbe, Industrie) oder für eine einzelne EAN gelten, mit einem Gültigkeitszeitraum — die spezifischste Regel gewinnt."
  - q: "Welche Dokumente erstellt OptimCE?"
    a: "Drei Dokumente, jedes mit eigener Nummernserie: die Rechnung (F-…) für die von einem Mitglied verbrauchte geteilte Energie, die Gutschrift (NC-…) zur Korrektur einer ausgestellten Rechnung und die Vergütungsabrechnung (DP-…) für die geteilte Einspeisung eines Erzeugers. Alle werden als PDF erzeugt; Entwürfe tragen ein 'Proforma'-Wasserzeichen."
  - q: "Was deckt die Rechnung einer Energiegemeinschaft ab?"
    a: "Nur die geteilte Energie, bewertet zum internen Preis der Gemeinschaft, ohne Netzentgelte und Steuern. Die Restenergie — der Teil, den das Teilen nicht abgedeckt hat — wird weiterhin vom Lieferanten jedes Mitglieds zu dessen Vertragstarif in Rechnung gestellt."
  - q: "Kann eine ausgestellte Rechnung korrigiert werden?"
    a: "Nicht direkt: Einmal ausgestellt, erhält eine Rechnung eine gesetzliche Nummer in einer lückenlosen Serie und kann weder geändert noch gelöscht werden. Zur Korrektur stellen Sie eine Gutschrift aus, die sie annulliert, und fakturieren dann neu. Ein Entwurf hingegen kann frei gelöscht oder neu berechnet werden."
  - q: "Wie greifen die Mitglieder auf ihre Rechnungen zu?"
    a: "Jedes Mitglied findet seine eigenen Rechnungen in der Anwendung und lädt das PDF herunter, wann es möchte. Auf Verwaltungsseite ist die Zahlungsverfolgung integriert: Sie erfassen Zahlungen — auch Teilzahlungen —, die Rechnung wechselt automatisch auf 'bezahlt', und überfällige Rechnungen werden nach dem Fälligkeitsdatum markiert."
---

Eine funktionierende Energiegemeinschaft produziert zwei Dinge: geteilte kWh … und Beträge, die abzurechnen sind. In jeder Periode weist die offizielle Verteilung jedem Mitglied seinen Anteil an der lokal erzeugten Energie zu — und dann muss jemand diese Volumina in Euro verwandeln: berechnen, was jeder Verbraucher schuldet und was jeder Erzeuger erhält, konforme Dokumente erstellen, Zahlungen einziehen und nachverfolgen. Bisher geschah diese Arbeit meist von Hand, zwischen Tabellenkalkulation und selbstgebasteltem Rechnungsmuster. Damit ist Schluss: OptimCE enthält jetzt ein **Abrechnungsmodul**, dessen erste Version einsatzbereit ist.

Das Prinzip ist einfach: Sie legen Ihre Preise fest, Sie wählen eine Periode, und OptimCE **erstellt die Rechnungen aller Mitglieder** aus den Verteilungsdaten, die bereits in der Plattform vorliegen — mit PDF, gesetzlicher Nummerierung, strukturierter Mitteilung und Zahlungsverfolgung.

Wenn Ihnen die Mechanik der Verteilung noch unklar ist, beginnen Sie mit unserem Referenzartikel [„Verteilungsschlüssel in Belgien: Wallonie, Brüssel, Flandern"](/de/aktuelles/2026/05/19/verteilungsschluessel-energiegemeinschaft-belgien/) — die Abrechnung ist ihre direkte Fortsetzung.

## Warum die interne Abrechnung das kritische Glied ist

Beim Energieteilen berechnet und übermittelt der Netzbetreiber, aber **er fakturiert nicht**: Er wendet den Verteilungsschlüssel Viertelstunde für Viertelstunde an und teilt die Volumina mit. Die Bewertung dieser Volumina — zu welchem Preis der Verbraucher die geteilte Energie bezahlt, zu welchem Preis der Erzeuger für seine Einspeisung vergütet wird — ist Sache der Gemeinschaft selbst.

Konkret lastet diese Aufgabe auf der Verwaltung der Gemeinschaft. Für jede Periode gilt es:

- **die exakten Volumina** pro Anschlusspunkt (EAN) zu übernehmen;
- **den richtigen Preis** auf jedes Profil anzuwenden, ohne Rechen- oder Rundungsfehler;
- **ein konformes Dokument** zu erstellen: [Mehrwertsteuer, Pflichtangaben](/de/aktuelles/2026/07/23/geteilten-strom-abrechnen-belgien/), fortlaufende Nummerierung;
- **eine Zahlungsreferenz** beizufügen und die eingehenden Überweisungen abzugleichen;
- **die Fragen der Mitglieder** zu ihrer Abrechnung zu beantworten.

Bei zehn Mitgliedern ist das mühsam, bei fünfzig unhaltbar. Und es geht um mehr als Verwaltung: Eine klare, regelmäßige Abrechnung ist die erste Voraussetzung für das **Vertrauen der Mitglieder** — sie macht den wirtschaftlichen Vorteil des Teilens schwarz auf weiß sichtbar. Wir haben es bereits in unserem [Leitfaden zur Gründung einer Energiegemeinschaft in der Wallonie](/de/aktuelles/2026/05/11/energiegemeinschaft-gruenden-wallonien/) geschrieben: In der Betriebsphase wird ein Verwaltungswerkzeug unverzichtbar.

## So funktioniert es: vom geteilten Volumen zur Rechnung

Das Modul ist in den Rest der Plattform integriert und folgt einem Ablauf in vier Schritten.

1. **Die Daten sind schon da.** Die Abrechnung stützt sich auf die offiziellen Verteilungsdaten, die bereits in OptimCE importiert sind: verbrauchte geteilte Energie und geteilte Einspeisung, pro EAN und pro Periode. Nichts neu eingeben, nichts exportieren — die Abrechnung liest dieselben Volumina wie Ihre Dashboards.
2. **Sie definieren Ihre Preise.** Zwei Preise, in €/kWh, frei von der Gemeinschaft festgelegt: der **Verkaufspreis** der geteilten Energie an die Verbraucher und der **Rückkaufpreis**, der den Erzeugern für ihre Einspeisung gezahlt wird. Jeder Preis kann global, pro Kundensegment (Haushalte, Gewerbe, Industrie) oder für eine einzelne EAN gelten — die spezifischste Regel gewinnt — und trägt einen Gültigkeitszeitraum. Welche Beträge Sie eintragen, ist eine andere Frage: Unser Leitfaden [„Strompreis in der Energiegemeinschaft: So legen Sie den internen Verrechnungspreis fest"](/de/aktuelles/2026/07/20/strompreis-energiegemeinschaft/) erläutert die vertretbare Bandbreite und fünf Berechnungsmethoden.
3. **Sie starten einen Abrechnungslauf.** Sie wählen die Periode — monatlich, vierteljährlich, ganz nach Bedarf — und OptimCE prüft vor der Berechnung, dass alles in Ordnung ist: Verbrauchsdaten vorhanden, Bankverbindung und rechtlicher Name der Gemeinschaft, anwendbarer Tarif, keine Duplikate in den Daten. Dann **friert es einen Schnappschuss** der Verteilung ein: Die Beträge werden auf eingefrorenen, nachvollziehbaren Volumina berechnet.
4. **Sie prüfen, dann stellen Sie aus.** Der Lauf erzeugt einen **Entwurf pro Mitglied**, als PDF mit „Proforma"-Wasserzeichen herunterladbar. Sie kontrollieren, dann stellen Sie aus: Die Rechnung erhält ihre gesetzliche Nummer, ihre strukturierte Mitteilung und ihr Fälligkeitsdatum.

Kurz gefasst — das geben Sie vor, das erhalten Sie:

| Sie definieren | OptimCE erstellt |
|---|---|
| Den Verkaufspreis für Verbraucher (€/kWh) | Eine Rechnung pro verbrauchendem Mitglied |
| Den Rückkaufpreis für Erzeuger (€/kWh) | Eine Vergütungsabrechnung pro Erzeuger |
| Die abzurechnende Periode | Nettosummen, Mehrwertsteuer und zu zahlenden Betrag |
| | Das versandfertige PDF mit IBAN und strukturierter Mitteilung |

## Drei Dokumente, lückenlose Nummerierung

Das Modul unterscheidet drei Dokumente, jedes mit eigener Serie:

| Dokument | Serie | Rolle |
|---|---|---|
| **Rechnung** | F-2026-00001 | Die von einem Mitglied verbrauchte geteilte Energie, zum internen Preis |
| **Gutschrift** | NC-2026-00001 | Die Korrektur einer bereits ausgestellten Rechnung |
| **Vergütungsabrechnung** | DP-2026-00001 | Die geteilte Einspeisung eines Erzeugers, zum Rückkaufpreis |

Jedes Dokument weist, Zeile für Zeile und EAN für EAN, die kWh multipliziert mit dem Einzelpreis aus, dann die Nettosumme, die Mehrwertsteuer und den zu zahlenden Betrag. Es zeigt den Aussteller (die Gemeinschaft als Vertreterin des Teilens), den Empfänger, die IBAN der Gemeinschaft, eine belgische **strukturierte Mitteilung**, um Überweisungen eindeutig abzugleichen, Ausstellungs- und Fälligkeitsdatum sowie die Pflichtangaben — einschließlich des Hinweises, dass die Rechnung die geteilte Energie **ohne Netzentgelte und Steuern** abdeckt.

Ein Mitglied, das zugleich verbraucht und erzeugt, erhält zwei getrennte Dokumente: seine Rechnung für geteilte Energie und seine Vergütungsabrechnung.

Die Nummerierung ist **fortlaufend und lückenlos**, wie es die Fakturierungsregeln verlangen: Eine ausgestellte Rechnung kann weder geändert noch gelöscht werden. Ein Fehler? Sie stellen eine **Gutschrift** aus, die sie annulliert, und fakturieren dann korrekt neu — die Historie bleibt intakt und prüfbar.

## Vom Entwurf zur Zahlung: der Lebenszyklus

Jede Rechnung folgt einem expliziten Lebenszyklus, auf einen Blick sichtbar:

| Status | Bedeutung |
|---|---|
| **Entwurf** | Berechneter Vorschlag, änderbar und löschbar — Proforma-PDF mit Wasserzeichen |
| **Ausgestellt** | Gesetzliche Nummer vergeben, endgültiges Dokument, Fälligkeit festgelegt |
| **Versendet** | An das Mitglied übermittelt |
| **Bezahlt** | Zahlungen in voller Höhe erfasst |
| **Überfällig** | Fälligkeit ohne vollständige Zahlung überschritten |

Die Zahlungsverfolgung ist integriert: Sie erfassen jede Überweisung — auch **Teilzahlungen** — und die Rechnung wechselt automatisch auf „bezahlt", sobald der Gesamtbetrag erreicht ist. Rechnungen mit überschrittener Fälligkeit werden als **überfällig** markiert, sodass Sie Erinnerungen gezielt versenden können, ohne Kontoauszüge zu durchforsten.

## Für die Mitglieder: Transparenz durch das Dokument

Jedes Mitglied findet **seine eigenen Rechnungen** in der Anwendung und lädt das PDF herunter, wann es möchte. Kein Warten mehr auf eine E-Mail der Verwaltung, kein Nachfragen nach einer Übersicht: Das Referenzdokument ist für alle am selben Ort verfügbar.

Zur Erinnerung an den Umfang: Die Rechnung der Gemeinschaft deckt die **geteilte Energie** ab, bewertet zum internen Preis. Die Restenergie — der Teil, den das Teilen nicht abgedeckt hat — wird weiterhin vom Lieferanten jedes Mitglieds zu dessen Vertragstarif in Rechnung gestellt. Erst beide Dokumente zusammen erzählen die erzielte Ersparnis; unser Artikel über [die Senkung der Stromrechnung durch Energieteilung](/de/aktuelles/2026/06/03/energiegemeinschaft-stromrechnung-senken/) erläutert diesen Mechanismus.

## Eine erste Version für die Wallonie — und die nächsten Schritte

Diese erste Version ist für den **wallonischen Rahmen** (CWaPE) konzipiert: angepasste Pflichtangaben und automatische Anwendung der Mehrwertsteuer auf die Rechnungen. Die Dokumente werden auf Französisch erzeugt; die Erzeugungskette ist bereits mehrsprachig ausgelegt, weitere Sprachen folgen.

Auf dem Programm der nächsten Versionen: der **automatische Rechnungsversand per E-Mail**, die Unterstützung des **flämischen und Brüsseler Rahmens** sowie reichere Tarifstrukturen. Getreu dem Ansatz von OptimCE: früh liefern, im Feld erproben, mit den Gemeinschaften iterieren.

Das Modul ist ab sofort auf [app.optimce.be](https://app.optimce.be) verfügbar — kostenlos, wie die gesamte Plattform während der Alpha-Phase.

## Fazit

Mit der Abrechnung schließt OptimCE den Kreis: Datenimport, [Auswahl und Simulation des Verteilungsschlüssels](/de/aktuelles/2026/06/09/verteilungsschluessel-simulieren-optimce/), Teilungsoperationen und jetzt die Rechnungen — der letzte Schritt, der bisher jedes Quartal in eine Tabellenkalkulations-Plackerei verwandelte. Volumina werden zu konformen Dokumenten, Zahlungen sind auf einen Blick nachverfolgbar, und jedes Mitglied sieht klar, was ihm das Teilen bringt.

> ### Rechnen Sie Ihre Energiegemeinschaft mit OptimCE ab
>
> Open-Source-Plattform für belgische Energiegemeinschaften: Importieren Sie Ihre Verteilungsdaten, definieren Sie Ihre Preise, erstellen Sie Rechnungen und Abrechnungen als PDF und verfolgen Sie die Zahlungen — alles in einer einzigen Anwendung.
>
> **[Loslegen auf app.optimce.be →](https://app.optimce.be)**

## FAQ

### Woher stammen die Daten für die Abrechnung?

Aus den offiziellen Verteilungsdaten, die der Netzbetreiber übermittelt und die **bereits in OptimCE importiert** sind: verbrauchte geteilte Energie und geteilte Einspeisung, pro EAN und pro Periode. Beim Start eines Abrechnungslaufs friert OptimCE einen Schnappschuss dieser Volumina ein: Die Beträge werden auf eingefrorenen, nachvollziehbaren Daten berechnet.

### Wer legt die Preise für die geteilte Energie fest?

**Die Gemeinschaft selbst.** Sie definieren frei zwei Preise in €/kWh: den Verkaufspreis der geteilten Energie an die Verbraucher und den Rückkaufpreis, der den Erzeugern für ihre Einspeisung gezahlt wird. Jeder Preis kann global, pro Kundensegment (Haushalte, Gewerbe, Industrie) oder für eine einzelne EAN gelten, mit einem Gültigkeitszeitraum — die spezifischste Regel gewinnt.

### Welche Dokumente erstellt OptimCE?

Drei Dokumente, jedes mit eigener Nummernserie: die **Rechnung** (F-…) für die von einem Mitglied verbrauchte geteilte Energie, die **Gutschrift** (NC-…) zur Korrektur einer ausgestellten Rechnung und die **Vergütungsabrechnung** (DP-…) für die geteilte Einspeisung eines Erzeugers. Alle werden als PDF erzeugt; Entwürfe tragen ein „Proforma"-Wasserzeichen.

### Was deckt die Rechnung einer Energiegemeinschaft ab?

Nur die **geteilte Energie**, bewertet zum internen Preis der Gemeinschaft, ohne Netzentgelte und Steuern. Die Restenergie — der Teil, den das Teilen nicht abgedeckt hat — wird weiterhin vom Lieferanten jedes Mitglieds zu dessen Vertragstarif in Rechnung gestellt.

### Kann eine ausgestellte Rechnung korrigiert werden?

Nicht direkt: Einmal ausgestellt, erhält eine Rechnung eine gesetzliche Nummer in einer **lückenlosen Serie** und kann weder geändert noch gelöscht werden. Zur Korrektur stellen Sie eine **Gutschrift** aus, die sie annulliert, und fakturieren dann neu. Ein Entwurf hingegen kann frei gelöscht oder neu berechnet werden.

### Wie greifen die Mitglieder auf ihre Rechnungen zu?

Jedes Mitglied findet **seine eigenen Rechnungen** in der Anwendung und lädt das PDF herunter, wann es möchte. Auf Verwaltungsseite ist die Zahlungsverfolgung integriert: Sie erfassen Zahlungen — auch Teilzahlungen —, die Rechnung wechselt automatisch auf „bezahlt", und überfällige Rechnungen werden nach dem Fälligkeitsdatum markiert.

## Quellen

- [CWaPE — Energiegemeinschaften](https://www.cwape.be/node/158) — der wallonische Rahmen für Energiegemeinschaften: Typen, Rechtsgrundlagen, Meldung und jährliche Berichterstattung.
- [CWaPE — Energiegemeinschaften und Energieteilung](https://www.cwape.be/secteur/communautes-partage-energie) — der allgemeine wallonische Rahmen der Energieteilung.
- [FÖD Finanzen — Mehrwertsteuer](https://finances.belgium.be/fr/entreprises/tva) — Fakturierungs-, Buchhaltungs- und Mehrwertsteuerpflichten für belgische Unternehmen und juristische Personen.
- [Pricing and sharing rules for energy communities](https://econpapers.repec.org/article/eeejuipol/v_3a96_3ay_3a2025_3ai_3ac_3as0957178725001109.htm) — Forschung zu Teilungsregeln und interner Preisgestaltung in Energiegemeinschaften.
