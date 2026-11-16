---
title: 'Codestral'
name: 'Codestral'
slug: 'codestral'
subtitle: 'Modell von Mistral zur Codegenerierung und -vervollständigung'
description: 'Modell von Mistral zur Codegenerierung und -vervollständigung'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral/'
price: 'Free'
rank: 6
release_date: '2024-05-29'
param_count: '22B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 0.9
api_available: true
humaneval_score: 81.1
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, code, open-weight, api]
i18n_source: '0c94b2ec4923'
---

Codestral ist Mistral AIs spezialisiertes Modell zur Codegenerierung. Es erschien im Mai 2024 mit 22 Milliarden Parametern und ist für Fill-in-the-Middle-Vervollständigung sowie die Codegenerierung in mehreren Sprachen ausgelegt. Beim Start erreichte es 81,1 Prozent pass@1 bei HumanEval und lag damit vor größeren Code-Modellen wie Code Llama 70B und DeepSeek Coder 33B. Die erste Version hatte ein Kontextfenster von 32.000 Tokens und wurde unter der Mistral AI Non-Production License veröffentlicht. Sie beschränkte die kostenlose Nutzung auf Forschung und Tests; für den produktiven kommerziellen Einsatz war eine separate Lizenz nötig.

Mistral erweiterte das Kontextfenster später auf 256.000 Tokens und veröffentlichte das Modell im April 2026 unter Apache 2.0 neu. Damit entfiel die frühere Beschränkung für kommerzielle Nutzung; der Einsatz in IDEs, Programmierassistenten und CI-Pipelines ist nun frei möglich. Codestral steht sowohl als herunterladbare Gewichte auf Hugging Face als auch über die Mistral-API zur Verfügung. Dort kostet es derzeit 0,30 US-Dollar pro Million Eingabetokens und 0,90 US-Dollar pro Million Ausgabetokens. Es konkurriert direkt mit mittelgroßen offenen Code-Modellen wie Codestral Mamba und Code Llama. Der Wechsel zu einer freizügigen Lizenz galt als bedeutende Veränderung im Bereich quelloffener Programmiermodelle.
