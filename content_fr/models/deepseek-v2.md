---
title: 'DeepSeek-V2'
name: 'DeepSeek-V2'
slug: 'deepseek-v2'
subtitle: "Le modèle de mélange d'experts de DeepSeek en 2024, bien moins cher en API que ses concurrents"
description: "Le modèle de mélange d'experts de DeepSeek en 2024, bien moins cher en API que ses concurrents"
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

DeepSeek-V2 est un modèle de langage à mélange d'experts que DeepSeek a publié en mai 2024, avec 236 milliards de paramètres au total et 21 milliards actifs par token. Son apport technique principal est la Multi-head Latent Attention, une méthode qui compresse le cache clé-valeur, réduit fortement l'usage mémoire et permet de servir bien plus de tokens par seconde que l'ancien modèle dense de 67B de DeepSeek, sur le même hardware. Entraîné sur 8,1 billions de tokens avec une fenêtre de contexte de 128K, il se plaçait bien sur MMLU et les benchmarks de code face aux autres modèles ouverts de l'époque.

Ce qui a fait remarquer V2, ce n'était pas seulement l'architecture, c'était le prix : DeepSeek a lancé son API à une fraction de ce que facturaient les concurrents chinois et occidentaux, ce qui a déclenché une série de baisses dans le secteur. Les commentateurs de l'époque ont parlé d'une « guerre des prix ». Les techniques MLA et DeepSeekMoE introduites ici se retrouvent dans tous les modèles DeepSeek suivants, dont V3 et R1. V2 est donc la base architecturale des sorties frontier ultérieures de l'entreprise.
