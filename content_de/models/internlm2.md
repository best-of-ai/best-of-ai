---
title: 'InternLM2'
name: 'InternLM2'
slug: 'internlm2'
subtitle: 'Offenes Grundlagenmodell des Shanghai AI Lab mit starkem Langkontext und Schlussfolgerungsfähigkeit'
description: 'Offenes Grundlagenmodell des Shanghai AI Lab mit starkem Langkontext und Schlussfolgerungsfähigkeit'
company: 'shanghai-ai-lab'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-01-17'
param_count: '20B'
context_window_tokens: 200000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.7
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, long-context]
i18n_source: 'e91b498370ff'
---
InternLM2 ist ein Sprachmodell mit offenen Gewichten des Shanghai AI Laboratory. Es wurde am 17. Januar 2024 in Größen mit 7B und 20B Parametern samt entsprechenden Chatvarianten veröffentlicht. Beide Größen unterstützen ein Kontextfenster von 200.000 Tokens. Dafür wurde das Training mit Sequenzen von 4K Tokens begonnen und schrittweise auf 32K und darüber hinaus erweitert. Bei Tests mit langen Dokumenten nach dem Needle-in-a-Haystack-Prinzip hält das Modell diese Länge gut durch. Die 20B-Chatvariante erreicht 67,7 Punkte bei MMLU und lag bei der Veröffentlichung damit vor mehreren offenen Modellen ähnlicher Größe. InternLM2 wurde mit einem großen mehrsprachigen Korpus trainiert und ist besonders stark in Englisch und Chinesisch. Vor der Ablösung durch InternLM2.5 im selben Jahr war es als universelles Grundlagenmodell für Schlussfolgern, Programmieren und Aufgaben mit langem Kontext positioniert. Es steht unter Apache 2.0 auf Hugging Face und im InternLM-GitHub-Repository bereit.
