---
title: 'Command R7B'
name: 'Command R7B'
slug: 'command-r7b'
subtitle: "Plus petit modèle Command de la génération actuelle chez Cohere"
description: "Plus petit modèle Command de la génération actuelle chez Cohere"
company: 'cohere'
model_type: 'Language'
logo_url: ''
product_url: 'https://cohere.com/command'
price: 'Free'
rank: 3
release_date: '2024-12-13'
param_count: '7B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
input_price_usd_per_m: 0.0375
output_price_usd_per_m: 0.15
api_available: true
mmlu_score: 70.4
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Cohere Platform', 'Hugging Face']
date: '2026-07-16'
tags: [llm, small-model, open-weight, low-latency]
i18n_source: 'a4ee277c137e'
---

Command R7B est le plus petit modèle de la série R de Cohere, sorti en décembre 2024. L'entreprise le présentait comme la dernière entrée de cette gamme. À 7 milliards de paramètres, il est fait pour tourner sur du matériel peu coûteux, y compris des CPU et un seul GPU, tout en gérant la génération augmentée par la recherche, l'usage d'outils et des tâches de raisonnement pour lesquelles les plus gros modèles de Cohere ont été conçus. Au lancement, il était en tête du Hugging Face Open LLM Leaderboard parmi les modèles à poids ouverts de taille proche, devant Gemma 2 9B, Ministral 8B et Llama 3.1 8B en moyenne, sur des benchmarks dont MMLU, IFEval et GPQA. Il garde la même fenêtre de contexte de 128 000 tokens que les plus gros de la série, et son tarif est bien plus bas que le leur. Il vise donc les applications à fort volume et sensibles à la latence, plutôt que les tâches du niveau des modèles frontière.
