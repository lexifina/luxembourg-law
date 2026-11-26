<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Surveillance des sources : ce qui est surveillé pour Luxembourg

[English](WATCHING.en.md)

Comment global-law surveille les sources de chaque pays : [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). Cette page fait de même pour Luxembourg seulement : chaque source officielle dont ce dépôt tire des textes, ce qui y est lu, à quelle fréquence et quand elle a été lue pour la dernière fois. Chaque lecture et son résultat : [monitoring/](monitoring/README.md).

| Source | Ce qui est lu | Dossiers | Fréquence | Dernière lecture | État |
| --- | --- | --- | --- | --- | --- |
| [Données ouvertes de Legilux (Journal officiel et textes consolidés)](https://data.legilux.public.lu/) | le point d’accès SPARQL de Legilux (quatre requêtes) : chaque loi et la Constitution, avec leur statut, leurs dates et l’existence de leur texte XML ; chacune de leurs versions consolidées, avec les jours où elle s’applique ; le nombre d’actes de chaque autre catégorie. Puis le XML de chaque loi nouvelle ou modifiée, et d’un septième des lois du dépôt chaque jour, depuis les fichiers de Legilux (legilux.public.lu), et le HTML de quelques-unes en contrôle | `constitution/`, `loi/`, `memorial-b/loi/`, `data/actes/loi.csv` | chaque jour | 2026-11-26 05:04 UTC | surveillée: le canal de données ouvertes (CC BY 4.0) dont le dépôt est tiré ; le site web n’est pas parcouru |
| [Juridictions judiciaires sur data.public.lu (Administration judiciaire) : Cour de cassation](https://data.public.lu/fr/datasets/cour-de-cassation-1/) | — | `jurisprudence/` | — | — | en pause: la jurisprudence attendra que la législation soit entièrement surveillée |
| [Avis du Conseil d’État sur data.public.lu](https://data.public.lu/fr/datasets/avis-du-conseil-detat/) | — | `avis/` | — | — | en pause: avis sur des projets, pas du droit : ils attendront, comme la jurisprudence, que la législation soit entièrement surveillée |
| [Chambre des Députés sur data.public.lu : projets et propositions de loi](https://data.public.lu/fr/organizations/627e56d3a9bc6b2dd946a3ea/) | — | `data/chambre/` | — | — | en pause: projets de loi, pas du droit : ils attendront, comme la jurisprudence, que la législation soit entièrement surveillée |

Les sources sont lues dans le respect de leur robots.txt et de leurs conditions, avec des pauses entre les requêtes.
