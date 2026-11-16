---
title: 'Chinchilla'
name: 'Chinchilla'
slug: 'chinchilla'
subtitle: 'Das Forschungsmodell von DeepMind aus dem Jahr 2022, das die Annahmen zu Skalierungsgesetzen für LLM-Training veränderte'
description: 'Das Forschungsmodell von DeepMind aus dem Jahr 2022, das die Annahmen zu Skalierungsgesetzen für LLM-Training veränderte'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/'
price: 'Paid'
rank: 4
release_date: '2022-03-29'
param_count: '70B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 67.5
access_methods: [Self-hosted]
runs_at_home: false
platforms: []
date: '2026-07-16'
tags: [llm, research, legacy]
i18n_source: '14414c05c298'
---
Chinchilla ist ein Forschungsmodell, das DeepMind in einer Arbeit vom März 2022 zum rechenoptimalen Training beschrieb. Mit 70 Milliarden Parametern ist es deutlich kleiner als DeepMinds früheres Gopher-Modell mit 280 Milliarden Parametern. Chinchilla wurde jedoch mit etwa viermal mehr Daten trainiert und übertraf Gopher, GPT-3 und andere größere Modelle jener Zeit in einer Vielzahl von Benchmarks, darunter mit einem durchschnittlichen MMLU-Wert von etwa 67,5 Prozent. Die zentrale Erkenntnis der Arbeit: Die meisten großen Sprachmodelle bis dahin waren gemessen an ihrer Größe untertrainiert. Bei einem festen Rechenbudget sollten Modellgröße und Trainingsdaten gemeinsam wachsen, statt ausschließlich die Parameterzahl zu erhöhen.

Dieses Ergebnis, heute als Chinchilla-Skalierungsgesetz bekannt, veränderte die Trainingsplanung der Labore. Das Feld setzte verstärkt auf kleinere Modelle mit deutlich größeren Datensätzen statt auf immer mehr Parameter. DeepMind veröffentlichte weder die Gewichte von Chinchilla noch einen öffentlichen Zugang; das Modell existiert nur als Forschungsartefakt der Arbeit. Sein Einfluss zeigt sich indirekt in fast jedem großen später trainierten Modell, von LLaMA bis GPT-4, deren Trainingsmethoden auf rechenoptimierte Skalierung setzen.
