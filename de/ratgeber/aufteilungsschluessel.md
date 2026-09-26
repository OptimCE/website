---
layout: pillar
title: "Aufteilungsschlüssel: verstehen, wählen, testen"
subtitle: "Was jede Region zulässt, wie Sie eine Schlüsselfamilie wählen und wie Sie sie auf Ihren eigenen Daten testen."
description: "Aufteilungsschlüssel belgischer Energiegemeinschaften: was CWaPE, BRUGEL und VREG zulassen, Wahl der Schlüsselfamilie, Generierung und Simulation."
lang: de
ref: pillar-cle-de-repartition
pillar: cle-de-repartition
permalink: /de/ratgeber/aufteilungsschluessel/
breadcrumb_parent: guides
last_modified_at: 2026-09-26
sections:
  - title: "Den Schlüssel verstehen: was jede Region zulässt"
    refs: [allocation-key-belgium]
  - title: "Ihren Schlüssel mit OptimCE generieren und simulieren"
    refs: [optimce-allocation-key-generator, optimce-allocation-key-simulation]
---
In einer Teilungsoperation ist der **Aufteilungsschlüssel** die in Prozenten ausgedrückte Berechnungsregel, die jedem verbrauchenden Mitglied einen Anteil der von den Erzeugern eingespeisten Energie zuweist. Physisch ist daran nichts: Der Verteilnetzbetreiber (VNB) wendet ihn Viertelstunde für Viertelstunde auf die Messwerte der Smart Meter an. Pro Teilungsoperation gilt nur ein Schlüssel, und er entscheidet nur über die kWh: Was sie in Euro wert sind, regelt der [interne Verrechnungspreis]({{ "internal-price-shared-energy" | ref_url }}), der gesondert in derselben Vereinbarung festgelegt wird.

Belgien kennt drei Rahmenwerke, und unser [Vergleich der drei Regionen]({{ "allocation-key-belgium" | ref_url }}) zeigt im Detail, was jedes zulässt:

- **Wallonie**: drei von der CWaPE veröffentlichte Standardschlüssel — egalitärer fester, spezifischer fester und verbrauchsbasierter dynamischer Schlüssel —, welche die VNB automatisch akzeptieren; jeder andere Schlüssel muss von der CWaPE genehmigt werden.
- **Brüssel**: drei von Sibelga betriebene und von BRUGEL vorgesehene Methoden — fest (in einer oder mehreren Runden), prorata, hybrid —, die auf Antrag der einzigen Kontaktstelle jederzeit geändert werden können.
- **Flandern**: keine vom VREG veröffentlichte Liste „standardisierter“ Schlüssel; maßgeblich ist das Fluvius-Protokoll, das drei *verdeelsleutels* unterstützt: vaste, relatieve und optimale.

Hinter diesen drei Vokabularen stehen überall dieselben zwei Familien: **feste** Schlüssel, egalitär oder nach den Beiträgen der Mitglieder gewichtet, und **dynamische oder optimierte** Schlüssel, die dem tatsächlichen Verbrauch folgen. Die Wahl zwischen ihnen ist keine technische Frage, sondern eine Governance-Entscheidung: Gleichheit unter den Mitgliedern, Anerkennung der Investition oder Maximierung des kollektiven Eigenverbrauchs. Auch die Vielfalt der Profile zählt — sobald eine Schule oder ein KMU hinzukommt, ist strikte Gleichheit nicht mehr optimal —, ebenso die finanzielle Vorhersehbarkeit, die die Mitglieder erwarten. Schließlich erlauben alle drei Regionen, einen Schlüssel nach dem Start zu ändern: Planen Sie am besten von Anfang an eine jährliche Überprüfung in der Generalversammlung ein.

Bleibt noch, diese Grundsätze an Ihren eigenen Profilen zu prüfen, denn derselbe Schlüssel kann in einer Gemeinschaft 70 % der verfügbaren Erzeugung wiedergewinnen und in einer anderen kaum 50 %. OptimCE bietet dafür zwei Funktionen, die beide mit einer CSV Ihrer Erzeugungs- und Verbrauchsdaten arbeiten. Die [automatische Generierung]({{ "optimce-allocation-key-generator" | ref_url }}) schlägt einen Kandidatenschlüssel vor, entweder per Brute-Force-Scan der Standardschlüssel Ihrer Region oder mit dem LOGAAS-Algorithmus, dessen Nicht-Standardschlüssel in der Wallonie den CWaPE-Genehmigungsweg durchlaufen muss. Die [Simulation]({{ "optimce-allocation-key-simulation" | ref_url }}) spielt einen von Ihnen gewählten Schlüssel durch und liefert Eigenverbrauch, Überschuss, Autarkiegrad und Teilungsgrad, ohne den vom Netzbetreiber angewandten Schlüssel zu berühren. Keine der beiden übermittelt einen Schlüssel an den VNB: Nachtrag, Unterschriften und Übermittlung bleiben in Ihrer Hand.

Die Leitfäden unten folgen derselben Reihenfolge: zuerst die drei regionalen Rahmenwerke, dann Generierung und Simulation eines Schlüssels auf Ihren Daten.
