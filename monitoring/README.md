<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Surveillance : ce qui est lu et ce qui en résulte

[English](README.en.md)

Comment global-law surveille chaque pays : [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Cette page fait de même pour Luxembourg seulement : chaque lecture d’une source officielle, sa date et ce qui en est ressorti (actes ajoutés, modifiés et retirés). La forme lisible par machine est dans [data/checks/](../data/checks/) (JSON Lines, schéma `lexifina-check/1`), dans `git log` sous forme de commits `Kind: check`, et mois par mois dans [checks/](checks/).

**Dernière vérification :** 2026-11-28 05:20 UTC, Données ouvertes de Legilux (Journal officiel et textes consolidés) : 1035 adresses lues ; 1 ajoutés, 13 modifiés, 0 retirés ; changements constatés, signalés ; 44 non publiés, dont 5 sans motif. Signalements: `unexplained-gap`, `publish-lag`.

## Sources

| Source | Dossiers | Fréquence | Dernière vérification réussie | Dernier résultat | État |
| --- | --- | --- | --- | --- | --- |
| [Données ouvertes de Legilux (Journal officiel et textes consolidés)](https://data.legilux.public.lu/) | `constitution/`, `loi/`, `memorial-b/loi/`, `data/actes/loi.csv` | chaque jour | 2026-11-28 05:20 UTC | changements constatés, signalés | surveillée: le canal de données ouvertes (CC BY 4.0) dont le dépôt est tiré ; le site web n’est pas parcouru |
| [Juridictions judiciaires sur data.public.lu (Administration judiciaire) : Cour de cassation](https://data.public.lu/fr/datasets/cour-de-cassation-1/) | `jurisprudence/` | — | — | — | en pause: la jurisprudence attendra que la législation soit entièrement surveillée |
| [Avis du Conseil d’État sur data.public.lu](https://data.public.lu/fr/datasets/avis-du-conseil-detat/) | `avis/` | — | — | — | en pause: avis sur des projets, pas du droit : ils attendront, comme la jurisprudence, que la législation soit entièrement surveillée |
| [Chambre des Députés sur data.public.lu : projets et propositions de loi](https://data.public.lu/fr/organizations/627e56d3a9bc6b2dd946a3ea/) | `data/chambre/` | — | — | — | en pause: projets de loi, pas du droit : ils attendront, comme la jurisprudence, que la législation soit entièrement surveillée |

## Les 30 derniers jours

| Début (UTC) | Source | Lues | Ajoutés | Modifiés | Retirés | Non publiés (sans motif) | Résultat | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-28 05:02](checks/2026-11.md#lu-legilux-20261128t050236z) | legilux | 1035 | 1 | 13 | 0 | 44 (5) | changements constatés, signalés `unexplained-gap` `publish-lag` | [11](https://github.com/lexifina/luxembourg-law/compare/43901e17456d...241201c9076f) |
| [2026-11-27 05:02](checks/2026-11.md#lu-legilux-20261127t050235z) | legilux | 1031 | 0 | 12 | 0 | 48 (4) | changements constatés, signalés `unexplained-gap` `publish-lag` | [8](https://github.com/lexifina/luxembourg-law/compare/70f3ec56fc25...b6581543b0f1) |
| [2026-11-26 05:04](checks/2026-11.md#lu-legilux-20261126t050423z) | legilux | 1029 | 1 | 13 | 0 | 45 (4) | changements constatés, signalés `unexplained-gap` `publish-lag` | [8](https://github.com/lexifina/luxembourg-law/compare/2f2f7d98c37e...07a313d38c7e) |
| [2026-11-25 05:02](checks/2026-11.md#lu-legilux-20261125t050234z) | legilux | 1020 | 3 | 5 | 0 | 40 (3) | changements constatés, signalés `unexplained-gap` | [6](https://github.com/lexifina/luxembourg-law/compare/a07ee150b162...0486711b0744) |
| [2026-11-24 05:18](checks/2026-11.md#lu-legilux-20261124t051847z) | legilux | 1011 | 1 | 0 | 0 | 37 (2) | changements constatés, signalés `unexplained-gap` | — |
| [2026-11-23 16:12](checks/2026-11.md#lu-legilux-20261123t161238z) | legilux | 1026 | 2 | 0 | 0 | 36 (2) | changements constatés, signalés `unexplained-gap` `audit-disagrees` | [9](https://github.com/lexifina/luxembourg-law/compare/df1119d9139c...6a4f0ff1becf) |
| [2026-11-23 14:10](checks/2026-11.md#lu-legilux-20261123t141047z) | legilux | 6973 | 0 | 2 | 0 | 33 (0) | changements constatés `verify-differ` | [57](https://github.com/lexifina/luxembourg-law/compare/ec1d05af361c...078a31e2dfcc) |
| [2026-11-23 02:03](checks/2026-11.md#lu-legilux-20261123t020354z) | legilux | 4 | 0 | 0 | 0 | 50 (0) | aucun changement `publish-lag` | — |

## Vérifiez vous-même

```
python tools/checktrail.py                      # la dernière vérification de chaque source
python tools/checktrail.py --day 2026-11-23     # toutes les vérifications d’un jour
python tools/checktrail.py --act <id>           # quand un acte a été vu et publié
git log --grep='^Kind: check' --format='%ci %s'  # les vérifications dans l’historique
```

Seule la publication officielle fait foi ; les textes de ce dépôt sont des copies destinées à la lecture et à la recherche.
