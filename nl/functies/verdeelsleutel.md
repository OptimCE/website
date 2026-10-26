---
layout: page
title: "Verdeelsleutel: genereren, simuleren, opvolgen"
breadcrumb_title: "Verdeelsleutel"
subtitle: "Van het eerste voorstel tot het addendum: de verdeelsleutel van uw gemeenschap op één plek aanmaken, genereren, testen en laten evolueren."
description: "Genereer, simuleer en volg de verdeelsleutel van uw energiegemeenschap op: kwartierdata, twee algoritmen, versies en aanvaarding door de leden."
lang: nl
ref: product-allocation-key
permalink: /nl/functies/verdeelsleutel/
breadcrumb_parent: features
product_page: true
last_modified_at: 2026-10-11
faq:
  - q: "Wat is het verschil tussen een sleutel genereren en simuleren?"
    a: "Generatie vertrekt van uw gegevens en stelt een kandidaat-sleutel voor, met de verwachte collectieve zelfverbruiksgraad. Simulatie vertrekt van een sleutel die u zelf hebt gekozen en meet wat die op uw gegevens zou hebben opgeleverd. U genereert om een sleutel te zoeken, u simuleert om de sleutel te toetsen die u overweegt."
  - q: "Welke gegevens hebt u nodig om een sleutel te genereren of te simuleren?"
    a: "Een CSV-bestand met verbruik en productie per kwartier, met één kolom per verbruiker en één kolom voor de geïnjecteerde productie, waarvan u de naam opgeeft. Het kwartier is de tijdstap van de verdeling in België: 96 waarden per dag en per meter."
  - q: "Wordt de gegenereerde sleutel naar de netbeheerder gestuurd?"
    a: "Nee. OptimCE stelt een sleutel voor, maar stuurt hem nooit zelf naar de netbeheerder. Een nieuwe sleutel volgt de gebruikelijke weg van het addendum; OptimCE bewaart elke versie ervan en volgt de aanvaarding door de leden op."
  - q: "Wat is LOGAAS?"
    a: "LOGAAS is een van de twee generatie-algoritmen, voortgekomen uit het onderzoek van het CeCoTePe binnen het project Locomotrice. Het combineert lineaire optimalisatie en een genetisch algoritme, en de standaardwaarden van zijn geavanceerde instellingen volstaan voor de meeste toepassingen. De applicatie toont het onder de naam “OLAGSA”. Het andere algoritme doorloopt de standaardsleutels van uw gewest."
---

De verdeelsleutel bepaalt, kwartier per kwartier, wie welk deel van de lokale productie krijgt.
Hem kiezen is maar een begin: de leden moeten hem aanvaarden, hij moet worden getest op echte
gegevens, en daarna evolueert hij per addendum, telkens wanneer leden toetreden of vertrekken. Wie
zijn verdeelsleutel in een rekenblad berekent, bewaart de coëfficiënten in bestanden die worden
gekopieerd tot niemand nog weet van wanneer ze dateren. OptimCE dekt die hele levenscyclus af. Onze
gidsen leggen uit hoe u een sleutel kiest; deze pagina toont waar elke stap in de tool gebeurt.

## Hoe OptimCE het aanpakt

### Een sleutel aanmaken

Een sleutel bouwt u op twee manieren op: in een volledige tabel, of met een stapsgewijze wizard.
Beide leiden tot dezelfde sleutel. De wizard vraagt het aantal verbruikers en hun naam, en daarna
de iteraties: elke iteratie verdeelt een percentage van de beschikbare energie, bijvoorbeeld
relatief, naar rato van ieders werkelijke verbruik, tot 100 % bereikt is. Een overzichtspagina
toont de volledige tabel voordat u de sleutel opslaat.

{% include product-shot.html name="key-wizard" alt="Overzichtstabel van een sleutel die met de wizard is aangemaakt: een eerste iteratie van 70 % en daarna een tweede van 30 % van de energie, telkens “Pro-rata” verdeeld over drie verbruikers, Cons1 tot Cons3." caption="Een sleutel in twee iteraties pro rata, nagelezen voordat hij wordt opgeslagen (testgegevens)." %}

### Een kandidaat-sleutel genereren

Op basis van een CSV-bestand met verbruik en productie per kwartier berekent de generatiemodule
een kandidaat-sleutel, met de verwachte collectieve zelfverbruiksgraad. Er zijn twee algoritmen
beschikbaar:

- het **volledig doorlopen van de standaardsleutels** van uw gewest;
- **LOGAAS** (in de applicatie weergegeven als “OLAGSA”), voortgekomen uit het onderzoek van het
  CeCoTePe binnen het project Locomotrice, dat lineaire optimalisatie en een genetisch algoritme
  combineert.

Het eerste blijft binnen de catalogus van standaardsleutels van uw gewest. Het tweede zoekt ook
buiten die catalogus: het kan een betere verdeling vinden, maar de sleutel die het voorstelt, vraagt
dan een bijzondere procedure (zie verder).

De generatie komt in een wachtrij, daarna verschijnt de lijst van berekende sleutels, elk met het
detail van de verdeling per iteratie. De sleutel die u bevalt, slaat u op bij uw verdeelsleutels. De
generatiemodule activeert u bij de annexdiensten van de gemeenschap.

{% include product-shot.html name="key-generation" alt="Formulier “Start een generatie”: het algoritme “Lineaire optimalisatie en genetisch algoritme met atypische speciatie” is geselecteerd, de verbruiksgegevens komen uit een geïmporteerd bestand, met de naam van de generatie en de injectiekolom “Production”." caption="Een generatie starten: het algoritme, de productiekolom en het gegevensbestand (testgegevens)." %}

### Een sleutel simuleren op uw gegevens

De simulatie vertrekt van een sleutel naar keuze en speelt die opnieuw af op uw eigen bestand,
zonder de toegepaste sleutel te raken. U leest het zelfverbruik, het overschot, de
zelfvoorzieningsgraad en de deelgraad af, globaal, per tijdstap en per iteratie. Het detail per
verbruiker toont de toewijzing, het verbruik, de zelfverbruikte energie, het overschot en het
residuele volume: daar vergelijkt u twee verdelingen voordat u een addendum voorstelt.

### Versies en aanvaarding opvolgen

Elke versie van de sleutel wordt bewaard, en de aanvaarding door de leden wordt opgevolgd. Treedt
een lid toe of vertrekt het, dan wordt de nieuwe versie aan de historiek toegevoegd in plaats van de
oude te vervangen. Een sleutel die de tool voorstelt, gaat nooit vanzelf naar de distributienetbeheerder:
hij volgt de gebruikelijke weg van het addendum, net als een sleutel die met de hand is opgebouwd.

## Wat het niet doet

**Niets wordt naar de netbeheerder gestuurd.** OptimCE bereidt de sleutel voor en bewaart hem; de
doorgifte volgt de procedure van het addendum, die de gemeenschap zelf voert.

**Geen realtime.** Generatie en simulatie werken op de bestanden die u importeert, niet op live
metingen.

**De generatie stelt voor, ze beslist niet.** De keuze van de sleutel blijft bij de gemeenschap en
haar leden. Een sleutel buiten de standaardcatalogus volgt in Wallonië een bijzondere procedure:
de gids over de generatie beschrijft die.

**Een simulatie is maar zo goed als het bestand.** Ze speelt de periode en de profielen af die u haar
geeft. Over een jaar dat er niet in zit, zeggen de resultaten niets.

## Veelgestelde vragen {#faq}

### Wat is het verschil tussen een sleutel genereren en simuleren?

Generatie vertrekt van uw gegevens en stelt een kandidaat-sleutel voor, met de verwachte
collectieve zelfverbruiksgraad. Simulatie vertrekt van een sleutel die u zelf hebt gekozen en meet
wat die op uw gegevens zou hebben opgeleverd. U genereert om een sleutel te zoeken, u simuleert om
de sleutel te toetsen die u overweegt.

### Welke gegevens hebt u nodig om een sleutel te genereren of te simuleren?

Een CSV-bestand met verbruik en productie per kwartier, met één kolom per verbruiker en één kolom
voor de geïnjecteerde productie, waarvan u de naam opgeeft. Het kwartier is de tijdstap van de
verdeling in België: 96 waarden per dag en per meter.

### Wordt de gegenereerde sleutel naar de netbeheerder gestuurd?

Nee. OptimCE stelt een sleutel voor, maar stuurt hem nooit zelf naar de netbeheerder. Een nieuwe
sleutel volgt de gebruikelijke weg van het addendum; OptimCE bewaart elke versie ervan en volgt de
aanvaarding door de leden op.

### Wat is LOGAAS?

LOGAAS is een van de twee generatie-algoritmen, voortgekomen uit het onderzoek van het CeCoTePe
binnen het project Locomotrice. Het combineert lineaire optimalisatie en een genetisch algoritme, en
de standaardwaarden van zijn geavanceerde instellingen volstaan voor de meeste toepassingen. De
applicatie toont het onder de naam “OLAGSA”. Het andere algoritme doorloopt de standaardsleutels van
uw gewest.

## Verder lezen

- [Verdeelsleutel automatisch genereren]({{ "optimce-allocation-key-generator" | ref_url }}):
  de twee algoritmen om een optimale verdeelsleutel te zoeken, en wanneer u het ene of het andere
  kiest.
- [Verdeelsleutel simuleren: test uw scenario's]({{ "optimce-allocation-key-simulation" | ref_url }}):
  de indicatoren lezen en scenario's vergelijken.
- [Verdeelsleutel in België: de 3 regio's]({{ "allocation-key-belgium" | ref_url }}):
  de standaardsleutels en de regels van elk gewest.

{% include product-cta.html page_key="allocation-key" guide="key-generation" title="Uw verdeelsleutel beheren met OptimCE" %}
