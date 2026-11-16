---
title: 'Kimi K2.7 Code'
name: 'Kimi K2.7 Code'
slug: 'kimi-k2-7-code'
subtitle: 'Offenes agentisches Programmiermodell von Moonshot, abgestimmt auf Tool-Nutzung und lang laufende Aufgaben'
description: 'Offenes agentisches Programmiermodell von Moonshot, abgestimmt auf Tool-Nutzung und lang laufende Aufgaben'
company: 'moonshot-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-06-12'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.95
output_price_usd_per_m: 4.0
api_available: true
humaneval_score: 90.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: '7d2adc3dc4a7'
---

Kimi K2.7 Code ist Moonshot AIs auf Programmierung spezialisiertes Modell und erschien im Juni 2026 als angepasste Variante von Kimi K2.6. Es behält die Mixture-of-Experts-Architektur mit einer Billion Parametern insgesamt, etwa 32 Milliarden aktiven Parametern und einem Kontextfenster von 256.000 Tokens bei. Feinabgestimmt wurde es auf langfristige Programmieraufgaben und die Zerlegung agentischer Aufgaben. Moonshot berichtet gegenüber K2.6 von Verbesserungen um rund 22 Prozent bei Kimi Code Bench v2, elf Prozent bei Program Bench und 31,5 Prozent bei MLS Bench Lite. Gleichzeitig benötige es pro Aufgabe etwa 30 Prozent weniger Schlussfolgerungstokens, was den effektiven Betrieb in Agentenschleifen günstiger macht. Das Modell läuft immer im Thinking-Modus und bietet keinen Modus ohne Schlussfolgern. Neben Code akzeptiert es Text-, Bild- und Videoeingaben. Die offenen Gewichte liegen auf Hugging Face; Moonshots API ist bei Ein- und Ausgabetokens deutlich günstiger als geschlossene Konkurrenzmodelle wie Claude Opus und GPT-5.5.
