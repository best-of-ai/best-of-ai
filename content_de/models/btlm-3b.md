---
title: 'BTLM-3B'
name: 'BTLM-3B'
slug: 'btlm-3b'
subtitle: 'Das kompakte Modell von Cerebras mit offenen Gewichten, das mehr leistet, als seine Parameterzahl erwarten lässt'
description: 'Das kompakte Modell von Cerebras mit offenen Gewichten, das mehr leistet, als seine Parameterzahl erwarten lässt'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/btlm-3b-8b-7b-parameter-performance-in-a-3-billion-parameter-model'
price: 'Free'
rank: 4
release_date: '2023-07-24'
param_count: '3B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model]
i18n_source: '2c4fad8daa2c'
---
BTLM-3B-8K ist ein Sprachmodell mit drei Milliarden Parametern, das Cerebras gemeinsam mit der Opentensor Foundation entwickelte und auf den Wafer-Scale-CS-2-Systemen von Cerebras trainierte. Es wurde im Sommer 2023 angekündigt und sollte die Qualität von Modellen mit 7B Parametern erreichen, aber klein genug bleiben, um auf Smartphones und Geräten mit wenig Speicher zu laufen. Laut Cerebras passt das quantisierte BTLM-3B in etwa 3 GB Speicher und läuft auf Geräten wie iPhone, Google Pixel und sogar Raspberry Pi. Bei gängigen Benchmarks liegt es auf dem Niveau damaliger 7B-Modelle wie RedPajama-INCITE-7B.

Das Modell wurde mit 627 Milliarden Tokens aus dem SlimPajama-Datensatz trainiert – weniger als bei mehreren konkurrierenden 3B-Modellen jener Zeit. ALiBi-Positionsembeddings ermöglichen ein natives Kontextfenster von 8192 Tokens und eine brauchbare Extrapolation darüber hinaus. Cerebras veröffentlichte BTLM-3B unter Apache 2.0 zur kostenlosen kommerziellen Nutzung. Kurzzeitig galt es als leistungsstärkstes offenes 3B-Modell, bevor neuere kleine Modelle von Microsoft, Google und anderen es übertrafen.
