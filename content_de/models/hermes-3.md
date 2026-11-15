---
title: 'Hermes 3'
name: 'Hermes 3'
slug: 'hermes-3'
subtitle: 'Open-Weight-Fine-Tuning von Nous Research mit Schwerpunkt auf Steuerbarkeit und Schlussfolgern.'
description: 'Open-Weight-Fine-Tuning von Nous Research mit Schwerpunkt auf Steuerbarkeit und Schlussfolgern.'
company: 'nous-research'
model_type: 'Language'
logo_url: ''
product_url: 'https://nousresearch.com/hermes3/'
price: 'Free'
rank: 4
release_date: '2024-08-27'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fine-tune, self-hosted]
i18n_source: 'b20d0dae77b1'
---

Hermes 3 ist ein Sprachmodell mit offenen Gewichten von Nous Research auf Basis von Metas Llama 3.1 405B. Nous veröffentlichte es im August 2024 als vollständiges Fine-Tuning aller Parameter statt als leichte Adapter-Variante. Nutzer:innen sollten mehr Kontrolle durch steuerbare Systemprompts, agentische Werkzeugnutzung und lange Schlussfolgerungsketten erhalten. Das Modell erscheint in drei Größen (8B, 70B und 405B) und wurde überwiegend mit von Nous kuratierten synthetischen Daten trainiert. Strukturierte Ausgaben und Funktionsaufrufe funktionieren gut genug, um es als direkten Ersatz für ein Agenten-Backend einzusetzen. Bei öffentlichen Benchmarks erreicht oder übertrifft es Metas eigenes Llama-3.1-Instruct-Fine-Tune bei Aufgaben wie ARC, HellaSwag und IFEval – bemerkenswert für ein Community-Fine-Tune im Vergleich zur offiziellen Veröffentlichung des Anbieters. Da die Gewichte unter der Llama-3.1-Lizenz offen sind, können Entwickler:innen das vollständige 405B-Modell selbst hosten oder über Drittanbieter ausführen, statt eine proprietäre API zu verwenden.
