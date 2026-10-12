---
layout: page
title: "Aufteilungsschlüssel: berechnen, testen, verfolgen"
breadcrumb_title: "Aufteilungsschlüssel"
subtitle: "Vom ersten Vorschlag bis zum Nachtrag: den Schlüssel Ihrer Gemeinschaft an einem Ort anlegen, generieren, testen und weiterentwickeln."
description: "Berechnen, simulieren und verfolgen Sie den Aufteilungsschlüssel Ihrer Energiegemeinschaft: Viertelstundendaten, zwei Algorithmen, Versionen, Zustimmung."
lang: de
ref: product-allocation-key
permalink: /de/funktionen/aufteilungsschluessel/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Was ist der Unterschied zwischen dem Generieren und dem Simulieren eines Schlüssels?"
    a: "Die Generierung geht von Ihren Daten aus und schlägt einen Kandidatenschlüssel vor, mit der erwarteten kollektiven Eigenverbrauchsquote. Die Simulation geht von einem Schlüssel aus, den Sie gewählt haben, und misst, was er auf Ihren Daten ergeben hätte. Man generiert, um einen Schlüssel zu suchen, und simuliert, um den Schlüssel zu prüfen, den man in Betracht zieht."
  - q: "Welche Daten braucht man, um einen Schlüssel zu generieren oder zu simulieren?"
    a: "Eine CSV-Datei mit Verbrauch und Erzeugung je Viertelstunde, mit einer Spalte je Verbraucher und einer Spalte für die eingespeiste Erzeugung, deren Namen Sie angeben. Das ist der Zeitschritt der Aufteilung in Belgien: 96 Werte pro Tag und Zähler."
  - q: "Wird der generierte Schlüssel an den Netzbetreiber gesendet?"
    a: "Nein. OptimCE schlägt einen Schlüssel vor, sendet ihn aber nie von selbst an den Netzbetreiber. Ein neuer Schlüssel folgt dem üblichen Weg des Nachtrags; OptimCE bewahrt jede seiner Versionen auf und verfolgt die Zustimmung der Mitglieder."
  - q: "Was ist LOGAAS?"
    a: "LOGAAS ist einer der beiden Generierungsalgorithmen, hervorgegangen aus der Forschung des CeCoTePe im Projekt Locomotrice. Er kombiniert lineare Optimierung und einen genetischen Algorithmus, und seine erweiterten Einstellungen haben Standardwerte, die für die meisten Anwendungsfälle passen. Die Anwendung zeigt ihn unter dem Namen „OLAGSA“ an. Der andere Algorithmus durchläuft die Standardschlüssel Ihrer Region."
---
Der Aufteilungsschlüssel legt Viertelstunde für Viertelstunde fest, wer welchen Anteil der lokalen
Erzeugung erhält. Ihn zu wählen ist nur der Anfang: Die Mitglieder müssen ihm zustimmen, er muss auf
echten Daten getestet und dann per Nachtrag angepasst werden, wenn Mitglieder beitreten oder
austreten. In einer Tabellenkalkulation stehen seine Koeffizienten in Dateien, die man immer wieder
kopiert und irgendwann nicht mehr datieren kann. OptimCE deckt diesen gesamten Lebenszyklus an einem
Ort ab. Unsere Leitfäden erklären, wie man einen Schlüssel wählt; diese Seite zeigt, wo im Werkzeug
jeder Schritt stattfindet.

## So übernimmt OptimCE das

### Einen Schlüssel anlegen

Ein Schlüssel lässt sich auf zwei Arten aufbauen: in einem vollständigen Raster oder mit einem
Schritt-für-Schritt-Assistenten. Beide Wege führen zum selben Schlüssel. Der Assistent fragt zuerst
nach der Zahl der Verbraucher und ihren Namen, dann nach den Iterationen: Jede verteilt einen
Prozentsatz der verfügbaren Energie, zum Beispiel anteilig zum tatsächlichen Verbrauch jedes
Einzelnen, bis 100 % erreicht sind. Eine Prüfseite zeigt Ihnen das vollständige Raster, bevor Sie
den Schlüssel speichern.

{% include product-shot.html name="key-wizard" alt="Prüfraster eines mit dem Assistenten erstellten Schlüssels in der englischen Oberfläche: eine erste Iteration mit 70 % und eine zweite mit 30 % der Energie, jeweils anteilig („Pro rata“) auf drei Verbraucher, Cons1 bis Cons3, verteilt." caption="Ein Schlüssel in zwei anteiligen Iterationen, vor dem Speichern geprüft (Testdaten, englische Oberfläche)." %}

### Einen Kandidatenschlüssel generieren

Aus einer CSV-Datei mit Verbrauch und Erzeugung je Viertelstunde schlägt das Generierungsmodul
einen Kandidatenschlüssel vor, mit der erwarteten kollektiven Eigenverbrauchsquote. Zwei
Algorithmen stehen zur Verfügung:

- der **vollständige Durchlauf der Standardschlüssel** Ihrer Region;
- **LOGAAS** (in der Anwendung als „OLAGSA“ angezeigt), hervorgegangen aus der Forschung des
  CeCoTePe im Projekt Locomotrice, der lineare Optimierung und einen genetischen Algorithmus
  kombiniert.

Der erste Algorithmus bleibt im Katalog der Standardschlüssel Ihrer Region. Der zweite sucht auch
außerhalb dieses Katalogs: Er kann eine bessere Aufteilung finden, doch der Schlüssel, den er
vorschlägt, erfordert dann ein besonderes Verfahren (siehe unten).

Die Generierung wird zunächst in eine Warteschlange gestellt, danach erscheint die Liste der
berechneten Schlüssel, jeder mit dem Detail seiner Aufteilung je Iteration. Den passenden Schlüssel
speichern Sie anschließend in Ihren Aufteilungsschlüsseln. Das Generierungsmodul wird unter den
Zusatzdiensten der Gemeinschaft aktiviert.

{% include product-shot.html name="key-generation" alt="Formular „Start a generation“ in der englischen Oberfläche: Der Algorithmus „Linear Optimization and Genetic Algorithm with Atypical Speciation“ ist ausgewählt, dazu der Name der Generierung, die Einspeisespalte „Production“ und das Feld zum Hochladen der Datendatei." caption="Der Start einer Generierung: Algorithmus, Erzeugungsspalte und Datendatei (Testdaten, englische Oberfläche)." %}

### Einen Schlüssel auf Ihren Daten simulieren

Die Simulation geht von einem Schlüssel Ihrer Wahl aus und spielt ihn auf Ihrer eigenen Datei
durch, ohne den angewandten Schlüssel zu berühren. Sie lesen dann Eigenverbrauch, Überschuss,
Autarkiegrad und Teilungsgrad ab, und zwar insgesamt, je Zeitschritt und je Iteration. Das Detail je
Verbraucher zeigt Zuteilung, Verbrauch, eigenverbrauchte Energie, Überschuss und Restmenge: Hier
vergleicht man zwei mögliche Aufteilungen miteinander, bevor man einen Nachtrag vorschlägt.

### Versionen und Zustimmung verfolgen

Jede Version des Schlüssels wird archiviert, und die Zustimmung der Mitglieder wird nachverfolgt.
Tritt ein Mitglied bei oder aus, kommt die neue Version zur Historie hinzu, statt die alte Version
zu ersetzen. Ein vom Werkzeug vorgeschlagener Schlüssel geht nie von selbst an den Netzbetreiber: Er
folgt dem üblichen Weg des Nachtrags, genau wie ein Schlüssel, den Sie von Hand erstellt haben.

## Was es nicht leistet

**Nichts wird an den Netzbetreiber gesendet.** OptimCE bereitet den Schlüssel vor und bewahrt ihn
auf; seine Übermittlung folgt dem Verfahren des Nachtrags, das die Gemeinschaft selbst durchführt.

**Keine Echtzeit.** Generierung und Simulation arbeiten mit den Dateien, die Sie selbst importieren,
nicht mit Live-Messwerten.

**Die Generierung schlägt vor, sie entscheidet nicht.** Die Wahl des Schlüssels bleibt Sache der
Gemeinschaft und ihrer Mitglieder. Ein Schlüssel außerhalb des Standardkatalogs folgt in der
Wallonie einem besonderen Verfahren: Der Leitfaden zur Generierung beschreibt es.

**Eine Simulation ist nur so gut wie die Datei.** Sie spielt genau den Zeitraum und die Profile
durch, die Sie ihr geben. Über ein Jahr, das nicht in der Datei enthalten ist, sagen ihre Ergebnisse
nichts.

## Häufige Fragen {#faq}

### Was ist der Unterschied zwischen dem Generieren und dem Simulieren eines Schlüssels?

Die Generierung geht von Ihren Daten aus und schlägt einen Kandidatenschlüssel vor, mit der
erwarteten kollektiven Eigenverbrauchsquote. Die Simulation geht von einem Schlüssel aus, den Sie
gewählt haben, und misst, was er auf Ihren Daten ergeben hätte. Man generiert, um einen Schlüssel
zu suchen, und simuliert, um den Schlüssel zu prüfen, den man in Betracht zieht.

### Welche Daten braucht man, um einen Schlüssel zu generieren oder zu simulieren?

Eine CSV-Datei mit Verbrauch und Erzeugung je Viertelstunde, mit einer Spalte je Verbraucher und
einer Spalte für die eingespeiste Erzeugung, deren Namen Sie angeben. Das ist der Zeitschritt der
Aufteilung in Belgien: 96 Werte pro Tag und Zähler.

### Wird der generierte Schlüssel an den Netzbetreiber gesendet?

Nein. OptimCE schlägt einen Schlüssel vor, sendet ihn aber nie von selbst an den Netzbetreiber. Ein
neuer Schlüssel folgt dem üblichen Weg des Nachtrags; OptimCE bewahrt jede seiner Versionen auf und
verfolgt die Zustimmung der Mitglieder.

### Was ist LOGAAS?

LOGAAS ist einer der beiden Generierungsalgorithmen, hervorgegangen aus der Forschung des CeCoTePe
im Projekt Locomotrice. Er kombiniert lineare Optimierung und einen genetischen Algorithmus, und
seine erweiterten Einstellungen haben Standardwerte, die für die meisten Anwendungsfälle passen.
Die Anwendung zeigt ihn unter dem Namen „OLAGSA“ an. Der andere Algorithmus durchläuft die
Standardschlüssel Ihrer Region.

## Weiterlesen

- [Aufteilungsschlüssel automatisch generieren]({{ "optimce-allocation-key-generator" | ref_url }}):
  die beiden Algorithmen im Detail und wann Sie sich für welchen entscheiden.
- [Aufteilungsschlüssel simulieren: Szenarien testen]({{ "optimce-allocation-key-simulation" | ref_url }}):
  die Kennzahlen richtig lesen und Szenarien miteinander vergleichen.
- [Aufteilungsschlüssel in Belgien: 3 Regionen]({{ "allocation-key-belgium" | ref_url }}):
  die Standardschlüssel und die Regeln, die in jeder Region gelten.

{% include product-cta.html page_key="allocation-key" guide="key-generation" title="Ihren Aufteilungsschlüssel mit OptimCE verwalten" %}
