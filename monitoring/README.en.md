<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Français](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Luxembourg only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-24 05:36 UTC, Legilux open data (Journal officiel and consolidated texts): 1011 addresses read; 1 added, 0 changed, 0 removed; changes found, flagged; 37 not published, 2 of them with no reason. Flags: `unexplained-gap`.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [Legilux open data (Journal officiel and consolidated texts)](https://data.legilux.public.lu/) | `constitution/`, `loi/`, `memorial-b/loi/`, `data/actes/loi.csv` | daily | 2026-11-24 05:36 UTC | changes found, flagged | watched: the open-data channel (CC BY 4.0) the repository is built from; the website is not crawled |
| [Judicial courts on data.public.lu (Administration judiciaire): Cour de cassation](https://data.public.lu/fr/datasets/cour-de-cassation-1/) | `jurisprudence/` | — | — | — | paused: case law waits until legislation is fully monitored |
| [Conseil d'État opinions on data.public.lu](https://data.public.lu/fr/datasets/avis-du-conseil-detat/) | `avis/` | — | — | — | paused: opinions on bills, not law: they wait, as case law does, until legislation is fully monitored |
| [Chambre des Députés on data.public.lu: bills](https://data.public.lu/fr/organizations/627e56d3a9bc6b2dd946a3ea/) | `data/chambre/` | — | — | — | paused: bills, not law: they wait, as case law does, until legislation is fully monitored |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-24 05:18](checks/2026-11.md#lu-legilux-20261124t051847z) | legilux | 1011 | 1 | 0 | 0 | 37 (2) | changes found, flagged `unexplained-gap` | — |
| [2026-11-23 16:12](checks/2026-11.md#lu-legilux-20261123t161238z) | legilux | 1026 | 2 | 0 | 0 | 36 (2) | changes found, flagged `unexplained-gap` `audit-disagrees` | [9](https://github.com/lexifina/luxembourg-law/compare/df1119d9139c...6a4f0ff1becf) |
| [2026-11-23 14:10](checks/2026-11.md#lu-legilux-20261123t141047z) | legilux | 6973 | 0 | 2 | 0 | 33 (0) | changes found `verify-differ` | [57](https://github.com/lexifina/luxembourg-law/compare/ec1d05af361c...078a31e2dfcc) |
| [2026-11-23 02:03](checks/2026-11.md#lu-legilux-20261123t020354z) | legilux | 4 | 0 | 0 | 0 | 50 (0) | no change `publish-lag` | — |

## Check it yourself

```
python tools/checktrail.py                      # the latest check of every source
python tools/checktrail.py --day 2026-11-23     # every check of a day
python tools/checktrail.py --act <id>           # when an act was seen and published
git log --grep='^Kind: check' --format='%ci %s'  # the checks in the history
```

Only the official publication has legal force; the texts here are copies for reading and searching.
