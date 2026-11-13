---
title: 'GTE-large'
name: 'GTE-large'
slug: 'gte-large'
subtitle: "Modèle d'embeddings de texte général d'Alibaba, pour la recherche et la similarité sémantique"
description: "Modèle d'embeddings de texte général d'Alibaba, pour la recherche et la similarité sémantique"
company: 'alibaba'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/thenlper/gte-large'
price: 'Free'
rank: 5
release_date: '2023-08-07'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud']
date: '2026-07-16'
tags: [embedding, open-weight, api]
i18n_source: '25ba91e27698'
---

GTE-large est un modèle d'embeddings de texte d'Alibaba DAMO Academy, publié sur Hugging Face à la mi-2023 dans la famille General Text Embeddings (GTE), aux côtés des variantes plus petites GTE-base et GTE-small. C'est un encodeur de style BERT de 335 millions de paramètres, entraîné par apprentissage contrastif en plusieurs étapes sur un large mélange de textes du web et de domaines. Il produit des vecteurs de 1 024 dimensions à partir d'entrées jusqu'à 512 tokens. Il sert à la recherche d'information, à la recherche sémantique, au regroupement et au reranking. À sa sortie, il se plaçait bien au classement du benchmark MTEB par rapport aux autres modèles d'embeddings ouverts de taille proche, en concurrence directe avec des modèles de style BGE et E5 d'autres labos chinois. GTE-large est à poids ouverts sous Apache 2.0, tourne facilement sur un seul GPU ou un CPU à l'inférence, et se distribue via Hugging Face et Alibaba Cloud. C'est un choix par défaut courant pour les équipes qui montent des pipelines RAG et veulent un modèle d'embeddings compact, sans dépendre d'une API.
