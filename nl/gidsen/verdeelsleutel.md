---
layout: pillar
title: "Verdeelsleutel: begrijpen, kiezen, testen"
subtitle: "Wat elk gewest aanvaardt, hoe u een sleutelfamilie kiest en hoe u die daarna op uw eigen data test."
description: "Verdeelsleutels voor Belgische energiegemeenschappen: wat CWaPE, BRUGEL en VREG aanvaarden, een sleutelfamilie kiezen, genereren en simuleren op uw data."
lang: nl
ref: pillar-cle-de-repartition
pillar: cle-de-repartition
permalink: /nl/gidsen/verdeelsleutel/
breadcrumb_parent: guides
last_modified_at: 2026-09-26
sections:
  - title: "De sleutel begrijpen en wat elk gewest aanvaardt"
    refs: [allocation-key-belgium]
  - title: "Uw sleutel genereren en simuleren met OptimCE"
    refs: [optimce-allocation-key-generator, optimce-allocation-key-simulation]
---
In een deelactie is de **verdeelsleutel** de rekenregel, uitgedrukt in percentages, die aan elk verbruikend lid een deel toewijst van de energie die de producenten injecteren. Er is niets fysieks aan: de distributienetbeheerder (DNB) past hem kwartier per kwartier toe op de registraties van de slimme meters. Per deelactie geldt slechts één sleutel, en die beslist alleen over de kWh: wat ze in euro waard zijn, hangt af van de [interne overdrachtsprijs]({{ "internal-price-shared-energy" | ref_url }}), die apart in dezelfde overeenkomst wordt vastgelegd.

België telt drie kaders, en onze [vergelijking van de drie gewesten]({{ "allocation-key-belgium" | ref_url }}) beschrijft wat elk ervan toelaat:

- **Wallonië**: drie standaardsleutels gepubliceerd door de CWaPE — egalitaire vaste, specifieke vaste en dynamische sleutel op basis van verbruik — die de DNB's automatisch aanvaarden; elke andere sleutel moet door de CWaPE worden toegestaan.
- **Brussel**: drie methoden die Sibelga hanteert en BRUGEL voorziet — vast (in één of meerdere rondes), prorata, hybride —, op elk moment wijzigbaar op verzoek van het enige contactpunt.
- **Vlaanderen**: geen door de VREG gepubliceerde lijst van “standaard” sleutels; het Fluvius-protocol, de bron van gezag, ondersteunt drie verdeelsleutels: vaste, relatieve en optimale.

Achter die drie terminologieën komen overal dezelfde twee families terug: **vaste** sleutels, egalitair of gewogen naar de inbreng van de leden, en **dynamische of geoptimaliseerde** sleutels, die het reële verbruik volgen. Tussen beide kiezen is geen technische kwestie, maar een governancekeuze: gelijkheid tussen de leden, erkenning van de investering of maximaal collectief zelfverbruik. Ook de diversiteit van de profielen weegt — zodra een school of een kmo toetreedt, is strikte gelijkheid niet meer optimaal —, net als de financiële voorspelbaarheid die de leden verwachten. Ten slotte staan de drie gewesten toe dat u een sleutel na de opstart wijzigt: voorzie dus meteen een jaarlijkse herziening op de algemene vergadering.

Rest nog de toets aan uw eigen profielen, want dezelfde sleutel kan in de ene gemeenschap 70 % van de beschikbare productie terugwinnen en in een andere amper 50 %. OptimCE biedt daarvoor twee functies, allebei gevoed met een CSV van uw productie- en verbruiksdata. De [automatische generatie]({{ "optimce-allocation-key-generator" | ref_url }}) stelt een kandidaat-sleutel voor, hetzij door de standaardsleutels van uw gewest af te zoeken (brute force), hetzij met het LOGAAS-algoritme, waarvan de niet-standaard sleutel in Wallonië het CWaPE-toestemmingsspoor moet doorlopen. De [simulatie]({{ "optimce-allocation-key-simulation" | ref_url }}) speelt uw data door een sleutel die u zelf hebt gekozen en geeft het zelfverbruik, het surplus, de zelfvoorzieningsgraad en de deelgraad terug, zonder te raken aan de sleutel die de netbeheerder toepast. Geen van beide bezorgt een sleutel aan de DNB: de bijlage bij de overeenkomst, de handtekeningen en de doorgifte blijven in uw handen.

De gidsen hieronder volgen dezelfde volgorde: eerst de drie gewestelijke kaders, daarna het genereren en simuleren van een sleutel op uw data.
