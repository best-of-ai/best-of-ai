---
title: 'Gemma'
name: 'Gemma'
slug: 'gemma'
subtitle: 'Ursprüngliche Veröffentlichung des offenen Gemma-Modells von Google, entwickelt auf Grundlage derselben Forschung wie Gemini'
description: 'Ursprüngliche Veröffentlichung des offenen Gemma-Modells von Google, entwickelt auf Grundlage derselben Forschung wie Gemini'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://blog.google/technology/developers/gemma-open-models/'
price: 'Free'
rank: 7
release_date: '2024-02-21'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 64.3
humaneval_score: 32.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Google AI Studio']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: 'b40c9be3f894'
---

Gemma ist Googles erste Familie offener Sprachmodelle. Sie erschien im Februar 2024 und basiert auf derselben Forschung wie Gemini. Die Familie umfasst Modelle mit zwei und sieben Milliarden Parametern, jeweils als Basis- und instruktionsoptimierter Checkpoint. Trainiert wurden sie mit zwei beziehungsweise sechs Billionen Tokens aus Webtexten, Mathematik und Code. Das Kontextfenster beträgt 8.192 Tokens und entspricht damit dem damaliger Modelle.

Die Veröffentlichung war bedeutsam, weil sie Entwickler:innen ein tatsächlich nutzbares kleines Modell bot, das auf einer einzelnen Consumer-GPU oder sogar einem Laptop laufen konnte, statt eine API vorauszusetzen. Die Lizenz gestattet kommerzielle Nutzung, untersagt aber bestimmte von Google benannte schädliche Anwendungen. Sie liegt damit zwischen vollständig offenen Lizenzen wie Apache 2.0 und den geschlossenen Bedingungen der meisten proprietären Modelle. Gemma wurde später von Gemma 2 und Gemma 3 abgelöst, etablierte aber das Namens- und Lizenzierungsschema, dem Google seither folgt.
