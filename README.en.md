# Luxembourg: law history in git

**English** · **[Ou lisez-le en français](README.md)**

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="Luxembourg law in this repository: what it holds, changes by the year they took effect, completeness against the official sources, and the correctness of what is held" src="data/effort-light.svg" width="880">
</picture>

The law of Luxembourg as a git history: one file per article, one commit per version on the day it took effect, and the act that made each change as the commit's author. `git blame` names the act behind every article; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Luxembourg's national law, which global-law reads at `luxembourg/national/acts/`.

**What is in it now:** the Constitution and 6,895 laws from Legilux, the official journal, with every version of the Constitution since 1868 (39 texts) and of the Covid-19 law of 17 July 2020 (33 texts) and the current text of the other laws, and 431 repealed laws in the history; 1,488 judgments of the Cour de cassation; 3,118 opinions of the Conseil d'État and a list of 4,593 bills, labelled as not law; 3,354 records of which act transposes which EU directive; and 55,449 more acts of the Mémorial listed with their metadata and official link only. [`PLAN.md`](PLAN.md) lists every part this repository is meant to hold and how far each one is; [`data/textes-en-vigueur.csv`](data/textes-en-vigueur.csv) lists the laws in force, and `data/actes/<kind>.csv` every other act, by kind.

Each act is in its ELI folder, `<kind>/<year>/<month>/<day>/<number>/`, one file per article (`texte.md` for an act without articles): `constitution/1868/10/17/n1/` is the Constitution and `loi/2006/07/31/n2/` the Code du travail, the Labour Code.

The text is in French, as Legilux publishes it. German and Luxembourgish texts and an English translation are not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 1 of the Constitution | `git log -p --word-diff -- constitution/1868/10/17/n1/art_1er.md` |
| Which act wrote each line of Article 1? | `git blame constitution/1868/10/17/n1/art_1er.md` |
| Every version of the Constitution, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constitution/1868/10/17/n1` |
| Article 1 as in force on 1 January 1990 | `python tools/en_vigueur_au.py 1990-01-01 constitution art_1er` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Luxembourg law](https://global-law.lexifina.com/v1/try_claude?country=luxembourg)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=luxembourg)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=cong%C3%A9+annuel&jurisdictions=luxembourg)**: a search of Luxembourg law for "congé annuel", returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in French or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add luxembourg/national/acts
python3 tools/law.py show 2026-01-01 luxembourg/national/acts/constitution/1868/10/17/n1/art_1er.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Europe/Luxembourg, on the day the text took effect, and carries it in its `In-force:` trailer:

- for the Constitution and the Covid-19 law, the day each consolidated version applies from (Legilux's `dateApplicability`); the amending law's other dates are in `Adopted:`, `Published:` and, where Legilux gives a different day, `Law-in-force:`;
- for any other law, its entry into force (the text as published) or the day its current consolidated text applies from; a repealed law is removed by a second commit on the day Legilux says it ceased to be in force; judgments and opinions are dated the day they were given;
- git cannot store dates before 1970, so the 2,514 earlier commits (laws from 1790 on) are dated 1970-01-01, with the real day in `In-force:`. Ask for a date with `tools/en_vigueur_au.py`, not `git log --before`.

Each change to the Constitution and the Covid-19 law is credited to the law that made it (`Loi du 15 mai 1919 (n1)`), from the modification markers and records in Legilux's XML. A text as published is credited to the law itself; a current consolidated text, a repeal with no single repealing act, and changes no law explains (`Kind: typesetting`, `Kind: unexplained`) to `Service central de législation (Legilux)`; judgments and opinions to their court or the Conseil d'État. The 2023 Constitution renumbered every article: it is one commit, credited to law A 29 of 17 January 2023, and from 1 July 2023 `art_32.md` is the new Article 32, not the old one.

## How it is checked

- `tools/check_repo.py` reads the 72 texts of the Constitution and the Covid-19 law back from git on the day each applies from and compares every article file, byte for byte, with the text rebuilt from Legilux's XML (its sha256 checked against `data/versions.json`), then word for word; the results are in [`REPRODUCE.md`](REPRODUCE.md).
- Before any other act is committed, every word of Legilux's XML for it (struck-through text and notes aside) must be in its files, in order; an act that fails is listed, not committed.
- Judgments and opinions are the text layer of the published PDF, verbatim; scanned ones, whose text would be OCR, are listed, not committed.
- History is append-only: a correction is a commit of its own (`Kind: correction`), recorded in [`CORRECTIONS.md`](CORRECTIONS.md).

## What it does not show

- **Earlier versions of most laws.** Apart from the Constitution and the Covid-19 law, each law has one text, its current consolidated text or, where Legilux never consolidated it, the text as published; the amending laws are not traced yet.
- **Most regulations and other acts as text.** The 55,449 acts listed with metadata and link (règlements grand-ducaux, arrêtés, ministerial acts, communal regulations, Mémorial notices) are mostly ones Legilux has only as scanned Mémorial pages; Legilux counts 15,402 règlements grand-ducaux and 33,351 communal regulations.
- **Acts about named private persons** adopted since 1926 (appointments, decorations, naturalisations, changes of name): listed without their title, not as text.
- **Most case law.** Of the judicial courts' decisions (about 75,000, estimated) only the Cour de cassation's are here; those of the administrative courts (422) and the Cour constitutionnelle (209, 49 of them listed) are not here as text yet (see `PLAN.md`).
- **Notes and struck-through text**, which are left out of the article files.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Legilux](https://legilux.public.lu) open data ([SPARQL](https://data.legilux.public.lu/sparqlendpoint)), Ministère d'État, Service central de législation | Official journal (Mémorial A and B) and consolidated texts | every consolidated version for the Constitution and the Covid-19 law; the current one for other consolidated laws | Only the Mémorial is authoritative |
| [Cour de cassation](https://data.public.lu/fr/datasets/cour-de-cassation-1/) on data.public.lu (Administration judiciaire) | Judgments | as published | Pseudonymised by the publisher |
| [Avis du Conseil d'État](https://data.public.lu/fr/datasets/avis-du-conseil-detat/) on data.public.lu | Opinions on bills and draft regulations | as published | Labelled as not law |
| [Chambre des Députés](https://data.public.lu/fr/organizations/627e56d3a9bc6b2dd946a3ea/) on data.public.lu | Bills since 1965 (`data/chambre/`) | as published | Labelled as not law |

## Licence

See [`LICENSE`](LICENSE). The legal texts and their data are reused from Legilux's open data under CC BY 4.0, with the attribution LICENSE gives and the wording unchanged; judgments and opinions are reproduced verbatim under CC BY-ND 4.0 and the bills under CC0 ([`TERMS.md`](TERMS.md)). Lexifina's own contributions are CC0 1.0.

No AI model wrote or changed legal text; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
