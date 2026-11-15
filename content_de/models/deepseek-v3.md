---
title: 'DeepSeek V3'
name: 'DeepSeek V3'
slug: 'deepseek-v3'
subtitle: 'Effizientes Mixture-of-Experts-Modell von DeepSeek, zu einem Bruchteil der Kosten konkurrierender Modelle trainiert'
description: 'Effizientes Mixture-of-Experts-Modell von DeepSeek, zu einem Bruchteil der Kosten konkurrierender Modelle trainiert'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2024-12-26'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.27
output_price_usd_per_m: 1.1
api_available: true
mmlu_score: 88.5
humaneval_score: 82.6
lmarena_score: 1330
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: '3c9c049bbd9a'
---

DeepSeek V3 ist ein Mixture-of-Experts-Modell mit insgesamt 671 Milliarden Parametern, von denen 37 Milliarden pro Token aktiv sind. DeepSeek veröffentlichte es am 26. Dezember 2024. Es ist ein Basismodell ohne speziellen Schlussfolgerungsmodus und nutzt dieselbe Multi-Head-Latent-Attention- und DeepSeekMoE-Architektur wie V2. DeepSeek zufolge kostete das Training etwa 5,6 Millionen US-Dollar an GPU-Zeit – deutlich weniger als westliche Labore für vergleichbare Modelle aufwendeten. Das Modell erreichte 88,5 Punkte bei MMLU und 82,6 bei HumanEval und lag bei vielen Benchmarks ungefähr gleichauf mit GPT-4o und Claude 3.5 Sonnet, trotz der niedrigen Trainingskosten.

V3 steht mit offenen Gewichten unter MIT-Lizenz bereit; DeepSeeks API war deutlich günstiger als konkurrierende Spitzenmodelle. Später diente es als Basismodell für das auf Schlussfolgern ausgerichtete Reinforcement Learning von R1. Seine Kosteneffizienz löste in der Branche eine Debatte darüber aus, wie viel Rechenleistung für Spitzenleistungen tatsächlich nötig ist.
