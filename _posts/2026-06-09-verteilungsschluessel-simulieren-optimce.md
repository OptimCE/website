---
layout: post
title: "Aufteilungsschlüssel simulieren: Szenarien testen"
date: 2026-06-09 10:00:00 +0200
author: "OptimCE-Team"
excerpt: "Neue OptimCE-Funktion: Simulieren Sie einen Aufteilungsschlüssel auf Ihren Daten und messen Sie Eigenverbrauch, Überschuss, Autarkie und Teilungsgrad."
description: "Simulieren Sie einen Schlüssel auf Ihren Daten und messen Sie Eigenverbrauch, Überschuss, Autarkie und Teilungsgrad vor der Freigabe."
tags: [allocation-key, app, news]
lang: de
ref: optimce-allocation-key-simulation
permalink: /de/aktuelles/2026/06/09/verteilungsschluessel-simulieren-optimce/
faq:
  - q: "Was bedeutet es, einen Aufteilungsschlüssel zu simulieren?"
    a: "Es bedeutet, reale Erzeugungs- und Verbrauchsdaten durch einen gewählten Aufteilungsschlüssel abzuspielen, ohne ihn produktiv anzuwenden, um seine Kennzahlen vorab zu messen: kollektiver Eigenverbrauch, Überschuss, Autarkiegrad und Teilungsgrad. Es ist ein 'Was-wäre-wenn'-Test, bevor Sie entscheiden."
  - q: "Was ist der Unterschied zwischen Simulieren und Generieren eines Aufteilungsschlüssels?"
    a: "Die automatische Generierung schlägt den besten Schlüssel aus Ihren Daten vor (Brute-Force über Standardschlüssel oder der LOGAAS-Algorithmus). Die Simulation testet einen Schlüssel, den Sie selbst gewählt haben, auf einem gegebenen Datensatz und zeigt dessen Kennzahlen. Beide ergänzen sich: Sie generieren, um einen guten Kandidaten zu finden, und Sie simulieren, um Szenarien zu verstehen und zu vergleichen."
  - q: "Was ist der Unterschied zwischen Eigenverbrauchsquote, Autarkiegrad und Teilungsgrad?"
    a: "Die Eigenverbrauchsquote wird auf der Erzeugungsseite gemessen: der Anteil der lokal erzeugten Energie, der von den Mitgliedern verbraucht wird. Der Autarkiegrad wird auf der Verbrauchsseite gemessen: der Anteil des Mitgliederverbrauchs, der durch lokale Erzeugung gedeckt wird. Der Teilungsgrad zeigt, wie viel der Einspeisung tatsächlich über den Schlüssel an die Mitglieder verteilt wurde."
  - q: "Was bedeuten die Ergebnisse 'pro Iteration'?"
    a: "Viele Schlüssel verteilen Energie in mehreren Runden (Iterationen): Eine erste Runde verteilt nach der Regel, dann wird die nicht verbrauchte Energie in der nächsten Runde umverteilt. Die Simulation zeigt das Ergebnis global, pro Zeitschritt und pro Iteration, sodass Sie sehen, wie das Teilen Runde für Runde voranschreitet."
  - q: "Welche Daten muss ich importieren, um eine Simulation zu starten?"
    a: "Eine CSV-Datei mit dem Verbrauch pro Zeitschritt (oft viertelstündlich) jedes Mitglieds und der Erzeugung jedes Erzeugers der Teilungsoperation. Jede Zeile entspricht einem Zeitschritt. Wenige Wochen Daten liefern bereits ein brauchbares Signal; ein volles Jahr erfasst die Saisonalität besser."
  - q: "Ändert die Simulation meinen produktiven Aufteilungsschlüssel?"
    a: "Nein. Die Simulation ist eine Berechnung 'außerhalb der Produktion': Sie berührt weder den vom Netzbetreiber angewandten Schlüssel noch Ihre realen Daten. Sie testen so viele Szenarien, wie Sie möchten, ohne jede Auswirkung auf die laufende Teilungsoperation."
---

Einen **Aufteilungsschlüssel** wählen heißt, Viertelstunde für Viertelstunde zu entscheiden, wer welchen Anteil der lokal erzeugten Energie erhält. Aber woher wissen Sie, *bevor* Sie ihn einführen, ob ein bestimmter Schlüssel den Eigenverbrauch Ihrer Gemeinschaft wirklich verbessert — oder Erzeugung ins Netz abfließen lässt? Die neue Funktion von OptimCE beantwortet genau diese Frage: einen **Aufteilungsschlüssel simulieren** auf Ihren eigenen Daten und die Leistungskennzahlen sofort ablesen.

Die Idee ist einfach: Sie importieren einen Datensatz, Sie wählen einen Schlüssel, und die Simulation spielt jeden Zeitschritt durch diesen Schlüssel, um Ihnen **Eigenverbrauch**, **Überschuss**, **Autarkiegrad** und **Teilungsgrad** zurückzugeben — global, pro Zeitschritt und pro Iteration. Sie testen ein Szenario, ohne es anzuwenden, risikofrei, und Sie entscheiden anhand von Zahlen statt aus dem Bauchgefühl.

Ist der Begriff Aufteilungsschlüssel neu für Sie, beginnen Sie mit unserem Referenzartikel [„Aufteilungsschlüssel in Belgien: 3 Regionen“](/de/aktuelles/2026/05/19/verteilungsschluessel-energiegemeinschaft-belgien/) — er legt das hier verwendete Vokabular dar.

## Warum einen Aufteilungsschlüssel simulieren?

Ein Aufteilungsschlüssel ist nicht neutral: Je nach Verbrauchs- und Erzeugungsprofilen der Gemeinschaft kann **derselbe Schlüssel in einem Projekt viel Wert schaffen und in einem anderen zerstören**. Ein fester egalitärer Schlüssel ist perfekt für zehn Haushalte mit ähnlichen Profilen, lässt aber Volumen ungenutzt, sobald ein Großverbraucher — eine Schule, ein KMU, ein öffentliches Gebäude — beitritt. Ein dynamischer Schlüssel hingegen gewinnt diese verlorene Erzeugung zurück, um den Preis eines von Monat zu Monat schwankenden Anteils.

Das Problem ist, dass **eine Entscheidung aus dem Bauchgefühl riskant ist**. Solarerzeugungskurven und Verbrauchsprofile kreuzen sich auf der 15-Minuten-Stufe auf nicht-triviale Weise; mit bloßem Auge lässt sich unmöglich vorhersagen, ob Schlüssel A über ein ganzes Jahr Schlüssel B schlägt. Und der Einsatz ist konkret: Jeder gewonnene Punkt Eigenverbrauch ist Überschuss, der nicht mehr zu niedrigem Preis eingespeist wird, also mehr Wert, der in der Gemeinschaft bleibt.

Simulieren bedeutet genau, **diese Entscheidung aus dem Bauchgefühl herauszuholen**. Sie messen die reale Wirkung eines Schlüssels auf die Kennzahlen, die zählen — Eigenverbrauch, Überschuss, Autarkie, Teilungsgrad — bevor Sie sich zu etwas verpflichten. Um zu verstehen, warum diese Kennzahlen für den Wert einer Gemeinschaft zentral sind, siehe unseren Artikel [„Eigenverbrauch von Energie in Belgien“](/de/aktuelles/2026/06/05/eigenverbrauch-energie-belgien/).

## Was die Simulation ermöglicht

Die Funktion ist in das **Modul „Aufteilungsschlüssel“** des Open-Source-Kerns von OptimCE eingebaut. Der Benutzerablauf umfasst nur wenige Schritte:

1. **Importieren Sie eine CSV** mit Verbrauchsdaten pro Zeitschritt (oft viertelstündlich) für jedes Mitglied und Erzeugungsdaten für jeden Erzeuger der Teilungsoperation. Jede Zeile der Datei entspricht einem Zeitschritt.
2. **Wählen Sie einen Aufteilungsschlüssel** zum Testen — einen Standardschlüssel Ihrer Region, einen bestehenden Schlüssel der Gemeinschaft oder ein Szenario, das Sie erkunden möchten.
3. **Starten Sie die Simulation.** OptimCE spielt jeden Zeitschritt durch den Schlüssel und seine verschiedenen Iterationen und aggregiert dann die Ergebnisse.
4. **Lesen Sie die zurückgegebenen Kennzahlen** auf drei Granularitätsebenen: **global** (über den gesamten Zeitraum), **pro Zeitschritt** (Viertelstunde für Viertelstunde) und **pro Iteration** (Runde für Runde der Verteilung).

Hier auf einen Blick, was Sie liefern und was Sie erhalten:

| Sie importieren | Sie erhalten |
|---|---|
| Verbrauch pro Zeitschritt, pro Mitglied | Simulierte kollektive Eigenverbrauchsquote |
| Erzeugung pro Zeitschritt, pro Erzeuger | Simulierter Überschuss (eingespeiste, nicht geteilte Energie) |
| Der zu testende Aufteilungsschlüssel | Autarkiegrad und Teilungsgrad |
| | Detail: global, pro Zeitschritt und pro Iteration |

Das Ergebnis ist keine theoretische Schätzung aus einem Lehrbuchbeispiel: Es wird **auf Ihren eigenen Daten** berechnet. Genau das macht die Simulation für die Entscheidung nützlich.

## Die Kennzahlen lesen

Vier Kennzahlen fassen die Leistung eines Schlüssels zusammen. Sie sind einfach, sobald man sie klar unterscheidet — und genau dort entsteht oft Verwirrung.

### Die Eigenverbrauchsquote

Die **kollektive Eigenverbrauchsquote** wird auf der **Erzeugungsseite** gemessen: der Anteil der lokal erzeugten Energie, den die Mitglieder tatsächlich verbrauchen, statt ihn ins Netz einzuspeisen. Je höher sie ist, desto besser wird die lokale Erzeugung innerhalb der Gemeinschaft verwertet.

### Der Überschuss

Der **Überschuss** ist die Kehrseite des Eigenverbrauchs: Es ist die von den Erzeugern eingespeiste Energie, die **niemand in der Gemeinschaft verbraucht hat**, und die daher ins öffentliche Netz zurückfließt, meist zu niedrigem Wert verkauft. Der Zusammenhang ist direkt: **Je mehr der lokale Verbrauch die Erzeugung aufnimmt, desto geringer der Überschuss**. Ein guter Schlüssel senkt den Überschuss, indem er Energie zu den Mitgliedern lenkt, die sie zum richtigen Zeitpunkt benötigen.

### Der Autarkiegrad

Der **Autarkiegrad** wird auf der **Verbrauchsseite** gemessen: der Anteil des Mitgliederverbrauchs, der durch geteilte lokale Erzeugung gedeckt wird, statt beim Lieferanten gekauft zu werden. Er ist das Spiegelbild des Eigenverbrauchs, betrachtet von der Rechnung der Mitglieder aus statt von den Panels.

### Der Teilungsgrad und die Lesart pro Iteration

Der **Teilungsgrad** zeigt, wie viel der verfügbaren Einspeisung tatsächlich **über den Schlüssel an die Mitglieder verteilt wurde**. Hier kommt die Lesart **pro Iteration** ins Spiel. Viele Schlüssel verteilen über mehrere Runden: Eine erste Runde verteilt die Energie nach der Regel, dann wird die Energie, die ein Mitglied nicht verbraucht hat, **in der nächsten Runde umverteilt** unter denen, die noch Bedarf haben (das ist das Prinzip der „mehrrundigen“, relativen oder optimalen Schlüssel). Die Simulation zeigt, wie der Teilungsgrad **bei jeder Iteration voranschreitet**, bis die teilbare Einspeisung erschöpft ist — Sie sehen genau, was die aufeinanderfolgenden Runden hinzufügen.

Um jede Verwirrung zu vermeiden, fasst diese Tabelle zusammen, wo jede Kennzahl angesiedelt ist:

| Kennzahl | Gemessen… | Beantwortet die Frage |
|---|---|---|
| Eigenverbrauchsquote | auf der **Erzeugungsseite** | Welcher Anteil der Erzeugung wird lokal verbraucht? |
| Überschuss | auf der **Erzeugungsseite** | Welcher Anteil der Erzeugung geht ins Netz? |
| Autarkiegrad | auf der **Verbrauchsseite** | Welcher Anteil des Verbrauchs wird lokal gedeckt? |
| Teilungsgrad | die Mechanik des **Schlüssels** | Welcher Anteil der Einspeisung wurde Runde für Runde verteilt? |

## Wann die Simulation nutzen?

Die Simulation ist in jeder Phase des Lebens einer Energiegemeinschaft nützlich.

- **Vor dem Start.** Sie vergleichen mehrere Kandidatenschlüssel auf historischen oder geschätzten Daten und wählen denjenigen, der die Projektziele am besten erfüllt — mit Sachkenntnis.
- **Während der Konzeption.** Sie wägen ausdrücklich zwischen **Fairness** (ein lesbarer, vorhersehbarer Schlüssel für die Mitglieder) und **Gesamtleistung** (ein Schlüssel, der den kollektiven Eigenverbrauch maximiert) ab — mit Zahlen als Beleg.
- **Im laufenden Betrieb.** Sie messen die Wirkung eines **neuen Datensatzes** oder einer **Profiländerung** (ein Mitglied installiert eine Wärmepumpe, ein anderes einen Ladepunkt) auf die Kennzahlen — ohne etwas im laufenden Betrieb zu zerstören.
- **Bei der Aktualisierung des Schlüssels.** Wenn ein **Mitglied beitritt oder austritt**, simulieren Sie den neu berechneten Schlüssel, bevor Sie ihn einreichen, um zu prüfen, ob er leistungsfähig bleibt. Unser Artikel über den [Aufteilungsschlüssel in Belgien](/de/aktuelles/2026/05/19/verteilungsschluessel-energiegemeinschaft-belgien/) beschreibt das Verfahren zur Änderung eines Schlüssels nach dem Start, und der [Leitfaden zur Gründung einer Gemeinschaft in Wallonien](/de/aktuelles/2026/05/11/energiegemeinschaft-gruenden-wallonien/) ordnet diesen Schritt in die Regulator-Akte ein.

## Der Wert für Gemeinschaften

Für einen Gemeinschaftsverwalter, einen Facilitator oder einen Projektträger ändert die Simulation die Art zu entscheiden:

- **Eine schnellere, rationalere Entscheidung.** Kein Jonglieren mehr zwischen Simulationstabellen und groben Schätzungen: Die Kennzahlen erscheinen direkt in dem Werkzeug, das die Gemeinschaft bereits verwaltet.
- **Pädagogik.** Indem die Mitglieder auf realen Daten sehen, *warum* ein Schlüssel besser funktioniert als ein anderer, verstehen und akzeptieren sie die Wahl leichter. Die Simulation macht aus einer abstrakten technischen Diskussion eine konkrete Demonstration.
- **Ein starkes Argument.** Vor einer Generalversammlung, einem Netzbetreiber oder einem Regulator wiegt es weit schwerer, einen Schlüssel mit Zahlen zu verteidigen — aus den eigenen Daten der Gemeinschaft — als eine grundsätzliche Empfehlung.

Es ist auch ein Hebel, um lokale Erzeugung zu verwerten und damit die [Stromrechnung der Mitglieder zu senken](/de/aktuelles/2026/06/03/energiegemeinschaft-stromrechnung-senken/): Jeder vermiedene Überschusspunkt ist Wert, der in der Gemeinschaft bleibt.

## Simulation und automatische Generierung: zwei komplementäre Werkzeuge

OptimCE bietet bereits ein **Modul zur automatischen Generierung**, das den besten Schlüssel aus den Daten *vorschlägt* — über eine **Brute-Force** über die regionalen Standardschlüssel und über **LOGAAS**, einen Algorithmus aus der Forschung von CeCoTePe für das Locomotrice-Projekt. Die Simulation hingegen *testet* einen Schlüssel, den **Sie** gewählt haben.

Es sind zwei komplementäre Anwendungen, keine konkurrierenden:

| | Simulation | Automatische Generierung |
|---|---|---|
| Gestellte Frage | „Was ergibt *dieser* Schlüssel auf diesen Daten?“ | „*Welcher* Schlüssel ist der beste für diese Daten?“ |
| Eingabe | Ein gewählter Schlüssel + eine CSV | Eine CSV |
| Ausgabe | Die KPIs des getesteten Schlüssels | Ein (oder mehrere) optimierte(r) Kandidatenschlüssel |
| Typische Nutzung | Szenarien vergleichen, verstehen, begründen | Einen guten Ausgangspunkt finden |

In der Praxis generieren Sie, um einen soliden Kandidaten zu finden, und simulieren dann, um sein Verhalten zu verstehen, Varianten zu vergleichen und ihn zu verteidigen. Für die Details der Algorithmen siehe [„Aufteilungsschlüssel automatisch generieren“](/de/aktuelles/2026/05/26/automatische-verteilungsschluessel-generierung/).

## Energiegemeinschaften in Belgien, kurz gefasst

Eine **Energiegemeinschaft** bringt Erzeuger und Verbraucher zusammen, die lokal erneuerbare Erzeugung teilen. Das Teilen ist administrativ: Intelligente Zähler werden in einer **15-Minuten-Stufe** ausgelesen, und der **Verteilnetzbetreiber (VNB)** wendet den gewählten Aufteilungsschlüssel an, um jedem Mitglied einen Anteil der eingespeisten Energie zuzuweisen. Belgien kennt mehrere Formen — EEG, BEG und, in Brüssel, LEG — unter Aufsicht der regionalen Regulatoren ([Brugel](https://energysharing.brugel.brussels) in Brüssel, mit [Sibelga](https://www.sibelga.be/en/connections-meters/renewable-energy/energy-sharing) als Netzbetreiber).

In dieser Landschaft ist der Aufteilungsschlüssel der zentrale Parameter für die Leistung einer Gemeinschaft — und die Simulation deckt einen realen Bedarf: **das Teilen von Energie zu strukturieren und zu verstehen**, bevor man sich dazu verpflichtet. Für den vollständigen Überblick über die Rechtsformen siehe [„Energiegemeinschaften in Belgien: CER, CEC, CEL“](/de/aktuelles/2026/05/11/energiegemeinschaften-belgien/).

## Fazit

Die Simulation von Aufteilungsschlüsseln bringt eine einfache, aber entscheidende Sache: **die Möglichkeit, vor der Bereitstellung zu testen**. Statt einen Schlüssel aus dem Bauchgefühl zu wählen und seine Wirkungen nachträglich zu entdecken, messen Sie Eigenverbrauch, Überschuss, Autarkie und Teilungsgrad vorab auf Ihren eigenen Daten — global und Runde für Runde. Das bedeutet weniger Risiko, mehr Pädagogik und mit Zahlen untermauerte Governance-Entscheidungen.

> ### Simulieren Sie Ihren Aufteilungsschlüssel mit OptimCE
>
> Open-Source-Plattform für belgische Energiegemeinschaften: Simulieren Sie einen Schlüssel auf Ihren Daten, vergleichen Sie Szenarien, generieren Sie einen optimalen Schlüssel, führen Sie eine Historie der Teilungsoperationen und bereiten Sie die Berichterstattung an den Regulator vor — alles in einer einzigen Anwendung.
>
> **[Auf app.optimce.be starten →](https://app.optimce.be)**

## FAQ

### Was bedeutet es, einen Aufteilungsschlüssel zu simulieren?

Es bedeutet, reale Erzeugungs- und Verbrauchsdaten durch einen gewählten Aufteilungsschlüssel abzuspielen, **ohne ihn produktiv anzuwenden**, um seine Kennzahlen vorab zu messen: kollektiver Eigenverbrauch, Überschuss, Autarkiegrad und Teilungsgrad. Es ist ein „Was-wäre-wenn“-Test, bevor Sie entscheiden.

### Was ist der Unterschied zwischen Simulieren und Generieren eines Aufteilungsschlüssels?

Die **automatische Generierung** schlägt den besten Schlüssel aus Ihren Daten vor (Brute-Force über Standardschlüssel oder der LOGAAS-Algorithmus). Die **Simulation** testet einen Schlüssel, den Sie selbst gewählt haben, auf einem gegebenen Datensatz und zeigt dessen Kennzahlen. Beide ergänzen sich: Sie generieren, um einen guten Kandidaten zu finden, und Sie simulieren, um Szenarien zu verstehen und zu vergleichen.

### Was ist der Unterschied zwischen Eigenverbrauchsquote, Autarkiegrad und Teilungsgrad?

Die **Eigenverbrauchsquote** wird auf der Erzeugungsseite gemessen: der Anteil der lokal erzeugten Energie, der von den Mitgliedern verbraucht wird. Der **Autarkiegrad** wird auf der Verbrauchsseite gemessen: der Anteil des Mitgliederverbrauchs, der durch lokale Erzeugung gedeckt wird. Der **Teilungsgrad** zeigt, wie viel der Einspeisung tatsächlich über den Schlüssel an die Mitglieder verteilt wurde.

### Was bedeuten die Ergebnisse „pro Iteration“?

Viele Schlüssel verteilen Energie in mehreren Runden (Iterationen): Eine erste Runde verteilt nach der Regel, dann wird die nicht verbrauchte Energie in der nächsten Runde umverteilt. Die Simulation zeigt das Ergebnis **global**, **pro Zeitschritt** und **pro Iteration**, sodass Sie sehen, wie das Teilen Runde für Runde voranschreitet.

### Welche Daten muss ich importieren, um eine Simulation zu starten?

Eine **CSV**-Datei mit dem Verbrauch pro Zeitschritt (oft viertelstündlich) jedes Mitglieds und der Erzeugung jedes Erzeugers der Teilungsoperation. Jede Zeile entspricht einem Zeitschritt. Wenige Wochen Daten liefern bereits ein brauchbares Signal; ein volles Jahr erfasst die Saisonalität besser.

### Ändert die Simulation meinen produktiven Aufteilungsschlüssel?

Nein. Die Simulation ist eine Berechnung „außerhalb der Produktion“: Sie berührt weder den vom Netzbetreiber angewandten Schlüssel noch Ihre realen Daten. Sie testen so viele Szenarien, wie Sie möchten, ohne jede Auswirkung auf die laufende Teilungsoperation.

## Quellen

- [Brugel — Energy Sharing](https://energysharing.brugel.brussels) — offizielles Portal des Brüsseler Regulators zum Energieteilen und zum Rahmen der Energiegemeinschaften.
- [Brugel — Energiegemeinschaften](https://energysharing.brugel.brussels/blog/energy-sharing-18/communautes-d-energie-406) — Genehmigung, Gültigkeitsdauer und Regulierungsrahmen in Brüssel.
- [Sibelga — Sharing energy in a community](https://www.sibelga.be/en/connections-meters/renewable-energy/energy-sharing/sharing-energy-in-an-energy-communitiy) — Bedingungen, Akteure und Prinzipien des Teilens in Brüssel.
- [IÖW — Eigenverbrauch und Eigenversorgung in Energy-Sharing-Gemeinschaften](https://www.ioew.de/en/publication/self_consumption_and_self_sufficiency_in_energy_sharing_communities_in_germany) — methodische Referenz zu den Kennzahlen Eigenverbrauch und Autarkie.
- [KPMG — Energy sharing in Belgium: overview and policy recommendations](https://kpmg.com/be/en/insights/industries/energy-natural-resources-insights/energy-sharing-in-belgium-overview-and-policy-recom.html) — Überblick über das Energieteilen in Belgien.
- [Pricing and sharing rules for energy communities](https://econpapers.repec.org/article/eeejuipol/v_3a96_3ay_3a2025_3ai_3ac_3as0957178725001109.htm) — Forschung zu Teilungsregeln und internen Preisen, die den Nutzen einer Simulation belegt.
