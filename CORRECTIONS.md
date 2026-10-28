# Corrections

Text that this record held wrongly, found after publication. The history is append-only: the wrong text stays in the
commits where it was written, and a correction commit, authored by the publisher whose text it restores, puts the right
text on top. Each correction commit carries `Kind: correction`, a `Corrected:` date and one `Corrects:` line per file
naming the days the wrong text was in force in this record.

## 2026-10-28: words run together at Legilux's modification markers

Commit: "Loi Covid-19 : Art. 10 (correction : mots accolés)", by Service central de législation (Legilux).

Legilux's XML marks the words an amending law wrote with an empty marker (`<mod class="mod-start"/>`) and often leaves
no space before it: `à partir du<mod class="mod-start" for="#pm20"/>sixième jour`. The build joined the text on either
side, so two words became one (`dusixième`). An independent check of every version (letters and digits of Legilux's own
XML against the files in git) found it in 13 article files of the Covid-19 law; the Constitution is not affected. The
build now treats such a marker between two words as a space. No word was added or removed; only the space between two
words was missing.

Only `art_10.md` still held a run-together word on the latest version, so it is the only file the correction commit
changes. The other files were already right again on the day shown as the end of their span (a later version rewrote or
repealed them); their spans are listed so that a reader of an earlier day knows the text then was affected.

| File | Days the wrong text was in force | Run-together words |
|---|---|---|
| `loi/2020/07/17/a624/art_1er.md` | 2021-09-15..2021-12-16 | `121-1et`, `articles1er`, `complettel`, `personnesremplissant`, `présenteun`, `santéet,`, `schémade` |
| `loi/2020/07/17/a624/art_1er.md` | 2022-10-27..2023-06-30 | `121-1et`, `articles1er`, `complettel`, `personnesremplissant`, `présenteun`, `santéet,`, `schémade` |
| `loi/2020/07/17/a624/art_3.md` | 2021-09-15..2021-12-16 | `quetoute` |
| `loi/2020/07/17/a624/art_4.md` | 2021-09-15..2021-12-16 | `autorisédans`, `auxparagraphes`, `desparagraphes`, `lorsqueles`, `l’article4bis` |
| `loi/2020/07/17/a624/art_4.md` | 2022-10-27..2023-03-31 | `autorisédans`, `auxparagraphes`, `desparagraphes`, `lorsqueles`, `l’article4bis` |
| `loi/2020/07/17/a624/art_4bis.md` | 2021-09-15..2021-12-16 | `dedix-neuf`, `prévuesaux`, `sportifslicenciés` |
| `loi/2020/07/17/a624/art_7.md` | 2021-09-15..2022-01-11 | `dusixième`, `dépistageà`, `ouen` |
| `loi/2020/07/17/a624/art_10.md` | 2021-09-15..2022-01-11 | `SARS-CoV-2et`, `parla` |
| `loi/2020/07/17/a624/art_10.md` | 2022-10-27..2026-08-28 | `SARS-CoV-2et`, `parla` |
| `loi/2020/07/17/a624/art_11.md` | 2021-09-15..2022-01-11 | `lerapport`, `l’alinéa3` |
| `loi/2020/07/17/a624/art_16.md` | 2021-09-15..2022-01-11 | `d’Étatpeuvent` |
| `loi/2020/07/17/a624/art_16.md` | 2022-10-27..2023-06-30 | `d’Étatpeuvent` |
| `loi/2020/07/17/a624/art_16bis.md` | 2021-09-15..2022-01-11 | `vétérinaireset` |
| `loi/2020/07/17/a624/art_16bis.md` | 2022-10-27..2023-06-30 | `vétérinaireset` |
| `loi/2020/07/17/a624/art_16sexties.md` | 2021-09-15..2023-06-30 | `mesureau` |
| `loi/2020/07/17/a624/art_3bis.md` | 2022-10-27..2023-06-30 | `complettel` |
| `loi/2020/07/17/a624/art_3quater.md` | 2022-10-27..2023-06-30 | `dequarante-huit`, `devingt-quatre` |
| `loi/2020/07/17/a624/art_9.md` | 2022-10-27..2023-03-31 | `applicationde` |
