---
title: 'Cohere Embed v3'
name: 'Cohere Embed v3'
slug: 'cohere-embed-v3'
subtitle: "Modèle d'embeddings de texte multilingue de Cohere, pour le RAG et la recherche"
description: "Modèle d'embeddings de texte multilingue de Cohere, pour le RAG et la recherche"
company: 'cohere'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://cohere.com/embed'
price: 'Paid'
rank: 5
release_date: '2023-11-02'
param_count: 'Undisclosed'
context_window_tokens: 512
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Cohere Platform']
date: '2026-07-16'
tags: [embedding, retrieval, rag, api]
i18n_source: '7f7e30fb76b2'
---

Cohere Embed v3 est un modèle d'embeddings de texte que Cohere a sorti en novembre 2023 pour la recherche, la génération augmentée par la recherche et la recherche sémantique. Il existe en variantes anglaise et multilingue. La version multilingue a été entraînée sur plus de 100 langues et a amélioré la précision de recherche sur le benchmark MIRACL d'environ 35 % par rapport à la génération précédente. L'appelant peut indiquer si un texte est une requête ou un document, ce qui ajuste l'espace d'embeddings et améliore la précision. Le modèle n'est disponible que par l'API de Cohere, à 0,10 $ par million de tokens d'entrée, et il accepte des entrées jusqu'à 512 tokens. Embed v3 est devenu un choix courant pour les pipelines RAG, à côté de text-embedding-3 d'OpenAI et des modèles d'embeddings de Voyage AI, avant que Cohere ne sorte Embed v4, multimodal, en 2025.
