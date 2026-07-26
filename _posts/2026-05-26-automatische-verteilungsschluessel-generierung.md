---
layout: post
title: "Aufteilungsschlüssel automatisch generieren"
date: 2026-05-26 00:00:00 +0200
author: "OptimCE-Team"
excerpt: "Das automatische Generierungsmodul von OptimCE ist live. Es schlägt optimierte Aufteilungsschlüssel auf Basis der realen Erzeugungs- und Verbrauchsdaten einer Gemeinschaft vor — mit zwei Algorithmen: Brute-Force auf Standardschlüsseln und LOGAAS, einem Forschungsergebnis von CeCoTePe aus dem Locomotrice-Projekt."
description: "Zwei Algorithmen — Brute-Force über alle Standardschlüssel und LOGAAS — schlagen einen optimierten Schlüssel aus Ihren realen Daten vor."
tags: [allocation-key, app, guide]
lang: de
ref: optimce-allocation-key-generator
permalink: /de/aktuelles/2026/05/26/automatische-verteilungsschluessel-generierung/
---

Den **Aufteilungsschlüssel** zu wählen, der das Beste aus der lokalen Erzeugung einer Gemeinschaft herausholt, ist schwieriger, als es scheint. Das Vokabular gibt der Regulator vor, die Standardschlüssel sind in einem Dokument von CWaPE oder Fluvius aufgelistet — und doch hängt die *richtige* Wahl von etwas ab, das keiner dieser Texte verraten kann: den realen Viertelstundenprofilen Ihrer Mitglieder. Ein Wohnviertel mit einer einzigen Schule verhält sich völlig anders als ein Gewerbepark mit Grundlast, und derselbe Schlüssel kann in einer Gemeinschaft 70 % der verfügbaren Erzeugung wiedergewinnen und in einer anderen kaum 50 %.

Das **automatische Generierungsmodul für Aufteilungsschlüssel** von OptimCE ist nun verfügbar, um diese Entscheidung aus dem Bauchgefühl-Bereich herauszuholen. Geben Sie ihm eine CSV mit den realen Erzeugungs- und Verbrauchsdaten der Gemeinschaft, und es liefert einen Kandidatenschlüssel mit der erwarteten kollektiven Eigenverbrauchsrate — berechnet auf Ihren eigenen Daten, nicht auf einem Lehrbuchbeispiel. Heute werden zwei **unabhängige** Algorithmen ausgeliefert, die beide dieselbe CSV verarbeiten: ein **Brute-Force-Scan** über die regional zugelassenen Standardschlüssel und **LOGAAS**, ein hybrider Ansatz aus linearer Optimierung und genetischem Algorithmus, entwickelt von [**CeCoTePe**](https://cecotepe.be/) für das **Locomotrice**-Projekt. Weitere Algorithmen können später ergänzt werden.

Wenn Sie sich noch im regulatorischen Umfeld orientieren — was CWaPE, BRUGEL und VREG als gültigen Schlüssel akzeptieren — beginnen Sie mit unserem Referenzartikel [„Aufteilungsschlüssel in Belgien: 3 Regionen“](/de/aktuelles/2026/05/19/verteilungsschluessel-energiegemeinschaft-belgien/).

<img src="/assets/images/diagrams/allocation-key-flow-de.svg"
     alt="Fünfstufiges Schema: Viertelstundendaten, Generierung oder Simulation, Kandidatenschlüssel, Freigabe durch die Mitglieder, Übermittlung an den Netzbetreiber."
     width="800" height="330" loading="lazy" decoding="async"
     style="width:100%;height:auto">

## Warum ein Aufteilungsschlüssel datengetrieben sein sollte

Die belgischen Rahmenwerke sind sich in einem Punkt einig: Der Aufteilungsschlüssel wird **viertelstündlich** auf die realen Messwerte intelligenter Zähler angewendet. Seine Leistung — die **kollektive Eigenverbrauchsrate**, der **Anteil der eingespeisten Energie, der tatsächlich von Mitgliedern verbraucht wird** — hängt vollständig davon ab, wie das Profil jedes Mitglieds mit der Erzeugungskurve übereinstimmt.

Mehrere Muster erklären, warum die manuelle Wahl häufiger unterperformt, als man denkt:

- **Die Profilvielfalt wächst schnell.** Eine Gemeinschaft, die mit fünf identischen Haushalten startet, lässt sich mit einem egalitären festen Schlüssel gut bedienen. Kommt ein gewerblicher Verbraucher dazu (Schule, KMU, öffentliches Gebäude), lässt die egalitäre Aufteilung sofort Energie liegen — gerade während der Bürozeiten, in denen der große Verbraucher sie hätte aufnehmen können.
- **Die Erzeugung verändert sich.** Eine Dacherweiterung, ein Wechselrichter-Upgrade, eine zusätzliche Kraft-Wärme-Kopplung — jede Änderung verschiebt die Kurve. Der letztes Jahr optimale Schlüssel kann heute suboptimal sein.
- **Standardschlüssel sind nicht austauschbar.** Die drei wallonischen Familien (egalitärer fester Schlüssel, spezifischer fester Schlüssel, dynamischer Schlüssel) decken viele Fälle ab — aber welcher der drei für eine konkrete Gemeinschaft *am besten* ist, ist ohne Simulation nicht offensichtlich. Dasselbe gilt für die Brüsseler Methoden (fest, prorata, hybrid) und die flämischen *verdeelsleutels* (vaste, relatieve, optimale).

Die manuelle Auswahl unterschätzt deshalb häufig die verfügbare Erzeugung. Sinn eines automatischen Generierungsmoduls ist nicht, das menschliche Urteil bei Governance-Fragen zu ersetzen — sondern die **Simulationskosten** aus der Entscheidung herauszunehmen. Sobald ein Kandidat vorgeschlagen ist, kann die Gemeinschaft weiterhin abstimmen, anpassen und verfeinern.

## Was das OptimCE-Modul leistet

Das Modul ist Teil des bestehenden **Aufteilungsschlüssel-Moduls** im Open-Source-Kern von OptimCE. Der Ablauf ist einfach:

1. **Eingaben** — 15-Minuten-Verbrauchsdaten je Mitglied, 15-Minuten-Erzeugungsdaten je Erzeuger, Teilnehmerliste der Sharing-Operation und Region (Wallonie / Brüssel / Flandern), damit der Algorithmus die jeweils zulässigen Standardfamilien respektiert.
2. **Algorithmus auswählen** — Brute-Force oder LOGAAS.
3. **Ausführen** — das Modul simuliert den gewählten Algorithmus auf den realen Daten und liefert einen **Kandidatenschlüssel** mit der **erwarteten kollektiven Eigenverbrauchsrate**, dem **Anteil geteilter Energie pro Mitglied** und der **Verteilung der Restinjektion**.
4. **Prüfen** — der Gemeinschaftsmanager kann Kandidaten vergleichen, Prozentsätze anpassen und validieren.
5. **Anwenden** — der validierte Schlüssel fließt als neuer Nachtrag in das Aufteilungsschlüssel-Modul, mit vollständiger Historie und Mitgliederakzeptanz-Status.

Das Modul übermittelt einen neuen Schlüssel **nicht** eigenständig an den Verteilnetzbetreiber. Es erzeugt einen Vorschlag; der bestehende Workflow — Nachtrag, Unterschriften, Übermittlung — bleibt bestehen, einschließlich der Regulatorgenehmigung für Nicht-Standardschlüssel in der Wallonie.

## Algorithmus 1 — Brute-Force auf Standardschlüsseln

Der erste Algorithmus ist bewusst einfach gehalten, und genau das ist seine Stärke.

Er baut eine **Kandidatenmenge** aus allen in der jeweiligen Region zulässigen Standardschlüsseln auf:

- In der **Wallonie**: egalitärer fester Schlüssel, spezifischer fester Schlüssel (gewichtet nach Mitgliedsbeiträgen), verbrauchsbasierter dynamischer Schlüssel.
- In **Brüssel**: feste Methode (Single-Round und Multi-Round), Prorata-Methode, hybride Methode.
- In **Flandern**: *vaste verdeelsleutel*, *relatieve verdeelsleutel*, *optimale verdeelsleutel*.

Für jeden Kandidaten **spielt der Algorithmus die realen Viertelstundendaten** der Gemeinschaft durch die entsprechende Verteilungsregel und berechnet die resultierende kollektive Eigenverbrauchsrate, den Anteil, den jedes Mitglied erhalten hätte, und die Restinjektion. Der leistungsfähigste Kandidat — standardmäßig der mit der höchsten kollektiven Eigenverbrauchsrate — gewinnt, und das Modul gibt die Folgeplätze aus, damit die Gemeinschaft bei Bedarf einige Prozentpunkte Performance gegen einfachere Governance eintauschen kann.

Der Brute-Force-Ansatz hat zwei große Vorteile:

- **Regulator-konform per Konstruktion.** Die Ausgabe ist immer einer der Standardschlüssel und durchläuft daher den üblichen Akzeptanzweg beim Verteilnetzbetreiber — keine zusätzliche CWaPE-Genehmigung in der Wallonie nötig.
- **Erklärbar.** Das Ergebnis ist eine bekannte Schlüsselfamilie mit bekannten Eigenschaften. Sie können es vor einer Generalversammlung verteidigen, ohne Optimierungstheorie bemühen zu müssen.

Seine Grenze ist der Katalog selbst. Sind die Profile einer Gemeinschaft atypisch — stark asymmetrisch, stark saisonal, mit einem dominanten Verbraucher — kann der beste Standardschlüssel weiterhin spürbares Performancepotenzial liegen lassen. Hier setzt der zweite Algorithmus an.

## Algorithmus 2 — LOGAAS

**LOGAAS** steht für *Linear Optimization with Genetic Algorithm with Atypical Speciation*. Er ist das Ergebnis von Forschungsarbeiten von [CeCoTePe](https://cecotepe.be/) für das Locomotrice-Projekt und ist formal beschrieben im Preprint *Paque, E. & Hiard, S. (2025), „LOGAAS: A hybrid algorithmic approach to ex-post electricity allocation for energy communities“*.

Während Brute-Force durch den Standardkatalog begrenzt ist, durchsucht LOGAAS einen **breiteren Raum von Kandidatenschlüsseln** — einschließlich Nicht-Standard-Kombinationen — indem er **lineare Optimierung** (findet die beste Ex-Post-Allokation für eine gegebene Iteration) mit einem **genetischen Algorithmus** mit **atypischer Speziation** (findet die beste Kombination von Prozentsätzen über die bis zu drei zulässigen Iterationen und erhält dabei die Populationsdiversität) kombiniert. Praktisch heißt das: Er kann zusätzliche Performance gewinnen, wenn die Standardfamilien nicht sauber auf die Profile passen — sehr heterogene Mitgliedergruppen, saisonale Industrieverbraucher zusammen mit Haushalten oder große Überschusserzeuger, die sonst den Großteil ihrer Erzeugung ins öffentliche Netz zurückspeisen würden.

LOGAAS gibt einen **Nicht-Standard-Kandidatenschlüssel** aus. In der Wallonie bedeutet das, dass die Gemeinschaft den **CWaPE-Genehmigungsweg** durchlaufen muss, bevor der Verteilnetzbetreiber den Schlüssel anwenden kann — siehe den [Artikel über Aufteilungsschlüssel in Belgien](/de/aktuelles/2026/05/19/verteilungsschluessel-energiegemeinschaft-belgien/) für das Verfahren. In Brüssel und Flandern ist der Spielraum für Nicht-Standardschlüssel enger; die LOGAAS-Ausgabe dient dort meist als **Performance-Referenz** — wie sähe das bestmögliche Ergebnis aus? — gegen die der gewählte Standardschlüssel verglichen wird.

Verwenden Sie LOGAAS, wenn das Brute-Force-Ergebnis nah dran, aber nicht ausreichend ist, wenn die Projektwirtschaftlichkeit von den letzten Prozentpunkten der kollektiven Eigenverbrauchsrate abhängt oder wenn Sie eine quantifizierte obere Schranke für eine Investitionsentscheidung benötigen.

## Vergleich auf einen Blick

| Kriterium | Manuelle Wahl | Brute-Force | LOGAAS |
|---|---|---|---|
| Erforderliche Daten | Mitgliederliste, Regionalrahmen | Mitgliederliste + 15-Min-Profile | Mitgliederliste + 15-Min-Profile |
| Suchraum | Ein vorausgewählter Schlüssel | Alle regionalen Standardschlüssel | Standard- + Nicht-Standardkombinationen |
| Laufzeit | Sofort (keine Berechnung) | Sekunden | Minuten |
| Regulator-konform ab Werk | Ja (falls Standard) | Ja — immer im Standardkatalog | Wallonie: CWaPE-Genehmigung nötig. Brüssel / Flandern: meist als Referenz. |
| Erklärbarkeit | Hoch | Hoch — benannte Schlüsselfamilie | Niedriger — numerische Ausgabe |
| Geeignet für | Homogene Gemeinschaft, governance-orientierte Projekte | Die meisten Projekte — neue Standardwahl | Heterogene Profile, performancekritische Projekte |

Die beiden Algorithmen sind **zwei unabhängige Wege**, einen Schlüssel aus derselben CSV zu erzeugen — keine Pipeline-Schritte. Brute-Force ist die sichere Standardwahl für die meisten Projekte; LOGAAS ist die Option, wenn der Standardkatalog Performance liegen lässt und ein Nicht-Standardschlüssel infrage kommt.

## So nutzen Sie das Modul

Das Modul ist heute in der OptimCE-Anwendung verfügbar:

1. Öffnen Sie das **Aufteilungsschlüssel-Modul** für die Sharing-Operation, die Sie optimieren möchten.
2. Klicken Sie auf **Schlüssel generieren**. Laden Sie eine CSV mit den Viertelstunden-Verbrauchsdaten (pro Mitglied) und -Erzeugungsdaten (pro Erzeuger) hoch.
3. Wählen Sie einen Algorithmus — Brute-Force oder LOGAAS. Beide laufen unabhängig auf derselben CSV; Sie können die Ergebnisse nebeneinanderlegen.
4. Starten Sie. Prüfen Sie den Kandidatenschlüssel, seine erwartete kollektive Eigenverbrauchsrate und die Tabelle der Anteile je Mitglied.
5. Validieren Sie den Kandidaten, um den Nachtrags-Workflow zu starten: Mitgliederunterschriften, Übermittlung an den Verteilnetzbetreiber durch den Vertreter, Wirksamkeit zum vereinbarten Datum.

Die gesamte Schleife — vom Daten-Upload bis zum Nachtrag — lebt in OptimCE. Kein Wechseln mehr zwischen Simulationstabellen, Governance und Reporting.

## Was kommt als Nächstes?

Das Modul ist um eine plugbare Algorithmusschnittstelle herum gebaut, sodass neue Ansätze hinzugefügt werden können, ohne den Kern anzufassen. Plausible nächste Schritte: **Mehrzieloptimierung** (kollektive Eigenverbrauchsrate vs. Fairness je Mitglied), **fairnessbeschränkte Varianten** (Begrenzung der Lücke zwischen am besten und am schlechtesten bedienten Mitgliedern) und **szenarienbasierte Simulation** (Test eines Schlüssels gegen erwartete Mitgliederfluktuation oder Erzeugungswachstum). Jede Erweiterung wird bei Auslieferung angekündigt.

> ### Erzeugen Sie Ihren Aufteilungsschlüssel mit OptimCE
>
> Eine Open-Source-Plattform für belgische Energiegemeinschaften: datengetriebene Schlüsselgenerierung, Historie der Sharing-Operationen, Tracking der Mitgliederakzeptanz und Vorbereitung des Regulator-Reportings — alles in einer Anwendung.
>
> **[Auf app.optimce.be starten →](https://app.optimce.be)**

## FAQ — Automatische Generierung von Aufteilungsschlüsseln

### Welche Daten benötigt das Modul?

**Verbrauchsdaten** je Mitglied im Viertelstundentakt, **Erzeugungsdaten** je Erzeuger im Viertelstundentakt, die Teilnehmerliste und die Region. Wenige Wochen Daten reichen für ein brauchbares Signal; ein ganzes Jahr bildet saisonale Effekte zuverlässiger ab.

### Welchen Algorithmus sollte ich wählen?

Standardmäßig **Brute-Force**: schnell, vollständig erklärbar, bleibt im Standardkatalog, der vom Verteilnetzbetreiber automatisch akzeptiert wird. Wählen Sie **LOGAAS**, wenn Sie gezielt über den Standardkatalog hinausschauen wollen — heterogene Profile, knappe Projektwirtschaftlichkeit oder Interesse daran, zu wissen, wie viel Performance der Standardkatalog liegen lässt. Beide laufen unabhängig auf derselben CSV; nichts hindert Sie daran, beide auszuführen und zu vergleichen.

### Wird der generierte Schlüssel regulator-konform sein?

Die Brute-Force-Ausgabe ist immer einer der regionalen Standardschlüssel — direkt vom Verteilnetzbetreiber akzeptiert, ohne zusätzliche Genehmigung. Die LOGAAS-Ausgabe ist ein Nicht-Standardschlüssel; in der Wallonie muss er den **CWaPE-Genehmigungsweg** durchlaufen, bevor der Verteilnetzbetreiber ihn anwendet. In Brüssel und Flandern sind Nicht-Standardschlüssel nicht der übliche Weg; dort wird die LOGAAS-Ausgabe meist als Performance-Referenz genutzt.

### Kann ich den Vorschlag vor der Anwendung anpassen?

Ja. Das Modul liefert einen **Kandidaten** — keine bindende Entscheidung. Sie können Prozentsätze anpassen, die Schlüsselfamilie wechseln oder die Algorithmuswahl vollständig überschreiben, bevor Sie den Schlüssel in den Nachtragsworkflow überführen.

### Ersetzt das Modul Expertenurteil?

Nein. Das Modul quantifiziert Trade-offs; es entscheidet nicht, ob Ihre Gemeinschaft Fairness vor Performance, Vorhersehbarkeit vor Optimierung oder Einfachheit vor dem letzten Prozentpunkt Eigenverbrauch stellt. Das sind Governance-Fragen. Das Modul verkürzt die technische Schleife, damit sich die Versammlung auf die Governance-Frage statt auf die Berechnung konzentrieren kann.

### Wie oft sollte ich den Algorithmus erneut laufen lassen?

Ein guter Rhythmus ist **jährlich**, idealerweise vor der ordentlichen Generalversammlung, die die Nachträge der Sharing-Operation genehmigt. Früher erneut starten, wenn die Gemeinschaft wächst, ein Erzeuger hinzukommt oder ausscheidet oder ein Mitglied sein Verbrauchsprofil deutlich ändert (z. B. Einbau einer Wärmepumpe, Verkauf eines Industriestandorts).

## Wesentliche Erkenntnisse

Das automatische Generierungsmodul verwandelt die Wahl des Aufteilungsschlüssels von einer Lehrbuchaufgabe in eine datengetriebene Entscheidung. **Brute-Force** findet den besten Standardschlüssel für die realen Profile der Gemeinschaft — schnell, erklärbar, regulator-konform. **LOGAAS** geht darüber hinaus, wenn die Projektwirtschaftlichkeit jeden Prozentpunkt braucht. Zusammen geben sie Gemeinschaftsmanagern ein Werkzeug, ihre Schlüsselwahl vor der Generalversammlung, dem Verteilnetzbetreiber und dem Regulator zu verteidigen — mit Zahlen aus den eigenen Daten der Gemeinschaft.

Um weiter zu gehen, lesen Sie unsere begleitenden Leitfäden:

> **[Aufteilungsschlüssel in Belgien: 3 Regionen](/de/aktuelles/2026/05/19/verteilungsschluessel-energiegemeinschaft-belgien/)**
>
> Der regulatorische Primer — was CWaPE, BRUGEL und VREG akzeptieren, die drei regionalen Vokabulare und wie man eine Schlüsselfamilie wählt, bevor OptimCE darin optimiert.

> **[Wie man eine Energiegemeinschaft in Wallonien gründet: Schritt-für-Schritt-Leitfaden](/de/aktuelles/2026/05/11/energiegemeinschaft-gruenden-wallonien/)**
>
> Das Projekt rahmen, zwischen CER und CEC wählen, die CWaPE benachrichtigen und das Sharing starten — und wo der Aufteilungsschlüssel in die Akte passt.

> **[Wie man einer Energiegemeinschaft in Wallonien beitritt: praktischer Leitfaden](/de/aktuelles/2026/05/11/energiegemeinschaft-beitreten-wallonien/)**
>
> Wo Sie eine offene Operation finden, Beitrittsschritte und Prüfpunkte vor Unterzeichnung der Sharing-Vereinbarung.

## Quellen

- Paque, E. & Hiard, S. (2025). *LOGAAS: A hybrid algorithmic approach to ex-post electricity allocation for energy communities*. CeCoTePe-Preprint — formale Beschreibung des Algorithmus, der Zielfunktion und der Simulationsergebnisse auf synthetischen Energiegemeinschaftsdaten.
- [CeCoTePe](https://cecotepe.be/) — Forschungszentrum hinter dem LOGAAS-Algorithmus, Partner im Locomotrice-Projekt.
- [CWaPE — Liste der Standard-Aufteilungsschlüssel](https://www.cwape.be/publications/document/5382) — Vorschlag CD-23d27-CWaPE-0928 vom 27. April 2023, kanonische Liste der wallonischen Standardschlüssel.
- [Sibelga — Verteilungsmethoden für das Energy-Sharing](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methodes-de-repartition) — feste, prorata und hybride Methoden in Brüssel.
- [Fluvius — Protocol energiedelen, persoon-aan-persoonverkoop](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf) — flämisches technisches Protokoll (v3.x, Juli 2024).
