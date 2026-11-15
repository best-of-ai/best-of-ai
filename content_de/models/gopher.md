---
title: 'Gopher'
name: 'Gopher'
slug: 'gopher'
subtitle: 'Forschungsmodell von DeepMind mit 280 Milliarden Parametern, das die Chinchilla-Skalierungsgesetze beeinflusste'
description: 'Forschungsmodell von DeepMind mit 280 Milliarden Parametern, das die Chinchilla-Skalierungsgesetze beeinflusste'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/'
price: 'Paid'
rank: 6
release_date: '2021-12-08'
param_count: '280B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 60.0
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
i18n_source: 'adb1e7eb1bf4'
---

Gopher ist ein Sprachmodell mit 280 Milliarden Parametern, das DeepMind trainierte und in einer Arbeit vom Dezember 2021 als Teil einer Studie zur Skalierung von Modellen beschrieb. Es wurde mit MassiveText, einem Korpus von 10,5 Terabyte, trainiert und zusammen mit fünf kleineren Modellen von 44 Millionen bis sieben Milliarden Parametern evaluiert, um zu untersuchen, wie sich Fähigkeiten mit der Größe verbessern. Beim MMLU-Benchmark erzielte Gopher im Fünf-Schuss-Verfahren 60 Prozent und übertraf damit deutlich frühere Modelle.

DeepMind veröffentlichte Gopher weder öffentlich noch über eine API; das Modell diente ausschließlich der Forschung. Seine wichtigste Nachwirkung war die Folgeanalyse im Chinchilla-Paper. Mithilfe von Gopher und verwandten Modellen zeigte diese Arbeit, dass die meisten damaligen großen Sprachmodelle gemessen an ihrer Parameterzahl zu wenig trainiert worden waren. Diese Erkenntnis veränderte über Jahre, wie Labore Rechenleistung zwischen Modellgröße und Trainingsdaten aufteilten.
