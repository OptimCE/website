---
layout: post
title: "Prix de l'électricité en communauté d'énergie : comment fixer le prix de cession interne"
date: 2026-07-20 10:00:00 +0200
author: "Équipe OptimCE"
excerpt: "Quel prix au kWh appliquer à l'électricité partagée entre membres ? Ce que le prix interne couvre réellement, la fourchette défendable entre tarif d'injection et composante énergie, cinq méthodes de calcul, un cas belge chiffré et les règles en Wallonie, à Bruxelles et en Flandre."
tags: [community, administrative, guide]
lang: fr
ref: internal-price-shared-energy
faq:
  - q: "Qui fixe le prix de l'électricité partagée dans une communauté d'énergie ?"
    a: "En Wallonie et à Bruxelles, les participants eux-mêmes. La CWaPE écrit que « le prix de l'électricité partagée est déterminé librement entre les participants au partage, dans la convention déterminant leurs droits et obligations ». Aucun régulateur belge ne publie de plafond ni de méthode de calcul. En Flandre, la question ne se pose pas de la même façon : le partage au sein d'une communauté d'énergie doit être gratuit."
  - q: "Le prix interne remplace-t-il ma facture d'électricité ?"
    a: "Non. Il ne remplace que la composante énergie, soit environ 38 % d'une facture résidentielle belge selon le tableau de bord CREG de juin 2026. Les frais de réseau, les accises, les surcharges régionales et la TVA restent dus sur les kWh partagés, et l'énergie non couverte par le partage reste facturée par votre fournisseur habituel."
  - q: "Entre quelles valeurs un prix de cession interne est-il défendable ?"
    a: "Entre le tarif d'injection que le producteur obtiendrait ailleurs — de 0,94 à 4,90 c€/kWh selon les contrats relevés par Test-Achats en mai 2026 — et la composante énergie que le consommateur paie à son fournisseur, de l'ordre de 14 c€/kWh. En dessous du plancher, le producteur perd à partager ; au-dessus du plafond, le consommateur perd à consommer local."
  - q: "Peut-on partager de l'électricité gratuitement ?"
    a: "Oui en Wallonie et à Bruxelles, où le prix est un paramètre contractuel qui peut valoir zéro. En Flandre, c'est même obligatoire au sein d'une communauté d'énergie : la Vlaamse Nutsregulator indique qu'on ne peut y partager de l'énergie que sans contrepartie, la vente passant par d'autres dispositifs."
  - q: "Faut-il une licence de fourniture pour vendre l'énergie partagée à ses membres ?"
    a: "Non, dans le périmètre du partage. En Wallonie, le SPW précise que l'électricité partagée n'est pas une opération de fourniture. À Bruxelles, l'ordonnance dit explicitement que la communauté « n'est pas soumise aux obligations à charge des fournisseurs pour l'électricité partagée en son sein ». L'exemption s'arrête au périmètre des participants : vendre au-delà relève du régime de licence."
  - q: "Quelle TVA appliquer sur l'électricité partagée ?"
    a: "6 % pour les membres particuliers et 21 % pour les membres professionnels : une communauté aux membres mixtes facture donc à deux taux. Sous 25 000 € de chiffre d'affaires hors TVA par an, le régime de franchise des petites entreprises peut s'appliquer. Vérifiez votre situation auprès du SPF Finances ou de votre comptable."
  - q: "À quelle fréquence faut-il revoir le prix ?"
    a: "Au moins une fois par an, en assemblée générale — c'est ce que pratique la communauté bruxelloise Énergie Solidaire du Balai. Un prix figé pendant que le marché bouge finit toujours par léser quelqu'un : soit les producteurs quand les prix montent, soit les consommateurs quand ils s'effondrent."
---

Un propriétaire de panneaux solaires revend aujourd'hui son surplus entre **0,94 et 4,90 c€/kWh** selon son contrat ([Test-Achats](https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee), mai 2026). Le même jour, son voisin achète son électricité à **36,94 c€/kWh** tout compris ([CREG](https://www.creg.be/fr/professionnels/fonctionnement-et-monitoring-du-marche/tableau-de-bord), juin 2026). Entre ces deux nombres, il y a un facteur onze — et c'est exactement l'espace dans lequel se loge une communauté d'énergie.

Reste la question que tout porteur de projet finit par poser, souvent trop tard : **quel prix inscrire dans la convention ?** Aucun régulateur belge ne publie de réponse. Ni la CWaPE, ni BRUGEL, ni la Vlaamse Nutsregulator ne diffusent de méthode de calcul ou de tarif de référence. Cet article comble ce vide : ce que le prix interne couvre réellement, entre quelles bornes il doit tomber, cinq méthodes pour le construire, un cas belge entièrement chiffré, et ce que le cadre autorise dans chaque région.

Si la mécanique du partage vous est encore étrangère, commencez par notre article de référence [« Clé de répartition en Belgique : Wallonie, Bruxelles, Flandre »](/actualites/2026/05/19/cle-repartition-communaute-energie-belgique/) : la clé décide *combien de kWh* reviennent à chacun, le prix décide *combien d'euros*.

## Le prix de cession interne ne remplace qu'un tiers de la facture

C'est l'erreur numéro un, et elle empoisonne les assemblées générales : croire qu'un prix interne de 14 c€/kWh fera payer 14 c€/kWh aux membres. Il n'en est rien.

Une facture d'électricité belge se décompose en quatre blocs. Voici leur poids réel, d'après le tableau de bord mensuel de la CREG pour **juin 2026** (profil résidentiel type, 3 500 kWh/an, mono-horaire) :

| Composante | Belgique | Flandre | Bruxelles | Wallonie |
|---|---|---|---|---|
| **Énergie** (la commodité) | 38,5 % | 39,3 % | 39,7 % | 37,2 % |
| Réseau (transport + distribution) | 29,7 % | 28,7 % | 24,6 % | 32,7 % |
| Taxes, accises et surcharges | 26,1 % | 26,4 % | 30,1 % | 24,5 % |
| TVA | 5,7 % | 5,7 % | 5,7 % | 5,7 % |
| **Prix total** | **36,94 c€/kWh** | 35,31 | 39,04 | 38,64 |

Le prix de cession interne ne concurrence que la **première ligne** : environ **14 c€/kWh** en valeur absolue. Tout le reste continue de courir sur les kWh partagés, parce que ces kWh transitent bel et bien par le réseau public. La CWaPE le formule sans ambiguïté : « l'électricité transitant par le réseau, tous les frais de réseau (transport et distribution), ainsi que les taxes et surcharges y relatives, sont dus sur l'électricité partagée » ([CWaPE](https://www.cwape.be/node/6062)).

Deux conséquences pratiques :

- **Annoncez toujours l'économie sur la composante énergie, jamais sur la facture.** Diviser le prix de l'énergie par deux ne divise pas la facture par deux : cela en retire environ 19 %.
- **Le poids du réseau varie fortement d'une région à l'autre** — 32,7 % en Wallonie contre 24,6 % à Bruxelles. Un même prix interne ne produit donc pas le même effet ressenti selon l'endroit.

### Ce que le représentant facture en plus du prix

Au prix convenu s'ajoutent, sur la facture de la communauté elle-même, « la TVA, les accises et l'obligation de service public de restitution des quotas de certificats verts » ([CWaPE](https://www.cwape.be/node/6063)). Deux précisions qui font trébucher beaucoup de projets :

- **La TVA n'est pas uniforme.** Le taux réduit de **6 % vise la fourniture d'électricité à un client particulier**, contre **21 % pour un client professionnel** : une communauté aux membres mixtes doit donc s'attendre à facturer à deux taux. En dessous de 25 000 € de chiffre d'affaires hors TVA par an, le [régime de franchise des petites entreprises](https://finances.belgium.be/fr/entreprises/tva/assujettissement-tva/regime-franchise-taxe) peut s'appliquer. Aucune circulaire ne traite spécifiquement du partage d'énergie : faites valider votre situation par votre comptable avant la première facture.
- **La cotisation fédérale n'existe plus.** Elle a été supprimée au 31 décembre 2021 et absorbée dans le droit d'accise spécial ([CREG](https://www.creg.be/fr/a-z-index/cotisation-federale)). Beaucoup de documents en circulation la mentionnent encore : ne la reprenez pas dans vos simulations.

## Les frais de réseau ne baissent presque jamais

L'idée qu'une communauté d'énergie bénéficie de tarifs de réseau réduits est très répandue. Elle est surtout **fausse dans le cas le plus courant**. Le détail par région :

| Région | Réduction des tarifs réseau sur les kWh partagés |
|---|---|
| **Wallonie** | 80 % sur les termes proportionnels, **uniquement au sein d'un même bâtiment**. Pour une communauté d'énergie : aucune réduction. La CWaPE l'écrit noir sur blanc — « il n'existe pas de réduction tarifaire pour le partage au sein d'une communauté d'énergie ». |
| **Bruxelles** | Le seul vrai régime préférentiel. Selon la proximité des participants : type A (même bâtiment) → tarifs proportionnels **réduits à 0 €** ; type B (même cabine BT) → **réduits de moitié** ; types C et D → inchangés. Confirmé jusqu'en 2027 au moins par la méthodologie tarifaire 2025-2029 de BRUGEL. |
| **Flandre** | Aucune. « Energiedelen … hebben enkel een effect op de energiecomponent van de elektriciteitsfactuur, maar niet op de netkosten, heffingen en taksen » (Fluvius). Le tarif capacitaire, basé sur la pointe mesurée au compteur, n'est pas allégé non plus. |

Ajoutez-y un poste que presque personne n'anticipe : **votre fournisseur peut facturer des frais pour votre participation au partage**. La CWaPE confirme que rien ne l'interdit ([CWaPE](https://www.cwape.be/node/6060)), et les montants relevés vont de zéro à environ 150 € par an et par point de fourniture. Sur une petite quantité d'énergie partagée, ces frais annulent purement et simplement le gain — c'est le principal tueur silencieux de rentabilité d'un projet.

## Qui a le droit de fixer un prix ? Les trois régions ne répondent pas pareil

C'est le point que la plupart des guides passent sous silence, et il est décisif : **en Flandre, la question du prix ne se pose pas**, parce que vendre à l'intérieur d'une communauté d'énergie n'y est pas permis.

| | Wallonie | Bruxelles | Flandre |
|---|---|---|---|
| **Prix dans une communauté** | Libre | Libre | **Interdit — le partage doit être gratuit** |
| Ce que dit le cadre | « Le prix de l'électricité partagée est déterminé librement entre les participants au partage » (CWaPE) | Aucun plafond ni prix de référence dans l'ordonnance ; obligation de règles « équitables, transparentes et non discriminatoires » | « In een energiegemeenschap kan je enkel energie delen. Energie verkopen in een energiegemeenschap is niet mogelijk » (Vlaamse Nutsregulator) |
| Convention-type officielle | Aucune pour la convention entre participants | Oui, publiée par Bruxelles Environnement | Modèle publié pour la vente de pair à pair |
| Licence de fourniture | Non requise : « l'électricité partagée n'est pas considérée comme une opération de fourniture » (SPW Énergie) | Non : la communauté « n'est pas soumise aux obligations à charge des fournisseurs pour l'électricité partagée en son sein » | Sans objet pour le partage ; la vente en immeuble est expressément exemptée |

### Wallonie : liberté totale, et page blanche

Le prix est libre, et la convention entre participants doit contenir « la clé de répartition, le coût de l'électricité partagée » — mais **aucun modèle-type n'existe** ([CWaPE](https://www.cwape.be/node/6064)). Vous partez d'une page blanche. À noter également : le pair-à-pair wallon n'est **pas encore opérationnel**, faute d'arrêté d'exécution ([CWaPE](https://www.cwape.be/node/6080)). Les seules voies pour appliquer un prix sont donc le partage en même bâtiment et le partage au sein d'une communauté autorisée.

### Bruxelles : encadrement de la forme, liberté sur le montant

L'ordonnance bruxelloise ne contient **ni le mot « prix » ni le mot « raisonnable »** dans son chapitre consacré aux communautés d'énergie. Ce qu'elle impose, c'est un encadrement procédural : la convention doit fixer « les règles équitables, transparentes et non discriminatoires de partage », être rédigée « dans un langage clair et compréhensible » et ne pas « créer de discrimination entre participants ». Le niveau du prix, lui, reste entièrement négocié — la convention-type officielle comporte d'ailleurs un champ à compléter : *« Le prix de vente de l'électricité partagée est fixé à ….. centimes€/kWh HTVA »*.

L'aide au chiffrage ne vient pas du régulateur mais de **Bruxelles Environnement**, qui met à disposition un outil de simulation économique et un facilitateur gratuit.

### Flandre : gratuit par définition

L'*energiedelen* est défini dans le décret énergie flamand comme l'attribution **« kosteloos »** — à titre gratuit — de l'énergie autoproduite. Le régulateur est catégorique : au sein d'une communauté d'énergie, on ne peut que partager, pas vendre. Un prix reste possible, mais par d'autres portes : la **vente de personne à personne** (*persoon-aan-persoonverkoop*), où « je bepaalt zelf de prijs », et la vente au sein d'un immeuble par l'association des copropriétaires. Attention au piège : la vente multiple de pair à pair va de *plusieurs vendeurs vers un seul acheteur* — elle ne permet donc pas à une communauté de facturer l'ensemble de ses membres.

**En clair : un projet flamand qui veut rémunérer ses producteurs doit choisir un autre montage juridique que la communauté d'énergie.** Mieux vaut le découvrir avant la constitution que devant le régulateur.

## La fourchette : plancher producteur, plafond consommateur

Toute la discussion sur le prix tient dans un raisonnement simple : **chaque partie a une alternative, et le prix doit être meilleur que cette alternative pour les deux.**

- **Le plancher, c'est ce que le producteur obtiendrait sans la communauté** : son tarif d'injection. Il n'existe aucun tarif d'injection régulé en Belgique — c'est un prix commercial. Relevé de mai 2026 : de **0,94 à 4,90 c€/kWh** en Flandre et Wallonie, de 1,40 à 4,81 c€/kWh à Bruxelles ([Test-Achats](https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee)). Et ce plancher peut devenir négatif : près de **29 000 prosumers flamands** ont subi un tarif de rachat négatif pendant au moins un mois en 2025 — ils ont dû *payer* pour injecter.
- **Le plafond, c'est ce que le consommateur paie déjà** pour la seule composante énergie de son contrat : de l'ordre de **14 c€/kWh**.

Entre 3 et 14 c€/kWh, tout le monde gagne. En dessous, le producteur a intérêt à quitter la communauté. Au-dessus, le consommateur aussi. **Le prix de cession interne n'est donc pas une question morale : c'est un partage de surplus, et la seule vraie question est de savoir dans quelles proportions.**

Un détail qui renforce l'argument, et qu'on oublie de citer : sur le marché de gros belge, en mai 2026, le prix des **heures pleines (69,78 €/MWh) est passé sous celui des heures creuses (103,03 €/MWh)** ([BELIX](https://www.elexys.be/en/insights/belix-average-day-ahead-spot-be)). L'électricité solaire de milieu de journée vaut de moins en moins cher sur le marché — et de plus en plus cher pour qui la consomme localement au même instant. L'écart entre plancher et plafond ne se referme pas : il s'élargit.

## Cinq méthodes pour construire le prix

Aucune n'est « la bonne ». Elles répondent à des priorités différentes.

### 1. Le prix fixe voté en assemblée générale

Un nombre, un vote, une date de révision. C'est de loin le plus répandu, et c'est ce que pratique la communauté bruxelloise Énergie Solidaire du Balai, dont le prix « est revu chaque année lors de l'assemblée générale ».

*Pour qui :* toutes les communautés qui démarrent. *Risque :* le prix dérive par rapport au marché si la révision est oubliée.

### 2. Le partage de la différence

On calcule explicitement le plancher et le plafond, puis on se place au milieu — ou à 40/60 si l'on veut favoriser le producteur qui a investi. Avec un tarif d'injection à 3 c€ et une composante énergie à 14 c€, le milieu tombe à **8,5 c€/kWh** : le producteur triple sa valorisation, le consommateur économise 40 % sur sa composante énergie.

*Pour qui :* les communautés qui veulent pouvoir **justifier** leur prix devant un membre mécontent. *Force :* c'est la seule méthode qui produit un argumentaire chiffré, symétrique et vérifiable.

### 3. Le coût de revient de l'installation

On divise l'investissement plus les frais d'exploitation par les kWh produits sur la durée de vie. Le prix devient un objectif d'amortissement plutôt qu'un arbitrage de marché.

*Pour qui :* les communautés qui possèdent elles-mêmes leur installation. *Risque :* un coût de revient photovoltaïque est très bas, ce qui donne un prix producteur faible — à combiner avec une marge explicite (voir plus bas).

### 4. La remise en pourcentage sur le tarif fournisseur

Le prix suit la composante énergie du fournisseur, moins X %. Il reste automatiquement cohérent avec le marché.

*Pour qui :* les communautés dont les membres comparent en permanence avec leur contrat. *Attention :* la remise doit porter sur la **composante énergie**, pas sur le prix all-in, sous peine de promettre une économie impossible à tenir.

### 5. L'indexation sur un indice de marché

Le prix suit un indice publié — par exemple la moyenne mensuelle du marché day-ahead belge. C'est le plus juste économiquement et le plus difficile à expliquer en assemblée générale.

*Pour qui :* les communautés à composante professionnelle, habituées aux contrats indexés. *Risque :* vous réimportez dans la communauté la volatilité que les membres étaient venus fuir. Or la stabilité du prix est souvent l'argument le plus apprécié, avant même l'économie.

| Méthode | Effort | Stabilité pour le membre | Justifiable |
|---|---|---|---|
| Prix fixe voté en AG | Faible | Très élevée | Moyennement |
| Partage de la différence | Moyen | Élevée | Très bien |
| Coût de revient | Moyen | Élevée | Bien |
| Remise en % | Faible | Moyenne | Bien |
| Indexation | Élevé | Faible | Très bien |

## Un cas belge entièrement chiffré

La communauté bruxelloise **Énergie Solidaire du Balai** publie ses tarifs — une rareté. Voici sa structure 2024, telle que documentée par le [Guide Bâtiment Durable de Bruxelles Environnement](https://guidebatimentdurable.brussels/partage-delectricite-sein-dune-communaute-denergie-energie-solidaire-balai/partage-delectricite) :

| Poste | Montant |
|---|---|
| Prix payé au producteur | **6 c€/kWh** |
| Marge conservée par la communauté | **8 c€/kWh** |
| **Prix de l'énergie locale facturé au consommateur** | **14 c€/kWh** |
| + frais de réseau | 9,575 c€/kWh HTVA |
| + taxes fédérales | 4,94 c€/kWh HTVA |
| **Total payé par le consommateur** | **≈ 32 c€/kWh TVAC** |

Trois enseignements, dont un que la source assume avec une honnêteté qu'on aimerait voir plus souvent :

1. **Le prix producteur (6 c€) est nettement au-dessus du tarif d'injection** (1 à 5 c€) : partager reste plus intéressant qu'injecter. Le même ordre de grandeur se retrouve chez [Renouvelle](https://www.renouvelle.be/fr/exemples-calculs-de-rentabilite-economique-dun-partage-delectricite-en-wallonie/), qui documente un prix de partage interne de 6 c€/kWh et un contrat d'injection communautaire à 3 c€/kWh garanti dix ans.
2. **La marge de 8 c€/kWh n'est pas un profit** : elle finance le fonctionnement de la communauté — administration, facturation, assurance, outils.
3. **Les membres, écrit la source, « ne réalisent pas de grosses économies ».** Ils paient un prix stable, légèrement sous le marché, et adhèrent d'abord pour le projet. Promettre autre chose, c'est préparer des départs.

## Les erreurs qui cassent une communauté

- **Oublier la marge de fonctionnement.** Un prix calé au centime sur le coût de production ne laisse rien pour la comptabilité, l'assurance ou la plateforme. La communauté vit un an, puis appelle des cotisations en urgence.
- **Figer le prix sans date de révision.** Les prix de gros belges ont oscillé entre 78,94 et 112,13 €/MWh sur le seul premier semestre 2026. Un prix arrêté « une fois pour toutes » finit par léser quelqu'un.
- **Annoncer une économie sur la facture au lieu de la composante énergie.** Le membre calcule, ne retrouve pas le compte, et la confiance s'effondre.
- **Ignorer les frais supplémentaires du fournisseur.** Jusqu'à 150 €/an et par point de fourniture : sur 500 kWh partagés, cela dépasse le gain.
- **Oublier que le prosumer perd la compensation annuelle** en participant au partage ([CWaPE](https://www.cwape.be/node/6075)), et que le tarif social ne s'applique pas aux volumes partagés. Ces deux effets doivent entrer dans la simulation, pas dans la découverte a posteriori.
- **Traiter identiquement le membre producteur-consommateur.** Il reçoit deux flux distincts : une rémunération pour son injection partagée, une facture pour l'énergie partagée qu'il consomme. Deux prix, deux documents.

## Faire vivre le prix : révision, transparence, traçabilité

Un prix de cession interne n'est pas une décision, c'est un processus. Trois habitudes suffisent :

- **Une révision annuelle inscrite à l'ordre du jour de l'assemblée générale**, avec un point de comparaison présenté à chaque fois : tarif d'injection du moment, composante énergie moyenne, résultat de l'exercice écoulé.
- **Une règle écrite plutôt qu'un nombre.** « Le prix producteur est fixé au double du tarif d'injection moyen constaté, plafonné à la moitié de la composante énergie » se défend mieux qu'un « 6 c€ » sans histoire — et se met à jour tout seul.
- **Un historique conservé.** Quand un membre conteste une facture de l'an dernier, vous devez pouvoir montrer quel prix s'appliquait à cette date, et sur décision de quelle assemblée.

Cette exigence de transparence n'est pas cosmétique : à Bruxelles, elle est explicitement dans le texte — les règles doivent être « équitables, transparentes et non discriminatoires » et rédigées « dans un langage clair et compréhensible ». Rien n'impose en revanche un prix **identique** pour tous : la contrainte porte sur les *règles*, pas sur l'uniformité des montants. Une différenciation entre catégories objectives — membres investisseurs, ménages, entreprises — reste défendable si elle est écrite, motivée et appliquée uniformément. En cas de doute sur une structure tarifaire différenciée, faites-la valider par le facilitateur régional avant de la mettre en œuvre.

## Appliquer votre prix dans OptimCE

Une fois le prix décidé, il doit atterrir sur des factures. C'est précisément ce que fait le [module de facturation d'OptimCE](/actualites/2026/07/16/facturation-communaute-energie-optimce/), disponible depuis juillet 2026.

Vous définissez **deux prix en €/kWh**, indépendants l'un de l'autre — le prix de vente de l'énergie partagée aux consommateurs et le prix de rachat de l'injection versé aux producteurs. Chacun peut s'appliquer globalement, par segment de clientèle (résidentiel, professionnel, industriel) ou à un point de fourniture précis, avec une **période de validité** : la règle la plus spécifique l'emporte, et un prix global reste toujours exigé comme filet de sécurité. Les prix sont enregistrés à six décimales, pour que les arrondis n'arrivent qu'au moment du montant à payer.

Vous couvrez ainsi les deux besoins décrits plus haut : la **différenciation par catégorie objective** et l'**historique des révisions**. Changer de prix ne remplace rien : vous ajoutez une nouvelle règle à partir d'une date, et l'ancienne reste consultable — exactement ce qu'il faut le jour où un membre conteste une facture de l'exercice précédent.

À partir de là, OptimCE reprend les volumes de répartition officiels déjà importés, applique le bon prix à chaque profil et génère les factures, les notes de crédit et les décomptes de rémunération en PDF, avec numérotation légale, communication structurée et suivi des paiements. Le prix que vous avez négocié en assemblée générale devient un document opposable, sans tableur intermédiaire.

## Conclusion

Fixer le prix de l'électricité partagée n'est ni une question technique ni une question morale : c'est un **partage de surplus entre deux parties qui ont chacune une alternative**. Le producteur peut injecter à 3 c€/kWh, le consommateur peut acheter sa composante énergie à 14 c€/kWh. Tout prix entre les deux crée de la valeur ; la seule décision qui reste est celle de la répartition — et elle appartient à l'assemblée générale, pas au régulateur.

Reste à vérifier que votre région autorise seulement ce que vous imaginez : liberté totale en Wallonie et à Bruxelles, gratuité imposée au sein des communautés flamandes. Puis à écrire la règle, prévoir sa révision, et l'appliquer sans erreur d'arrondi sur chaque facture.

> ### Facturez l'énergie partagée au bon prix avec OptimCE
>
> Plateforme open source pour les communautés d'énergie belges : définissez vos prix de vente et de rachat, par segment ou par point de fourniture, avec période de validité — et générez factures et décomptes en PDF à partir de vos données de répartition officielles.
>
> **[Démarrer sur app.optimce.be →](https://app.optimce.be)**

## FAQ

### Qui fixe le prix de l'électricité partagée dans une communauté d'énergie ?

En **Wallonie et à Bruxelles, les participants eux-mêmes**. La CWaPE écrit que « le prix de l'électricité partagée est déterminé librement entre les participants au partage, dans la convention déterminant leurs droits et obligations ». Aucun régulateur belge ne publie de plafond ni de méthode de calcul. En **Flandre**, la question ne se pose pas de la même façon : le partage au sein d'une communauté d'énergie doit être gratuit.

### Le prix interne remplace-t-il ma facture d'électricité ?

Non. Il ne remplace que la **composante énergie**, soit environ 38 % d'une facture résidentielle belge selon le tableau de bord CREG de juin 2026. Les frais de réseau, les accises, les surcharges régionales et la TVA restent dus sur les kWh partagés, et l'énergie non couverte par le partage reste facturée par votre fournisseur habituel.

### Entre quelles valeurs un prix de cession interne est-il défendable ?

Entre le **tarif d'injection** que le producteur obtiendrait ailleurs — de 0,94 à 4,90 c€/kWh selon les contrats relevés par Test-Achats en mai 2026 — et la **composante énergie** que le consommateur paie à son fournisseur, de l'ordre de 14 c€/kWh. En dessous du plancher, le producteur perd à partager ; au-dessus du plafond, le consommateur perd à consommer local.

### Peut-on partager de l'électricité gratuitement ?

Oui en Wallonie et à Bruxelles, où le prix est un paramètre contractuel qui peut valoir zéro. En **Flandre, c'est même obligatoire** au sein d'une communauté d'énergie : la Vlaamse Nutsregulator indique qu'on ne peut y partager de l'énergie que sans contrepartie, la vente passant par d'autres dispositifs.

### Faut-il une licence de fourniture pour vendre l'énergie partagée à ses membres ?

Non, **dans le périmètre du partage**. En Wallonie, le SPW précise que l'électricité partagée n'est pas considérée comme une opération de fourniture. À Bruxelles, l'ordonnance dit explicitement que la communauté « n'est pas soumise aux obligations à charge des fournisseurs pour l'électricité partagée en son sein ». L'exemption s'arrête au périmètre des participants : vendre au-delà relève du régime de licence.

### Quelle TVA appliquer sur l'électricité partagée ?

**6 % pour les membres particuliers et 21 % pour les membres professionnels** : une communauté aux membres mixtes facture donc à deux taux. Sous 25 000 € de chiffre d'affaires hors TVA par an, le régime de franchise des petites entreprises peut s'appliquer. Vérifiez votre situation auprès du SPF Finances ou de votre comptable.

### À quelle fréquence faut-il revoir le prix ?

**Au moins une fois par an, en assemblée générale** — c'est ce que pratique la communauté bruxelloise Énergie Solidaire du Balai. Un prix figé pendant que le marché bouge finit toujours par léser quelqu'un : soit les producteurs quand les prix montent, soit les consommateurs quand ils s'effondrent.

## Sources

- [CREG — Tableau de bord mensuel électricité et gaz naturel](https://www.creg.be/fr/professionnels/fonctionnement-et-monitoring-du-marche/tableau-de-bord) — prix all-in et décomposition par composante, par région (édition de juin 2026).
- [CREG — Comment est composé le prix de l'énergie ?](https://www.creg.be/fr/consommateurs/le-marche-de-lenergie/comment-est-compose-le-prix-de-lenergie) — structure de la facture et taux de TVA applicable.
- [CREG — Cotisation fédérale](https://www.creg.be/fr/a-z-index/cotisation-federale) — suppression au 31 décembre 2021.
- [CWaPE — Quel est le coût de l'électricité partagée ?](https://www.cwape.be/node/6063) — liberté de fixation du prix et éléments facturés en plus.
- [CWaPE — Frais de réseau sur l'électricité partagée](https://www.cwape.be/node/6062) — tarifs dus, réduction de 80 % limitée au partage en immeuble.
- [CWaPE — Conventions de partage](https://www.cwape.be/node/6064) — contenu minimal, absence de modèle-type entre participants.
- [SPW Énergie — Communautés d'énergie et partage](https://energie.wallonie.be/home/les-marches-et-les-acteurs/communautes-d-energie/communautes-d-energie-et-partage-d-energie-au-sein-d-un-meme-batiment-electricite.html) — le partage n'est pas une opération de fourniture.
- [BRUGEL — Partage d'énergie : tarifs de réseau](https://energysharing.brugel.brussels/energysharing/tarifs-de-reseau-409) — types A à D et réductions applicables aux volumes locaux.
- [Vlaamse Nutsregulator — Energiedelen en energie verkopen](https://www.vlaamsenutsregulator.be/elektriciteit-en-aardgas/energieprijzen-en-facturen/energiedelen-en-energie-verkopen) — gratuité du partage en communauté et liberté de prix en vente de pair à pair.
- [Bruxelles Environnement — Partage d'électricité : Énergie Solidaire du Balai](https://guidebatimentdurable.brussels/partage-delectricite-sein-dune-communaute-denergie-energie-solidaire-balai/partage-delectricite) — structure de prix complète d'une communauté bruxelloise (tarifs 2024).
- [Renouvelle — Exemples de calculs de rentabilité d'un partage d'électricité en Wallonie](https://www.renouvelle.be/fr/exemples-calculs-de-rentabilite-economique-dun-partage-delectricite-en-wallonie/) — prix internes pratiqués et impact des frais fournisseurs.
- [Test-Achats — Coût de l'électricité solaire injectée sur le réseau](https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee) — fourchette des tarifs d'injection en Belgique, mai 2026.
- [Elexys — BELIX, moyenne mensuelle du marché day-ahead belge](https://www.elexys.be/en/insights/belix-average-day-ahead-spot-be) — prix de gros base, pointe et hors pointe.
- [SPF Finances — Régime de la franchise de taxe](https://finances.belgium.be/fr/entreprises/tva/assujettissement-tva/regime-franchise-taxe) — seuil de 25 000 € pour les petites entreprises.
