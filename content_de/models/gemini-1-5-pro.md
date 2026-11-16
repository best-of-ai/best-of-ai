---
title: 'Gemini 1.5 Pro'
name: 'Gemini 1.5 Pro'
slug: 'gemini-1-5-pro'
subtitle: 'Modell von Google aus dem Jahr 2024, das ein Kontextfenster von einer Million Tokens einführte'
description: 'Modell von Google aus dem Jahr 2024, das ein Kontextfenster von einer Million Tokens einführte'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 6
release_date: '2024-02-15'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.25
output_price_usd_per_m: 5
api_available: true
mmlu_score: 85.9
humaneval_score: 71.9
lmarena_score: 1260
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, multimodal, long-context, api, legacy]
extra_model_types: ['Code']
i18n_source: 'eceffcd944e2'
---

Gemini 1.5 Pro führte Kontextfenster von einer Million Tokens in einer weit verbreiteten API ein. Google veröffentlichte es im Februar 2024 und machte es im Mai allgemein verfügbar. Es verarbeitet Text, Bilder, Audio und Video in einem Prompt. Google zeigte, dass das Modell eine ganze Stunde Video oder Hunderte Dokumentseiten gleichzeitig im Kontext halten konnte – deutlich mehr, als GPT-4 oder Claude damals boten. Es verwendet eine Mixture-of-Experts-Architektur, die laut Google bei den meisten Benchmarks die größere Gemini-1.0-Ultra-Version erreichte oder übertraf und zugleich günstiger lief.

Google senkte den Preis von 1.5 Pro 2024 zweimal und setzte ihn schließlich auf ungefähr 1,25 US-Dollar pro Million Eingabetokens und 5 US-Dollar pro Million Ausgabetokens bei Prompts unter 128.000 Tokens. Es erzielte rund 85,9 Punkte bei MMLU und 71,9 bei HumanEval und war 2024 über die Gemini-App, Vertex AI und Gemini-API Googles wichtigstes Produktivmodell. 2025 löste Gemini 2.5 Pro es als Spitzenmodell ab. Für bestehende Integrationen ist 1.5 Pro über die API weiterhin verfügbar.
