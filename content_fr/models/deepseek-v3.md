---
title: 'DeepSeek V3'
name: 'DeepSeek V3'
slug: 'deepseek-v3'
subtitle: "Le modèle de mélange d'experts efficace de DeepSeek, entraîné pour une fraction du coût des rivaux"
description: "Le modèle de mélange d'experts efficace de DeepSeek, entraîné pour une fraction du coût des rivaux"
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

DeepSeek V3 est un modèle de mélange d'experts de 671 milliards de paramètres, dont 37 milliards actifs par token, que DeepSeek a publié le 26 décembre 2024. C'est un modèle de base sans raisonnement, construit sur la même architecture Multi-head Latent Attention et DeepSeekMoE que V2. DeepSeek a indiqué l'avoir entraîné pour environ 5,6 millions de dollars de temps GPU, un chiffre très inférieur à ce que les labos occidentaux dépensaient pour des modèles comparables. Il a obtenu 88,5 sur MMLU et 82,6 sur HumanEval, ce qui le place à peu près au niveau de GPT-4o et de Claude 3.5 Sonnet sur beaucoup de benchmarks, malgré le faible coût d'entraînement.

V3 est publié sous licence MIT avec des poids ouverts, et DeepSeek a tarifé son API nettement en dessous des modèles frontier concurrents. Il a ensuite servi de base au-dessus de laquelle l'apprentissage par renforcement orienté raisonnement de R1 a été construit. Son coût d'entraînement est devenu un sujet de discussion dans le secteur : combien de calcul faut-il vraiment pour atteindre une performance de niveau frontier.
