---
title: 'DeepSeek V4-Pro'
name: 'DeepSeek V4-Pro'
slug: 'deepseek-v4-pro'
subtitle: "Le meilleur modèle à poids ouverts de 2026, en tête sur le code agentique et le raisonnement de niveau graduate"
description: "Le meilleur modèle à poids ouverts de 2026, en tête sur le code agentique et le raisonnement de niveau graduate"
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 9
release_date: '2026-04-24'
param_count: '1.6T (49B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 0.87
api_available: true
mmlu_score: 90.0
humaneval_score: 91.0
lmarena_score: 1390
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: '3dcf4ddbbacd'
---

DeepSeek V4-Pro est le modèle phare de DeepSeek, publié le 24 avril 2026 en même temps qu'un modèle plus petit, V4-Flash. C'est un mélange d'experts de 1,6 billion de paramètres au total et 49 milliards actifs par token. Il introduit une attention hybride qui combine la Compressed Sparse Attention et la Heavily Compressed Attention, ce qui réduit fortement le calcul d'inférence et la taille du cache KV par rapport à V3.2, et lui permet une fenêtre de contexte d'un million de tokens. Le modèle tourne en mode « thinking », pour un raisonnement étape par étape, et en mode non-thinking, pour des réponses rapides. DeepSeek indique qu'il mène les modèles à poids ouverts sur les benchmarks de maths, de sciences et de code agentique, avec un score SWE-bench Verified au-dessus de 80 %.

Comme le reste de la gamme DeepSeek, V4-Pro sort avec des poids ouverts sous licence MIT et un tarif d'API bien en dessous des modèles fermés comparables d'OpenAI, d'Anthropic et de Google. Il est présenté comme la réponse de DeepSeek aux modèles de raisonnement frontier sortis par les labos occidentaux début 2026. Sa publication a été largement couverte comme un signe que l'écart entre modèles frontier ouverts et fermés continue de se réduire.
