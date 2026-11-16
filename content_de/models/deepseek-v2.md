---
title: 'DeepSeek-V2'
name: 'DeepSeek-V2'
slug: 'deepseek-v2'
subtitle: 'DeepSeeks Mixture-of-Experts-Modell von 2024 mit besonders günstigen API-Preisen'
description: 'DeepSeeks Mixture-of-Experts-Modell von 2024 mit besonders günstigen API-Preisen'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-05-06'
param_count: '236B (21B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'DeepSeek License'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
mmlu_score: 78.5
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
i18n_source: '988dda9730f9'
---
DeepSeek-V2 ist ein Mixture-of-Experts-Sprachmodell, das DeepSeek im Mai 2024 veröffentlichte. Es umfasst 236 Milliarden Parameter, von denen 21 Milliarden pro Token aktiv sind. Der wichtigste technische Beitrag war Multi-head Latent Attention (MLA), ein Verfahren zur Komprimierung des Key-Value-Caches. Es verringerte den Speicherbedarf deutlich und ermöglichte einen wesentlich höheren Token-Durchsatz als beim früheren dichten DeepSeek-67B-Modell auf derselben Hardware. Das Modell wurde mit 8,1 Billionen Tokens trainiert, bietet ein Kontextfenster von 128.000 Tokens und erzielte bei damaligen offenen Modellen konkurrenzfähige Ergebnisse in MMLU- und Programmier-Benchmarks.

Bemerkenswert war nicht nur die Architektur, sondern auch der Preis: DeepSeek startete seine API zu einem Bruchteil der Preise chinesischer und westlicher Wettbewerber. Das löste branchenweit Preissenkungen aus, die Kommentatoren damals als „Preiskrieg“ bezeichneten. Die hier eingeführten MLA- und DeepSeekMoE-Techniken wurden in allen späteren Modellen von DeepSeek weitergeführt, darunter V3 und R1. V2 bildet damit die Architekturgrundlage für die späteren Spitzenmodelle des Unternehmens.
