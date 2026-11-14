# Luxembourg : l’histoire du droit dans git

**Français** · **[Or read it in English](README.en.md)**

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/fr/effort-dark.svg">
<img alt="Le droit luxembourgeois dans ce dépôt : ce qu’il contient, les modifications par année d’entrée en vigueur, l’exhaustivité au regard des sources officielles et l’exactitude de son contenu" src="data/fr/effort-light.svg" width="880">
</picture>

Le droit luxembourgeois sous forme d’historique git : un fichier par article, un commit par version au jour de son entrée en vigueur, et pour auteur de chaque commit l’acte qui a fait la modification. `git blame` nomme l’acte à l’origine de chaque article ; `git log` énumère chaque modification d’un article ; le choix d’une date donne le texte en vigueur ce jour-là.

Fait partie de [lexifina/global-law](https://github.com/lexifina/global-law), un historique git unique pour le droit de chaque pays : ce dépôt contient le droit national luxembourgeois, que global-law lit dans `luxembourg/national/acts/`.

**Ce qu’il contient aujourd’hui :** la Constitution et 6 895 lois issues de Legilux, le journal officiel, avec toutes les versions de la Constitution depuis 1868 (39 textes) et de la loi Covid-19 du 17 juillet 2020 (33 textes) et le texte actuel des autres lois, ainsi que 431 lois abrogées dans l’historique ; 1 488 arrêts de la Cour de cassation ; 3 118 avis du Conseil d’État et une liste de 4 593 projets et propositions de loi, signalés comme n’étant pas du droit ; 3 354 relevés indiquant quel acte transpose quelle directive de l’UE ; et 55 449 autres actes du Mémorial, répertoriés avec leurs seules métadonnées et leur lien officiel. [`PLAN.md`](PLAN.md) énumère toutes les parties que ce dépôt doit contenir et l’avancement de chacune ; [`data/textes-en-vigueur.csv`](data/textes-en-vigueur.csv) répertorie les lois en vigueur, et `data/actes/<kind>.csv` tous les autres actes, par catégorie.

Chaque acte se trouve dans le dossier de son ELI, `<kind>/<année>/<mois>/<jour>/<numéro>/`, un fichier par article (`texte.md` pour un acte sans articles) : `constitution/1868/10/17/n1/` est la Constitution et `loi/2006/07/31/n2/` le Code du travail.

Le texte est en français, tel que Legilux le publie. Les textes en allemand et en luxembourgeois et une traduction anglaise ne font pas partie de ce registre.

## Les questions, en commandes git

| Question | Commande |
| --- | --- |
| Toutes les modifications de l’article 1er de la Constitution | `git log -p --word-diff -- constitution/1868/10/17/n1/art_1er.md` |
| Quel acte a écrit chaque ligne de l’article 1er ? | `git blame constitution/1868/10/17/n1/art_1er.md` |
| Toutes les versions de la Constitution, avec le jour de leur entrée en vigueur | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constitution/1868/10/17/n1` |
| L’article 1er tel qu’en vigueur le 1er janvier 1990 | `python tools/en_vigueur_au.py 1990-01-01 constitution art_1er` |

**En dehors de git**, nous mettons aussi ce registre à disposition du public, gratuitement :

- **[Interrogez Claude sur le droit luxembourgeois](https://global-law.lexifina.com/v1/try_claude?country=luxembourg)** : ouvre Claude avec une première question prête.
- **[Interrogez ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=luxembourg)** : la même question dans ChatGPT.
- **[Appelez l’API dans votre navigateur](https://global-law.lexifina.com/v1/search_law?query=cong%C3%A9+annuel&jurisdictions=luxembourg)** : une recherche de « congé annuel » dans le droit luxembourgeois, renvoyée en JSON. La documentation est [ici](https://lexifina.com/api/global-law).

Les deux assistants lisent le registre par le connecteur gratuit Global law (MCP, `https://global-law.lexifina.com/mcp`) ; la première fois, la conversation vous donne le lien qui l’ajoute. Posez vos questions en français ou en anglais.

**Hébergez-le vous-même, simplement.** Il suffit de git et de Python, et les outils tournent sur votre machine :

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add luxembourg/national/acts
python3 tools/law.py show 2026-01-01 luxembourg/national/acts/constitution/1868/10/17/n1/art_1er.md
```

Ouvert dans Claude Code, Cursor, VS Code ou Codex, le clone démarre aussi un serveur MCP local doté des mêmes outils ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Chaque commit est daté à midi, heure de Luxembourg (Europe/Luxembourg), du jour où le texte est entré en vigueur, et porte ce jour dans son trailer `In-force:` :

- pour la Constitution et la loi Covid-19, le jour à partir duquel s’applique chaque version consolidée (la `dateApplicability` de Legilux) ; les autres dates de la loi modificative figurent dans `Adopted:`, `Published:` et, lorsque Legilux indique un autre jour, `Law-in-force:` ;
- pour toute autre loi, son entrée en vigueur (texte tel que publié) ou le jour à partir duquel s’applique son texte consolidé actuel ; une loi abrogée est supprimée par un second commit le jour où, selon Legilux, elle a cessé d’être en vigueur ; les arrêts et les avis sont datés du jour où ils ont été rendus ;
- git ne peut pas enregistrer de dates antérieures à 1970 : les 2 514 commits antérieurs (des lois depuis 1790) sont donc datés du 1970-01-01, le jour réel figurant dans `In-force:`. Interrogez une date avec `tools/en_vigueur_au.py`, et non avec `git log --before`.

Chaque modification de la Constitution et de la loi Covid-19 est attribuée à la loi qui l’a faite (`Loi du 15 mai 1919 (n1)`), d’après les marqueurs et relevés de modification du XML de Legilux. Un texte tel que publié est attribué à la loi elle-même ; un texte consolidé actuel, une abrogation sans acte abrogatoire unique et les modifications qu’aucune loi n’explique (`Kind: typesetting`, `Kind: unexplained`) à `Service central de législation (Legilux)` ; les arrêts et les avis à leur juridiction ou au Conseil d’État. La Constitution de 2023 a renuméroté tous les articles : elle forme un seul commit, attribué à la loi A 29 du 17 janvier 2023, et à partir du 1er juillet 2023 `art_32.md` est le nouvel article 32, et non l’ancien.

## Comment il est vérifié

- `tools/check_repo.py` relit depuis git les 72 textes de la Constitution et de la loi Covid-19 au jour à partir duquel chacun s’applique et compare chaque fichier d’article, octet par octet, au texte reconstruit à partir du XML de Legilux (dont le sha256 est vérifié par rapport à `data/versions.json`), puis mot par mot ; les résultats figurent dans [`REPRODUCE.md`](REPRODUCE.md).
- Avant le commit de tout autre acte, chaque mot du XML de Legilux qui le concerne (hors texte barré et notes) doit figurer dans ses fichiers, dans l’ordre ; un acte qui échoue est répertorié, sans commit.
- Les arrêts et les avis sont la couche texte du PDF publié, à l’identique ; ceux qui sont numérisés, dont le texte serait issu d’une OCR, sont répertoriés, sans commit.
- L’historique ne fait que s’allonger : une correction est un commit à part entière (`Kind: correction`), consigné dans [`CORRECTIONS.md`](CORRECTIONS.md).

## Ce qu’il ne montre pas

- **Les versions antérieures de la plupart des lois.** Hormis la Constitution et la loi Covid-19, chaque loi a un seul texte, son texte consolidé actuel ou, lorsque Legilux ne l’a jamais consolidée, le texte tel que publié ; les lois modificatives ne sont pas encore retracées.
- **La plupart des règlements et autres actes sous forme de texte.** Les 55 449 actes répertoriés avec métadonnées et lien (règlements grand-ducaux, arrêtés, actes ministériels, règlements communaux, avis du Mémorial) sont pour la plupart des actes que Legilux ne possède que sous forme de pages numérisées du Mémorial ; Legilux compte 15 402 règlements grand-ducaux et 33 351 règlements communaux.
- **Les actes concernant des personnes privées nommément désignées** adoptés depuis 1926 (nominations, décorations, naturalisations, changements de nom) : répertoriés sans leur intitulé, et non sous forme de texte.
- **La plus grande partie de la jurisprudence.** Des décisions des juridictions judiciaires (environ 75 000, estimation), seules celles de la Cour de cassation figurent ici ; celles des juridictions administratives (422) et de la Cour constitutionnelle (209, dont 49 répertoriées) n’y figurent pas encore sous forme de texte (voir `PLAN.md`).
- **Les notes et le texte barré**, qui sont omis des fichiers d’articles.

## Sources

| Source | Nature | Versions antérieures | Remarques |
| --- | --- | --- | --- |
| Données ouvertes de [Legilux](https://legilux.public.lu) ([SPARQL](https://data.legilux.public.lu/sparqlendpoint)), Ministère d’État, Service central de législation | Journal officiel (Mémorial A et B) et textes consolidés | toutes les versions consolidées pour la Constitution et la loi Covid-19 ; l’actuelle pour les autres lois consolidées | Seul le Mémorial fait foi |
| [Cour de cassation](https://data.public.lu/fr/datasets/cour-de-cassation-1/) sur data.public.lu (Administration judiciaire) | Arrêts | tels que publiés | Pseudonymisés par l’éditeur |
| [Avis du Conseil d’État](https://data.public.lu/fr/datasets/avis-du-conseil-detat/) sur data.public.lu | Avis sur les projets de loi et de règlement | tels que publiés | Signalés comme n’étant pas du droit |
| [Chambre des Députés](https://data.public.lu/fr/organizations/627e56d3a9bc6b2dd946a3ea/) sur data.public.lu | Projets et propositions de loi depuis 1965 (`data/chambre/`) | tels que publiés | Signalés comme n’étant pas du droit |

## Licence

Voir [`LICENSE`](LICENSE). Les textes juridiques et leurs données sont réutilisés à partir des données ouvertes de Legilux sous licence CC BY 4.0, avec l’attribution que donne LICENSE et sans modification du libellé ; les arrêts et les avis sont reproduits à l’identique sous licence CC BY-ND 4.0 et les projets de loi sous CC0 ([`TERMS.md`](TERMS.md)). Les contributions propres de Lexifina sont placées sous CC0 1.0.

Aucun modèle d’IA n’a écrit ni modifié de texte juridique ; les scripts ont été écrits par un modèle d’IA (voir [`REPRODUCE.md`](REPRODUCE.md)).

Ceci est une traduction de la version anglaise ([README.en.md](README.en.md)) ; en cas de divergence, la version anglaise fait foi.

## En savoir plus

Dans le dépôt [lexifina/global-law](https://github.com/lexifina/global-law) (pages en anglais) :

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): toutes les fonctionnalités et ce que chaque corpus doit prendre en charge (`git blame`, `law.py`, outils MCP)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions et réponses · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposer une modification · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): serveur MCP · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): comment il a été construit · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): à quel point chaque corpus est à jour · [Surveillance](https://github.com/lexifina/global-law/tree/main/monitoring): si les mises à jour fonctionnent · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): comment chaque source officielle est surveillée pour repérer les modifications
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): la rapidité des outils, mesurée
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): graphiques et liens à travers le droit du monde entier
- [Vulnérabilités](https://github.com/lexifina/global-law/tree/main/vulnerabilities): erreurs dans les textes tels qu’ils ont été publiés
