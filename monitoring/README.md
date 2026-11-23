<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Surveillance : ce qui est lu et ce qui en résulte

[English](README.en.md)

Comment global-law surveille chaque pays : [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Cette page fait de même pour Luxembourg seulement : chaque lecture d’une source officielle, sa date et ce qui en est ressorti (actes ajoutés, modifiés et retirés). La forme lisible par machine est dans [data/checks/](../data/checks/) (JSON Lines, schéma `lexifina-check/1`), dans `git log` sous forme de commits `Kind: check`, et mois par mois dans [checks/](checks/).

**Dernière vérification :** 2026-11-23 02:04 UTC, Données ouvertes de Legilux (Journal officiel et textes consolidés) : 4 adresses lues ; 0 ajoutés, 0 modifiés, 0 retirés ; aucun changement ; 50 non publiés, dont 0 sans motif. Signalements: `publish-lag`.

## Sources

| Source | Dossiers | Fréquence | Dernière vérification réussie | Dernier résultat | État |
| --- | --- | --- | --- | --- | --- |
| [Données ouvertes de Legilux (Journal officiel et textes consolidés)](https://data.legilux.public.lu/) | `constitution/`, `loi/`, `memorial-b/loi/`, `data/actes/loi.csv` | chaque jour | 2026-11-23 02:04 UTC | aucun changement | surveillée: le canal de données ouvertes (CC BY 4.0) dont le dépôt est tiré ; le site web n’est pas parcouru |
| [Juridictions judiciaires sur data.public.lu (Administration judiciaire) : Cour de cassation](https://data.public.lu/fr/datasets/cour-de-cassation-1/) | `jurisprudence/` | — | — | — | en pause: la jurisprudence attendra que la législation soit entièrement surveillée |
| [Avis du Conseil d’État sur data.public.lu](https://data.public.lu/fr/datasets/avis-du-conseil-detat/) | `avis/` | — | — | — | en pause: avis sur des projets, pas du droit : ils attendront, comme la jurisprudence, que la législation soit entièrement surveillée |
| [Chambre des Députés sur data.public.lu : projets et propositions de loi](https://data.public.lu/fr/organizations/627e56d3a9bc6b2dd946a3ea/) | `data/chambre/` | — | — | — | en pause: projets de loi, pas du droit : ils attendront, comme la jurisprudence, que la législation soit entièrement surveillée |

## Les 30 derniers jours

| Début (UTC) | Source | Lues | Ajoutés | Modifiés | Retirés | Non publiés (sans motif) | Résultat | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-23 02:03](checks/2026-11.md#lu-legilux-20261123t020354z) | legilux | 4 | 0 | 0 | 0 | 50 (0) | aucun changement `publish-lag` | — |

## Vérifiez vous-même

```
python tools/checktrail.py                      # la dernière vérification de chaque source
python tools/checktrail.py --day 2026-11-23     # toutes les vérifications d’un jour
python tools/checktrail.py --act <id>           # quand un acte a été vu et publié
git log --grep='^Kind: check' --format='%ci %s'  # les vérifications dans l’historique
```

Seule la publication officielle fait foi ; les textes de ce dépôt sont des copies destinées à la lecture et à la recherche.
