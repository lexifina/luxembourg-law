# Le droit luxembourgeois, modification par modification

**Français** · [English](README.en.md)

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/fr/effort-dark.svg">
<img alt="Le droit luxembourgeois dans ce dépôt : ce qu’il contient, les modifications par année d’entrée en vigueur, l’exhaustivité au regard des sources officielles et l’exactitude de son contenu" src="data/fr/effort-light.svg" width="880">
</picture>

Fait partie de [lexifina/global-law](https://github.com/lexifina/global-law), un historique git unique pour le droit de chaque pays : ce dépôt contient le droit national luxembourgeois, que global-law lit dans `luxembourg/national/acts/`.

Deux actes luxembourgeois sous forme de dépôt git : la **Constitution** (du texte de 1868, à travers 38 versions consolidées, jusqu’en 2026, y compris la Constitution révisée entrée en vigueur le 1er juillet 2023) et la **loi Covid-19 du 17 juillet 2020** (32 versions). Chaque loi modificative constitue un commit, attribué à cette loi et daté du jour où ses modifications ont pris effet, à midi, heure de Luxembourg. Le texte est le texte français publié par [Legilux](https://legilux.public.lu), le journal officiel du Grand-Duché.

## En cours d’extension à tous les actes publiés par Legilux (depuis le 13 novembre 2026)

Le registre est en cours d’extension, par des envois successifs toutes les quelques minutes, de la Constitution et des
lois en vigueur à toutes les catégories d’actes du Mémorial que contiennent les données ouvertes de Legilux.
**[`PLAN.md`](PLAN.md)** énumère chaque partie avec son avancement par rapport aux décomptes de Legilux ;
[`TERMS.md`](TERMS.md) indique les licences et la manière dont les données à caractère personnel sont traitées.

| Dossier | Contenu |
| --- | --- |
| `loi/`, `rgd/`, `agd/`, `argd/`, `a/`, `amin/`, `rmin/`, `rcsf/`, `rbcl/`, `conv/`, `acc/` ... | actes du Mémorial A, un dossier par acte, nommé d’après son ELI (`rgd/2020/03/18/a165/`) |
| `memorial-b/<kind>/` | actes du Mémorial B (publications administratives), dont les numéros peuvent reprendre ceux du Mémorial A |
| `local/<commune>/<kind>/` | règlements communaux (`rc`) et règlements temporaires de circulation (`rtc`), classés selon la commune que nomme l’avis |
| `data/actes/<kind>.csv` | tous les actes traités : avec leur texte sur `main`, ou avec leurs seules métadonnées et le lien officiel |
| `data/eu-transposition.csv` | quel acte transpose quelle directive de l’UE (relevés de transposition de Legilux) |
| `data/chambre/projets-et-propositions-de-loi.csv` | les projets et propositions de loi déposés à la Chambre des Députés depuis 1965 (ce n’est pas du droit) |
| `jurisprudence/<court>/<yyyy>/<mm>/` | décisions des juridictions judiciaires telles que l’Administration judiciaire les publie, pseudonymisées par elle (CC BY-ND) : la couche texte de chaque PDF, à l’identique ; répertoriées dans `data/jurisprudence/<court>.csv` |
| `avis/conseil-etat/<yyyy>/<mm>/` | avis du Conseil d’État sur les projets de loi et de règlement (ce n’est pas du droit), à l’identique ; répertoriés dans `data/avis/conseil-etat.csv` |

- Un fichier par article (`texte.md` pour un acte imprimé sans articles). Un acte jamais consolidé figure avec son texte
  tel que publié, attribué à l’acte lui-même et daté de son entrée en vigueur ; un acte en vigueur que Legilux consolide
  figure avec son dernier texte consolidé, sans attribution à un acte (`Kind: publisher`).
- Un acte abrogé fait l’objet d’un commit avec son texte tel que publié, puis est supprimé par un second commit le jour
  où, selon Legilux, il a cessé d’être en vigueur, attribué à l’acte abrogatoire lorsque Legilux en nomme exactement un
  (`Repealed-by:`), sinon à l’éditeur (`Kind: repeal`). `tools/en_vigueur_au.py <day> <folder>` le montre tel qu’il
  était à une date donnée.
- Répertoriés avec leurs seules métadonnées et leur lien, jamais sous forme de texte : les actes que Legilux ne possède
  que sous la forme d’un numéro numérisé du Mémorial (sans XML), les actes concernant des personnes privées nommément
  désignées (nominations, décorations, naturalisations, changements de nom ; leurs intitulés sont également omis) et
  les actes qui ne sont pas encore en vigueur.
- Les décisions et avis imprimés à partir d’une numérisation (une image par page) sont répertoriés, sans commit : leur
  couche texte est le produit d’une reconnaissance optique de caractères (OCR), et non le texte tel que rendu.
- Avant le commit de chaque acte, il est vérifié que chaque mot du XML de Legilux qui le concerne (hors texte barré et
  notes) figure dans ses fichiers, dans l’ordre ; un acte qui échoue à ce contrôle est répertorié, sans commit.

## Les questions d’un juriste, en commandes git

| Question | Commande |
| --- | --- |
| Que disait l’art. 32 de la Constitution le 1er janvier 1950 ? | `python tools/en_vigueur_au.py 1950-01-01 constitution art_32` |
| L’ensemble de la loi Covid-19 au 1er mars 2021 | `python tools/en_vigueur_au.py 2021-03-01 covid` |
| Quelle loi a écrit chaque ligne d’un article ? | `git blame constitution/1868/10/17/n1/art_15.md` |
| Toutes les modifications d’un article, avec la loi qui en est à l’origine | `git log -p constitution/1868/10/17/n1/art_32.md` |
| Tout ce qu’une loi a modifié | `git show loi/2016-10-18-n1` |
| Toutes les lois qui ont modifié la loi Covid-19, dans l’ordre | `git log --format='%(trailers:key=In-force,valueonly,separator=) %an' -- loi/2020/07/17/a624` |
| L’état d’un acte un jour où il a changé | `git checkout constitution/1989-07-14` |
| Ce qu’aucune loi n’explique | `git log --grep='Kind: unexplained' --grep='Kind: typesetting'` |

Les lois et leurs dates figurent dans [`lois.csv`](lois.csv) ; les articles de chaque acte, avec le nombre de modifications de chacun, figurent dans le `README.md` de son dossier.

## Les dates, et celle que nous retenons

Une loi luxembourgeoise est adoptée (`Adopted:`), publiée au Mémorial (`Published:`) et prend effet (par défaut le quatrième jour qui suit sa publication). **Les commits sont datés du jour à partir duquel le texte modifié s’applique**, soit la `dateApplicability` de Legilux pour la version consolidée : la date qui détermine quel texte régit une affaire. Chaque commit porte les autres dates sous forme de trailers, ainsi que `Law-in-force:` lorsque les métadonnées de Legilux relatives à la loi indiquent un autre jour.

**Git ne peut pas enregistrer de dates antérieures à 1970.** Les commits de 1868 à 1956 sont datés du 1970-01-01, à une seconde d’intervalle et dans l’ordre ; leur jour réel figure dans le trailer `In-force:` et dans les tags (`constitution/1948-05-14`). `tools/en_vigueur_au.py` lit `In-force:` et donne donc le bon texte pour n’importe quel jour.

## Comment il est vérifié

`tools/check_repo.py` relit depuis git chacun des 72 textes au jour à partir duquel il s’applique et compare chaque fichier d’article, octet par octet, au texte reconstruit à partir du XML de Legilux (après avoir vérifié le sha256 du XML par rapport à [`data/versions.json`](data/versions.json)). Un second contrôle confirme que chaque mot de chaque article du XML, hors texte barré et notes, figure dans le fichier, dans l’ordre. La construction est déterministe : reconstruite à partir des mêmes données, elle donne les mêmes empreintes de commit. Voir [`REPRODUCE.md`](REPRODUCE.md).

## Ce que signifie « auteur »

L’auteur d’un commit est la loi qui a fait la modification, désignée par sa nature, sa date et son ELI (`Loi du 15 mai 1919 (n1)`), avec une adresse formée à partir de son ELI et qui ne peut pas exister (`loi-1919-05-15-n1@legilux.invalid`). Ainsi, `git blame` nomme, pour chaque ligne, la loi qui l’a écrite en dernier. Les données propres à chaque version indiquent quelle loi a modifié quel article : les marqueurs de modification que Legilux imprime autour des mots modifiés, et les destinations de ses relevés de modification. Lorsqu’aucun marqueur ni relevé ne relie l’article, mais qu’exactement une loi a pris effet ce jour-là, le commit indique que la modification est attribuée **par la seule date** (`Evidence: … date`).

Les textes d’origine ont pour auteur l’acte lui-même (`Constitution du 17 octobre 1868`). Les modifications qu’aucune loi n’explique ont pour auteur `Service central de législation (Legilux)` et sont étiquetées : `Kind: typesetting` lorsque seuls les espacements ont changé, `Kind: unexplained` dans les autres cas (par exemple « Roi Grand-Duc » devenu « Grand-Duc » dans trois articles en 2020, alors que la seule loi entrée en vigueur ce jour-là révisait l’art. 95ter).

**La Constitution de 2023** constitue un seul commit, étiqueté comme remplacement, attribué à la loi A 29 du 17 janvier 2023, dont l’article 4 dispose que le texte qui y est annexé « constitue le texte de la Constitution ». Il nomme les trois autres lois de ce jour. La révision a renuméroté tous les articles : `art_32.md` après le 1er juillet 2023 n’est donc pas l’ancien art. 32. La consolidation de Legilux attribue l’ensemble du texte à une note unique nommant la loi A 26 ; le registre ne la suit pas.

## Ce qu’il ne montre pas

- Les intitulés de chapitres et de sections (ils figurent dans le `README.md` de chaque acte, et non dans l’historique), les notes et le texte barré.
- Tout acte autre que ces deux-là. La plupart des lois ordinaires n’ont que leurs deux ou trois dernières consolidations dans les données de Legilux.
- Les textes en allemand et en luxembourgeois.
- L’auteur des mots qu’une version ultérieure reproduit inchangés sous un nouveau numéro après la renumérotation de 2023.

Ce dépôt est un outil de recherche. Seul le Journal officiel (Mémorial) fait foi ; les textes consolidés de Legilux, et donc ce dépôt, ne font pas foi.

## Comment il est construit

`tools/build.py` lit le point d’accès SPARQL de Legilux et le XML Akoma Ntoso de chaque version, compare les versions successives article par article, attribue chaque modification et écrit les commits. Aucun modèle d’IA n’intervient dans sa construction ni dans sa vérification. Chaque étape, commande et décision figure dans [`REPRODUCE.md`](REPRODUCE.md).

## Licence

Source : Legilux — Journal officiel du Grand-Duché de Luxembourg (Ministère d'État, Service central de législation). Données réutilisées sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Copyright : Ministère d'État du Grand-Duché de Luxembourg - Service central de législation. Les textes ont été convertis en un fichier par article et organisés en commits ; leur libellé n’a pas été modifié. Les contributions propres de Lexifina sont placées sous CC0. Voir [`LICENSE`](LICENSE).

Ceci est une traduction de la version anglaise ([README.en.md](README.en.md)) ; en cas de divergence, la version anglaise fait foi.

## Lois en vigueur, texte actuel

Outre la Constitution et la loi Covid-19, retracées version par version, le registre contient 6 884 lois en vigueur selon Legilux (statut « in force » ou « applicable »), chacune en un commit : la version consolidée en vigueur (datée du jour à partir duquel elle s’applique, par le Service central de législation, sans attribution à une loi) ou, pour une loi jamais consolidée, le texte tel que publié au Mémorial (daté de son entrée en vigueur et attribué à la loi). Les versions antérieures seront ajoutées derrière elles, sans réécrire l’historique. Liste : `data/textes-en-vigueur.csv`.

## En savoir plus

Dans le dépôt [lexifina/global-law](https://github.com/lexifina/global-law) (pages en anglais) :

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): toutes les fonctionnalités et ce que chaque corpus doit prendre en charge (`git blame`, `law.py`, outils MCP)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions et réponses · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposer une modification · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): serveur MCP · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): comment il a été construit · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): à quel point chaque corpus est à jour · [Surveillance](https://github.com/lexifina/global-law/tree/main/monitoring): si les mises à jour fonctionnent · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): comment chaque source officielle est surveillée pour repérer les modifications
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): la rapidité des outils, mesurée
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): graphiques et liens à travers le droit du monde entier
- [Vulnérabilités](https://github.com/lexifina/global-law/tree/main/vulnerabilities): erreurs dans les textes tels qu’ils ont été publiés
