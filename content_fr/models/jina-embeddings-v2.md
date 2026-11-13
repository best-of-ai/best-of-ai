---
title: 'Jina Embeddings v2'
name: 'Jina Embeddings v2'
slug: 'jina-embeddings-v2'
subtitle: "Modèle d'embeddings de Jina AI, remarqué pour une fenêtre de 8 000 tokens au lancement"
description: "Modèle d'embeddings de Jina AI, remarqué pour une fenêtre de 8 000 tokens au lancement"
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/news/jina-embeddings-2-the-best-solution-for-embedding-long-documents/'
price: 'Free'
rank: 5
release_date: '2023-10-30'
param_count: '137M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Jina API']
date: '2026-07-16'
tags: [embedding, open-weight, api, legacy]
i18n_source: '9b381be032d7'
---

Jina Embeddings v2 est un modèle d'embeddings de texte de Jina AI, sorti en octobre 2023. Il existait en deux tailles principales, une petite version de 33 millions de paramètres et une version de base de 137 millions, toutes deux sur une architecture BERT modifiée qui utilise l'encodage de position ALiBi plutôt que des embeddings positionnels classiques. Ce choix lui permettait des séquences jusqu'à 8 192 tokens, ce qui était rare pour un modèle d'embeddings ouvert à l'époque, et lui permettait de tenir face au text-embedding-ada-002 propriétaire d'OpenAI sur la recherche dans de longs documents, tout en étant bien plus petit. Le modèle est sous licence Apache 2.0, et on peut le faire tourner en local ou y accéder via l'API de Jina. Il a depuis été remplacé par jina-embeddings-v3, qui ajoute le multilingue et des adaptateurs par tâche, mais v2 reste utilisé pour la recherche en anglais, là où sa taille plus petite est un avantage.
