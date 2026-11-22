---
layout: post
title: "Données de comptage en communauté d'énergie"
date: 2026-11-22 06:00:00 +0100
author: "Eric d'OptimCE"
excerpt: "Une communauté d'énergie ne mesure rien elle-même. Chaque mois, au plus tard le douzième jour ouvrable, le gestionnaire de réseau envoie à son représentant les volumes de chaque membre, quart d'heure par quart d'heure : 2 880 valeurs par compteur et par grandeur pour un mois de trente jours. Ce flux-là est une condition de la participation, pas un consentement. Tout le reste, de l'historique qui sert à simuler une clé au boîtier branché sur le port P1, demande l'accord de chaque membre."
description: "Données de comptage d'une communauté d'énergie : ce que le GRD transmet et quand, sur quelle base légale, ce que voit chaque membre, et le port P1."
tags: [guide, community]
lang: fr
ref: meter-data-energy-community
pillar: communautes-energie
permalink: /guides/donnees-comptage-communaute-energie/
faq:
  - q: "Quelles données de comptage le GRD transmet-il à une communauté d'énergie ?"
    a: "En Wallonie, le gestionnaire de réseau de distribution envoie au représentant du partage, pour chaque membre et chaque quart d'heure, le prélèvement, le volume partagé consommé et l'alloconsommation, c'est-à-dire la part que le fournisseur facture. Il y ajoute l'injection de chaque producteur, le volume partagé total, le surplus et la méthode de répartition utilisée. La convention type approuvée par la CWaPE le 12 octobre 2023 lui impose de mettre ces données à disposition chaque mois, au plus tard le douzième jour ouvrable du mois suivant. C'est une obligation de moyens, et des données non validées peuvent arriver chaque semaine. Le canal et le format sont ceux que le GRD a choisis. Chez ORES, ce sont deux fichiers CSV envoyés par e-mail, l'un pour la production, l'autre pour la consommation, avec une ligne par quart d'heure, par code EAN et par itération de la clé de répartition."
  - q: "Faut-il donner son consentement pour que ses données aillent à la communauté ?"
    a: "Pour le flux du partage lui-même, non. Le décret électricité wallon oblige le GRD à transmettre au représentant les données de mesure de chaque participant, et la convention type de la CWaPE précise que toute participation requiert la collecte et l'utilisation des courbes de charge par le GRD. Ce flux est une condition de la participation : on ne peut pas rester dans le partage et le refuser. Le participant signe toutefois l'annexe 8 du formulaire de partage. Il y mandate le représentant pour communiquer ses données dans la procédure, et autorise le GRD à transmettre sa courbe au quart d'heure à son fournisseur. Tout ce qui sort de ce cadre exige en revanche un accord préalable, libre, spécifique, éclairé et univoque : l'historique demandé pour simuler une clé, un boîtier branché sur le port P1, des courbes individuelles montrées aux autres membres."
  - q: "Les autres membres peuvent-ils voir ma consommation ?"
    a: "Pas par défaut. Le GRD envoie les données de chaque membre au représentant, pas aux autres membres, et le décret wallon impose que la convention entre chaque participant et la communauté règle la protection de la vie privée et la procédure de transmission de données entre participants. L'Autorité de protection des données rappelle que les compteurs communicants permettent d'inférer des données sensibles sur les comportements des habitants : une courbe au quart d'heure dit quand un ménage se lève, part et rentre. Une pratique prudente consiste à montrer à chaque membre ses propres chiffres, et au groupe les seuls agrégats : production, volume partagé, part de la consommation couverte. Un classement nominatif ou une courbe individuelle ne se montrent qu'avec l'accord explicite de la personne. Seule exception de fait : quand la communauté n'a qu'un producteur, la production partagée est l'injection de ce membre."
  - q: "Comment accéder aux données de mon compteur communicant ?"
    a: "Par le portail de votre gestionnaire de réseau, gratuitement : le décret wallon l'impose. L'arrêté du 1er décembre 2022 fixe le minimum : des vues annuelles, mensuelles, hebdomadaires et journalières sur les vingt-quatre derniers mois, le détail infrajournalier sur demande explicite, et un export vers un tableur. Chez ORES, la vue au quart d'heure se demande dans l'espace client de myORES ; ORES indique que ces données ne remontent pas vers votre fournisseur, mais que cette activation lui est transmise, ce qui peut entraîner chez certains fournisseurs une facture intermédiaire, sans effet sur la facture annuelle de régularisation. RESA propose un profil au quart d'heure dans MyRESA, l'AIEG et l'AIESH dans MyConso. Ces mêmes données sont celles qu'une communauté vous demandera pour simuler une clé de répartition avant le partage : vous pouvez les exporter et les lui confier, avec un accord écrit pour cet usage. Pendant le partage, vos volumes partagés vous parviennent par la communauté, qui les reçoit du GRD chaque mois."
  - q: "Le port P1 peut-il servir au partage d'énergie ?"
    a: "Pas pour le calcul. Le port P1 du compteur communicant envoie un relevé par seconde, utile pour suivre sa consommation en temps réel, mais il ne montre que votre propre compteur : ni la production de la toiture partagée, ni la part qui vous est allouée. Les volumes du partage sont ceux que le GRD détermine à partir des relevés et de la clé de répartition, et qu'il transmet chaque mois au représentant ; c'est sur eux que la facture du partage est établie. En Wallonie, le port est désactivé par défaut, et son activation est gratuite sur simple demande au GRD. Le décret fait de celui qui collecte des données par ce port le responsable de leur traitement : une communauté qui distribue des boîtiers P1 et centralise leurs mesures doit recueillir l'accord préalable de chaque membre et l'informer de l'usage qu'elle en fait."
  - q: "Combien de temps les données de partage sont-elles conservées ?"
    a: "En Wallonie, le décret électricité fixe la règle pour la CWaPE et le gestionnaire de réseau : les données à caractère personnel liées au partage sont conservées cinq ans après l'arrêt de l'activité de partage, et celles d'un participant qui a quitté le partage sont supprimées cinq ans après la notification de sa sortie. Le texte ne fixe pas de durée pour le représentant. Responsable du traitement des données qu'il reçoit du GRD, il ne peut les utiliser que pour les finalités prévues par le décret, et le RGPD l'oblige à fixer lui-même une durée de conservation et à l'annoncer aux membres. Côté compteur, le décret impose que l'appareil garde, lisibles à distance, les courbes de charge des dix derniers jours, les index journaliers des quarante derniers jours et les index mensuels des treize derniers mois."
---

Une communauté d'énergie vit de données qu'elle ne produit pas. Ses **données de comptage** viennent toutes du gestionnaire de réseau de distribution (GRD), à qui le décret wallon réserve la collecte des données de comptage. Chaque mois, il envoie au représentant du partage les volumes de chaque membre, quart d'heure par quart d'heure : **2 880 valeurs par compteur** et par grandeur pour un mois de trente jours, **au plus tard le douzième jour ouvrable** du mois suivant.

Ces données circulent selon deux régimes. Le premier est fixé par la loi : le GRD transmet, la communauté reçoit, et aucun membre n'a de consentement à donner. Le second couvre tout le reste, de l'historique qui sert à simuler une clé au boîtier branché sur le port P1, et il exige l'accord de chaque membre.

Ce site traite déjà les régimes de comptage et le port P1 ([« Compteur communicant en Wallonie : le guide »](/guides/compteur-communicant-wallonie/)), l'application de la clé ([« Clé de répartition en Belgique : les 3 régions »](/guides/cle-repartition-communaute-energie-belgique/)), la simulation ([« Simuler une clé de répartition : scénarios »](/guides/simuler-cle-repartition-optimce/)), la règle du quart d'heure ([« Électricité en circuit court : le mode d'emploi »](/guides/electricite-circuit-court-mode-emploi/)) et les formulaires ([« Communauté d'énergie : documents et délais CWaPE »](/guides/documents-administratifs-communaute-energie-wallonie/)).

**La question posée ici est celle de la circulation : quelles données passent du GRD à la communauté, à quel rythme, sur quelle base légale, et ce qu'un membre a le droit de voir, de lui-même et des autres.** L'article décrit la Wallonie et l'électricité au 22 novembre 2026 ; la Flandre et Bruxelles sont résumées à la fin.

## Les données dont une communauté a besoin

Une communauté a besoin de données à trois moments. **Avant le partage**, pour choisir sa clé de répartition : l'historique de chaque futur membre et le profil de production, idéalement une année au quart d'heure. Le GRD n'envoie rien à ce stade ; ce sont les membres qui fournissent ces courbes. **Pendant le partage**, pour facturer : les volumes que le GRD calcule chaque mois. **Après**, pour rendre des comptes : le GRD transmet chaque année à la CWaPE les données de comptage de chaque communauté (article 35*sexdecies*, § 3 du décret du 12 avril 2001).

Les grandeurs du partage sont définies par la convention type que la CWaPE a approuvée le 12 octobre 2023 et que chaque communauté signe avec son GRD. Elles sont calculées pour chaque code EAN et chaque quart d'heure.

| Grandeur | Sigle | Ce qu'elle mesure |
|---|---|---|
| Injection | I | La production non consommée sur place, injectée sur le réseau |
| Prélèvement | Pl | La consommation venue du réseau : Pl = VPC + AL |
| Volume partagé | VP | La somme des injections mises à disposition du partage |
| Volume partagé consommé | VPC | La consommation d'un participant couverte par le partage |
| Excédent | E | Le volume alloué à un participant qu'il n'a pas consommé |
| Surplus | S | Le volume partagé que personne n'a consommé : S = VP − ∑ VPC |
| Alloconsommation | AL | La part non couverte, facturée par le fournisseur : AL = Pl − VPC |

*Hypothèses : définitions de l'article 6.2.1 de la convention type (décision CWaPE CD-23j12-CWaPE-0818), reformulées ; les formules sont celles du texte, qui appelle aussi l'alloconsommation « volume résiduel ».*

### Le compteur doit pouvoir les mesurer

Pour un compteur communicant, le guide explicatif du formulaire de partage de la CWaPE pose deux conditions : une fonction communicante « activée et fonctionnelle », et le régime de comptage 3, qui transmet la courbe au quart d'heure vers le marché, activé « auprès du fournisseur, à la demande du participant ». En attendant ce régime, l'annexe 8 du formulaire en tient lieu : le participant y autorise le GRD à transmettre à son fournisseur ses données de comptage quart-horaire.

Un membre doit donc le savoir avant de signer : **sa courbe part chez le représentant, mais aussi chez son fournisseur.** Notre [baromètre des partages autorisés](/guides/barometre-communautes-energie-wallonie/) l'a relevé : quand la CWaPE autorise un partage sous condition suspensive, la condition consiste toujours à passer tous les participants en régime 3.

## Ce que le GRD transmet, à qui et quand

Les gestionnaires de réseau « déterminent les volumes d'électricité consommés dans le cadre de l'opération de partage », puis transmettent à la communauté « les données de mesure » de la production et de chaque participant, et aux fournisseurs « les données nécessaires à la facturation » (article 35*sexdecies*, § 2). Le décret ne fixe ni rythme, ni délai, ni format.

La convention type les fixe : le GRD « met en œuvre tous les moyens » pour fournir ces données « mensuellement, et au plus tard le douzième jour ouvrable du mois suivant » (article 6.2.2). C'est une obligation de moyens. Des données non validées peuvent arriver chaque semaine, par le canal que le GRD a choisi.

Chez ORES, ce sont deux fichiers CSV envoyés par e-mail chaque mois, l'un pour la production, l'autre pour la consommation. Chaque ligne du second porte un quart d'heure, un code EAN et une itération de la clé ; le résultat d'un membre est la somme de ses itérations. Douze consommateurs et une clé en trois itérations, c'est jusqu'à **103 680 lignes** par mois de trente jours.

| Destinataire | Ce qu'il reçoit | Rythme |
|---|---|---|
| Représentant du partage | Les grandeurs ci-dessus, par EAN et par quart d'heure, et la méthode de répartition | Chaque mois, au plus tard le 12<sup>e</sup> jour ouvrable du mois suivant |
| Fournisseur de chaque membre | La courbe au quart d'heure et les volumes partagés, pour facturer le complément | Chaque mois, hors des processus de marché |
| Membre | Ce que la communauté lui communique ; sa courbe sur le portail du GRD | Selon sa convention ; portail en accès libre |
| CWaPE | Les données de comptage de chaque communauté | Chaque année |

*Hypothèses : règles en vigueur en Wallonie au 22 novembre 2026 : décret du 12 avril 2001 (articles 35ter, 35duodecies et 35sexdecies), convention type de la CWaPE et rapport d'évaluation de la CWaPE du 20 février 2025.*

Les fournisseurs ne reçoivent pas les volumes partagés par le circuit habituel : selon le rapport d'évaluation de la CWaPE du 20 février 2025, ils passent « en dehors des processus de marché par un canal distinct (serveurs SFTP) », et chaque fournisseur recalcule ce qu'il facture.

Le nouveau règlement technique, adopté par la CWaPE le 27 août 2026, garde le délai du douzième jour ouvrable. Les données partiront « sous la forme de courbe quart horaire ainsi que de manière agrégée sur le mois », par une interface de programmation si le GRD en a développé une (article IX.7), et les corrections seront possibles jusqu'à douze mois après le mois concerné (article IX.17). Au 22 novembre 2026, sa publication au Moniteur belge est « en préparation » ; il s'appliquera dix jours après.

Pour le gestionnaire, cela fixe un calendrier : les volumes d'un mois arrivent au plus tard vers le milieu du mois suivant, et les factures du partage partent ensuite. Une rectification tardive passe par une note de crédit, comme l'explique [« Facturer l'électricité partagée en Belgique »](/guides/facturer-electricite-partagee-belgique/). Si un membre conteste un volume, le représentant transmet sa réclamation au GRD dans les cinq jours ouvrés, et le GRD répond dans les trente jours (convention type, article 6.1.4).

## Base légale et consentement : deux régimes

### Ce que la loi fait circuler

Le GRD est responsable du traitement des données du compteur, et il les traite « uniquement pour réaliser ses missions légales ou réglementaires » (article 35*septies*, § 2). Pour la notification et l'autorisation du partage, la CWaPE fonde le traitement sur l'article 6.1.e du RGPD, la mission d'intérêt public. La convention type est nette : « Toute participation requiert la collecte et l'utilisation des Courbes de Charge » des participants par le GRD (article 6.1.3). Une fois les données reçues, le représentant en devient à son tour responsable, pour les seules finalités prévues par le décret (article 9.4).

Ce flux ne repose donc pas sur un consentement qu'un membre pourrait retirer en restant dans le partage : il est la condition de la participation. L'annexe 8 le documente, avec le mandat donné au représentant et l'autorisation d'envoyer la courbe au fournisseur. La CWaPE et le GRD conservent ces données cinq ans après l'arrêt du partage ; celles d'un membre sorti sont supprimées cinq ans après la notification de sa sortie (article 35*quaterdecies*, § 3).

### Ce qui demande l'accord de chaque membre

Tout le reste relève d'une règle stricte. Hors disposition légale et hors sous-traitant du GRD, « nul ne peut lire, exporter ou traiter les informations » d'un compteur communicant sans l'accord « préalable, libre, spécifique, éclairée et univoque » de son utilisateur (article 35*septies*, § 3). Pour une communauté, cela vise l'historique demandé pour simuler une clé, un boîtier branché sur le port P1, une courbe ou des volumes nominatifs montrés aux autres membres, et toute donnée confiée à un tiers pour un autre usage.

Une clause noyée dans des statuts ne suffit pas. Dès 2018, la Commission de la protection de la vie privée, à laquelle l'Autorité de protection des données a succédé, écrivait que « la pratique courante consistant à accorder le “consentement” via une clause dans les conditions générales ne peut plus être retenue ». Un accord se demande à part, pour un usage précis, et se retire aussi facilement qu'il s'est donné (article 7, § 3 du RGPD). Quel que soit l'accord, le décret interdit le commerce des données de comptage et des profils qui permettent de déduire les comportements de consommation.

Ces règles s'écrivent dans la convention entre chaque participant et la communauté, qui doit contenir « les règles et responsabilités applicables en matière de respect de la vie privée et de protection des données à caractère personnel » et « la procédure de transmission de données entre les participants » (article 35*duodecies*, § 2). Si la communauté confie ses fichiers à un logiciel en ligne, l'éditeur qui les héberge est un sous-traitant au sens de l'article 28 du RGPD, avec un contrat à la clé. Nous n'avons trouvé aucune ligne directrice belge propre aux communautés sur ce point : les règles générales du RGPD s'appliquent.

### L'historique, avant le partage

Avant l'autorisation, les courbes qui servent à simuler une clé viennent des membres. Le chemin le plus simple est l'export : l'arrêté du Gouvernement wallon du 1er décembre 2022 impose que le portail du GRD couvre vingt-quatre mois, affiche le détail infrajournalier « sur demande explicite du client » et permette d'exporter les données « sous une forme exploitable par un tableur » (article 4). Le membre exporte, puis confie le fichier à la communauté avec un accord écrit pour cet usage.

L'autre chemin est l'accès délégué. ORES ouvre une interface de programmation à des prestataires de services énergétiques, qui récupèrent jusqu'à trois ans de volumes au quart d'heure avec le consentement que le client donne dans myORES. Le règlement d'exécution (UE) 2023/1162 range d'ailleurs les communautés d'énergie renouvelable et citoyennes parmi les parties admissibles auxquelles un client peut autoriser l'accès à ses données de comptage.

## Ce que chaque membre peut voir, et ce qu'il ne doit pas voir des autres

Le GRD envoie les volumes du partage au représentant, pas aux membres. Ce qu'un membre en reçoit dépend de la communauté : sa facture de partage, qui reprend son volume partagé consommé, et ce que sa convention prévoit en plus. Sa courbe complète, il la voit gratuitement sur le portail de son GRD (article 35*ter*, § 3). Chez ORES, la vue au quart d'heure se demande dans l'espace client de myORES. Elle ne fait pas remonter ces données chez le fournisseur, qui doit les demander lui-même à ORES pour les utiliser ; mais, selon la FAQ de myORES, l'activation « est transmise à votre fournisseur d'énergie », et certains fournisseurs émettent alors une facture intermédiaire, sans effet sur la facture annuelle de régularisation ni sur la compensation. RESA propose un profil au quart d'heure dans MyRESA, l'AIEG et l'AIESH dans MyConso. S'il exerce son droit d'accès auprès du représentant pour des données que détient le GRD, le représentant transmet la demande sans délai et le GRD répond directement au membre (convention type, article 9.4).

Ce que les membres voient les uns des autres est une autre affaire. L'Autorité de protection des données le rappelait en 2023 : les compteurs communicants « permettent d'inférer des données potentiellement sensibles sur les comportements des habitants ». Une courbe au quart d'heure dit quand un ménage se lève, quand la maison se vide et quand elle se remplit. Le décret renvoie ce point à la convention de chaque participant ; à défaut, le RGPD impose la minimisation (article 5, § 1, c). Nous recommandons trois règles :

- chaque membre voit ses propres chiffres, quarts d'heure compris ;
- le groupe voit les agrégats : production, volume partagé, part de la consommation couverte ;
- un classement nominatif ou une courbe individuelle ne se montrent qu'avec l'accord explicite de la personne.

Une exception : quand il n'y a qu'un producteur, la production de la communauté est son injection, et tous la voient au moins en total. Mieux vaut le lui dire avant qu'il signe. [« Animer une communauté d'énergie au quotidien »](/guides/animer-communaute-energie/) donne des exemples de ce qu'on peut partager avec le groupe.

## Le port P1 : la mesure en temps réel, à côté des données officielles

Le compteur communicant a une seconde sortie, locale. Le décret lui impose de fournir des informations « en temps quasi réel », « exploitables sur un port de sortie » (article 35*bis*, § 1er) : c'est le port P1. En Wallonie, il est « désactivé par défaut » et s'active sur simple demande au GRD (article 35*bis*, § 4), gratuitement selon la grille des tarifs non périodiques harmonisés de 2026 ; notre [guide du compteur communicant](/guides/compteur-communicant-wallonie/) décrit les démarches. Le port suit la spécification belge eMUCS-P1, fondée sur la spécification néerlandaise DSMR 5.0.2 : un relevé chaque seconde, avec la puissance prélevée et injectée, la tension et le courant par phase, les index et la dernière valeur du compteur de gaz. Un quart d'heure de comptage officiel, ce sont **900 relevés** sur le port P1.

Pour une communauté, il a trois limites.

**Il ne montre que votre compteur.** Un consommateur y lit son prélèvement, un producteur son injection nette. Personne n'y voit la production de la toiture partagée, ni la part qui lui est allouée, qui n'existe qu'après le calcul du GRD.

**Il ne produit pas les volumes officiels.** Les volumes du partage sont ceux que le GRD « détermine » et transmet chaque mois ; la CWaPE rappelle que les factures du partage sont établies sur la base des données reçues du gestionnaire de réseau.

**Il fait de celui qui le lit un responsable de traitement.** Le tiers qui collecte des informations via le port « devient le responsable du traitement des données à caractère personnel pour les informations qu'il collecte » (article 35*septies*, § 3), et ORES prévient qu'une fois le port ouvert, il n'en contrôle plus les données. Une communauté qui distribue des boîtiers P1 et centralise leurs mesures doit obtenir l'accord préalable de chaque membre, l'informer de l'usage prévu et sécuriser ce qu'elle collecte.

Pour savoir en direct que la toiture commune produit, il faudrait réunir les mesures des producteurs et les diffuser au groupe, avec, de nouveau, l'accord de chacun. Chez OptimCE, une fonction de ce type est à l'étude ; elle n'est pas disponible aujourd'hui.

## Lire une courbe de charge

Une courbe de charge au quart d'heure, ce sont 96 valeurs par jour et par compteur. Prenons le cas qui alimente la grille de notre page d'accueil, et que reprend [« Tarif Impact et communauté d'énergie »](/guides/tarif-impact-communaute-energie/) : une toiture de 24 kWc à Namur, partagée entre douze ménages de 3 500 kWh par an.

<img src="/assets/images/diagrams/community-load-curve-day-fr.svg"
     alt="Graphique d'une journée de partage, le mardi 13 juin 2023, pour une communauté de référence : une toiture solaire de 24 kilowatts-crête à Namur et douze ménages qui consomment chacun 3 500 kilowattheures par an. L'axe horizontal couvre les 96 quarts d'heure de la journée, de 0 h à 24 h ; l'axe vertical donne l'énergie de chaque quart d'heure, de 0 à 5 kilowattheures. La production de la toiture, nulle la nuit, commence vers 5 h 15, culmine à 4,72 kilowattheures dans le quart d'heure de 13 h et s'éteint vers 22 h : 152,9 kilowattheures sur la journée. La consommation des douze ménages varie entre 0,68 et 1,73 kilowattheure par quart d'heure, avec une pointe vers 7 h 15 et une plus forte vers 18 h 45 : 93,9 kilowattheures. La zone verte, l'énergie partagée, vaut à chaque quart d'heure le plus petit des deux volumes : 50,6 kilowattheures. De 8 h 15 à 18 h 30, la production dépasse la consommation, et le surplus, 102,3 kilowattheures en ambre, part sur le réseau. Le matin et le soir, c'est l'inverse : le complément, 43,3 kilowattheures en gris, vient du fournisseur de chaque ménage. Trois repères marquent 7 h 00, 12 h 30 et 19 h 00, les quarts d'heure détaillés dans le tableau de l'article. Une note rappelle qu'un kilowattheure consommé en un quart d'heure correspond à 4 kilowatts de puissance moyenne. Sources : PVGIS pour la production, profil synthétique de consommation, qui n'est pas un profil Synergrid."
     width="800" height="520" loading="lazy" decoding="async"
     style="width:100%;height:auto">

**L'unité d'abord.** Chaque valeur est une énergie, en kilowattheures par quart d'heure, et non une puissance. Pour retrouver la puissance moyenne, on multiplie par quatre : à 12 h 30, la toiture produit 4,57 kWh en un quart d'heure, soit 18,3 kW en moyenne pour une installation de 24 kWc.

| Quart d'heure | Production | Consommation | Partagé | Surplus injecté | Complément fournisseurs |
|---|---|---|---|---|---|
| 7 h 00 – 7 h 15 | 0,24 | 1,10 | 0,24 | 0 | 0,86 |
| 12 h 30 – 12 h 45 | 4,57 | 0,99 | 0,99 | 3,58 | 0 |
| 19 h 00 – 19 h 15 | 0,90 | 1,73 | 0,90 | 0 | 0,83 |
| **Journée entière** | **152,9** | **93,9** | **50,6** | **102,3** | **43,3** |

*Hypothèses : valeurs en kWh pour les douze ménages ensemble. Toiture de 24 kWc plein sud, inclinée à 35°, à Namur, production PVGIS v5.3 (SARAH-3) avec la météo du 13 juin 2023 ; douze ménages de 3 500 kWh par an au profil synthétique, qui n'est pas un profil Synergrid. Le partagé est le plus petit des deux volumes à chaque quart d'heure, soit le maximum qu'une clé puisse répartir ; une clé fixe peut laisser un excédent chez un membre pendant qu'un autre manque.*

Le matin et le soir, tout ce que la toiture injecte est partagé ; à midi, les ménages n'en consomment qu'un cinquième. Sur la journée, le partage couvre 54 % de la consommation, mais deux tiers de la production ne trouvent pas preneur. Sur toute l'année 2023, la même communauté produit 24 812 kWh, en consomme 42 000 et en partage 12 624 : la moitié de la production (50,9 %) trouve preneur, et le partage couvre 30,1 % de la consommation.

### Lire la ligne d'un membre

Ici, les douze ménages ont le même profil. À 19 h 00, un membre prélève 0,144 kWh ; le partage lui en couvre 0,075, et les 0,069 kWh restants forment son alloconsommation. Dans le fichier de consommation d'ORES, ce sont les colonnes « Prélèvement brut », « Prélèvement couvert par le partage » et « Allo Consommation » : Pl = VPC + AL. Le représentant facture la somme mensuelle du prélèvement couvert par le partage ; le fournisseur facture l'alloconsommation, et, dans l'exemple du guide d'ORES, les frais de réseau sur tout le prélèvement.

### Quatre contrôles avant de facturer

- **Le nombre de lignes** : 96 par jour et par EAN, fois le nombre d'itérations. Horodaté en heure locale, le jour du passage à l'heure d'été compte 92 quarts d'heure, celui du retour 100.
- **L'égalité du membre** : prélèvement = partagé consommé + alloconsommation. Un écart trahit souvent une itération oubliée.
- **L'égalité du groupe** : la somme des partagés consommés ne dépasse jamais le volume partagé ; la différence est le surplus.
- **Les silences** : un membre absent, ou à zéro partout, signale un compteur qui ne remonte pas ses quarts d'heure. À vérifier avec le GRD avant de facturer.

## Bruxelles et la Flandre

**En Flandre**, Fluvius calcule le partage chaque mois à partir des valeurs au quart d'heure ; les résultats sont en général disponibles vers le 25 du mois suivant dans Mijn Fluvius, où le gestionnaire de la communauté télécharge un fichier CSV et où chaque participant ne voit que ses propres volumes. Le compteur digital doit être en « meetregime 3 ». Depuis 2026, Fluvius lit par défaut les valeurs au quart d'heure, mais ne les transmet au fournisseur qu'en cas, par exemple, de contrat dynamique ou de partage. Le régulateur est la Vlaamse Nutsregulator (anciennement VREG).

**À Bruxelles**, le règlement technique impose à Sibelga d'envoyer chaque mois à l'interlocuteur unique du partage les prélèvements, les injections, la consommation partagée de chaque participant et le surplus de chaque producteur, au quart d'heure ou en total mensuel (article 4.70) ; en pratique, un fichier Excel déposé dans un dossier en ligne privé. L'ordonnance électricité subordonne la collecte à distance au consentement de l'utilisateur (article 26*octies*, § 4), et le port P1 y est actif par défaut. Le régulateur est Brugel.

## Ce qu'il faut retenir

1. **Une communauté ne mesure rien elle-même.** Le GRD collecte les données, détermine les volumes partagés et les transmet au représentant et aux fournisseurs.
2. **Le rythme est mensuel** : au plus tard le douzième jour ouvrable du mois suivant, au quart d'heure et par EAN ; chez ORES, deux CSV par e-mail.
3. **Ce flux ne demande pas de consentement : il est la condition de la participation.** Le représentant devient responsable des données qu'il reçoit ; l'annexe 8 autorise l'envoi de la courbe au fournisseur.
4. **Tout le reste exige un accord préalable, libre, spécifique, éclairé et univoque** : historique pour simuler une clé, boîtier P1, courbes montrées aux autres.
5. **Chaque membre voit ses chiffres, le groupe voit les agrégats**, et la convention de chaque participant doit l'écrire.
6. **Le port P1 mesure chaque seconde, mais seulement votre compteur**, et celui qui collecte ses données en devient responsable.
7. **Une courbe se lit en kilowattheures par quart d'heure** : multipliez par quatre pour la puissance, et vérifiez que prélèvement = partagé consommé + alloconsommation.

> ### Testez une clé sur les courbes de vos membres
>
> OptimCE est une plateforme open source, en phase alpha, pensée pour gérer une communauté d'énergie. Sa fonctionnalité clé de répartition génère et simule une clé à partir d'un fichier CSV au quart d'heure, avec une colonne par consommateur et une pour la production : les courbes que vos membres ont exportées, avec leur accord. Elle travaille sur les fichiers que vous importez, pas en temps réel.
>
> **[Voir la fonctionnalité clé de répartition →](/fonctionnalites/cle-de-repartition/)**

## FAQ

### Quelles données de comptage le GRD transmet-il à une communauté d'énergie ?

En Wallonie, le gestionnaire de réseau envoie au représentant du partage, pour chaque membre et chaque quart d'heure, le prélèvement, le volume partagé consommé et l'alloconsommation, c'est-à-dire la part que le fournisseur facture. Il y ajoute l'injection de chaque producteur, le volume partagé total, le surplus et la méthode de répartition utilisée.

La convention type approuvée par la CWaPE le 12 octobre 2023 lui impose de mettre ces données à disposition chaque mois, au plus tard le douzième jour ouvrable du mois suivant ; c'est une obligation de moyens. Chez ORES, ce sont deux fichiers CSV envoyés par e-mail, avec une ligne par quart d'heure, par code EAN et par itération de la clé.

### Faut-il donner son consentement pour que ses données aillent à la communauté ?

Pour le flux du partage lui-même, non. Le décret wallon oblige le GRD à transmettre au représentant les données de mesure de chaque participant, et la convention type précise que toute participation requiert la collecte et l'utilisation des courbes de charge. On ne peut pas rester dans le partage et refuser ce flux. Le participant signe toutefois l'annexe 8, qui autorise notamment la transmission de sa courbe à son fournisseur.

Tout ce qui sort de ce cadre exige un accord préalable, libre, spécifique, éclairé et univoque : l'historique demandé pour simuler une clé, un boîtier sur le port P1, des courbes individuelles montrées aux autres membres.

### Les autres membres peuvent-ils voir ma consommation ?

Pas par défaut. Le GRD envoie les données de chaque membre au représentant, pas aux autres membres, et la convention de chaque participant doit régler la vie privée et la transmission de données entre participants. L'Autorité de protection des données rappelle qu'une courbe au quart d'heure permet d'inférer les comportements d'un ménage.

Une pratique prudente consiste à montrer à chaque membre ses propres chiffres, et au groupe les seuls agrégats. Un classement nominatif ou une courbe individuelle ne se montrent qu'avec l'accord explicite de la personne. Quand la communauté n'a qu'un producteur, sa production est, par construction, visible de tous en total.

### Comment accéder aux données de mon compteur communicant ?

Par le portail de votre gestionnaire de réseau, gratuitement. L'arrêté du 1er décembre 2022 impose vingt-quatre mois d'historique, le détail infrajournalier sur demande explicite et un export vers un tableur. Chez ORES, la vue au quart d'heure se demande dans l'espace client de myORES ; RESA propose un profil au quart d'heure dans MyRESA, l'AIEG et l'AIESH dans MyConso.

Ce sont aussi ces données qu'une communauté vous demandera pour simuler une clé avant le partage : vous pouvez les exporter et les lui confier, avec un accord écrit pour cet usage.

### Le port P1 peut-il servir au partage d'énergie ?

Pas pour le calcul. Le port P1 envoie un relevé par seconde, mais il ne montre que votre propre compteur : ni la production de la toiture partagée, ni la part qui vous est allouée. Les volumes du partage sont ceux que le GRD détermine et transmet chaque mois, et c'est sur eux que la facture est établie.

En Wallonie, le port est désactivé par défaut et s'active gratuitement sur simple demande au GRD. Celui qui collecte des données par ce port en devient responsable : une communauté qui distribue des boîtiers P1 doit recueillir l'accord préalable de chaque membre.

### Combien de temps les données de partage sont-elles conservées ?

En Wallonie, la CWaPE et le gestionnaire de réseau conservent les données liées au partage cinq ans après l'arrêt de l'activité. Celles d'un participant qui a quitté le partage sont supprimées cinq ans après la notification de sa sortie.

Le décret ne fixe pas de durée pour le représentant. Responsable du traitement des données qu'il reçoit, il doit en fixer une lui-même et l'annoncer aux membres, comme le RGPD l'exige. Le compteur, lui, garde lisibles à distance les courbes de charge des dix derniers jours, les index journaliers de quarante jours et les index mensuels de treize mois.

## Sources

- [Wallex — Décret du 12 avril 2001 relatif à l'organisation du marché régional de l'électricité, texte coordonné](https://wallex.wallonie.be/sites/wallex/contents/acts/19/19848.html) — source de la réservation au GRD de la collecte des données de comptage (article 11), du port de sortie en temps quasi réel désactivé par défaut (article 35*bis*, § 1er, § 2 et § 4), du régime de comptage par défaut et de la consultation gratuite (article 35*ter*, § 2 et § 3), du statut de responsable du traitement du GRD, de la règle de l'accord préalable, des interdictions de commerce et de la responsabilité du tiers qui lit le port (article 35*septies*, § 2 et § 3), du contenu imposé à la convention du participant (article 35*duodecies*, § 2), de la conservation de cinq ans (article 35*quaterdecies*, § 3) et des transmissions du GRD au représentant, aux fournisseurs et à la CWaPE (article 35*sexdecies*, § 2 et § 3). Consulté le 22 novembre 2026.
- [CWaPE — Décision CD-23j12-CWaPE-0818 approuvant les conventions types de partage](https://cwape.be/sites/default/files/cwape-documents/2023.10.12-0818-D%C3%A9cision%20approbation%20conventions-types%20partage%20-%20avec%20annexes.pdf) — décision du 12 octobre 2023, annexes comprises. Source de la définition des sept grandeurs et de leurs formules (article 6.2.1), du délai du douzième jour ouvrable et de l'obligation de moyens (article 6.2.2), de la collecte des courbes de charge comme condition de participation (article 6.1.3), du circuit des réclamations (article 6.1.4) et de la répartition des responsabilités de traitement (article 9.4). Consulté le 22 novembre 2026.
- [CWaPE — Guide explicatif du formulaire relatif au partage d'électricité](https://www.cwape.be/documents/download/5610) — version de juillet 2025. Source des conditions de comptage (fonction communicante activée, régime 3 demandé au fournisseur, autorisation de l'annexe 8, point 9.1) et de la déclaration de protection des données : base de l'article 6.1.e du RGPD, responsabilité conjointe des GRD et de la CWaPE, conservation de cinq ans. Consulté le 22 novembre 2026.
- [CWaPE — Annexe 8 : déclaration sur l'honneur des personnes prenant part au partage](https://www.cwape.be/documents/download/5612) — version du 12 octobre 2023. Source du mandat donné au représentant et de l'autorisation de transmettre au fournisseur les données de comptage quart-horaire en attendant le régime 3. Consulté le 22 novembre 2026.
- [CWaPE — Rapport d'évaluation des communautés d'énergie et du partage (CD-25b20-CWaPE-0109)](https://www.cwape.be/sites/default/files/cwape-documents/2025.02.20-0109-Rapport%20%C3%A9valuation%20CE%20et%20partage.pdf) — rapport du 20 février 2025. Source du rythme actuel (mois écoulé plus douze jours ouvrables au maximum) et du canal distinct, hors processus de marché, par lequel les volumes partagés parviennent aux fournisseurs. Consulté le 22 novembre 2026.
- [CWaPE — Décision CD-26h27-CWaPE-1284 approuvant le règlement technique distribution électricité](https://www.cwape.be/sites/default/files/cwape-documents/CD-26h27-CWaPE-1284-D%C3%A9cision%20d%27approbation%20du%20RTDE%20%26%20annexes_site.pdf) — décision du 27 août 2026. Source des articles IX.6 (passage au MIG « dès que le MIG le permettra »), IX.7 (courbe quart-horaire et agrégat mensuel, interface de programmation) et IX.17 (rectifications sur douze mois et leur répartition). Son statut, « en préparation » de publication au Moniteur belge, vient de la page [Règlements et contrats](https://www.cwape.be/node/161). Consultés le 22 novembre 2026.
- [CWaPE — Qui facture l'électricité partagée ?](https://www.cwape.be/node/6059) — question de la FAQ du régulateur, source du principe selon lequel les factures du partage sont établies sur la base des données de consommation reçues du gestionnaire de réseau. Consulté le 22 novembre 2026.
- [Wallex — Arrêté du Gouvernement wallon du 1er décembre 2022 relatif aux compteurs communicants](https://wallex.wallonie.be/eli/arrete/2022/12/01/2022034594) — article 4, source du contenu minimal du portail : vingt-quatre mois, détail infrajournalier sur demande explicite, export vers un tableur. Consulté le 22 novembre 2026.
- [ORES — Guide explicatif de la facturation pour le représentant d'un partage d'énergie](https://media.ores.be/ores-cms/vi2eqxam/ores_guide_explicatif_facturation_representant_partage_energie_fr.pdf) — guide de juillet 2024. Source de la description des deux fichiers CSV, du nom des colonnes, de la ligne par itération, de la somme des itérations par EAN et par période, et de l'exemple où le fournisseur facture les frais de réseau sur tout le prélèvement. Consulté le 22 novembre 2026.
- [ORES — Le partage d'énergie en pratique](https://www.ores.be/particulier/en-pratique) — source de l'envoi mensuel des deux CSV par e-mail, et de la précision selon laquelle les données de la vue au quart d'heure de myORES « ne remonteront pas » vers le fournisseur, qui doit les demander lui-même à ORES. Consulté le 22 novembre 2026.
- [ORES — FAQ myORES](https://www.ores.be/faq/myores) — source de la transmission au fournisseur de l'activation de la vue au quart d'heure, de la facture intermédiaire qu'elle peut entraîner chez certains fournisseurs, et de son absence d'effet sur la facture annuelle de régularisation et la compensation. Consulté le 22 novembre 2026.
- [ORES — Le partage de données avec les fournisseurs de services énergétiques (API)](https://media.ores.be/ores-cms/ahgjzcld/utilisation-des-api-tpda-ores.pdf) — document de septembre 2025. Source de l'accès délégué : volumes journaliers et quart-horaires, historique de trois ans au maximum, consentement donné par le client dans myORES. Consulté le 22 novembre 2026.
- [CWaPE — Annexe TNP-E0 : tarifs non périodiques 2026, électricité, tarifs harmonisés](https://www.cwape.be/sites/default/files/cwape-documents/ANNEXE%20TNP-E0%20-%20Tarifs%20non-p%C3%A9riodiques%202026%20-%20Electricit%C3%A9%20-%20Tarifs%20harmonis%C3%A9s%20et%20uniformis%C3%A9s.pdf) — source de la gratuité de l'activation et de la désactivation du port P1 en 2026. Consulté le 22 novembre 2026.
- [Fluvius — Digital Metering System eMUCS-P1, version 2.1](https://partner.fluvius.be/sites/fluvius/files/2025-09/digital-metering-system-emucs-p1-v2-1.pdf) — spécification belge du port P1, fondée sur DSMR 5.0.2 : télégramme mis à jour chaque seconde et liste des valeurs publiées. Consulté le 22 novembre 2026.
- [Commission de la protection de la vie privée — Avis n° 23/2018](https://www.autoriteprotectiondonnees.be/publications/avis-n-23-2018.pdf) — avis du 21 mars 2018, publié sur le site de l'Autorité de protection des données qui a succédé à la Commission, sur l'avant-projet de décret relatif aux compteurs intelligents, source de la phrase sur le « consentement » par clause de conditions générales. Consulté le 22 novembre 2026.
- [Autorité de protection des données — Avis n° 132/2023](https://www.autoriteprotectiondonnees.be/publications/avis-n-132-2023.pdf) — avis du 8 septembre 2023, source de la citation sur les données potentiellement sensibles qu'on peut inférer des compteurs communicants. Consulté le 22 novembre 2026.
- [Autorité de protection des données — Avis n° 130/2025](https://www.autoriteprotectiondonnees.be/publications/avis-n0-130-2025.pdf) — avis du 3 décembre 2025, source de la règle bruxelloise actuelle : l'article 26*octies*, § 4 de l'ordonnance électricité subordonne la collecte à distance au consentement de l'utilisateur. Consulté le 22 novembre 2026.
- [EUR-Lex — Règlement (UE) 2016/679 (RGPD)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — articles 5, § 1, c (minimisation), 6, § 1, e (mission d'intérêt public), 7, § 3 (retrait du consentement) et 28 (sous-traitant). Consulté le 22 novembre 2026.
- [EUR-Lex — Directive (UE) 2019/944](https://eur-lex.europa.eu/eli/dir/2019/944/oj) — article 20, source de l'accès du client, sans frais supplémentaires, à ses données non validées en quasi-temps réel. Consulté le 22 novembre 2026.
- [EUR-Lex — Règlement d'exécution (UE) 2023/1162](https://eur-lex.europa.eu/eli/reg_impl/2023/1162/oj) — article 2, définitions de la partie admissible, qui inclut les communautés d'énergie renouvelable et les communautés énergétiques citoyennes, et de l'autorisation donnée par le client. Consulté le 22 novembre 2026.
- [Fluvius — Questions fréquentes sur le partage d'énergie](https://www.fluvius.be/nl/veelgestelde-vragen/energiedelen-persoon-aan-persoonverkoop-energiegemeenschappen) — en néerlandais. Source du calcul mensuel, de la disponibilité des résultats vers le 25 du mois suivant dans Mijn Fluvius, et de l'exigence du « meetregime 3 ». Consulté le 22 novembre 2026.
- [Fluvius — Kwartierwaarden](https://www.fluvius.be/nl/factuur-en-tarieven/kwartierwaarden) — en néerlandais. Source de la lecture par défaut des valeurs au quart d'heure depuis 2026 et de leur transmission au fournisseur seulement en cas de contrat dynamique ou de partage. Consulté le 22 novembre 2026.
- [Fluvius — Protocol energiedelen, persoon-aan-persoonverkoop en verkoop in gebouwen, version 3.2](https://www.fluvius.be/sites/fluvius/files/2024-07/protocol-energiedelen-p2p-verkoop-in-gebouwen-v3-2.pdf) — en néerlandais. Source des options de téléchargement du fichier CSV pour le gestionnaire et de la visibilité limitée de chaque participant à ses propres volumes. Consulté le 22 novembre 2026.
- [Brugel — Règlements techniques électricité et gaz, version au 1er janvier 2025](https://brugel.brussels/publication/document/notype/2024/fr/Reglements-techniques-2025.pdf) — article 4.70, source des données que Sibelga transmet chaque mois à l'interlocuteur unique d'un partage. Consulté le 22 novembre 2026.
- [Sibelga — Méthode de facturation du partage d'énergie](https://www.sibelga.be/fr/raccordements-compteurs/energie-renouvelable/partage-energie/methode-de-facturation) et [Le port P1 du compteur intelligent](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents/le-port-p1-du-compteur-intelligent) — source du fichier Excel mensuel déposé dans un dossier en ligne, de l'option quart-horaire et du port P1 actif par défaut à Bruxelles. Consultés le 22 novembre 2026.
- [JRC — PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/fr/) — outil de la Commission européenne d'où viennent les valeurs de production du cas de référence (version 5.3, base SARAH-3, météo 2023). Le profil de consommation est synthétique et documenté dans le code source du site, qui n'est pas un profil Synergrid. Consulté le 22 novembre 2026.
