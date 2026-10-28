# Luxembourg law, change by change


Two Luxembourg acts as a git repository: the **Constitution** (from the text of 1868, through 38 consolidated versions to 2026, including the revised Constitution in force on 1 July 2023) and the **Covid-19 law of 17 July 2020** (32 versions). Each amending law is one commit, credited to that law and dated the day its changes took effect, at noon in Luxembourg. The text is the French text published by [Legilux](https://legilux.public.lu), the official journal of the Grand Duchy.

*Français : [plus bas](#français).*

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did Art. 32 of the Constitution say on 1 January 1950? | `python tools/en_vigueur_au.py 1950-01-01 constitution art_32` |
| The whole Covid-19 law on 1 March 2021 | `python tools/en_vigueur_au.py 2021-03-01 covid` |
| Which law wrote each line of an article? | `git blame constitution/1868/10/17/n1/art_15.md` |
| Every change to an article, with the law behind it | `git log -p constitution/1868/10/17/n1/art_32.md` |
| Everything one law changed | `git show loi/2016-10-18-n1` |
| Every law that changed the Covid-19 law, in order | `git log --format='%(trailers:key=In-force,valueonly,separator=) %an' -- loi/2020/07/17/a624` |
| The state of an act on a day it changed | `git checkout constitution/1989-07-14` |
| What no law explains | `git log --grep='Kind: unexplained' --grep='Kind: typesetting'` |

The laws with their dates are in [`lois.csv`](lois.csv); each act's articles, with how often each changed, are in its folder's `README.md`.

## The dates, and which one we use

A Luxembourg law is adopted (`Adopted:`), published in the Mémorial (`Published:`), and takes effect (by default on the fourth day after publication). **Commits are dated the day the changed text applies from**, Legilux's `dateApplicability` for the consolidated version: the date that decides which text governs a case. Every commit carries the other dates as trailers, and `Law-in-force:` where Legilux's metadata for the law gives a different day.

**Git cannot store dates before 1970.** The commits for 1868 to 1956 are dated 1970-01-01, one second apart and in order; their real day is in the `In-force:` trailer and the tags (`constitution/1948-05-14`). `tools/en_vigueur_au.py` reads `In-force:`, so it gives the right text for any day.

## How it is checked

`tools/check_repo.py` reads every one of the 72 texts back from git on the day it applies from and compares each article file, byte for byte, with the text rebuilt from Legilux's XML (after checking the XML's sha256 against [`data/versions.json`](data/versions.json)). A second check confirms that every word of every article in the XML, apart from struck-through text and notes, is in the file, in order. The build is deterministic: rebuilt from the same data, it gives the same commit hashes. See [`REPRODUCE.md`](REPRODUCE.md).

## What "author" means

The author of a commit is the law that made the change, named by its kind, date and ELI (`Loi du 15 mai 1919 (n1)`), at an address that cannot exist made from its ELI (`loi-1919-05-15-n1@legilux.invalid`). So `git blame` names, for each line, the law that last wrote it. Each version's own data says which law changed which article: the modification markers Legilux prints around amended words, and the destinations of its modification records. Where no marker or record links the article, but exactly one law took effect that day, the commit says the change is credited **by date only** (`Evidence: … date`).

The original texts are by the act itself (`Constitution du 17 octobre 1868`). Changes no law explains are by `Service central de législation (Legilux)` and labelled: `Kind: typesetting` where only spacing changed, `Kind: unexplained` otherwise (for example "Roi Grand-Duc" becoming "Grand-Duc" in three articles in 2020, while the only law in force that day revised Art. 95ter).

**The 2023 Constitution** is one commit, labelled a replacement, by law A 29 of 17 January 2023, whose Art. 4 provides that the text annexed to it "constitue le texte de la Constitution". It names the three other laws of that day. The revision renumbered every article, so `art_32.md` after 1 July 2023 is not the old Art. 32. Legilux's consolidation credits the whole text to a single note naming law A 26; the record does not follow it.

## What it does not show

- Chapter and section headings (they are in each act's `README.md`, not in the history), notes, and struck-through text.
- Any act beyond these two. Most ordinary laws have only their latest two or three consolidations in Legilux's data.
- German and Luxembourgish texts.
- Who wrote words that a later version reproduces unchanged under a new number after the 2023 renumbering.

This is a research aid. Only the Journal officiel (Mémorial) is authoritative; the consolidated texts on Legilux, and so this repository, are not.

## How it is built

`tools/build.py` reads Legilux's SPARQL endpoint and the Akoma Ntoso XML of each version, compares consecutive versions article by article, credits each change, and writes the commits. No AI model takes part in building or checking it. Every step, command and decision is in [`REPRODUCE.md`](REPRODUCE.md).

## Licence

Source : Legilux — Journal officiel du Grand-Duché de Luxembourg (Ministère d'État, Service central de législation). Données réutilisées sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Copyright : Ministère d'État du Grand-Duché de Luxembourg - Service central de législation. The texts were converted to one file per article and arranged as commits; the wording was not changed. Lexifina's own contributions are CC0. See [`LICENSE`](LICENSE).

---

## Français

Deux textes luxembourgeois en dépôt git : la **Constitution** (du texte de 1868 aux 38 versions consolidées jusqu'en 2026, dont la Constitution révisée entrée en vigueur le 1er juillet 2023) et la **loi Covid-19 du 17 juillet 2020**.

- **Chaque commit est une loi modificative**, inscrite comme auteur : `git blame` montre quelle loi a écrit chaque alinéa.
- **Chaque commit porte la date d'application du texte modifié**, à midi à Luxembourg. Les dates d'avant 1970 sont ramenées au 1er janvier 1970 ; la vraie date est dans `In-force:`.
- **Un fichier par article**, une ligne par alinéa ou par point.
- **Ce qu'aucune loi n'explique est étiqueté**, jamais attribué à une loi.
- **La Constitution de 2023** est un remplacement étiqueté, attribué à la loi A 29 dont l'article 4 dispose que le texte annexé « constitue le texte de la Constitution ».

Seul le Mémorial fait foi.
