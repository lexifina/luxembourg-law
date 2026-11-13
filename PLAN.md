# The plan: every source a Luxembourg lawyer or citizen needs

This is the plan for this repository, part by part, with what is published so far. It is regenerated with each documentation commit, so the gap can be followed over time.

**37.4%** of the plan is published, weighted by how binding each source is and how often it is used. Updated 2026-11-13 02:22 UTC.

| Part | Will be in | Weight | Progress | How | Status |
| --- | --- | ---: | --- | --- | --- |
| **Primary legislation** | | | | | |
| Constitution | constitution/1868/10/17/n1/ | 8.1% | 1 of 1 acts · 100.0% | every consolidated version since 1868, each change credited to the law that made it | done |
| Laws (in force and repealed) | loi/ | 24.2% | 9,038 of 9,265 acts (1,835 as metadata and link) · 97.5% | the text as published in the Mémorial, or the latest consolidated text; repealed laws leave the record on the day they cease to be in force | collecting |
| **Government secondary legislation** | | | | | |
| Règlements grand-ducaux | rgd/ | 14.1% | 2,824 of 15,402 acts (2,824 as metadata and link) · 18.3% | as the laws | collecting |
| Arrêtés grand-ducaux and royaux grand-ducaux, arrêtés | agd/, argd/, a/ | 5.1% | 0 of 19,014 acts · 0.0% | as the laws; acts about named persons (appointments, decorations, naturalisations) as metadata and link only | planned |
| Government in Council, royal and other decrees | agc/, rgc/, dgc/, igc/, ar/, ord/, ordr/, ogd/, dec/, rap/, reex/, reg/, d/ | 1.5% | 0 of 1,395 acts · 0.0% | as the laws | planned |
| **Ministerial and authority acts** | | | | | |
| Règlements ministériels | rmin/ | 6.1% | 0 of 6,106 acts · 0.0% | as the laws | planned |
| Arrêtés ministériels | amin/ | 4.0% | 0 of 12,766 acts · 0.0% | as the laws; individual decisions about named persons as metadata and link only | planned |
| Circulars, instructions and decisions | cmin/, imin/, dmin/ | 1.0% | 0 of 1,678 acts · 0.0% | as the laws | planned |
| CSSF, BCL and ILR regulations, internal rules | rcsf/, rbcl/, rilr/, ri/ | 3.0% | 0 of 801 acts · 0.0% | as published in the Mémorial | planned |
| **Local acts** | | | | | |
| Règlements communaux (Mémorial B notices of the 100 communes) | local/<commune>/ | 4.0% | 0 of 33,351 acts · 0.0% | the Mémorial B notice of each communal regulation, by commune and date | planned |
| Temporary traffic regulations and coordinated communal texts | local/<commune>/ (rtc, tc) | 1.0% | 0 of 1,791 acts · 0.0% | as published in the Mémorial | planned |
| Communal regulations in full (each commune's own register) | local/<commune>/reglements/ | 3.0% | target to be counted | each commune's published regulations, where it publishes them | planned |
| **Case law** | | | | | |
| Cour constitutionnelle | acc/ | 3.0% | 0 of 209 acts · 0.0% | the judgments as published in the Mémorial A | planned |
| Juridictions administratives | jurisprudence/admin/ | 3.0% | 0 of 422 acts · 0.0% | the decisions as published (anonymised by the courts) | planned |
| Cour de cassation and other judicial courts | jurisprudence/judiciaire/ | 4.0% | 0 of 1 acts · 0.0% | decisions as anonymised by the courts (justice.public.lu); others as metadata and link | planned |
| **Oversight and advice** | | | | | |
| Conseil d'État opinions, Cour des comptes, Médiateur | avis/ | 2.0% | 0 of 2 acts · 0.0% | official texts as published | planned |
| **EU and international** | | | | | |
| Treaties, conventions, protocols | conv/, prot/, acco/ | 3.0% | 0 of 552 acts · 0.0% | as published in the Mémorial A; the approving laws are in loi/ | planned |
| EU transposition links | data/eu-transposition.csv | 3.0% | 3,354 of 3,354 records · 100.0% | Legilux's transposition records (jolux:transposes) for each act | done |
| **Parliament** | | | | | |
| Bills and parliamentary resolutions (not law) | projets/, res/ | 3.5% | 0 of 13 acts · 0.0% | Chamber of Deputies bills and their stages, labelled "not law"; resolutions as published | planned |
| **Publications** | | | | | |
| Mémorial publications: notices, corrigenda, republished texts, miscellany | pa/, rect/, trep/, div/, rv/, st/, rtde/, rtf/ | 3.0% | 0 of 49,454 acts · 0.0% | as published; notices about named persons as metadata and link only | planned |

Targets are Legilux's own counts of acts of each kind (its SPARQL endpoint, 2026-11-13). Progress counts what is on `main`: acts committed as text, plus acts listed in `data/actes/<kind>.csv` with metadata and the official link only (acts naming private persons, acts Legilux has only as a scanned PDF, acts not yet in force). A repealed act is committed with its text and then removed on the day it ceased to be in force, so it is in the history, not in the latest tree. Folders not on `main` yet will appear as the parts are published.

Source and licence: Legilux open data (data.legilux.public.lu), published by the Ministère d'État, Service central de législation, under CC BY 4.0. See `TERMS.md`.
