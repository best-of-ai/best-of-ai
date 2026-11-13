---
title: 'Llama 3.3'
name: 'Llama 3.3'
slug: 'llama-3-3'
subtitle: "Modèle 70B à poids ouverts et économe de Meta, au niveau de prédécesseurs plus grands"
description: "Modèle 70B à poids ouverts et économe de Meta, au niveau de prédécesseurs plus grands"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2024-12-06'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.3 Community License'
api_available: true
mmlu_score: 86.0
humaneval_score: 88.4
lmarena_score: 1270
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, foundation-model]
extra_model_types: ['Code']
i18n_source: '00af49010fb3'
---

Llama 3.3 est un modèle texte seul de 70B que Meta a sorti en décembre 2024 comme mise à niveau directe de Llama 3.1 70B. Meta l'a ajusté avec de nouvelles techniques de post-training plutôt qu'en ajoutant des paramètres, et il finit par égaler ou dépasser le modèle 405B de la même famille sur le suivi d'instructions et les maths, tout en étant environ six fois plus petit. Les scores HumanEval et MMLU ont tous les deux progressé par rapport à Llama 3.1 70B, et des benchmarks indépendants montrent qu'il tient bien face aux modèles contemporains d'autres labos sur les tâches courantes. Comme il coûte bien moins cher à faire tourner qu'un modèle 405B, Llama 3.3 70B est vite devenu un choix courant sur des plateformes d'inférence comme Together AI et Groq, pour les équipes qui veulent une qualité proche du modèle phare à un prix plus bas.
