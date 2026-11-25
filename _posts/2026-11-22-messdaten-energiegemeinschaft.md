---
layout: post
title: "Messdaten in der Energiegemeinschaft"
date: 2026-11-22 06:00:00 +0100
author: "Eric von OptimCE"
excerpt: "Eine Energiegemeinschaft misst nichts selbst. Jeden Monat, spätestens am zwölften Werktag, schickt der Netzbetreiber ihrem Vertreter die Mengen jedes Mitglieds, Viertelstunde für Viertelstunde: 2 880 Werte je Zähler und Größe für einen Monat mit dreißig Tagen. Dieser Datenfluss ist eine Bedingung der Teilnahme, keine Einwilligung. Alles andere, von den Verlaufsdaten zur Simulation eines Aufteilungsschlüssels bis zum Gerät am P1-Port, braucht die Zustimmung jedes Mitglieds."
description: "Messdaten einer Energiegemeinschaft: was der Netzbetreiber wann übermittelt, auf welcher Rechtsgrundlage, was jedes Mitglied sieht, und der P1-Port."
tags: [guide, community]
lang: de
ref: meter-data-energy-community
pillar: communautes-energie
last_modified_at: 2026-11-24 06:00:00 +0100
permalink: /de/ratgeber/messdaten-energiegemeinschaft/
faq:
  - q: "Welche Messdaten übermittelt der Netzbetreiber einer Energiegemeinschaft?"
    a: "In der Wallonie schickt der Verteilernetzbetreiber dem Vertreter der Teilung für jedes Mitglied und jede Viertelstunde die Entnahme, die geteilte verbrauchte Menge und den Restverbrauch, den die CWaPE „alloconsommation“ nennt: den Teil, den der Lieferant in Rechnung stellt. Dazu kommen die Einspeisung jedes Erzeugers, die gesamte geteilte Menge, der Überschuss und die verwendete Aufteilungsmethode. Der von der CWaPE am 12. Oktober 2023 genehmigte Mustervertrag verpflichtet ihn, diese Daten jeden Monat bereitzustellen, spätestens am zwölften Werktag des Folgemonats. Das ist eine Bemühenspflicht, und nicht validierte Daten können wöchentlich kommen. Kanal und Format wählt der Netzbetreiber. Bei ORES sind es zwei CSV-Dateien per E-Mail, eine für die Erzeugung, eine für den Verbrauch, mit einer Zeile je Viertelstunde, EAN-Code und Iteration des Aufteilungsschlüssels."
  - q: "Muss ich einwilligen, damit meine Daten an die Gemeinschaft gehen?"
    a: "Für den Datenfluss des Teilens selbst nicht. Das wallonische Stromdekret verpflichtet den Netzbetreiber, dem Vertreter die Messdaten jedes Teilnehmers zu übermitteln, und der Mustervertrag der CWaPE hält fest, dass jede Teilnahme die Erhebung und Nutzung der Lastkurven durch den Netzbetreiber erfordert. Dieser Datenfluss ist eine Bedingung der Teilnahme: Man kann nicht im Teilen bleiben und ihn ablehnen. Der Teilnehmer unterschreibt jedoch die Anlage 8 des Teilungsformulars. Darin beauftragt er den Vertreter, seine Daten im Verfahren mitzuteilen, und erlaubt dem Netzbetreiber, seine Viertelstundenkurve an seinen Lieferanten zu übermitteln. Alles, was über diesen Rahmen hinausgeht, verlangt dagegen eine vorherige, freie, spezifische, informierte und unmissverständliche Zustimmung: die Verlaufsdaten zur Simulation eines Aufteilungsschlüssels, ein Gerät am P1-Port, einzelne Lastkurven, die anderen Mitgliedern gezeigt werden."
  - q: "Können die anderen Mitglieder meinen Verbrauch sehen?"
    a: "Nicht standardmäßig. Der Netzbetreiber schickt die Daten jedes Mitglieds an den Vertreter, nicht an die anderen Mitglieder, und das wallonische Dekret schreibt vor, dass der Vertrag zwischen jedem Teilnehmer und der Gemeinschaft den Schutz der Privatsphäre und das Verfahren für die Übermittlung von Daten zwischen Teilnehmern regelt. Die belgische Datenschutzbehörde erinnert daran, dass kommunizierende Zähler Rückschlüsse auf sensible Daten über das Verhalten der Bewohner erlauben: Eine Viertelstundenkurve zeigt, wann ein Haushalt aufsteht, das Haus verlässt und zurückkommt. Eine vorsichtige Praxis besteht darin, jedem Mitglied seine eigenen Zahlen zu zeigen und der Gruppe nur die Gesamtwerte: Erzeugung, geteilte Menge, gedeckter Anteil des Verbrauchs. Eine namentliche Rangliste oder eine einzelne Lastkurve wird nur mit ausdrücklicher Zustimmung der Person gezeigt. Eine Ausnahme ergibt sich aus der Sache: Hat die Gemeinschaft nur einen Erzeuger, ist die geteilte Erzeugung die Einspeisung dieses Mitglieds."
  - q: "Wie komme ich an die Daten meines Smart Meters?"
    a: "Über das Portal Ihres Netzbetreibers, kostenlos: Das wallonische Dekret schreibt es vor. Der Erlass vom 1. Dezember 2022 legt das Minimum fest: Jahres-, Monats-, Wochen- und Tagesansichten über die letzten vierundzwanzig Monate, Details innerhalb des Tages auf ausdrücklichen Antrag und einen Export in eine Tabellenkalkulation. Bei ORES beantragen Sie die Viertelstundenansicht im Kundenbereich myORES; laut ORES gehen diese Daten nicht an Ihren Lieferanten, die Aktivierung selbst wird ihm aber übermittelt, was bei manchen Lieferanten eine Zwischenrechnung auslösen kann, ohne Folgen für die Jahresabrechnung. RESA bietet ein Viertelstundenprofil in MyRESA, die AIEG und die AIESH in MyConso. Dieselben Daten wird eine Gemeinschaft von Ihnen verlangen, um vor dem Teilen einen Aufteilungsschlüssel zu simulieren: Sie können sie exportieren und ihr anvertrauen, mit einer schriftlichen Zustimmung für diesen Zweck. Während des Teilens erhalten Sie Ihre geteilten Mengen über die Gemeinschaft, die sie jeden Monat vom Netzbetreiber bekommt."
  - q: "Kann der P1-Port für das Energieteilen dienen?"
    a: "Nicht für die Berechnung. Der P1-Port des Smart Meters liefert einen Datensatz pro Sekunde, nützlich, um den eigenen Verbrauch in Echtzeit zu verfolgen, aber er zeigt nur Ihren eigenen Zähler: weder die Erzeugung des geteilten Dachs noch den Anteil, der Ihnen zugeteilt wird. Die Mengen des Teilens bestimmt der Netzbetreiber anhand der Messwerte und des Aufteilungsschlüssels und übermittelt sie jeden Monat dem Vertreter; auf ihrer Grundlage wird die Rechnung des Teilens erstellt. In der Wallonie ist der Port standardmäßig deaktiviert, und seine Aktivierung ist auf einfachen Antrag beim Netzbetreiber kostenlos. Das Dekret macht denjenigen, der über diesen Port Daten erhebt, zum Verantwortlichen für ihre Verarbeitung: Eine Gemeinschaft, die P1-Geräte verteilt und ihre Messungen zentral sammelt, muss die vorherige Zustimmung jedes Mitglieds einholen und es über die Nutzung informieren."
  - q: "Wie lange werden die Daten des Teilens aufbewahrt?"
    a: "In der Wallonie legt das Stromdekret die Regel für die CWaPE und den Netzbetreiber fest: Personenbezogene Daten im Zusammenhang mit dem Teilen werden fünf Jahre nach dem Ende der Teilungsaktivität aufbewahrt, und die Daten eines Teilnehmers, der das Teilen verlassen hat, werden fünf Jahre nach der Mitteilung seines Austritts gelöscht. Für den Vertreter legt der Text keine Frist fest. Als Verantwortlicher für die Daten, die er vom Netzbetreiber erhält, darf er sie nur für die im Dekret vorgesehenen Zwecke verwenden, und die DSGVO verpflichtet ihn, selbst eine Aufbewahrungsdauer festzulegen und sie den Mitgliedern mitzuteilen. Für den Zähler schreibt das Dekret vor, dass er die Lastkurven der letzten zehn Tage, die täglichen Zählerstände der letzten vierzig Tage und die monatlichen Zählerstände der letzten dreizehn Monate aus der Ferne lesbar speichert."
---

Eine Energiegemeinschaft lebt von Daten, die sie nicht selbst erzeugt. Ihre **Messdaten** kommen alle vom Verteilernetzbetreiber (VNB), dem das wallonische Dekret die Erhebung der Messdaten vorbehält. Jeden Monat schickt er dem Vertreter der Teilung die Mengen jedes Mitglieds, Viertelstunde für Viertelstunde: **2 880 Werte je Zähler** und Größe für einen Monat mit dreißig Tagen, **spätestens am zwölften Werktag** des Folgemonats.

Diese Daten fließen nach zwei Regelungen. Die erste legt das Gesetz fest: Der Netzbetreiber übermittelt, die Gemeinschaft empfängt, und kein Mitglied muss einwilligen. Die zweite deckt alles andere ab, von den Verlaufsdaten zur Simulation eines Aufteilungsschlüssels bis zum Gerät am P1-Port, und sie verlangt die Zustimmung jedes Mitglieds.

Andere Ratgeber dieser Website behandeln bereits die Messregime und den P1-Port ([„Smart Meter in der Wallonie: der Ratgeber“](/de/ratgeber/smart-meter-wallonie/)), die Anwendung des Schlüssels ([„Aufteilungsschlüssel in Belgien: 3 Regionen“](/de/ratgeber/verteilungsschluessel-energiegemeinschaft-belgien/)), die Simulation ([„Aufteilungsschlüssel simulieren: Szenarien testen“](/de/ratgeber/verteilungsschluessel-simulieren-optimce/)), die Viertelstundenregel ([„Strom auf kurzem Weg: Anleitung für Wallonien“](/de/ratgeber/strom-kurze-wege-anleitung/)) und die Formulare ([„Energiegemeinschaft: CWaPE-Dokumente und Fristen“](/de/ratgeber/energiegemeinschaft-verwaltungsdokumente-wallonien/)).

**Hier geht es um den Weg der Daten: welche Daten vom Netzbetreiber zur Gemeinschaft gehen, in welchem Rhythmus, auf welcher Rechtsgrundlage, und was ein Mitglied von sich selbst und von den anderen sehen darf.** Der Artikel beschreibt die Regeln für Strom in der Wallonie, Stand 22. November 2026; sie gelten damit auch in Ostbelgien. Flandern und Brüssel werden am Ende zusammengefasst.

## Welche Daten eine Gemeinschaft braucht

Eine Gemeinschaft braucht Daten zu drei Zeitpunkten. **Vor dem Teilen**, um ihren Aufteilungsschlüssel zu wählen: die Verlaufsdaten jedes künftigen Mitglieds und das Erzeugungsprofil, idealerweise ein Jahr in Viertelstunden. Der Netzbetreiber schickt in dieser Phase nichts; die Mitglieder liefern diese Kurven. **Während des Teilens**, um abzurechnen: die Mengen, die der Netzbetreiber jeden Monat berechnet. **Danach**, um Rechenschaft abzulegen: Der Netzbetreiber übermittelt der CWaPE jedes Jahr die Messdaten jeder Gemeinschaft (Artikel 35*sexdecies* § 3 des Dekrets vom 12. April 2001).

Die Größen des Teilens definiert der Mustervertrag, den die CWaPE am 12. Oktober 2023 genehmigt hat und den jede Gemeinschaft mit ihrem Netzbetreiber unterschreibt. Sie werden für jeden EAN-Code und jede Viertelstunde berechnet. Abkürzungen und Formeln sind die des französischen Textes.

| Größe | Abkürzung | Was sie misst |
|---|---|---|
| Einspeisung | I | Die vor Ort nicht verbrauchte Erzeugung, die ins Netz eingespeist wird |
| Entnahme | Pl | Der Verbrauch aus dem Netz: Pl = VPC + AL |
| Geteilte Menge | VP | Die Summe der Einspeisungen, die dem Teilen zur Verfügung stehen |
| Geteilte verbrauchte Menge | VPC | Der Verbrauch eines Teilnehmers, den das Teilen deckt |
| Überschuss je Teilnehmer | E | Die einem Teilnehmer zugeteilte Menge, die er nicht verbraucht hat |
| Überschuss | S | Die geteilte Menge, die niemand verbraucht hat: S = VP − ∑ VPC |
| Restverbrauch („alloconsommation“) | AL | Der nicht gedeckte Teil, den der Lieferant in Rechnung stellt: AL = Pl − VPC |

*Annahmen: Definitionen aus Artikel 6.2.1 des Mustervertrags (Entscheidung CWaPE CD-23j12-CWaPE-0818), umformuliert; die Formeln sind die des Textes, der den Restverbrauch auch „volume résiduel“ (Restmenge) nennt.*

### Der Zähler muss sie messen können

Für einen Smart Meter stellt der Leitfaden der CWaPE zum Teilungsformular zwei Bedingungen: eine Kommunikationsfunktion, die aktiviert ist und funktioniert, und das Messregime 3 (R3), das die Viertelstundenkurve an den Markt übermittelt und *„beim Lieferanten, auf Antrag des Teilnehmers“* aktiviert wird (unsere Übersetzung). Bis dieses Regime aktiv ist, tritt die Anlage 8 des Formulars an seine Stelle: Der Teilnehmer erlaubt dort dem Netzbetreiber, seinem Lieferanten seine Viertelstunden-Messdaten zu übermitteln.

Ein Mitglied muss das also vor der Unterschrift wissen: **Seine Lastkurve geht an den Vertreter, aber auch an seinen Lieferanten.** Unser [Barometer der genehmigten Teilungen](/de/ratgeber/energiegemeinschaften-wallonien-barometer/) hat es festgestellt: Wenn die CWaPE ein Teilen unter aufschiebender Bedingung genehmigt, besteht die Bedingung immer darin, alle Teilnehmer in das Regime R3 zu bringen.

## Was der Netzbetreiber übermittelt, an wen und wann

Die Netzbetreiber *„bestimmen die im Rahmen der Teilungsaktivität verbrauchten Strommengen“* und übermitteln dann der Gemeinschaft *„die Messdaten“* der Erzeugung und jedes Teilnehmers, den Lieferanten *„die für die Abrechnung erforderlichen Daten“* (Artikel 35*sexdecies* § 2; unsere Übersetzung). Das Dekret legt weder Rhythmus noch Frist noch Format fest.

Der Mustervertrag legt sie fest: Der Netzbetreiber *„setzt alle Mittel ein“*, um diese Daten *„monatlich und spätestens am zwölften Werktag des Folgemonats“* bereitzustellen (Artikel 6.2.2; unsere Übersetzung). Das ist eine Bemühenspflicht. Nicht validierte Daten können wöchentlich kommen, über den Kanal, den der Netzbetreiber gewählt hat.

Bei ORES sind es zwei CSV-Dateien, die jeden Monat per E-Mail kommen, eine für die Erzeugung, eine für den Verbrauch. Jede Zeile der zweiten enthält eine Viertelstunde, einen EAN-Code und eine Iteration des Schlüssels; das Ergebnis eines Mitglieds ist die Summe seiner Iterationen. Zwölf Verbraucher und ein Schlüssel in drei Iterationen ergeben bis zu **103 680 Zeilen** für einen Monat mit dreißig Tagen.

| Empfänger | Was er erhält | Rhythmus |
|---|---|---|
| Vertreter der Teilung | Die Größen oben, je EAN und Viertelstunde, und die Aufteilungsmethode | Jeden Monat, spätestens am 12. Werktag des Folgemonats |
| Lieferant jedes Mitglieds | Die Viertelstundenkurve und die geteilten Mengen, um den Rest abzurechnen | Jeden Monat, außerhalb der Marktprozesse |
| Mitglied | Was die Gemeinschaft ihm mitteilt; seine Lastkurve im Portal des Netzbetreibers | Nach seinem Vertrag; Portal frei zugänglich |
| CWaPE | Die Messdaten jeder Gemeinschaft | Jedes Jahr |

*Annahmen: in der Wallonie am 22. November 2026 geltende Regeln: Dekret vom 12. April 2001 (Artikel 35ter, 35duodecies und 35sexdecies), Mustervertrag der CWaPE und Evaluierungsbericht der CWaPE vom 20. Februar 2025.*

Die Lieferanten erhalten die geteilten Mengen nicht auf dem üblichen Weg: Laut dem Evaluierungsbericht der CWaPE vom 20. Februar 2025 laufen sie außerhalb der Marktprozesse über einen getrennten Kanal (SFTP-Server), und jeder Lieferant berechnet neu, was er in Rechnung stellt.

Die neue technische Regelung, die die CWaPE am 27. August 2026 genehmigt hat, behält die Frist des zwölften Werktags bei. Die Daten gehen dann als Viertelstundenkurve und zusätzlich als Monatssumme hinaus, über eine Programmierschnittstelle (API), wenn der Netzbetreiber eine entwickelt hat (Artikel IX.7), und Korrekturen sind bis zu zwölf Monate nach dem betroffenen Monat möglich (Artikel IX.17). Am 20. November 2026 im Belgischen Staatsblatt veröffentlicht, tritt sie am 30. November 2026 in Kraft.

Für den Verwalter der Gemeinschaft ergibt das einen Zeitplan: Die Mengen eines Monats kommen spätestens um die Mitte des Folgemonats, und danach gehen die Rechnungen des Teilens hinaus. Eine späte Korrektur läuft über eine Gutschrift, wie [„Geteilten Strom in Belgien abrechnen“](/de/ratgeber/geteilten-strom-abrechnen-belgien/) erklärt. Bestreitet ein Mitglied eine Menge, leitet der Vertreter seine Beanstandung binnen fünf Werktagen an den Netzbetreiber weiter, und der Netzbetreiber antwortet binnen dreißig Tagen (Mustervertrag, Artikel 6.1.4).

## Rechtsgrundlage und Einwilligung: zwei Regelungen

### Was kraft Gesetzes fließt

Der Netzbetreiber ist Verantwortlicher für die Verarbeitung der Zählerdaten, und er verarbeitet sie *„ausschließlich zur Erfüllung seiner gesetzlichen oder verordnungsrechtlichen Aufgaben“* (Artikel 35*septies* § 2; unsere Übersetzung). Für die Meldung und die Genehmigung des Teilens stützt die CWaPE die Verarbeitung auf Artikel 6 Absatz 1 Buchstabe e der Datenschutz-Grundverordnung (DSGVO), die Aufgabe im öffentlichen Interesse. Der Mustervertrag ist eindeutig: *„Jede Teilnahme erfordert die Erhebung und Nutzung der Lastkurven“* der Teilnehmer durch den Netzbetreiber (Artikel 6.1.3; unsere Übersetzung). Sobald der Vertreter die Daten erhalten hat, wird er seinerseits Verantwortlicher für sie, allein für die im Dekret vorgesehenen Zwecke (Artikel 9.4).

Dieser Datenfluss beruht also nicht auf einer Einwilligung, die ein Mitglied widerrufen und trotzdem im Teilen bleiben könnte: Er ist die Bedingung der Teilnahme. Die Anlage 8 dokumentiert ihn, mit dem Auftrag an den Vertreter und der Erlaubnis, die Lastkurve an den Lieferanten zu schicken. Die CWaPE und der Netzbetreiber bewahren diese Daten fünf Jahre nach dem Ende des Teilens auf; die Daten eines ausgetretenen Mitglieds werden fünf Jahre nach der Mitteilung seines Austritts gelöscht (Artikel 35*quaterdecies* § 3).

### Was die Zustimmung jedes Mitglieds braucht

Für alles andere gilt eine strenge Regel. Außerhalb gesetzlicher Bestimmungen und außerhalb der Auftragsverarbeiter des Netzbetreibers gilt: *„Niemand darf die Informationen lesen, exportieren oder verarbeiten“*, die ein kommunizierender Zähler liefert, ohne die *„vorherige, freie, spezifische, informierte und unmissverständliche“* Zustimmung seines Nutzers (Artikel 35*septies* § 3; unsere Übersetzung). Für eine Gemeinschaft betrifft das die Verlaufsdaten zur Simulation eines Schlüssels, ein Gerät am P1-Port, eine Lastkurve oder namentliche Mengen, die anderen Mitgliedern gezeigt werden, und alle Daten, die einem Dritten für einen anderen Zweck anvertraut werden.

Eine Klausel, die in der Satzung untergeht, genügt nicht. Schon 2018 schrieb der belgische Ausschuss für den Schutz des Privatlebens, Vorgänger der Datenschutzbehörde: *„Die gängige Praxis, die ‚Einwilligung‘ über eine Klausel in den allgemeinen Geschäftsbedingungen zu erteilen, kann nicht mehr anerkannt werden“* (unsere Übersetzung). Eine Zustimmung wird gesondert eingeholt, für einen bestimmten Zweck, und lässt sich so leicht widerrufen, wie sie erteilt wurde (Artikel 7 Absatz 3 DSGVO). Unabhängig von jeder Zustimmung verbietet das Dekret den Handel mit Messdaten und mit Profilen, aus denen sich das Verbrauchsverhalten ableiten lässt.

Diese Regeln gehören in den Vertrag zwischen jedem Teilnehmer und der Gemeinschaft. Er muss *„die Regeln und Verantwortlichkeiten in Bezug auf die Achtung der Privatsphäre und den Schutz personenbezogener Daten“* und *„das Verfahren der Datenübermittlung zwischen den Teilnehmern“* enthalten (Artikel 35*duodecies* § 2; unsere Übersetzung). Vertraut die Gemeinschaft ihre Dateien einer Online-Software an, ist der Anbieter, der sie speichert, Auftragsverarbeiter im Sinne von Artikel 28 DSGVO, und es braucht einen Vertrag mit ihm. Wir haben keine belgische Leitlinie gefunden, die sich eigens an Gemeinschaften richtet: Es gelten die allgemeinen Regeln der DSGVO.

### Die Verlaufsdaten vor dem Teilen

Vor der Genehmigung kommen die Kurven, mit denen ein Schlüssel simuliert wird, von den Mitgliedern. Der einfachste Weg ist der Export: Der Erlass der Wallonischen Regierung vom 1. Dezember 2022 schreibt vor, dass das Portal des Netzbetreibers vierundzwanzig Monate abdeckt, die Details innerhalb des Tages auf ausdrücklichen Antrag des Kunden anzeigt und den Export der Daten in einer Form erlaubt, die eine Tabellenkalkulation verarbeiten kann (Artikel 4). Das Mitglied exportiert und vertraut die Datei dann der Gemeinschaft an, mit einer schriftlichen Zustimmung für diesen Zweck.

Der andere Weg ist der delegierte Zugang. ORES öffnet eine Programmierschnittstelle für Energiedienstleister, die mit der Einwilligung, die der Kunde in myORES erteilt, bis zu drei Jahre Viertelstundenmengen abrufen. Die Durchführungsverordnung (EU) 2023/1162 zählt Erneuerbare-Energie-Gemeinschaften und Bürgerenergiegemeinschaften übrigens zu den berechtigten Parteien, denen ein Kunde den Zugang zu seinen Messdaten erlauben kann.

## Was jedes Mitglied sehen kann und was es von den anderen nicht sehen soll

Der Netzbetreiber schickt die Mengen des Teilens an den Vertreter, nicht an die Mitglieder. Was ein Mitglied davon erhält, hängt von der Gemeinschaft ab: seine Teilungsrechnung, die seine geteilte verbrauchte Menge ausweist, und was sein Vertrag zusätzlich vorsieht. Seine vollständige Lastkurve sieht es kostenlos im Portal seines Netzbetreibers (Artikel 35*ter* § 3). Bei ORES wird die Viertelstundenansicht im Kundenbereich myORES beantragt. Sie leitet diese Daten nicht an den Lieferanten weiter, der sie selbst bei ORES anfordern muss, um sie zu nutzen; laut der FAQ von myORES wird die Aktivierung dem Lieferanten aber übermittelt, und manche Lieferanten stellen dann eine Zwischenrechnung aus, ohne Folgen für die Jahresabrechnung oder die Kompensation. RESA bietet ein Viertelstundenprofil in MyRESA, die AIEG und die AIESH in MyConso. Macht das Mitglied beim Vertreter sein Auskunftsrecht für Daten geltend, die der Netzbetreiber hält, leitet der Vertreter den Antrag unverzüglich weiter, und der Netzbetreiber antwortet dem Mitglied direkt (Mustervertrag, Artikel 9.4).

Was die Mitglieder voneinander sehen, ist eine andere Frage. Die Datenschutzbehörde erinnerte 2023 daran, dass kommunizierende Zähler es *„ermöglichen, potenziell sensible Daten über das Verhalten der Bewohner abzuleiten“* (unsere Übersetzung). Eine Viertelstundenkurve zeigt, wann ein Haushalt aufsteht, wann sich das Haus leert und wann es sich wieder füllt. Das Dekret überlässt diesen Punkt dem Vertrag jedes Teilnehmers; regelt dieser nichts, schreibt die DSGVO die Datenminimierung vor (Artikel 5 Absatz 1 Buchstabe c). Wir empfehlen drei Regeln:

- jedes Mitglied sieht seine eigenen Zahlen, einschließlich der Viertelstunden;
- die Gruppe sieht die Gesamtwerte: Erzeugung, geteilte Menge, gedeckter Anteil des Verbrauchs;
- eine namentliche Rangliste oder eine einzelne Lastkurve wird nur mit ausdrücklicher Zustimmung der Person gezeigt.

Eine Ausnahme: Gibt es nur einen Erzeuger, ist die Erzeugung der Gemeinschaft seine Einspeisung, und alle sehen sie zumindest als Summe. Sagen Sie es ihm am besten, bevor er unterschreibt. [„Mitglieder einer Energiegemeinschaft einbinden“](/de/ratgeber/energiegemeinschaft-mitglieder-einbinden/) gibt Beispiele dafür, was man mit der Gruppe teilen kann.

## Der P1-Port: Echtzeitmessung neben den offiziellen Daten

Der Smart Meter hat einen zweiten, lokalen Ausgang. Das Dekret verlangt, dass er Informationen nahezu in Echtzeit liefert, die über einen Ausgangsport nutzbar sind (Artikel 35*bis* § 1): Das ist der P1-Port. In der Wallonie ist er standardmäßig deaktiviert und wird auf einfachen Antrag beim Netzbetreiber aktiviert (Artikel 35*bis* § 4), laut der Tabelle der harmonisierten nichtperiodischen Tarife 2026 kostenlos; unser [Ratgeber zum Smart Meter](/de/ratgeber/smart-meter-wallonie/) beschreibt das Vorgehen. Der Port folgt der belgischen Spezifikation eMUCS-P1, die auf der niederländischen Spezifikation DSMR 5.0.2 beruht: ein Datensatz pro Sekunde, mit bezogener und eingespeister Leistung, Spannung und Strom je Phase, den Zählerständen und dem letzten Wert des Gaszählers. Eine Viertelstunde der offiziellen Messung entspricht **900 Datensätzen** am P1-Port.

Für eine Gemeinschaft hat er drei Grenzen.

**Er zeigt nur Ihren Zähler.** Ein Verbraucher liest dort seine Entnahme ab, ein Erzeuger seine Nettoeinspeisung. Niemand sieht dort die Erzeugung des geteilten Dachs oder den Anteil, der ihm zugeteilt wird; dieser entsteht erst durch die Berechnung des Netzbetreibers.

**Er liefert nicht die offiziellen Mengen.** Die Mengen des Teilens sind die, die der Netzbetreiber laut Dekret bestimmt und jeden Monat übermittelt; die CWaPE erinnert daran, dass die Rechnungen des Teilens auf Grundlage der vom Netzbetreiber erhaltenen Daten erstellt werden.

**Wer ihn ausliest, wird Verantwortlicher.** Der Dritte, der Informationen über den Port erhebt, *„wird für die von ihm erhobenen Informationen zum Verantwortlichen für die Verarbeitung personenbezogener Daten“* (Artikel 35*septies* § 3; unsere Übersetzung), und ORES weist darauf hin, dass es die Daten nicht mehr kontrolliert, sobald der Port geöffnet ist. Eine Gemeinschaft, die P1-Geräte verteilt und ihre Messungen zentral sammelt, muss die vorherige Zustimmung jedes Mitglieds einholen, es über die vorgesehene Nutzung informieren und das Erhobene absichern.

Um live zu wissen, dass das gemeinsame Dach erzeugt, müsste man die Messungen der Erzeuger zusammenführen und an die Gruppe weitergeben, wiederum mit der Zustimmung jedes Einzelnen. Eine solche Funktion wird bei OptimCE geprüft; sie ist heute nicht verfügbar.

## Eine Lastkurve lesen

Eine Viertelstunden-Lastkurve, das sind 96 Werte pro Tag und Zähler. Nehmen wir den Fall, der das Raster unserer Startseite speist und den auch [„Impact-Tarif und Energiegemeinschaft“](/de/ratgeber/impact-tarif-energiegemeinschaft/) verwendet: ein 24-kWp-Dach in Namur, geteilt zwischen zwölf Haushalten mit je 3 500 kWh im Jahr.

<img src="/assets/images/diagrams/community-load-curve-day-de.svg"
     alt="Diagramm eines Tages Energieteilung, Dienstag, 13. Juni 2023, für eine Referenzgemeinschaft: ein Solardach mit 24 Kilowatt-Peak in Namur und zwölf Haushalte, die je 3 500 Kilowattstunden im Jahr verbrauchen. Die waagerechte Achse umfasst die 96 Viertelstunden des Tages, von 0 bis 24 Uhr; die senkrechte Achse zeigt die Energie jeder Viertelstunde, von 0 bis 5 Kilowattstunden. Die Erzeugung des Dachs ist nachts null, beginnt gegen 5:15 Uhr, erreicht in der Viertelstunde ab 13 Uhr ihr Maximum von 4,72 Kilowattstunden und endet gegen 22 Uhr: 152,9 Kilowattstunden am Tag. Der Verbrauch der zwölf Haushalte liegt zwischen 0,68 und 1,73 Kilowattstunden je Viertelstunde, mit einer Spitze gegen 7:15 Uhr und einer höheren gegen 18:45 Uhr: 93,9 Kilowattstunden. Die grüne Fläche, die geteilte Energie, ist in jeder Viertelstunde der kleinere der beiden Werte: 50,6 Kilowattstunden. Von 8:15 bis 18:30 Uhr übersteigt die Erzeugung den Verbrauch, und der Überschuss, 102,3 Kilowattstunden in Bernstein, geht ins Netz. Morgens und abends ist es umgekehrt: Der Restbezug, 43,3 Kilowattstunden in Grau, kommt vom Lieferanten jedes Haushalts. Drei Markierungen zeigen 7:00, 12:30 und 19:00 Uhr, die Viertelstunden, die die Tabelle des Artikels aufschlüsselt. Ein Hinweis erinnert daran, dass eine in einer Viertelstunde verbrauchte Kilowattstunde 4 Kilowatt mittlerer Leistung entspricht. Quellen: PVGIS für die Erzeugung, ein synthetisches Verbrauchsprofil, das kein Synergrid-Profil ist."
     width="800" height="520" loading="lazy" decoding="async"
     style="width:100%;height:auto">

**Zuerst die Einheit.** Jeder Wert ist eine Energie, in Kilowattstunden je Viertelstunde, keine Leistung. Die mittlere Leistung erhalten Sie, wenn Sie mit vier multiplizieren: Um 12:30 Uhr erzeugt das Dach 4,57 kWh in einer Viertelstunde, also durchschnittlich 18,3 kW bei einer Anlage mit 24 kWp.

| Viertelstunde | Erzeugung | Verbrauch | Geteilt | Überschuss ins Netz | Restbezug vom Lieferanten |
|---|---|---|---|---|---|
| 7:00–7:15 Uhr | 0,24 | 1,10 | 0,24 | 0 | 0,86 |
| 12:30–12:45 Uhr | 4,57 | 0,99 | 0,99 | 3,58 | 0 |
| 19:00–19:15 Uhr | 0,90 | 1,73 | 0,90 | 0 | 0,83 |
| **Ganzer Tag** | **152,9** | **93,9** | **50,6** | **102,3** | **43,3** |

*Annahmen: Werte in kWh für die zwölf Haushalte zusammen. Dach mit 24 kWp nach Süden, 35° Neigung, in Namur, Erzeugung PVGIS v5.3 (SARAH-3) mit dem Wetter vom 13. Juni 2023; zwölf Haushalte mit je 3 500 kWh im Jahr nach einem synthetischen Profil, das kein Synergrid-Profil ist. Geteilt ist in jeder Viertelstunde der kleinere der beiden Werte, also das Maximum, das ein Schlüssel aufteilen kann; ein fester Schlüssel kann bei einem Mitglied einen Überschuss lassen, während einem anderen Strom fehlt.*

Morgens und abends wird alles geteilt, was das Dach einspeist; mittags verbrauchen die Haushalte nur ein Fünftel davon. Über den Tag deckt das Teilen 54 % des Verbrauchs, aber zwei Drittel der Erzeugung finden keinen Abnehmer. Über das ganze Jahr 2023 erzeugt dieselbe Gemeinschaft 24 812 kWh, verbraucht 42 000 und teilt 12 624: Die Hälfte der Erzeugung (50,9 %) findet einen Abnehmer, und das Teilen deckt 30,1 % des Verbrauchs.

### Die Zeile eines Mitglieds lesen

Hier haben die zwölf Haushalte dasselbe Profil. Um 19:00 Uhr entnimmt ein Mitglied 0,144 kWh; das Teilen deckt davon 0,075, und die restlichen 0,069 kWh bilden seinen Restverbrauch. In der Verbrauchsdatei von ORES sind das die Spalten „Prélèvement brut“ (Bruttoentnahme), „Prélèvement couvert par le partage“ (durch das Teilen gedeckte Entnahme) und „Allo Consommation“ (Restverbrauch): Pl = VPC + AL. Der Vertreter stellt die monatliche Summe der durch das Teilen gedeckten Entnahme in Rechnung; der Lieferant stellt den Restverbrauch in Rechnung, im Beispiel des ORES-Leitfadens auch die Netzkosten auf die gesamte Entnahme.

### Vier Prüfungen vor der Abrechnung

- **Die Zahl der Zeilen**: 96 pro Tag und EAN, mal die Zahl der Iterationen. Bei Zeitstempeln in Ortszeit hat der Tag der Umstellung auf die Sommerzeit 92 Viertelstunden, der Tag der Rückstellung 100.
- **Die Gleichung des Mitglieds**: Entnahme = geteilte verbrauchte Menge + Restverbrauch. Eine Abweichung verrät oft eine vergessene Iteration.
- **Die Gleichung der Gruppe**: Die Summe der geteilten verbrauchten Mengen übersteigt nie die geteilte Menge; die Differenz ist der Überschuss.
- **Die Lücken**: Ein fehlendes Mitglied oder eines, das überall null zeigt, deutet auf einen Zähler hin, der seine Viertelstunden nicht übermittelt. Klären Sie das vor der Abrechnung mit dem Netzbetreiber.

## Brüssel und Flandern

**In Flandern** berechnet Fluvius das Teilen jeden Monat anhand der Viertelstundenwerte; die Ergebnisse stehen in der Regel um den 25. des Folgemonats in Mijn Fluvius bereit, wo der Verwalter der Gemeinschaft eine CSV-Datei herunterlädt und jeder Teilnehmer nur seine eigenen Mengen sieht. Der digitale Zähler muss im „meetregime 3“ sein. Seit 2026 liest Fluvius die Viertelstundenwerte standardmäßig aus, übermittelt sie dem Lieferanten aber nur in bestimmten Fällen, etwa bei einem dynamischen Vertrag oder beim Teilen. Die Regulierungsbehörde ist die Vlaamse Nutsregulator (früher VREG).

**In Brüssel** verpflichtet die technische Regelung Sibelga, dem einzigen Ansprechpartner des Teilens jeden Monat die Entnahmen, die Einspeisungen, den geteilten Verbrauch jedes Teilnehmers und den Überschuss jedes Erzeugers zu schicken, je Viertelstunde oder als Monatssumme (Artikel 4.70); in der Praxis eine Excel-Datei in einem privaten Online-Ordner. Die Stromordonnanz macht die Fernerhebung von der Einwilligung des Nutzers abhängig (Artikel 26*octies* § 4), und der P1-Port ist dort standardmäßig aktiv. Die Regulierungsbehörde ist Brugel.

## Das Wichtigste in Kürze

1. **Eine Gemeinschaft misst nichts selbst.** Der Netzbetreiber erhebt die Daten, bestimmt die geteilten Mengen und übermittelt sie dem Vertreter und den Lieferanten.
2. **Der Rhythmus ist monatlich**: spätestens am zwölften Werktag des Folgemonats, je Viertelstunde und je EAN; bei ORES zwei CSV-Dateien per E-Mail.
3. **Dieser Datenfluss braucht keine Einwilligung: Er ist die Bedingung der Teilnahme.** Der Vertreter wird für die Daten verantwortlich, die er erhält; die Anlage 8 erlaubt die Übermittlung der Lastkurve an den Lieferanten.
4. **Alles andere verlangt eine vorherige, freie, spezifische, informierte und unmissverständliche Zustimmung**: Verlaufsdaten zur Simulation eines Schlüssels, P1-Gerät, Lastkurven, die anderen gezeigt werden.
5. **Jedes Mitglied sieht seine Zahlen, die Gruppe sieht die Gesamtwerte**, und der Vertrag jedes Teilnehmers muss das festhalten.
6. **Der P1-Port misst jede Sekunde, aber nur Ihren Zähler**, und wer seine Daten erhebt, wird dafür verantwortlich.
7. **Eine Lastkurve liest man in Kilowattstunden je Viertelstunde**: Multiplizieren Sie mit vier für die Leistung, und prüfen Sie, dass Entnahme = geteilte verbrauchte Menge + Restverbrauch.

> ### Testen Sie einen Schlüssel mit den Lastkurven Ihrer Mitglieder
>
> OptimCE ist eine Open-Source-Plattform in der Alpha-Phase für die Verwaltung einer Energiegemeinschaft. Die Funktion Aufteilungsschlüssel erzeugt und simuliert einen Schlüssel aus einer CSV-Datei im Viertelstundentakt, mit einer Spalte je Verbraucher und einer für die Erzeugung: den Lastkurven, die Ihre Mitglieder mit ihrer Zustimmung exportiert haben. Die Funktion arbeitet mit den Dateien, die Sie importieren, nicht in Echtzeit.
>
> **[Funktion Aufteilungsschlüssel ansehen →](/de/funktionen/aufteilungsschluessel/)**

## FAQ

### Welche Messdaten übermittelt der Netzbetreiber einer Energiegemeinschaft?

In der Wallonie schickt der Netzbetreiber dem Vertreter der Teilung für jedes Mitglied und jede Viertelstunde die Entnahme, die geteilte verbrauchte Menge und den Restverbrauch, also den Teil, den der Lieferant in Rechnung stellt. Dazu kommen die Einspeisung jedes Erzeugers, die gesamte geteilte Menge, der Überschuss und die verwendete Aufteilungsmethode.

Der von der CWaPE am 12. Oktober 2023 genehmigte Mustervertrag verpflichtet ihn, diese Daten jeden Monat bereitzustellen, spätestens am zwölften Werktag des Folgemonats; das ist eine Bemühenspflicht. Bei ORES sind es zwei CSV-Dateien per E-Mail, mit einer Zeile je Viertelstunde, EAN-Code und Iteration des Schlüssels.

### Muss ich einwilligen, damit meine Daten an die Gemeinschaft gehen?

Für den Datenfluss des Teilens selbst nicht. Das wallonische Dekret verpflichtet den Netzbetreiber, dem Vertreter die Messdaten jedes Teilnehmers zu übermitteln, und der Mustervertrag hält fest, dass jede Teilnahme die Erhebung und Nutzung der Lastkurven erfordert. Man kann nicht im Teilen bleiben und diesen Datenfluss ablehnen. Der Teilnehmer unterschreibt jedoch die Anlage 8, die unter anderem die Übermittlung seiner Lastkurve an seinen Lieferanten erlaubt.

Alles, was über diesen Rahmen hinausgeht, verlangt eine vorherige, freie, spezifische, informierte und unmissverständliche Zustimmung: die Verlaufsdaten zur Simulation eines Schlüssels, ein Gerät am P1-Port, einzelne Lastkurven, die anderen Mitgliedern gezeigt werden.

### Können die anderen Mitglieder meinen Verbrauch sehen?

Nicht standardmäßig. Der Netzbetreiber schickt die Daten jedes Mitglieds an den Vertreter, nicht an die anderen Mitglieder, und der Vertrag jedes Teilnehmers muss die Privatsphäre und die Datenübermittlung zwischen Teilnehmern regeln. Die Datenschutzbehörde erinnert daran, dass eine Viertelstundenkurve Rückschlüsse auf das Verhalten eines Haushalts erlaubt.

Eine vorsichtige Praxis besteht darin, jedem Mitglied seine eigenen Zahlen zu zeigen und der Gruppe nur die Gesamtwerte. Eine namentliche Rangliste oder eine einzelne Lastkurve wird nur mit ausdrücklicher Zustimmung der Person gezeigt. Hat die Gemeinschaft nur einen Erzeuger, ist seine Erzeugung zwangsläufig für alle als Summe sichtbar.

### Wie komme ich an die Daten meines Smart Meters?

Über das Portal Ihres Netzbetreibers, kostenlos. Der Erlass vom 1. Dezember 2022 schreibt vierundzwanzig Monate Verlauf vor, Details innerhalb des Tages auf ausdrücklichen Antrag und einen Export in eine Tabellenkalkulation. Bei ORES beantragen Sie die Viertelstundenansicht im Kundenbereich myORES; RESA bietet ein Viertelstundenprofil in MyRESA, die AIEG und die AIESH in MyConso.

Dieselben Daten wird eine Gemeinschaft von Ihnen verlangen, um vor dem Teilen einen Schlüssel zu simulieren: Sie können sie exportieren und ihr anvertrauen, mit einer schriftlichen Zustimmung für diesen Zweck.

### Kann der P1-Port für das Energieteilen dienen?

Nicht für die Berechnung. Der P1-Port liefert einen Datensatz pro Sekunde, zeigt aber nur Ihren eigenen Zähler: weder die Erzeugung des geteilten Dachs noch den Anteil, der Ihnen zugeteilt wird. Die Mengen des Teilens bestimmt der Netzbetreiber und übermittelt sie jeden Monat, und auf ihrer Grundlage wird die Rechnung erstellt.

In der Wallonie ist der Port standardmäßig deaktiviert und wird auf einfachen Antrag beim Netzbetreiber kostenlos aktiviert. Wer über diesen Port Daten erhebt, wird dafür verantwortlich: Eine Gemeinschaft, die P1-Geräte verteilt, muss die vorherige Zustimmung jedes Mitglieds einholen.

### Wie lange werden die Daten des Teilens aufbewahrt?

In der Wallonie bewahren die CWaPE und der Netzbetreiber die Daten des Teilens fünf Jahre nach dem Ende der Aktivität auf. Die Daten eines Teilnehmers, der das Teilen verlassen hat, werden fünf Jahre nach der Mitteilung seines Austritts gelöscht.

Für den Vertreter legt das Dekret keine Frist fest. Als Verantwortlicher für die Daten, die er erhält, muss er selbst eine festlegen und den Mitgliedern mitteilen, wie es die DSGVO verlangt. Der Zähler selbst speichert, aus der Ferne lesbar, die Lastkurven der letzten zehn Tage, die täglichen Zählerstände von vierzig Tagen und die monatlichen von dreizehn Monaten.

## Quellen

- [Wallex — Dekret vom 12. April 2001 über die Organisation des regionalen Elektrizitätsmarktes, koordinierte Fassung](https://wallex.wallonie.be/sites/wallex/contents/acts/19/19848.html) (auf Französisch) — Quelle dafür, dass die Erhebung der Messdaten dem Netzbetreiber vorbehalten ist (Artikel 11), für den standardmäßig deaktivierten Ausgangsport nahezu in Echtzeit (Artikel 35*bis* § 1, § 2 und § 4), das Standard-Messregime und die kostenlose Einsicht (Artikel 35*ter* § 2 und § 3), die Rolle des Netzbetreibers als Verantwortlicher, die Regel der vorherigen Zustimmung, die Handelsverbote und die Verantwortung des Dritten, der den Port ausliest (Artikel 35*septies* § 2 und § 3), den vorgeschriebenen Inhalt des Teilnehmervertrags (Artikel 35*duodecies* § 2), die Aufbewahrung von fünf Jahren (Artikel 35*quaterdecies* § 3) und die Übermittlungen des Netzbetreibers an den Vertreter, die Lieferanten und die CWaPE (Artikel 35*sexdecies* § 2 und § 3). Abgerufen am 22. November 2026.
- [CWaPE — Entscheidung CD-23j12-CWaPE-0818 zur Genehmigung der Musterverträge für das Teilen](https://cwape.be/sites/default/files/cwape-documents/2023.10.12-0818-D%C3%A9cision%20approbation%20conventions-types%20partage%20-%20avec%20annexes.pdf) (auf Französisch) — Entscheidung vom 12. Oktober 2023, einschließlich Anhänge. Quelle für die Definition der sieben Größen und ihrer Formeln (Artikel 6.2.1), die Frist des zwölften Werktags und die Bemühenspflicht (Artikel 6.2.2), die Erhebung der Lastkurven als Bedingung der Teilnahme (Artikel 6.1.3), den Weg der Beanstandungen (Artikel 6.1.4) und die Aufteilung der Verantwortlichkeiten für die Verarbeitung (Artikel 9.4). Abgerufen am 22. November 2026.
- [CWaPE — Leitfaden zum Formular für die Stromteilung in der Wallonie](https://www.cwape.be/documents/download/5610) (auf Französisch) — Fassung vom Juli 2025. Quelle für die Messbedingungen (aktivierte Kommunikationsfunktion, beim Lieferanten beantragtes Regime 3, Erlaubnis der Anlage 8, Punkt 9.1) und für die Datenschutzerklärung: Grundlage Artikel 6 Absatz 1 Buchstabe e DSGVO, gemeinsame Verantwortung der Netzbetreiber und der CWaPE, Aufbewahrung von fünf Jahren. Abgerufen am 22. November 2026.
- [CWaPE — Anlage 8, ehrenwörtliche Erklärung der an der Teilung beteiligten Personen](https://www.cwape.be/documents/download/5612) (auf Französisch) — Fassung vom 12. Oktober 2023. Quelle für den Auftrag an den Vertreter und die Erlaubnis, dem Lieferanten die Viertelstunden-Messdaten zu übermitteln, bis das Regime 3 aktiv ist. Abgerufen am 22. November 2026.
- [CWaPE — Evaluierungsbericht zu Energiegemeinschaften und Teilen (CD-25b20-CWaPE-0109)](https://www.cwape.be/sites/default/files/cwape-documents/2025.02.20-0109-Rapport%20%C3%A9valuation%20CE%20et%20partage.pdf) (auf Französisch) — Bericht vom 20. Februar 2025. Quelle für den aktuellen Rhythmus (abgelaufener Monat plus höchstens zwölf Werktage) und für den getrennten Kanal außerhalb der Marktprozesse, über den die geteilten Mengen zu den Lieferanten gelangen. Abgerufen am 22. November 2026.
- [CWaPE — Entscheidung CD-26h27-CWaPE-1284 zur Genehmigung der technischen Regelung für die Stromverteilung](https://www.cwape.be/sites/default/files/cwape-documents/CD-26h27-CWaPE-1284-D%C3%A9cision%20d%27approbation%20du%20RTDE%20%26%20annexes_site.pdf) (auf Französisch) — Entscheidung vom 27. August 2026. Quelle für die Artikel IX.6 (Übergang zum MIG, „dès que le MIG le permettra“, sobald der MIG es erlaubt), IX.7 (Viertelstundenkurve und Monatssumme, Programmierschnittstelle) und IX.17 (Korrekturen über zwölf Monate und ihre Aufteilung). Entscheidung [am 20. November 2026 im Belgischen Staatsblatt veröffentlicht](https://www.ejustice.just.fgov.be/cgi/article_body.pl?language=fr&caller=summary&pub_date=2026-11-20&numac=2026007520), laut der Seite [Règlements et contrats](https://www.cwape.be/node/161) (auf Französisch) ab dem 30. November 2026 in Kraft. Abgerufen am 22. und 24. November 2026.
- [CWaPE — Wer stellt geteilten Strom in Rechnung?](https://www.cwape.be/node/6059) (auf Französisch) — Frage aus den FAQ der Regulierungsbehörde, Quelle für den Grundsatz, dass die Rechnungen des Teilens auf Grundlage der vom Netzbetreiber erhaltenen Verbrauchsdaten erstellt werden. Abgerufen am 22. November 2026.
- [Wallex — Erlass der Wallonischen Regierung vom 1. Dezember 2022 über kommunizierende Zähler](https://wallex.wallonie.be/eli/arrete/2022/12/01/2022034594) (auf Französisch) — Artikel 4, Quelle für den Mindestinhalt des Portals: vierundzwanzig Monate, Details innerhalb des Tages auf ausdrücklichen Antrag, Export in eine Tabellenkalkulation. Abgerufen am 22. November 2026.
- [ORES — Leitfaden zur Abrechnung für den Vertreter einer Energieteilung](https://media.ores.be/ores-cms/vi2eqxam/ores_guide_explicatif_facturation_representant_partage_energie_fr.pdf) (auf Französisch) — Leitfaden vom Juli 2024. Quelle für die Beschreibung der beiden CSV-Dateien, die Spaltennamen, die Zeile je Iteration, die Summe der Iterationen je EAN und Zeitraum sowie das Beispiel, in dem der Lieferant die Netzkosten auf die gesamte Entnahme berechnet. Abgerufen am 22. November 2026.
- [ORES — Energieteilen in der Praxis](https://www.ores.be/particulier/en-pratique) (auf Französisch) — Quelle für den monatlichen Versand der beiden CSV-Dateien per E-Mail und für den Hinweis, dass die Daten der Viertelstundenansicht in myORES „ne remonteront pas“ (nicht weitergeleitet werden) an den Lieferanten, der sie selbst bei ORES anfordern muss. Abgerufen am 22. November 2026.
- [ORES — FAQ myORES](https://www.ores.be/faq/myores) (auf Französisch) — Quelle für die Übermittlung der Aktivierung der Viertelstundenansicht an den Lieferanten, die mögliche Zwischenrechnung bei manchen Lieferanten und ihre fehlende Wirkung auf Jahresabrechnung und Kompensation. Abgerufen am 22. November 2026.
- [ORES — Datenaustausch mit Energiedienstleistern (API)](https://media.ores.be/ores-cms/ahgjzcld/utilisation-des-api-tpda-ores.pdf) (auf Französisch) — Dokument vom September 2025. Quelle für den delegierten Zugang: Tages- und Viertelstundenmengen, Verlauf von höchstens drei Jahren, Einwilligung des Kunden in myORES. Abgerufen am 22. November 2026.
- [CWaPE — Anhang TNP-E0: nichtperiodische Tarife 2026, Strom, harmonisierte Tarife](https://www.cwape.be/sites/default/files/cwape-documents/ANNEXE%20TNP-E0%20-%20Tarifs%20non-p%C3%A9riodiques%202026%20-%20Electricit%C3%A9%20-%20Tarifs%20harmonis%C3%A9s%20et%20uniformis%C3%A9s.pdf) (auf Französisch) — Quelle für die kostenlose Aktivierung und Deaktivierung des P1-Ports im Jahr 2026. Abgerufen am 22. November 2026.
- [Fluvius — Digital Metering System eMUCS-P1, Version 2.1](https://partner.fluvius.be/sites/fluvius/files/2025-09/digital-metering-system-emucs-p1-v2-1.pdf) (auf Englisch) — belgische Spezifikation des P1-Ports, beruhend auf DSMR 5.0.2: jede Sekunde aktualisiertes Telegramm und Liste der veröffentlichten Werte. Abgerufen am 22. November 2026.
- [Ausschuss für den Schutz des Privatlebens — Stellungnahme Nr. 23/2018](https://www.autoriteprotectiondonnees.be/publications/avis-n-23-2018.pdf) (auf Französisch) — Stellungnahme vom 21. März 2018, veröffentlicht auf der Website der Datenschutzbehörde, die den Ausschuss abgelöst hat, zum Vorentwurf des Dekrets über intelligente Zähler, Quelle des Satzes über die „Einwilligung“ per Klausel in allgemeinen Geschäftsbedingungen. Abgerufen am 22. November 2026.
- [Datenschutzbehörde — Stellungnahme Nr. 132/2023](https://www.autoriteprotectiondonnees.be/publications/avis-n-132-2023.pdf) (auf Französisch) — Stellungnahme vom 8. September 2023, Quelle des Zitats über potenziell sensible Daten, die sich aus kommunizierenden Zählern ableiten lassen. Abgerufen am 22. November 2026.
- [Datenschutzbehörde — Stellungnahme Nr. 130/2025](https://www.autoriteprotectiondonnees.be/publications/avis-n0-130-2025.pdf) (auf Französisch) — Stellungnahme vom 3. Dezember 2025, Quelle der geltenden Brüsseler Regel: Artikel 26*octies* § 4 der Stromordonnanz macht die Fernerhebung von der Einwilligung des Nutzers abhängig. Abgerufen am 22. November 2026.
- [EUR-Lex — Verordnung (EU) 2016/679 (DSGVO)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — Artikel 5 Absatz 1 Buchstabe c (Datenminimierung), 6 Absatz 1 Buchstabe e (Aufgabe im öffentlichen Interesse), 7 Absatz 3 (Widerruf der Einwilligung) und 28 (Auftragsverarbeiter). Abgerufen am 22. November 2026.
- [EUR-Lex — Richtlinie (EU) 2019/944](https://eur-lex.europa.eu/eli/dir/2019/944/oj) — Artikel 20, Quelle für den Zugang des Kunden ohne zusätzliche Kosten zu seinen nicht validierten Daten nahezu in Echtzeit. Abgerufen am 22. November 2026.
- [EUR-Lex — Durchführungsverordnung (EU) 2023/1162](https://eur-lex.europa.eu/eli/reg_impl/2023/1162/oj) — Artikel 2, Definitionen der berechtigten Partei, zu der Erneuerbare-Energie-Gemeinschaften und Bürgerenergiegemeinschaften gehören, und der vom Kunden erteilten Erlaubnis. Abgerufen am 22. November 2026.
- [Fluvius — Häufige Fragen zum Energieteilen](https://www.fluvius.be/nl/veelgestelde-vragen/energiedelen-persoon-aan-persoonverkoop-energiegemeenschappen) (auf Niederländisch) — Quelle für die monatliche Berechnung, die Verfügbarkeit der Ergebnisse um den 25. des Folgemonats in Mijn Fluvius und die Anforderung des „meetregime 3“. Abgerufen am 22. November 2026.
- [Fluvius — Kwartierwaarden](https://www.fluvius.be/nl/factuur-en-tarieven/kwartierwaarden) (auf Niederländisch) — Quelle für das standardmäßige Auslesen der Viertelstundenwerte seit 2026 und ihre Übermittlung an den Lieferanten nur bei dynamischem Vertrag oder beim Teilen. Abgerufen am 22. November 2026.
- [Fluvius — Protocol energiedelen, persoon-aan-persoonverkoop en verkoop in gebouwen, Version 3.2](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf) (auf Niederländisch) — Quelle für die Optionen zum Herunterladen der CSV-Datei durch den Verwalter und dafür, dass jeder Teilnehmer nur seine eigenen Mengen sieht. Abgerufen am 22. November 2026.
- [Brugel — Technische Regelungen Strom und Gas, Fassung vom 1. Januar 2025](https://brugel.brussels/publication/document/notype/2024/fr/Reglements-techniques-2025.pdf) (auf Französisch) — Artikel 4.70, Quelle für die Daten, die Sibelga jeden Monat dem einzigen Ansprechpartner eines Teilens übermittelt. Abgerufen am 22. November 2026.
- [Sibelga — Abrechnungsmethode für das Energieteilen](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methode-de-facturation) und [Der P1-Port des Smart Meters](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents/le-port-p1-du-compteur-intelligent) (auf Französisch) — Quelle für die monatliche Excel-Datei in einem Online-Ordner, die Viertelstundenoption und den in Brüssel standardmäßig aktiven P1-Port. Abgerufen am 22. November 2026.
- [JRC — PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/fr/) — Werkzeug der Europäischen Kommission, aus dem die Erzeugungswerte des Referenzfalls stammen (Version 5.3, Datenbank SARAH-3, Wetter 2023). Das Verbrauchsprofil ist synthetisch und im Quellcode der Website dokumentiert; es ist kein Synergrid-Profil. Abgerufen am 22. November 2026.
