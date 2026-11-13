---
title: 'DeepSeek-R1-Distill-Llama-70B'
name: 'DeepSeek-R1-Distill-Llama-70B'
slug: 'deepseek-r1-distill-llama-70b'
subtitle: "Distillation sur base Llama des traces de raisonnement de DeepSeek-R1, la plus grande variante distillée"
description: "Distillation sur base Llama des traces de raisonnement de DeepSeek-R1, la plus grande variante distillée"
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

DeepSeek-R1-Distill-Llama-70B est un modèle de raisonnement distillé que DeepSeek a publié avec DeepSeek-R1 en janvier 2025. Au lieu d'entraîner un modèle de raisonnement depuis zéro, DeepSeek a ajusté Llama 3.3 70B Instruct de Meta sur des traces de raisonnement produites par le modèle R1 complet, pour transférer une grande part de la résolution par chaîne de pensée de R1 dans une architecture plus petite et moins coûteuse à faire tourner. C'est la plus grande des six variantes R1 distillées, sur des bases Qwen et Llama allant de 1,5B à 70B de paramètres. À la sortie, il a obtenu 70,0 % en pass@1 sur AIME 2024 et 94,5 % sur MATH-500, loin devant des modèles généralistes comme GPT-4o et Claude 3.5 Sonnet sur les mêmes benchmarks de maths. La fenêtre de contexte est de 128 000 tokens, héritée de la base Llama 3.3. Il est distribué sous la Llama 3.3 Community License, avec les poids sur Hugging Face et un accès API hébergé chez des fournisseurs, dont Together AI.
