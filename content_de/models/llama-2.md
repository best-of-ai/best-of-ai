---
title: 'Llama 2'
name: 'Llama 2'
slug: 'llama-2'
subtitle: 'Open-Weight-Veröffentlichung von Meta aus dem Jahr 2023, die das offene LLM-Ökosystem anschob'
description: 'Open-Weight-Veröffentlichung von Meta aus dem Jahr 2023, die das offene LLM-Ökosystem anschob'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2023-07-18'
param_count: '70B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
mmlu_score: 68.9
humaneval_score: 29.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '69c51717a945'
---

Llama 2 ist Metas Sprachmodellfamilie mit offenen Gewichten der zweiten Generation. Sie erschien am 18. Juli 2023 in Größen mit 7, 13 und 70 Milliarden Parametern sowie jeweils feinabgestimmten Chatvarianten. Trainiert wurde sie mit zwei Billionen Tokens; das Kontextfenster umfasst 4.096 Tokens – nach heutigen Maßstäben wenig, damals aber konkurrenzfähig. Das 70B-Modell erreichte 68,9 Punkte bei MMLU und lag damit nahe an GPT-3.5, fiel bei Codegenerierung jedoch zurück: 29,9 bei HumanEval gegenüber 48,1 für GPT-3.5. Wichtiger als die Rohwerte war die Lizenz: Meta erlaubte den meisten Unternehmen die kommerzielle Nutzung. Damit war Llama 2 das erste offene Modell mit ausreichend guter Leistung für Produktentwicklung und löste eine Welle von Fine-Tunes, quantisierten Varianten und Ablegern aus, die heute Hugging Face füllen. Die Gewichte lassen sich noch Jahre später kostenlos herunterladen, obwohl Meta inzwischen Llama 3 und Llama 4 veröffentlicht hat.
