# Spanish translation guide for bestofai.io

Read this before translating anything into `content_es/`. It applies to every file type.

## Voice

- Neutral international Spanish (no regionalisms from one country). Spelling follows the RAE.
- Address the reader as **tú** or avoid the pronoun by using impersonal phrasing ("Se puede...", "Sirve para..."). Never "usted", never "vosotros".
- Write the way a knowledgeable person would explain the product to a friend. Plain, specific, a little dry. No hype.
- Translate meaning, not words. Reorder sentences so they read as if written in Spanish first. A literal translation that sounds stiff is wrong even if every word is correct.
- Keep the same facts, numbers and claims as the English. Do not add information, opinions or marketing, and do not drop details.
- Same structure: same number of paragraphs, same Markdown, same links in the same order.

## Avoid translated-AI tone

The English copy was rewritten to avoid AI-sounding patterns. Keep it that way in Spanish:

- No inflated words ("revolucionario", "innovador", "potente", "increíble", "sin igual", "de vanguardia") unless the English says it.
- No filler openings ("Cabe destacar que", "Es importante señalar", "En el mundo actual", "En resumen").
- No stacks of three adjectives or three verbs where the English has one.
- No "no solo... sino también..." unless the English has that construction.
- Prefer a plain verb ("ofrece", "permite", "incluye", "sirve para") over "se erige como", "juega un papel clave", "ofrece una solución integral".
- Avoid gerund chains ("permitiendo, facilitando y mejorando...").
- Do not overuse the passive or "se" constructions when an active sentence is natural.
- Mixed lengths are fine. Do not make every sentence the same shape.
- Use "—" sparingly; a comma, colon or full stop usually reads better in Spanish.

## What never changes

- Frontmatter keys, slugs, URLs, tool/company/category slugs, tags, ranks, prices, dates, numbers, `price` values (`Free`, `Freemium`, `Paid`), `model_type`, `hardware_type`, `skill_type`, `alternatives`, `specific_tools`, `general_tools`.
- Product, company, model and brand names (ChatGPT, Claude, Midjourney, NVIDIA RTX 4090, GPT-5...). Do not translate or localize them.
- Code, commands, file names, API names, model IDs, version numbers, units (GB, TFLOPS, MHz).
- Markdown structure and link targets.
- Section headings in English code blocks, shell output, quoted UI strings of the English product (keep the English label and optionally explain it in Spanish in parentheses the first time).

## Terms

Keep in English (Spanish speakers in tech use them as is): prompt, fine-tuning, RAG, API, SDK, token(s), embedding(s), open source (but "código abierto" in running prose), freemium, no-code, low-code, pull request, issue, commit, GitHub, benchmark, workflow (use "flujo de trabajo" in running prose), dashboard (use "panel" if natural), plugin, chatbot, startup, awesome list, frontmatter, backlink, nofollow, SEO, CRM, SaaS, GPU, CPU, VRAM, LLM.

| English | Spanish |
|---|---|
| AI | IA |
| AI tool | herramienta de IA |
| AI agent | agente de IA |
| Agent Skills / skill | Agent Skills / skill (plural: skills) |
| assistant | asistente |
| generator | generador |
| image / video / audio generation | generación de imágenes / vídeo / audio |
| model / large language model | modelo / gran modelo de lenguaje (LLM) |
| open-weight | de pesos abiertos |
| runs locally / at home | funciona en local / en casa |
| free tier | nivel gratuito |
| paid plan | plan de pago |
| free trial | prueba gratuita |
| pricing | precios |
| subscription | suscripción |
| enterprise | empresas (plan para empresas) |
| team / teams | equipo / equipos |
| workspace | espacio de trabajo |
| integration | integración |
| browser extension | extensión de navegador |
| mobile app | app móvil |
| desktop app | app de escritorio |
| real time | tiempo real |
| leaderboard | ranking |
| tag | etiqueta |
| profession | profesión |
| alternative | alternativa |
| dead / no longer active | descontinuada / ya no está activa |
| handpicked | elegido a mano |
| curated | seleccionado |
| hardware / GPU / accelerator | hardware / GPU / acelerador |
| context window | ventana de contexto |
| parameters | parámetros |
| fine-tuned | ajustado (fine-tuned) |
| open source | de código abierto |
| video | vídeo (with accent, RAE) |
| email | correo electrónico / correo |
| website | sitio web |
| chat | chat |
| prompt | prompt |
| workflow | flujo de trabajo |
| automation | automatización |
| spreadsheet | hoja de cálculo |
| presentation / slides | presentación / diapositivas |
| note-taking | toma de notas |
| meeting | reunión |
| transcription | transcripción |
| voice | voz |
| dubbing | doblaje |
| subtitle / caption | subtítulo |
| design | diseño |
| coding | programación |
| developer | desarrollador / desarrolladora (use "desarrolladores" in plural, or "equipos de desarrollo") |
| researcher | investigador / investigadora (prefer plural or neutral phrasing) |

Category names (use exactly these in `category_name`, they are generated from `data/categories_es.yaml`): see that file. Model/skill/hardware type labels: see `i18n/es.yaml` keys `enum_*`.

## Gender and people

Prefer plural or collective forms ("desarrolladores", "equipos", "quienes escriben", "las personas que...") over he/she. Never assume a person's gender.

## Fields

- `description`: one or two sentences, as long as the English. Keeps the English meaning, written for search results in Spanish (the main keyword near the start, no keyword stuffing).
- `subtitle`: a short phrase, no final period if the English has none.
- `category_name`: the exact Spanish name from `data/categories_es.yaml` for that tool's `category` slug.
- `dead_reason`: one plain sentence, same facts.
- Professions: `name` is the profession as a plural noun phrase that fits "Mejores herramientas de IA para {name}" (for example "Agentes de viajes", "Investigadores académicos"). `title` is "IA para {name}". The `icon` is an emoji and stays.
- Body (Markdown): same paragraphs, same order. Keep inline links, bold and code exactly.

## Workflow for a translated file

1. Read `content/<section>/<name>.md` (English source).
2. Write `content_es/<section>/<name>.md` with the same frontmatter (only the text keys translated) and the translated body.
3. Run `python3 scripts/validate-translation.py --stamp content_es/<section>/<name>.md`. It adds `i18n_source`, then checks the file against the English one. Fix every reported problem.
