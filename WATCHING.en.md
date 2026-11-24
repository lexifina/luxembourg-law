<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Watching the sources: what is watched for Luxembourg

[Français](WATCHING.md)

How global-law watches every country's sources: [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). This page is the same for Luxembourg only: every official source this repository takes text from, what is read on it, how often and when it was last read. Every read and what came of it: [monitoring/](monitoring/README.en.md).

| Source | What is read | Folders | How often | Last read | State |
| --- | --- | --- | --- | --- | --- |
| [Legilux open data (Journal officiel and consolidated texts)](https://data.legilux.public.lu/) | Legilux's SPARQL endpoint (four queries): every law and the Constitution with its status, its dates and whether Legilux has its XML text; every consolidated version of them with the days it applies from and to; the number of acts of each other kind. Then the XML of each new or changed law, and of a seventh of the held laws each day, from Legilux's file store (legilux.public.lu), and the HTML of a few as a second check | `constitution/`, `loi/`, `memorial-b/loi/`, `data/actes/loi.csv` | daily | 2026-11-24 05:18 UTC | watched: the open-data channel (CC BY 4.0) the repository is built from; the website is not crawled |
| [Judicial courts on data.public.lu (Administration judiciaire): Cour de cassation](https://data.public.lu/fr/datasets/cour-de-cassation-1/) | — | `jurisprudence/` | — | — | paused: case law waits until legislation is fully monitored |
| [Conseil d'État opinions on data.public.lu](https://data.public.lu/fr/datasets/avis-du-conseil-detat/) | — | `avis/` | — | — | paused: opinions on bills, not law: they wait, as case law does, until legislation is fully monitored |
| [Chambre des Députés on data.public.lu: bills](https://data.public.lu/fr/organizations/627e56d3a9bc6b2dd946a3ea/) | — | `data/chambre/` | — | — | paused: bills, not law: they wait, as case law does, until legislation is fully monitored |

Sources are read within their robots.txt and terms, with pauses between requests.
