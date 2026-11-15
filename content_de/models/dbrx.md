---
title: 'DBRX'
name: 'DBRX'
slug: 'dbrx'
subtitle: 'Offenes Mixture-of-Experts-Modell von Databricks'
description: 'Offenes Mixture-of-Experts-Modell von Databricks'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 5
release_date: '2024-03-27'
param_count: '132B (36B active)'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Databricks Open Model License'
api_available: true
mmlu_score: 73.7
humaneval_score: 70.1
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Databricks']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: 'c49f11ecc44d'
---
DBRX ist das Modell mit offenen Gewichten von Databricks und wurde im März 2024 als Basismodell für das instruction-tuned DBRX Instruct veröffentlicht. Es ist ein fein abgestimmtes Mixture-of-Experts-Modell mit insgesamt 132 Milliarden Parametern und 36 Milliarden aktiven Parametern pro Token. Trainiert wurde es von Grund auf mit 12 Billionen Tokens aus Text und Code auf Databricks eigenem Mosaic-AI-Trainingsstack. Bei der Veröffentlichung gab Databricks an, dass es andere damalige offene Modelle wie Llama 2 70B und Mixtral bei Benchmarks wie MMLU und HumanEval übertraf. Das Modell sollte zeigen, dass auch ein auf Unternehmen ausgerichtetes Unternehmen ohne das Forschungsbudget eines großen KI-Labors ein konkurrenzfähiges Grundlagenmodell trainieren kann. DBRX hat ein Kontextfenster von 32.000 Tokens und steht unter der Databricks Open Model License. Die Gewichte sind auf Hugging Face zur Selbstbereitstellung sowie über Databricks eigene Serving-Infrastruktur verfügbar.
