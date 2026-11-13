# The plan: every source a Luxembourg lawyer or citizen needs

This is the plan for this repository, part by part, with what is published so far. It is regenerated with each documentation commit, so the gap can be followed over time.

**53.8%** of the plan is published, weighted by how binding each source is and how often it is used. Updated 2026-11-13 02:54 UTC.

| Part | Will be in | Weight | Progress | How | Status |
| --- | --- | ---: | --- | --- | --- |
| **Primary legislation** | | | | | |
| Constitution | constitution/1868/10/17/n1/ | 8.1% | 1 of 1 acts · 100.0% | every consolidated version since 1868, each change credited to the law that made it | done |
| Laws (in force and repealed) | loi/ | 24.2% | 9,264 of 9,265 acts (1,938 as metadata and link) · 100.0% | the text as published in the Mémorial, or the latest consolidated text; repealed laws leave the record on the day they cease to be in force | done |
| **Government secondary legislation** | | | | | |
| Règlements grand-ducaux | rgd/ | 14.1% | 2,824 of 15,402 acts (2,824 as metadata and link) · 18.3% | as the laws | collecting |
| Arrêtés grand-ducaux and royaux grand-ducaux, arrêtés | agd/, argd/, a/ | 5.1% | 9,687 of 19,014 acts (9,687 as metadata and link) · 50.9% | as the laws; acts about named persons (appointments, decorations, naturalisations) as metadata and link only | collecting |
| Government in Council, royal and other decrees | agc/, rgc/, dgc/, igc/, ar/, ord/, ordr/, ogd/, dec/, rap/, reex/, reg/, d/ | 1.5% | 556 of 1,395 acts (556 as metadata and link) · 39.9% | as the laws | collecting |
| **Ministerial and authority acts** | | | | | |
| Règlements ministériels | rmin/ | 6.1% | 1,215 of 6,106 acts (1,215 as metadata and link) · 19.9% | as the laws | collecting |
| Arrêtés ministériels | amin/ | 4.0% | 5,174 of 12,766 acts (5,174 as metadata and link) · 40.5% | as the laws; individual decisions about named persons as metadata and link only | collecting |
| Circulars, instructions and decisions | cmin/, imin/, dmin/ | 1.0% | 1,323 of 1,678 acts (1,323 as metadata and link) · 78.8% | as the laws | collecting |
| CSSF, BCL and ILR regulations, internal rules | rcsf/, rbcl/, rilr/, ri/ | 3.0% | 26 of 801 acts (26 as metadata and link) · 3.2% | as published in the Mémorial | collecting |
| **Local acts** | | | | | |
| Règlements communaux (Mémorial B notices of the 100 communes) | local/<commune>/ | 4.0% | 16,554 of 33,351 acts (16,554 as metadata and link) · 49.6% | the Mémorial B notice of each communal regulation, by commune and date | collecting |
| Temporary traffic regulations and coordinated communal texts | local/<commune>/ (rtc, tc) | 1.0% | 435 of 1,791 acts (435 as metadata and link) · 24.3% | as published in the Mémorial | collecting |
| Communal regulations in full (each commune's own register) | local/<commune>/reglements/ | 3.0% | target to be counted | each commune's published regulations, where it publishes them | planned |
| **Case law** | | | | | |
| Cour constitutionnelle | acc/ | 3.0% | 49 of 209 acts (49 as metadata and link) · 23.4% | the judgments as published in the Mémorial A | collecting |
| Juridictions administratives | jurisprudence/admin/ | 3.0% | 0 of 422 acts · 0.0% | the decisions as published (anonymised by the courts) | planned |
| Cour de cassation and other judicial courts | jurisprudence/<court>/ | 4.0% | 654 of 75,001 acts (92 as metadata and link) · 0.9% | the courts' own open data (data.public.lu, CC BY-ND): pseudonymised decisions verbatim; scanned ones as metadata and link; target estimated | collecting |
| **Oversight and advice** | | | | | |
| Conseil d'État opinions, Cour des comptes, Médiateur | avis/conseil-etat/ | 2.0% | 1,928 of 7,336 acts (15 as metadata and link) · 26.3% | the Conseil d'État's own open data (data.public.lu, CC BY-ND), each opinion verbatim; Cour des comptes and Médiateur planned | collecting |
| **EU and international** | | | | | |
| Treaties, conventions, protocols | conv/, prot/, acco/ | 3.0% | 172 of 552 acts (172 as metadata and link) · 31.2% | as published in the Mémorial A; the approving laws are in loi/ | collecting |
| EU transposition links | data/eu-transposition.csv | 3.0% | 3,354 of 3,354 records · 100.0% | Legilux's transposition records (jolux:transposes) for each act | done |
| **Parliament** | | | | | |
| Bills and parliamentary resolutions (not law) | data/chambre/projets-et-propositions-de-loi.csv, res/ | 3.5% | 4,595 of 4,606 bills and acts (2 as metadata and link) · 99.8% | Chamber of Deputies bills and their stages, labelled "not law"; resolutions as published | collecting |
| **Publications** | | | | | |
| Mémorial publications: notices, corrigenda, republished texts, miscellany | pa/, rect/, trep/, div/, rv/, st/, rtde/, rtf/ | 3.0% | 15,494 of 49,454 acts (15,494 as metadata and link) · 31.3% | as published; notices about named persons as metadata and link only | collecting |

Targets are Legilux's own counts of acts of each kind (its SPARQL endpoint, 2026-11-13). Progress counts what is on `main`: acts committed as text, plus acts listed in `data/actes/<kind>.csv` with metadata and the official link only (acts naming private persons, acts Legilux has only as a scanned PDF, acts not yet in force). A repealed act is committed with its text and then removed on the day it ceased to be in force, so it is in the history, not in the latest tree. Folders not on `main` yet will appear as the parts are published.

Source and licence: Legilux open data (data.legilux.public.lu), published by the Ministère d'État, Service central de législation, under CC BY 4.0. See `TERMS.md`.
