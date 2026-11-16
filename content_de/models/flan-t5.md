---
title: 'Flan-T5'
name: 'Flan-T5'
slug: 'flan-t5'
subtitle: 'Der instruction-tuned Nachfolger von T5 mit offenen Gewichten von Google'
description: 'Der instruction-tuned Nachfolger von T5 mit offenen Gewichten von Google'
company: 'google'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/google/flan-t5-xxl'
price: 'Free'
rank: 4
release_date: '2022-10-20'
param_count: '11B'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, instruction-tuned, legacy]
i18n_source: '01962c85d25c'
---
Flan-T5 ist die instruction-tuned Version von Googles früherem Text-zu-Text-Transformer T5 und erschien im Oktober 2022. Statt die Basisarchitektur zu ändern, feinabstimmte Google T5 mit über tausend als Anweisungen formulierten Aufgaben aus Übersetzung, Zusammenfassung, Schlussfolgern und Klassifizierung in vielen Sprachen. Dadurch war das Modell sofort deutlich vielseitiger als das unveränderte T5, das für gute Ergebnisse eine aufgabenspezifische Abstimmung benötigte. Google veröffentlichte die Familie in mehreren Größen: von einer Small-Version mit 80 Millionen bis zu Flan-T5-XXL mit elf Milliarden Parametern. Alle stehen unter Apache 2.0 und können kostenlos von Hugging Face heruntergeladen werden. Das Kontextfenster von 512 Tokens ist nach heutigen Maßstäben kurz und beschränkt die Nutzung auf kürzere Dokumente und Eingaben. Flan-T5 bleibt ein häufiger Forschungsbenchmark für Instruction-Tuning und eine leichtgewichtige Option für Teams, die ein offenes, selbst gehostetes Modell für einfache NLP-Aufgaben ohne den Rechenaufwand eines größeren Decoder-LLM benötigen.
