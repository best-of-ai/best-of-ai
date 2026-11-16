---
title: 'BTLM-3B'
name: 'BTLM-3B'
slug: 'btlm-3b'
subtitle: 'Le modèle compact à poids ouverts de Cerebras, réglé pour dépasser ce que son nombre de paramètres laisse attendre'
description: 'Le modèle compact à poids ouverts de Cerebras, réglé pour dépasser ce que son nombre de paramètres laisse attendre'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/btlm-3b-8b-7b-parameter-performance-in-a-3-billion-parameter-model'
price: 'Free'
rank: 4
release_date: '2023-07-24'
param_count: '3B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model]
i18n_source: '2c4fad8daa2c'
---

BTLM-3B-8K est un modèle de langage de 3 milliards de paramètres que Cerebras a construit avec l'Opentensor Foundation et entraîné sur ses systèmes CS-2 à l'échelle du wafer. Annoncé à l'été 2023, il visait un but précis : égaler la qualité de modèles à 7 milliards de paramètres tout en restant assez petit pour tourner sur des téléphones et des appareils à peu de mémoire. Cerebras indique qu'une fois quantifié, BTLM-3B tient dans environ 3 GB de mémoire et tourne sur des appareils comme l'iPhone, le Google Pixel, et même un Raspberry Pi, avec des résultats au niveau de modèles 7B de l'époque, comme RedPajama-INCITE-7B, sur les benchmarks courants.

Le modèle a été entraîné sur 627 milliards de tokens du jeu de données SlimPajama, moins que ce qu'utilisaient plusieurs modèles 3B concurrents à l'époque. Il utilise des embeddings de position ALiBi pour une fenêtre de contexte native de 8 192 tokens, avec une extrapolation raisonnable au-delà. Cerebras a publié BTLM-3B sous Apache 2.0, donc libre pour un usage commercial. Il a brièvement été celui qui obtenait les meilleurs résultats parmi les modèles ouverts en 3B, avant que de petits modèles plus récents, chez Microsoft, Google et ailleurs, le dépassent.
