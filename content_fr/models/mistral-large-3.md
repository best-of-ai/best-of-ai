---
title: 'Mistral Large 3'
name: 'Mistral Large 3'
slug: 'mistral-large-3'
subtitle: "Le grand modèle de langage phare de Mistral, au niveau frontière"
description: "Le grand modèle de langage phare de Mistral, au niveau frontière"
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/'
price: 'Freemium'
rank: 7
release_date: '2025-12-02'
param_count: '675B (41B active)'
context_window_tokens: 256000
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.5
output_price_usd_per_m: 1.5
api_available: true
access_methods: [API, Chat UI, Self-hosted]
runs_at_home: true
platforms: ['Le Chat', 'Azure AI', 'API', 'Hugging Face']
date: '2026-07-16'
tags: [llm, foundation-model, api, open-weight]
i18n_source: 'b27612444904'
---

Mistral Large 3 est le modèle de langage phare de Mistral AI, publié le 2 décembre 2025 dans la gamme plus large Mistral 3. Il utilise un mélange d'experts épars, avec 675 milliards de paramètres au total mais seulement environ 41 milliards actifs par token. Il tourne donc à peu près au coût de calcul d'un modèle dense bien plus petit, tout en s'appuyant sur un stock de poids appris bien plus large. Il prend du texte et des images en entrée, gère une fenêtre de contexte de 256 000 tokens, et Mistral a publié les poids sous licence Apache 2.0, un changement par rapport à l'approche fermée retenue pour Mistral Large 2.

Au lancement, le modèle s'est placé près du haut du classement LMArena parmi les modèles à poids ouverts. Il vise les développeurs qui veulent un raisonnement, du code et des performances multilingues de niveau frontière, sans être enfermés dans une API fermée. Il est disponible via l'assistant Le Chat de Mistral, sa propre API, Azure AI, et en poids téléchargeables sur Hugging Face pour qui veut l'auto-héberger ou l'ajuster par fine-tuning. Le tarif API est nettement sous ce que Mistral demandait pour Large 2.
