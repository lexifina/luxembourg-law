# Terms of the sources

Checked on 2026-11-13 by Lexifina, before the record was extended beyond the Constitution and the laws in force.

## Legilux open data: CC BY 4.0

Every text and every date in this repository comes from the open-data channel of Legilux, the official journal of the
Grand Duchy: the SPARQL endpoint `https://data.legilux.public.lu/sparqlendpoint` and the files it lists under
`https://data.legilux.public.lu/filestore/`.

The national open-data portal lists that channel as the dataset "Legilux - Journal officiel du Grand-Duché de
Luxembourg" (`https://data.public.lu/fr/datasets/legilux-journal-officiel-du-grand-duche-de-luxembourg-1/`), published by
the Ministère d'État - Service central de législation, under the licence **CC BY 4.0** (`cc-by` in the portal's own
metadata, dataset created 2022-07-08, last modified 2026-08-24). Its description says the project "permet de récupérer
et réutiliser aussi bien les fichiers de contenu que les métadonnées descriptives de la législation et des projets
législatifs du Luxembourg", made available "avec une licence qui autorise leur réutilisation par les entreprises, le
monde associatif ou toute personne intéressée".

So the content files (the Akoma Ntoso XML of each act and each consolidated version) and the metadata are reused here
under CC BY 4.0, with the attribution in [`LICENSE`](LICENSE).

## legilux.public.lu, the website

The website's own conditions page (`https://legilux.public.lu/editorial/use-conditions`, as served on 2026-11-13) is a
privacy and cookie policy; it says nothing about reproducing the texts. An earlier note (2026-11-03) recorded website
wording that reserved reproduction to written permission; the record is not built from the website, only from the open
data above, whose licence is explicit. The website is linked from every commit (`Source:`) as the place to read the
official text.

## Personal data

Legilux publishes acts that concern named private persons (appointments, decorations, naturalisations, individual
authorisations, Mémorial B notices). This record does not reproduce those texts: they are listed in
`data/actes/<kind>.csv` with their kind, dates and official link only, without their title (titles name the persons). Court decisions are taken only
as the courts themselves anonymise them.

## Only the Mémorial is authoritative

This repository is a research aid. Only the Journal officiel (Mémorial) is authoritative; the consolidated texts on
Legilux, and so this repository, are not.
