---
layout: post
title: "Compteur communicant en Wallonie : le guide"
date: 2026-11-02 06:00:00 +0100
author: "Eric d'OptimCE"
excerpt: "Depuis janvier 2026, chaque point de fourniture wallon doit recevoir un compteur communicant d'ici fin 2029, et la pose ne se refuse plus. Ce guide dit comment le demander sans attendre chez chacun des cinq gestionnaires de réseau, ce qu'il coûte, ce que coûte la désactivation de sa communication, et ce qu'il ouvre : le tarif Impact, le port P1, vos données au quart d'heure et le partage d'énergie."
description: "Compteur communicant en Wallonie : qui le reçoit, comment le demander à votre GRD, ce qu'il coûte, comment le désactiver et ce qu'il permet."
tags: [guide, community]
lang: fr
ref: smart-meter-wallonia
pillar: reseau-grd
last_modified_at: 2026-11-06
permalink: /guides/compteur-communicant-wallonie/
faq:
  - q: "Comment demander un compteur communicant en Wallonie ?"
    a: "Adressez la demande à votre gestionnaire de réseau de distribution, pas à votre fournisseur. ORES propose un formulaire en ligne de remplacement par un compteur communicant ; RESA a une rubrique « Demander un compteur communicant » sur son site ; l'AIEG demande d'utiliser son formulaire de demande en précisant en remarque que vous souhaitez un compteur communicant. Pour l'AIESH et la REW, aucune procédure n'est décrite en ligne : contactez leur service clientèle. L'arrêté du Gouvernement wallon du 1er décembre 2022 encadre la suite : accusé de réception dans les dix jours, offre dans les dix jours suivants, et placement au plus tard quatre mois après la demande complète. Le remplacement d'un compteur classique est gratuit dans les cinq réseaux wallons."
  - q: "Le compteur communicant est-il obligatoire en Wallonie ?"
    a: "Oui, pour la pose. Depuis le décret du 19 décembre 2025, en vigueur le 9 janvier 2026, le gestionnaire de réseau installe un compteur qui communique à chaque point de fourniture, sauf accès impossible, impossibilité technique ou coût non économiquement raisonnable, et doit atteindre 100 % de compteurs communicants sur son réseau au 31 décembre 2029. ORES, RESA et la REW écrivent qu'il n'est plus possible de refuser le remplacement. Ce qui reste un choix, c'est la fonction communicante : vous pouvez refuser son activation ou en demander la désactivation, avec des conséquences que le décret énumère."
  - q: "Peut-on désactiver la fonction communicante, et combien cela coûte-t-il ?"
    a: "Oui, sur demande au gestionnaire de réseau. La désactivation est gratuite si vous la demandez dans les quinze jours calendrier qui suivent la pose ; au-delà, elle coûte 128,33 euros hors TVA en 2026, un tarif identique chez les cinq gestionnaires wallons. La réactivation est gratuite. Chez RESA, la demande se fait par formulaire, à envoyer à desacom@resa.be, et ne peut pas être faite sur place le jour de la pose. Les conséquences sont lourdes : relevé manuel des index, aucun partage d'énergie ni échange de pair-à-pair, pas de prépaiement, pas de services de flexibilité, et une demande d'indemnisation pour décrochage d'onduleur devient irrecevable. Une personne qui a acquis une installation de production de 10 kVA ou moins depuis le 1er janvier 2024 peut seulement refuser l'activation."
  - q: "Comment activer le port P1 de mon compteur communicant ?"
    a: "En Wallonie, le port de sortie du compteur est désactivé par défaut et s'active sur simple demande au gestionnaire de réseau. L'activation est gratuite : les grilles tarifaires 2026 classent l'activation et la désactivation du port P1 parmi les téléopérations, gratuites et harmonisées dans toute la Wallonie. Chez ORES, la demande se fait par téléphone au 078/15.78.01, le port n'est activé qu'avec votre autorisation explicite et se raccorde par un câble RJ12. RESA, l'AIEG, l'AIESH et la REW passent par un formulaire. Selon la spécification belge des compteurs, le port P1 fournit des valeurs instantanées chaque seconde ; il faut ensuite un module ou une application pour les lire."
  - q: "Faut-il un compteur communicant pour le tarif Impact ?"
    a: "Oui. La CWaPE réserve le tarif Impact aux raccordements de 56 kVA ou moins équipés d'un compteur communicant dont la fonction communicante est active. Il n'est pas automatique : vous le demandez à votre fournisseur. La CWaPE a refusé d'imposer le régime de comptage au quart d'heure (R3) pour ce tarif, qui doit fonctionner aussi en régime R1, mais certains fournisseurs l'exigent dans leurs conditions. Un compteur dont la fonction communicante est désactivée exclut donc le tarif Impact."
  - q: "Faut-il un compteur communicant pour rejoindre une communauté d'énergie ?"
    a: "Il faut un compteur qui mesure séparément le prélèvement et l'injection et transmet les données par quart d'heure : le décret électricité l'impose à chaque participant à un partage. Pour un ménage, c'est en pratique le compteur communicant ; ORES accepte aussi un compteur AMR, réservé en général aux raccordements plus puissants. Il faut en plus que la fonction communicante soit active et que vos données soient transmises au quart d'heure, le régime R3, que vous demandez à votre fournisseur. Si vous n'avez pas encore de compteur communicant, demandez-le à votre gestionnaire de réseau : le remplacement est gratuit et doit intervenir dans les quatre mois."
---

En Wallonie, le compteur communicant doit équiper tous les logements d'ici fin 2029. La pose ne se refuse plus depuis janvier 2026, mais sa communication peut être coupée, et ce choix ferme plusieurs portes. Ce guide répond à trois questions pratiques : quand vous le recevrez, comment le demander plus tôt, et ce qu'il coûte. Il dit aussi ce qu'il permet de faire, et pourquoi le partage d'énergie n'existe pas sans lui.

Cet article ne refait pas ce qui est déjà écrit ailleurs sur ce site. Le calcul du tarif Impact pour un membre de communauté est dans [« Tarif Impact et communauté d'énergie »](/guides/tarif-impact-communaute-energie/), et la règle du quart d'heure dans [« Électricité en circuit court : le mode d'emploi »](/guides/electricite-circuit-court-mode-emploi/). Le contrat dynamique, qui suppose lui aussi ce compteur, est traité dans [« Quel tarif d'électricité choisir en Belgique ? »](/guides/quel-tarif-electricite-choisir-belgique/).

**Les règles décrites sont wallonnes.** Bruxelles et la Flandre sont résumées à la fin.

## Ce qu'est un compteur communicant, et ce qu'il n'est pas

Un compteur communicant est un compteur électronique « double flux » : il mesure séparément l'électricité que vous prélevez sur le réseau et celle que vous y injectez. Il enregistre ces données par plage horaire et peut les transmettre à distance au gestionnaire de réseau de distribution (GRD).

Il faut distinguer deux choses que le langage courant confond :

- **le compteur**, qui mesure et affiche ;
- **sa fonction communicante**, qui transmet les données à distance. Elle est activée à la pose, mais vous pouvez la refuser ou la faire désactiver (voir plus bas).

Et même quand la communication est active, le compteur n'envoie pas tout au marché. Le décret électricité est clair : par défaut, « seuls les index du compteur et les volumes d'énergie sont utilisés dans les processus de marché », et leur transmission aux fournisseurs « est effectuée sur base annuelle » (article 35*ter*, § 2). Votre courbe de consommation au quart d'heure ne quitte le gestionnaire de réseau que si vous le demandez.

Le règlement technique approuvé par la CWaPE le 27 août 2026 nomme ces niveaux des « régimes de comptage » :

| Régime | Quand il s'applique | Ce que le GRD transmet au marché |
|---|---|---|
| R0 | fonction communicante désactivée | rien à distance : les index sont relevés sur place |
| R1 | par défaut, communication active | index de début et de fin, volumes par plage horaire ; une fois par an, ou chaque mois à votre demande |
| R3 | sur demande explicite, via votre fournisseur | en plus, la courbe de charge au quart d'heure, au moins chaque mois |

*Hypothèses : règlement technique pour la gestion des réseaux de distribution d'électricité en Wallonie, article V.45bis, dans la version approuvée par la CWaPE le 27 août 2026. Le R3 est aussi appelé SMR3 par les fournisseurs ; il est obligatoire pour une offre à prix dynamique et pour le partage d'énergie.*

Un compteur communicant n'est pas non plus le seul compteur « intelligent ». Les raccordements plus puissants ont souvent un compteur AMR, télérelevé au quart d'heure, que les règles du partage acceptent aussi. Pour un ménage, le compteur communicant est la voie normale.

## Qui en reçoit un, et quand

Jusqu'en 2025, le déploiement wallon visait des publics prioritaires. Le décret du 19 décembre 2025, en vigueur depuis le 9 janvier 2026, a supprimé cette logique. L'article 35 du décret électricité dit désormais que le gestionnaire de réseau « installe un compteur qui communique à chaque point de fourniture », sauf si l'accès est impossible, si l'installation est techniquement impossible ou si elle n'est pas économiquement raisonnable. Il fixe l'échéance : « au plus tard au 31 décembre 2029 », 100 % de compteurs communicants sur chaque réseau.

Il n'y a donc plus d'ordre légal entre les ménages : chaque GRD planifie le remplacement dans son plan d'adaptation, en général commune par commune. ORES et RESA permettent de consulter la date prévue en ligne, ORES sur sa page « Placement du compteur », RESA à partir de votre code EAN. Trois situations accélèrent les choses :

- **Une nouvelle installation de production de 10 kVA ou moins.** Depuis le 1er janvier 2024, la pose d'un compteur communicant est systématique à sa mise en service, comme l'explique [notre guide sur le solaire pour les locataires](/guides/guide-solaire-locataire-sans-toit/).
- **Le prépaiement.** Les anciens compteurs à budget à carte ont été remplacés par des compteurs communicants avec fonction de prépaiement, la plateforme de rechargement des cartes ayant pris fin le 1er janvier 2026. Fin 2025, 98,8 % des 59 294 compteurs à prépaiement actifs en électricité étaient communicants ; il en restait quelques-uns à remplacer chez RESA (CWaPE, rapport sur les obligations de service public 2025).
- **Votre demande.** Vous n'êtes pas obligé d'attendre votre tour (section suivante).

Où en est le déploiement ? Fin 2025, plus de 537 000 compteurs électriques communicants étaient placés sur les réseaux wallons, soit environ 28 % du parc (CWaPE, rapport annuel général 2025). Il en reste donc plus de deux sur trois à poser en quatre ans. Par gestionnaire, seul RESA publie un chiffre récent : « près de 84.862 » compteurs fin 2024, soit 18,42 % de son parc (rapport annuel 2024). L'AIEG, l'AIESH et la REW ne publient pas de décompte propre.

## Demander un compteur communicant : procédure et coût par GRD

Vous pouvez demander un compteur communicant sans attendre le planning. L'arrêté du Gouvernement wallon du 1er décembre 2022 fixe la procédure : le GRD accuse réception dans les dix jours, envoie une offre dans les dix jours suivants (date estimée, fonctions du compteur, coût éventuel), et le placement « n'excède pas quatre mois après la demande complète » (article 2, § 1er à § 3).

La demande se fait auprès du gestionnaire de réseau, jamais du fournisseur. **Vérifiez d'abord quel est le vôtre** : [l'outil « Quel est mon GRD ? »](/outils/quel-est-mon-grd/) le trouve à partir de votre code postal, et [la liste par commune](/outils/quel-est-mon-grd/communes/) couvre les 565 communes belges.

| GRD | Demander un compteur communicant | Activer le port P1 | Désactiver la communication après 15 jours |
|---|---|---|---|
| ORES | formulaire en ligne « compteur intelligent » ; date prévue sur la page « Placement du compteur » | par téléphone, 078/15.78.01 ; gratuit | 128,33 € HTVA |
| RESA | rubrique « Demander un compteur communicant » ; date prévue à partir du code EAN | formulaire « port client » ; gratuit | formulaire à desacom@resa.be ; 128,33 € HTVA |
| AIEG | formulaire de demande, en précisant en remarque « compteur communicant » | formulaire à envoyer à stech@aieg.be ; gratuit | 128,33 € HTVA |
| AIESH | aucune procédure en ligne : service clientèle, 060/45.91.60 | formulaire « Activation/désactivation port P1 » ; gratuit | 128,33 € HTVA |
| REW | aucune procédure en ligne : service clientèle | formulaire d'activation ; gratuit | 128,33 € HTVA |

*Hypothèses : procédures relevées sur les sites des cinq GRD le 2 novembre 2026. Montants des tarifs non périodiques 2026 approuvés par la CWaPE (ORES, RESA, AIESH, REW) et de la grille harmonisée et uniformisée en Wallonie (AIEG). Le remplacement d'un compteur classique par un compteur communicant est gratuit partout ; des travaux complémentaires (déplacement du compteur, hausse de puissance) restent facturés sur devis.*

Deux précisions sur le coût. Le compteur lui-même est « à charge du gestionnaire de réseau de distribution, qui en est le propriétaire » (même arrêté, article 2, § 5). La CWaPE le confirme dans son rapport annuel 2025 : en basse tension, le remplacement d'un type de compteur par un autre « est devenu gratuit, comme toutes les opérations réalisées à distance et l'activation de la fonction communicante ». ORES précise que le coffret et la borne interruptible posés avec le compteur sont eux aussi gratuits.

## Compteur communicant obligatoire : peut-on refuser ?

**La pose, non.** ORES l'écrit sans détour : « il n'est donc plus possible de refuser la pose du compteur communicant ». RESA et la REW disent la même chose.

**La communication, oui.** Le décret prévoit que l'utilisateur du réseau « peut refuser l'activation de la fonction communicante du compteur ou demander la désactivation de celle-ci » (article 35, § 3). La désactivation est gratuite si vous la demandez dans les quinze jours calendrier qui suivent la pose. Au-delà, elle coûte 128,33 € HTVA en 2026, le même montant chez les cinq GRD. La réactivation est gratuite. Chez RESA, la désactivation « ne peut être réalisée sur place lors de la pose » : il faut renvoyer le formulaire.

Une exception : si vous avez mis en service une installation de production de 10 kVA ou moins depuis le 1er janvier 2024, vous pouvez « uniquement refuser l'activation » (arrêté du 1er décembre 2022, article 3, § 1er).

Le GRD doit vous informer des conséquences, que le décret énumère :

1. le relevé manuel de vos index quand un processus de marché le nécessite ;
2. l'impossibilité technique de participer à un partage d'énergie ;
3. l'impossibilité technique de participer à un échange de pair-à-pair ;
4. l'impossibilité de fournir des services de flexibilité au réseau ;
5. l'impossibilité de toute autre activité de marché qui exige une transmission quotidienne des données ;
6. l'impossibilité d'activer le prépaiement ;
7. l'irrecevabilité d'une demande d'indemnisation pour décrochage de votre onduleur, faute de pouvoir vérifier la qualité de la tension.

RESA ajoute, pour un prosumer encore sous compensation, qu'une désactivation entraîne une facture intermédiaire à la date de coupure : la compensation annuelle se fait alors en deux périodes. Le port P1 est désactivé lui aussi.

Si votre crainte porte sur la vie privée, il existe une voie intermédiaire : garder la communication active, en régime R1. Le GRD ne transmet alors au marché que vos index et vos volumes, une fois par an, et rien au quart d'heure sans votre demande. Un tiers ne peut lire vos données qu'avec votre « accord préalable, libre, spécifique, éclairé et univoque » (décret électricité, article 35*septies*, § 3).

## Ce qu'il permet

### Le tarif Impact

Le [tarif Impact](/guides/tarif-impact-communaute-energie/), en vigueur depuis le 1er janvier 2026, facture le réseau selon trois plages horaires. La CWaPE le réserve aux clients qui ont « un compteur communicant avec fonction de communication active, avec une puissance de raccordement au réseau inférieure ou égale à 56 kVA ». Il n'est pas automatique : vous le demandez à votre fournisseur.

La CWaPE a refusé d'imposer le régime R3 pour ce tarif : il doit pouvoir fonctionner « tant en régime de comptage R1 qu'en régime de comptage R3 » (dossier de presse du 3 novembre 2025). Certains fournisseurs exigent pourtant le R3 dans leurs conditions. Lisez celles de votre offre avant de demander le changement.

### Vos données, gratuitement

Le gestionnaire de réseau doit permettre « la consultation libre et gratuite » de vos données de consommation (décret, article 35*ter*, § 3). Sa plateforme les montre par année, mois, semaine et jour, et, « sur demande explicite », par quart d'heure, sur les vingt-quatre derniers mois, avec un export tableur (arrêté du 1er décembre 2022, article 4).

En pratique :

- **chez ORES**, l'espace myORES affiche les données de la veille, avec un délai d'environ 72 heures ; la vue au quart d'heure s'active dans le portail, et cette activation « est transmise à votre fournisseur d'énergie », qui peut émettre une facture intermédiaire ;
- **chez RESA**, l'espace MyRESA affiche votre profil de prélèvement et d'injection « ¼ h par ¼ h » ;
- **à l'AIESH**, c'est la plateforme MyConso d'Arewal.

Ces données suffisent à voir à quelle heure part votre consommation, et donc ce qu'un déplacement d'usage ou un partage changerait.

### Le port P1

Le compteur fournit aussi des informations en temps quasi réel sur un « port de sortie » local, le port P1. Il est « désactivé par défaut » et s'active « sur simple demande de l'utilisateur au gestionnaire de réseau » (décret, article 35*bis*, § 4). Son activation est gratuite chez les cinq GRD. Chez ORES, il n'est activé qu'« après avoir reçu votre autorisation explicite », et il se raccorde « via un câble RJ12 ».

La spécification belge des compteurs (eMUCs-P1) indique que le port P1 « provides every second instantaneous values ». Selon Sibelga, il « ne communique que localement ». Pour l'exploiter, il faut un module P1 ou un gestionnaire d'énergie qui lit ces valeurs et, par exemple, lance un appareil quand vos panneaux injectent. C'est un usage local et privé : les données ne sortent de chez vous que si vous branchez un appareil connecté à internet.

## Pourquoi le partage d'énergie l'exige

Le partage d'énergie répartit, quart d'heure par quart d'heure, l'électricité injectée par une installation entre les participants. Le règlement technique le dit : la répartition « est réalisée sur une base quart horaire » (article IX.14). Pour faire ce calcul, le gestionnaire de réseau a besoin de la consommation de chaque participant à ce pas de temps. C'est pourquoi le décret électricité impose à chaque participant un compteur qui « mesure de manière distincte l'énergie prélevée et injectée » et « transmet les données agrégées par période de règlement des déséquilibres », c'est-à-dire par quart d'heure (article 35*octies*, § 3). La règle vaut pour le partage dans un même bâtiment (article 35*nonies*) comme pour les communautés d'énergie (article 35*quaterdecies*).

Concrètement, trois conditions :

1. **un compteur communicant**, ou un compteur AMR : ORES écrit qu'« un compteur double flux (compteur communicant ou compteur AMR) doit être installé chez tous les participants » ;
2. **la fonction communicante active** : la désactiver rend le partage « techniquement impossible » (décret, article 35, § 3) ;
3. **le régime R3**, que les participants activent « en faisant la demande à leur fournisseur d'énergie » (ORES). Le règlement technique le rend obligatoire pour le partage.

Si vous voulez rejoindre une communauté et n'avez pas encore de compteur communicant, faites la demande à votre GRD dès que le projet se précise : c'est le délai le plus long, jusqu'à quatre mois. La suite des démarches est dans [« Rejoindre une communauté d'énergie en Wallonie »](/guides/rejoindre-communaute-energie-wallonie/), et les formes de partage dans [« Autoconsommation collective en Belgique »](/guides/autoconsommation-energie-belgique/).

Le compteur ne fait qu'ouvrir la porte. Le partage ne réduit que la composante énergie des kilowattheures partagés : le réseau, les taxes et les surcharges restent dus sur tout votre prélèvement, à la seule exception de la réduction accordée au partage au sein d'un même bâtiment.

## Bruxelles et la Flandre

**À Bruxelles**, Sibelga a lancé le déploiement à grande échelle en octobre 2023 et vise 80 % des compteurs d'électricité remplacés d'ici 2030. Le remplacement est gratuit, et vous pouvez demander un compteur intelligent sans attendre le planning. Certains cas imposent de le demander vous-même : production (panneaux solaires), borne de recharge, batterie et partage d'énergie. Le port P1 y est « activé par défaut » ([Sibelga](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents/quand-recevrai-je-un-compteur-intelligent)).

**En Flandre**, le compteur digital est obligatoire : « je kan de plaatsing van een digitale meter niet weigeren ». Un refus peut mener à une procédure, avec des frais de mise en demeure de 298,76 €, puis de 322,59 € ([Fluvius](https://www.fluvius.be/nl/meters-en-meterstanden/digitale-meter/weigeren)). Le port P1 s'active en ligne sur Mijn Fluvius, en 72 heures au plus.

## Ce qu'il faut retenir

1. **Chaque point de fourniture wallon doit avoir un compteur communicant au 31 décembre 2029** ; il n'y a plus de publics prioritaires depuis le décret du 19 décembre 2025.
2. **La pose ne se refuse plus ; la communication, oui** : gratuitement dans les quinze jours, puis pour 128,33 € HTVA en 2026, avec des conséquences listées par le décret.
3. **Vous pouvez le demander sans attendre** à votre GRD : remplacement gratuit, placement en quatre mois au plus.
4. **Par défaut, seuls vos index partent chez le fournisseur, une fois par an** ; le quart d'heure (R3) se demande explicitement.
5. **Le port P1 est gratuit** et donne vos valeurs chaque seconde, chez vous, sans les envoyer au réseau.
6. **Pas de partage d'énergie sans compteur communicant actif en régime R3** (ou compteur AMR) ; pas de tarif Impact sans communication active.

## FAQ

### Comment demander un compteur communicant en Wallonie ?

Auprès de votre gestionnaire de réseau : formulaire en ligne chez ORES, rubrique dédiée chez RESA, formulaire avec une remarque à l'AIEG, service clientèle à l'AIESH et à la REW. Le remplacement est gratuit et doit intervenir au plus tard quatre mois après la demande complète.

### Le compteur communicant est-il obligatoire en Wallonie ?

La pose, oui : le GRD doit en installer un à chaque point de fourniture d'ici fin 2029, et la pose ne se refuse plus. Vous pouvez en revanche refuser ou faire désactiver sa fonction communicante.

### Peut-on désactiver la fonction communicante, et combien cela coûte-t-il ?

Oui. C'est gratuit dans les quinze jours qui suivent la pose, puis 128,33 € HTVA en 2026 ; la réactivation est gratuite. Sans communication, plus de partage d'énergie, de prépaiement ni de tarif Impact, et les index se relèvent à la main.

### Comment activer le port P1 de mon compteur communicant ?

Demandez-le à votre GRD : par téléphone chez ORES (078/15.78.01), par formulaire chez les autres. C'est gratuit. Il faut ensuite un module P1 ou un gestionnaire d'énergie, raccordé par un câble RJ12.

### Faut-il un compteur communicant pour le tarif Impact ?

Oui, avec la fonction communicante active et un raccordement de 56 kVA au plus. Le tarif se demande au fournisseur ; la CWaPE n'impose pas le régime R3, mais certains fournisseurs l'exigent.

### Faut-il un compteur communicant pour rejoindre une communauté d'énergie ?

Oui, ou un compteur AMR, avec la communication active et le régime R3 demandé à votre fournisseur. Sans compteur communicant, demandez-le à votre GRD dès le début du projet.

## Sources

- [Wallex — Décret du 12 avril 2001 relatif à l'organisation du marché régional de l'électricité, version consolidée](https://wallex.wallonie.be/eli/loi-decret/2001/04/12/2001027238) — article 35, § 1er (installation à chaque point de fourniture, exceptions, 100 % au 31 décembre 2029, rédaction du décret du 19 décembre 2025) et § 3 (refus ou désactivation de la fonction communicante et ses sept conséquences), article 35*bis*, § 1er et § 4 (informations en temps quasi réel, port de sortie désactivé par défaut), article 35*ter*, § 2 et § 3 (régime de comptage par défaut, transmission annuelle, consultation libre et gratuite), article 35*septies*, § 3 (accord préalable pour l'accès des tiers), articles 35*octies*, § 3, 35*nonies* et 35*quaterdecies* (compteur exigé pour le partage). Version en vigueur au 2 novembre 2026, consultée le 2 novembre 2026.
- [Wallex — Décret du 19 décembre 2025 portant dispositions diverses en matière d'énergie](https://wallex.wallonie.be/files/pdfs/22/124958_D%C3%A9cret_portant_dispositions_diverses_en_mati%C3%A8re_d'%C3%A9nergie_09-01-2026-.pdf) — article 26, réécriture de l'article 35 du décret électricité, en vigueur le 9 janvier 2026. Consulté le 2 novembre 2026.
- [Wallex — Arrêté du Gouvernement wallon du 1er décembre 2022 relatif aux compteurs communicants](https://wallex.wallonie.be/eli/arrete/2022/12/01/2022034594) — article 2 (demande, accusé de réception, offre, placement en quatre mois, coût du compteur à charge du GRD), article 3, § 1er (producteur de 10 kVA ou moins depuis le 1er janvier 2024), article 4 (plateforme de consultation, vingt-quatre mois, export). Consulté le 2 novembre 2026.
- [CWaPE — Décision CD-26h27-CWaPE-1284 d'approbation du règlement technique pour la gestion des réseaux de distribution d'électricité en Région wallonne](https://www.cwape.be/sites/default/files/cwape-documents/CD-26h27-CWaPE-1284-D%C3%A9cision%20d%27approbation%20du%20RTDE%20%26%20annexes_site.pdf) — article V.45*bis* (régimes R0, R1, R3 ; R3 obligatoire pour le partage et les offres à prix dynamique), article IX.14 (répartition sur une base quart-horaire). Document du 27 août 2026, consulté le 2 novembre 2026.
- [CWaPE — Rapport annuel général 2025](https://www.cwape.be/sites/default/files/cwape-documents/2026.07.03-RAG%202025.pdf) — plus de 537 000 compteurs électriques communicants fin 2025, environ 28 % du parc ; gratuité du remplacement de compteur, des téléopérations et de l'activation ; désactivation tarifée plus de deux semaines après la pose. Rapport du 3 juillet 2026, consulté le 2 novembre 2026.
- [CWaPE — Rapport annuel spécifique 2025 sur les obligations de service public](https://www.cwape.be/sites/default/files/cwape-documents/2026.07.03-RAS%20OSP%202025.pdf) — fin des compteurs à budget au 1er janvier 2026, 59 294 compteurs à prépaiement actifs dont 98,8 % communicants. Rapport du 3 juillet 2026, consulté le 2 novembre 2026.
- [CWaPE — Tarification incitative, FAQ](https://cwape.be/sites/default/files/cwape-documents/2024.07.15-Tarification%20incitative-FAQ.pdf) — compteur communicant avec fonction de communication active, 56 kVA au plus. Document du 15 juillet 2024. [CWaPE — Dossier de presse sur les tarifs de distribution](https://www.cwape.be/sites/default/files/cwape-documents/2025.11.03-Tarifs%20distribution_dossier%20de%20presse%20-%20final.pdf) — refus d'imposer le régime R3 pour le tarif Impact, définition des régimes R1 et R3. Document du 3 novembre 2025. Consultés le 2 novembre 2026.
- Tarifs non périodiques 2026 approuvés par la CWaPE : [ORES, décision CD-26c26-CWaPE-1246, annexe 8](https://www.cwape.be/sites/default/files/cwape-documents/2026.03.26-1246-ORES-D%C3%A9cision%20TPDA%20%26%20Rectification%20TNP%202025-29%20%2B%20annexes.pdf), [RESA](https://cwape.be/sites/default/files/cwape-documents/ANNEXE%20TNP-E0_B%20-%20RESA_ELEC_TARIFS%20NP_2026_0.pdf), [AIEG, décision du 19 décembre 2024](https://cwape.be/sites/default/files/cwape-documents/2024.12.19-1026-AIEG-D%C3%A9cision%20approbation%20TNP%202025-2029%2Bannexes.pdf), [AIESH, décision du 19 décembre 2024](https://cwape.be/sites/default/files/cwape-documents/2024.12.19-1027-AIESH-D%C3%A9cision%20approbation%20TNP%202025-2029%2Bannexes.pdf) et [REW](https://www.rew.be/document/download/191/fdd71d0b-f3ed-4a70-8731-6eb4dccc1610/118) — téléopérations y compris le port P1 gratuites, désactivation de la fonction communicante à 128,33 € hors TVA au-delà de quinze jours après la pose, réactivation gratuite, remplacement d'un compteur électromécanique par un compteur communicant gratuit. Consultés le 2 novembre 2026.
- ORES — [Les compteurs (FAQ)](https://www.ores.be/faq/les-compteurs), [Port client](https://www.ores.be/particulier/port-client/), [Le compteur communicant](https://www.ores.be/particulier/compteur-communicant-fonctionnement), [myORES (FAQ)](https://www.ores.be/faq/myores) et [Démarrer un partage](https://www.ores.be/particulier/demarrer-partage-cer-cec) — formulaire de demande, gratuité, refus de la pose impossible, activation du port P1 par téléphone, câble RJ12, déploiement d'ici fin 2029, vue au quart d'heure et délai de 72 heures, compteur communicant ou AMR et « régime 3 » pour le partage. Pages non datées, consultées le 2 novembre 2026.
- [RESA — Le compteur communicant](https://www.resa.be/fr/ma-situation/mon-compteur/compteur-communicant/) — demande, date de remplacement par code EAN, gratuité, désactivation par formulaire, conséquences, MyRESA au quart d'heure. [RESA — Rapport annuel 2024](https://cms.resa.be/app/uploads/2025/09/Rapport-annuel-2024.pdf) — 84 862 compteurs communicants fin 2024, 18,42 % du parc. Consultés le 2 novembre 2026.
- [AIEG — Compteur communicant](https://www.aieg.be/compteur-communicant-ou-smart-metering/) et [Le port P1](https://www.aieg.be/le-port-p1/) ; [AIESH — Compteurs communicants](https://aiesh.be/consommateurs/compteurs_communicants/) ; [REW — FAQ](https://www.rew.be/faq) — formulaires de demande et d'activation du port P1, plateforme MyConso, refus du remplacement impossible et coût de la désactivation. Pages consultées le 2 novembre 2026.
- [Fluvius — eMUCs-P1, spécification du port P1, version 1.7.1](https://partner.fluvius.be/sites/fluvius/files/2025-09/smart-metering-system-emucs-p1-v1-7.pdf) — valeurs instantanées chaque seconde, interface fondée sur la spécification néerlandaise DSMR P1. Document du 5 septembre 2022, consulté le 2 novembre 2026.
- [Sibelga — Quand recevrai-je un compteur intelligent ?](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents/quand-recevrai-je-un-compteur-intelligent), [Compteurs intelligents](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents) et [Le port P1](https://www.sibelga.be/fr/raccordements-compteurs/compteurs-intelligents/le-port-p1-du-compteur-intelligent) ; [Fluvius — Digitale meter weigeren](https://www.fluvius.be/nl/meters-en-meterstanden/digitale-meter/weigeren) et [Maak je meter slim](https://www.fluvius.be/nl/meters-en-meterstanden/maak-je-meter-slim) — déploiement bruxellois et flamand, gratuité, cas obligatoires, port P1. Consultés le 2 novembre 2026.
