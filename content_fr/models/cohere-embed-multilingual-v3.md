---
title: 'Cohere Embed Multilingual v3'
name: 'Cohere Embed Multilingual v3'
slug: 'cohere-embed-multilingual-v3'
subtitle: "Modèle d'embeddings de Cohere, réglé pour la recherche dans plus de 100 langues"
description: "Modèle d'embeddings de Cohere, réglé pour la recherche dans plus de 100 langues"
company: 'cohere'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://cohere.com/blog/introducing-embed-v3'
price: 'Paid'
rank: 6
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
platforms: ['Cohere API']
date: '2026-07-16'
tags: [embedding, api, multilingual]
i18n_source: '5c2674ca56c9'
---

Cohere Embed Multilingual v3 est un modèle d'embeddings de texte que Cohere a sorti en novembre 2023 pour la recherche, la génération augmentée par la recherche et la similarité sémantique, dans plus de 100 langues. Il prend un texte jusqu'à 512 tokens et sort un vecteur de 1 024 dimensions par défaut, avec des embeddings plus courts en 384 ou 768 dimensions si une équipe veut une recherche plus rapide ou moins de stockage. Cohere l'a entraîné à côté d'un jumeau réservé à l'anglais, Embed English v3, et a présenté les deux comme un progrès par rapport à la v2 : ils pondèrent les passages selon leur pertinence probable, pas seulement selon leur similarité, ce qui réduit le bruit dans les résultats des pipelines RAG. Le tarif est de 0,10 $ par million de tokens via l'API Cohere, et le modèle est aussi distribué sur les places de marché d'AWS, d'Azure et d'Oracle Cloud. Cohere a depuis sorti des Embed v4 plus récents, et certains fournisseurs de cloud, comme Oracle, listent désormais la v3 comme option héritée ou dépréciée. Elle reste disponible via l'API de Cohere et sur Hugging Face.
