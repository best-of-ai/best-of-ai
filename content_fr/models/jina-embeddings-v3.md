---
title: 'jina-embeddings-v3'
name: 'jina-embeddings-v3'
slug: 'jina-embeddings-v3'
subtitle: "Modèle d'embeddings multilingue à poids ouverts de Jina AI"
description: "Modèle d'embeddings multilingue à poids ouverts de Jina AI"
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/embeddings/'
price: 'Free'
rank: 4
release_date: '2024-09-18'
param_count: '570M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [embedding, open-weight, retrieval, multilingual]
i18n_source: '881f6947c894'
---

jina-embeddings-v3 est le modèle d'embeddings de texte multilingue de Jina AI, sorti en septembre 2024. Il a 570 millions de paramètres et prend en charge 89 langues, avec une fenêtre de contexte de 8 192 tokens et des embeddings de position rotatifs. Le modèle utilise des adaptateurs LoRA selon la tâche, pour la recherche requête-document, le clustering, la classification et l'appariement de textes : un seul jeu de poids peut donc s'adapter à des travaux différents sans réentraînement complet. Il prend aussi en charge le Matryoshka representation learning, qui permet de tronquer l'embedding de sortie depuis ses 1 024 dimensions par défaut jusqu'à 32, en gardant l'essentiel de la qualité de recherche. Sur le benchmark MTEB, Jina AI indiquait que v3 dépassait les embeddings propriétaires d'OpenAI et de Cohere sur les tâches en anglais, et multilingual-e5-large-instruct sur les tâches multilingues. Il est sous licence CC BY-NC 4.0, qui autorise un usage gratuit pour la recherche et l'évaluation, mais exige une licence commerciale pour un usage en production à grande échelle.
