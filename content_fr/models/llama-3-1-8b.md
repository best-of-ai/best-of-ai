---
title: 'Llama 3.1 8B'
name: 'Llama 3.1 8B'
slug: 'llama-3-1-8b'
subtitle: "Palier compact de la génération Llama 3.1 chez Meta"
description: "Palier compact de la génération Llama 3.1 chez Meta"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2024-07-23'
param_count: '8B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
mmlu_score: 69.4
humaneval_score: 72.6
lmarena_score: 1180
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
extra_model_types: ['Code']
i18n_source: 'fa37d1d53ede'
---

Llama 3.1 8B est le petit palier de la même sortie de juillet 2024, fait pour les gens qui veulent faire tourner un modèle capable sur un seul GPU, ou même sur un ordinateur portable haut de gamme. Il partage la fenêtre de contexte de 128 000 tokens et l'entraînement multilingue de ses grands frères, et il obtient un score plus haut que le Llama 3 8B d'origine au MMLU et au HumanEval, grâce à plus de données d'entraînement et à un post-training affiné. Les développeurs l'utilisent pour des assistants sur l'appareil, du traitement par lots peu coûteux et des expériences de fine-tuning, là où les modèles 70B ou 405B seraient trop lourds ou trop chers à servir. Il tourne facilement avec des outils comme Ollama, et c'est l'un des modèles les plus téléchargés sur Hugging Face.
