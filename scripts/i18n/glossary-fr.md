# French translation guide for bestofai.io

Read this before translating anything into `content_fr/`, `i18n/fr.yaml`, or `data/*_fr.yaml`. It applies to every file type. It mirrors `scripts/i18n/glossary-es.md`: same facts, same structure, French voice.

## Voice

- Neutral international French, spelling and accents as in France (no Quebec-only terms such as "courriel" or "clavardage", no Belgian or Swiss variants).
- Address the reader as **tu**, or avoid the pronoun with "on" or an impersonal phrase ("On peut...", "Ça sert à..."). Never "vous".
- Write the way a knowledgeable person would explain the product to a friend. Plain, specific, a little dry. No hype.
- Translate meaning, not words. Reorder sentences so they read as if written in French first. A literal translation that sounds stiff is wrong even if every word is correct.
- Keep the same facts, numbers and claims as the English. Do not add information, opinions or marketing, and do not drop details.
- Same structure: same number of paragraphs, same Markdown, same links in the same order.
- French typography in prose: a space before `:` `;` `!` `?`, and apostrophes in *d'IA*, *l'outil*, *qu'il*. In YAML, prefer double quotes when the value contains an apostrophe.

## Brand

- Keep the product name **Best of AI** unchanged. Use **IA** only in the surrounding French prose. Do not rename the brand to "Best of IA".

## Avoid translated-AI tone

The English copy was rewritten to avoid AI-sounding patterns. Keep it that way in French:

- No inflated words ("révolutionnaire", "innovant", "puissant", "incroyable", "inégalé", "de pointe", "à la pointe", "ultime") unless the English says it.
- No filler openings ("Il convient de noter", "Il est important de", "Dans le monde actuel", "En résumé", "Force est de constater").
- No stacks of three adjectives or three verbs where the English has one.
- No "non seulement... mais aussi..." unless the English has that construction.
- Prefer a plain verb ("propose", "permet", "inclut", "sert à") over "s'érige comme", "joue un rôle clé", "offre une solution complète".
- Avoid gerund chains ("permettant, facilitant et améliorant...").
- Do not overuse the passive when an active sentence is natural.
- Mixed lengths are fine. Do not make every sentence the same shape.
- Use "—" sparingly; a comma, colon or full stop usually reads better in French.

## What never changes

- Frontmatter keys, slugs, URLs, tool/company/category slugs, tags, ranks, prices, dates, numbers, `price` values (`Free`, `Freemium`, `Paid`), `model_type`, `hardware_type`, `skill_type`, `alternatives`, `specific_tools`, `general_tools`.
- Product, company, model and brand names (ChatGPT, Claude, Midjourney, NVIDIA RTX 4090, GPT-5...). Do not translate or localize them.
- Code, commands, file names, API names, model IDs, version numbers, units (GB, TFLOPS, MHz, nm). Keep "16 GB", not "16 Go".
- Markdown structure and link targets.
- Section headings inside code blocks, shell output, and quoted UI strings of the English product (keep the English label).
- The word **Best of AI**.

## Numbers

- Frontmatter numbers stay identical to English, including `500000` or `16`.
- In prose, the thousands separator is a space (`500 000`) and the decimal mark is a comma (`1,5`).
- Short scale: English *billion* (10^9) is **milliard**. English *trillion* (10^12) is **billion**. Do not use *trillion* for 10^12.

## Terms

Keep in English (French tech readers use them as is): prompt, fine-tuning, RAG, API, SDK, token(s), embedding(s), open source, freemium, no-code, low-code, pull request, issue, commit, GitHub, benchmark, plugin, chatbot, startup, awesome list, frontmatter, backlink, nofollow, SEO, CRM, SaaS, GPU, CPU, VRAM, LLM, dashboard when "tableau de bord" sounds heavy in a short label, workflow when it is the product term.

In running prose, prefer the French word from the table when one is listed.

| English | French |
|---|---|
| AI | IA |
| AI tool | outil d'IA |
| AI agent | agent d'IA |
| Agent Skills / skill | Agent Skills / skill (plural: skills) |
| assistant | assistant |
| generator | générateur |
| image / video / audio generation | génération d'images / de vidéo / audio |
| model / large language model | modèle / grand modèle de langage (LLM) |
| open-weight | à poids ouverts |
| runs locally / at home | tourne en local / à la maison |
| free tier | offre gratuite |
| paid plan | offre payante |
| free trial | essai gratuit |
| pricing | tarifs |
| subscription | abonnement |
| enterprise | entreprises (offre pour les entreprises) |
| team / teams | équipe / équipes |
| workspace | espace de travail |
| integration | intégration |
| browser extension | extension de navigateur |
| mobile app | app mobile |
| desktop app | app de bureau |
| real time | temps réel |
| leaderboard | classement |
| tag | étiquette |
| profession | métier |
| alternative | alternative |
| dead / no longer active | arrêté / n'est plus actif |
| handpicked | choisi à la main |
| curated | sélectionné |
| hardware / GPU / accelerator | hardware / GPU / accélérateur |
| context window | fenêtre de contexte |
| parameters | paramètres |
| fine-tuned | ajusté (fine-tuning) |
| open source | open source |
| video | vidéo |
| email | e-mail |
| website | site web |
| chat | chat |
| prompt | prompt |
| workflow | flux de travail |
| automation | automatisation |
| spreadsheet | tableur |
| presentation / slides | présentation / diapositives |
| note-taking | prise de notes |
| meeting | réunion |
| transcription | transcription |
| voice | voix |
| dubbing | doublage |
| subtitle / caption | sous-titre |
| design | design |
| coding | programmation |
| developer | développeur (plural: développeurs, or "équipes de développement") |
| researcher | chercheur (prefer plural or a collective) |
| makers | amateurs |
| prosumer | utilisateurs avancés |

Category names (use exactly these in `category_name`) come from `data/categories_fr.yaml`. Model, skill and hardware type labels come from `i18n/fr.yaml` keys `enum_*`.

## Gender and people

Prefer a plural or a collective ("développeurs", "équipes", "les gens qui écrivent"). Use the ordinary masculine plural as the generic form. Do not use the point médian or doubled forms ("développeur·euse", "développeur(se)"). Never assume a named person's gender.

## Fields

- `description`: one or two sentences, as long as the English. Same meaning, written for French search results (the main keyword near the start, no keyword stuffing).
- `subtitle`: a short phrase, no final period if the English has none.
- `category_name`: the exact `name` from `data/categories_fr.yaml` for that tool's `category` slug. Copy it. Do not invent a variant.
- `dead_reason`: one plain sentence, same facts.
- Professions: `name` is a lowercase plural noun phrase that fits "Meilleurs outils d'IA pour {name}", article included when French needs it (for example "les chercheurs académiques"). `title` is "IA pour {name}" with that same phrase. The `icon` is an emoji and stays.
- Categories: `title` is "Meilleurs outils d'IA : {name}" using the overlay name. `name` matches `data/categories_fr.yaml`.
- Model categories: `title` is "Meilleurs modèles d'IA : {name}". Skill categories: `title` is "Meilleures Agent Skills : {name}". `filter_field`, `filter_value` and `slug` stay English.
- Body (Markdown): same paragraphs, same order. Keep inline links, bold and code exactly. Link URLs stay identical and in the same order.

## Workflow for a translated file

1. Read `content/<section>/<name>.md` (English source).
2. Write `content_fr/<section>/<name>.md` with the same frontmatter (only the text keys translated) and the translated body.
3. Run `python3 scripts/validate-translation.py --stamp --lang fr content_fr/<section>/<name>.md`. It adds `i18n_source`, then checks the file against the English one. Fix every reported problem.
