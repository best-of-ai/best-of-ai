---
title: 'Llama 4 Scout'
name: 'Llama 4 Scout'
slug: 'llama-4-scout'
subtitle: 'Kleinere, schnellere Llama-4-Variante von Meta mit einem Kontextfenster von 10 Millionen Tokens'
description: 'Kleinere, schnellere Llama-4-Variante von Meta mit einem Kontextfenster von 10 Millionen Tokens'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2025-04-05'
param_count: '109B (17B active)'
context_window_tokens: 10000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 80.5
lmarena_score: 1290
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, self-hosted]
i18n_source: 'a01f39772dca'
---

Llama 4 Scout ist das kleinere Schwestermodell der Llama-4-Veröffentlichung von Meta vom April 2025. Das Mixture-of-Experts-Modell umfasst 109 Milliarden Parameter, davon 17 Milliarden aktiv pro Token und verteilt auf 16 Experten. Herausragend ist das Kontextfenster von bis zu zehn Millionen Tokens – weit mehr als andere offene Modelle zum Start boten. Das eignet sich für Aufgaben wie die Zusammenfassung einer vollständigen Codebasis oder einer langen Dokumentensammlung in einem Durchgang. Wie Maverick ist Scout nativ multimodal und wurde für die gemeinsame Verarbeitung von Text und Bildern trainiert. Meta positionierte es als schnellere, günstigere Option, die in öffentlichen Benchmarks dennoch Gemma 3 und Gemini 2.0 Flash-Lite übertrifft. Quantisiert läuft es auf einer einzelnen H100-GPU und wurde dadurch für selbst gehostete Anwendungen beliebt.
