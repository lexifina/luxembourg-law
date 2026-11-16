# Tools

The scripts behind this Luxembourg-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/luxembourg-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only luxembourg-law and its commit (language
`fr`, code `LU`). `build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py` and `config.json` sit two
folders above the scripts.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, maps paths to moved folders (`map_moved.py`), adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`) |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change |
| `map_moved.py` | Rewrites the paths in the history table to each act's folder after a repository moves its act folders (`data/paths.json`); this repository has no such file, so it changes nothing here |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category (there were none here) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in French and English, light and dark |
| `config.json` | The repository, the French category names, the folders and files that are not law, and the chart's labels |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `patch_detectors_vi.py`, `patch_es.py`, `patch_ca.py`, `patch_en.py`, `patch_de.py`, `patch_en_et.py`, `patch_co.py`, `patch_sv.py`, `patch_pt.py`, `patch_ru.py` | The same for the Vietnamese, Spanish, Catalan, English (two rounds), German, Colombian, Salvadoran, Brazilian and Russian blind spots found by other runs; this run's copy carries them all |
| `patch_lu.py` | The two fixes below, made for this repository |
| `apply_patches.py` | Applies every patch above once, in order (`patch_lu.py` last), recording each in `.kit_patches.json` beside the scripts so that none runs twice (`python -X utf8 apply_patches.py <scripts dir>`) |
| `redo.py` | Runs those patches, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`; `--full` runs every step again through `run.sh`; `EMBED_FONTS` names the script that embeds the chart's fonts) |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as `bash run_triage.sh '^(avis|jurisprudence|memorial-b|data|tools|vulnerabilities)/'`. The 40 strongest lapsed
time limits were all in law texts, so the two reviews of that category drew the same flags; `build_vulns.py` keeps the later
review of each flag.

Changes made for this repository:

- `add_root.py` counts as law the kinds `repeal` (the day Legilux records an act as no longer in force, with or without a
  repealing act named: 45 commits) and `replacement` (the 2023 revision that rewrote and renumbered the Constitution), beside
  the commits without a `Kind:` (each law as published, each amendment of the Constitution and the Covid-19 law) and
  `publisher` (Legilux's current consolidated text, 483 commits), which the kit already counted: 7,909 commits. The opinions
  (`opinion`), judgments (`decision`), documentation, corrections, and the changes no law explains (`typesetting`,
  `unexplained`) are left out.
- `patch_lu.py`, dead currencies: the scan reads the Luxembourg franc written out ("500 francs", "francs luxembourgeois"),
  and leaves out Swiss, CFA and CFP francs, but Luxembourg's laws also write it "fr.", "frs" or "LUF" ("1200 fr. par an",
  "11,475 frs.", "250.000.000 LUF"). These are now read, for Luxembourg only (`pins.json` code `LU`): 1,805 of the 2,845
  flags in law texts come from them. "fr" after a dot, slash or @ (a web address) is not read.
- `patch_lu.py`, file names: git quotes a path with non-ASCII characters in `ls-tree` and `grep` output
  (`"loi/2015/03/25/n3/art_12_rubrique_administration_g\303\251n\303\251rale.md"`, with the quotes), while the history,
  read with `log -z`, has it as written. The text and reference scans therefore filed such a file under another act, so a
  reference to its article read as a reference to a deleted provision, and the text and currency flags carried the quoted
  path. `ingest/common.py`'s `git()`, `currency_scan.py` and `notes_scan.py` now run git with `core.quotepath=false`, and
  `build_vulns.py` does the same when it lists the files at the pin and the deleted ones. 486 files at the pin have such
  names (188 in the income tax law of 4 December 1967). References to deleted provisions went from 66 to 9; the run was
  repeated in full, and the triage kept every review already made and sent only the strong flags not yet reviewed to the
  model (2 lapsed time limits in each of its two passes).
- `config.json` counts as not law `avis/` (Conseil d'État opinions), `jurisprudence/` (Cour de cassation judgments),
  `memorial-b/` (one Mémorial B notice, a list of insurance-broker approvals), `data/`, `tools/` and the top-level files
  (`README`, `REPRODUCE.md`, `PLAN.md`, `TERMS.md`, `CORRECTIONS.md`, `LICENSE`, `corpus.json`, `lois.csv`).
- `pins.json` already named the language (`fr`); French month names were already in the time-limit search.
