---
title: 'DeepSeek-R1-Distill-Llama-70B'
name: 'DeepSeek-R1-Distill-Llama-70B'
slug: 'deepseek-r1-distill-llama-70b'
subtitle: 'Llama-basierte Destillation der Reasoning-Abläufe von DeepSeek-R1 und größte destillierte Variante'
description: 'Llama-basierte Destillation der Reasoning-Abläufe von DeepSeek-R1 und größte destillierte Variante'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-R1'
price: 'Free'
rank: 6
release_date: '2025-01-20'
param_count: '70B'
context_window_tokens: 131072
modality: [text]
open_weight: true
license: 'Llama 3.3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: '875e7d1cacd9'
---

DeepSeek-R1-Distill-Llama-70B ist ein destilliertes Schlussfolgerungsmodell, das DeepSeek im Januar 2025 zusammen mit DeepSeek-R1 veröffentlichte. Statt ein Schlussfolgerungsmodell neu zu trainieren, stimmte DeepSeek Meta Llama 3.3 70B Instruct mit vom vollständigen R1 erzeugten Schlussfolgerungsspuren fein ab. So gelangten große Teile von R1s schrittweiser Problemlösung in eine kleinere und günstigere Architektur. Es ist die größte von sechs R1-Destillationsvarianten auf Qwen- und Llama-Basis mit 1,5 bis 70 Milliarden Parametern. Bei Veröffentlichung erzielte es 70,0 Prozent pass@1 bei AIME 2024 und 94,5 Prozent bei MATH-500 und lag damit bei Mathematik-Benchmarks deutlich vor GPT-4o und Claude 3.5 Sonnet. Das Kontextfenster umfasst 128.000 Tokens, übernommen von Llama 3.3. Die Gewichte stehen unter der Llama-3.3-Community-Lizenz auf Hugging Face; gehostete APIs bieten unter anderem Together AI an.
