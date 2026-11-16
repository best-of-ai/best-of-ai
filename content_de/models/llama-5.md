---
title: 'Llama 5'
name: 'Llama 5'
slug: 'llama-5'
subtitle: 'Metas nächstes offenes multimodales Flaggschiffmodell für Geräte und Rechenzentren'
description: 'Metas nächstes offenes multimodales Flaggschiffmodell für Geräte und Rechenzentren'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 9
release_date: '2026-07-14'
param_count: '520B (24B active)'
context_window_tokens: 2000000
modality: [text, image, audio]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 89.5
humaneval_score: 90.0
lmarena_score: 1381
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock', 'Azure AI Foundry']
date: '2026-07-19'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
i18n_source: '47cdfc96510e'
---

Llama 5 ist Metas Nachfolger der letztjährigen Llama-4-Reihe. Es nutzt erneut ein Mixture-of-Experts-Modell, vergrößert es aber auf insgesamt 520 Milliarden Parameter mit 24 Milliarden aktiven pro Token. Die größere Änderung ist das Kontextfenster von zwei Millionen Tokens – doppelt so viel wie Llama 4 Maverick. Meta bewirbt es für Aufgaben wie die Verarbeitung ganzer Codebasen oder langer Videotranskripte in einem Durchgang. Text, Bild und Audio werden nativ verarbeitet, statt Encoder nachträglich an ein reines Textmodell anzufügen. Meta zufolge übertrifft es Gemini 3.5 Pro und GPT-5.6 in mehreren offenen Benchmarks und bleibt dank sparsamer Expertenweiterleitung effizient.

Wie bei früheren Llama-Veröffentlichungen stehen die Gewichte unter der Llama-4-Community-Lizenz ab sofort auf Hugging Face bereit. Hostingpartner wie Together AI, AWS Bedrock und Azure AI Foundry bieten verwaltete Inferenz für Teams, die das Modell nicht selbst betreiben möchten. Meta beschränkt weiterhin die vollständigen kommerziellen Rechte für Unternehmen oberhalb einer bestimmten Nutzerzahl – dieselbe Ausnahme wie seit Llama 2.
