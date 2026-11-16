---
title: 'GPT-OSS-20B'
name: 'GPT-OSS-20B'
slug: 'gpt-oss-20b'
subtitle: "Le palier plus petit de la sortie à poids ouverts d'OpenAI, fait pour tenir sur un seul GPU"
description: "Le palier plus petit de la sortie à poids ouverts d'OpenAI, fait pour tenir sur un seul GPU"
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 7
release_date: '2025-08-05'
param_count: '21B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 85.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, small-model, api]
i18n_source: '7a4a62f3cc31'
---

GPT-OSS-20B est le plus petit des deux modèles à poids ouverts qu'OpenAI a publiés le 5 août 2025, à côté du plus grand GPT-OSS-120B, dans sa première sortie de modèle ouvert depuis GPT-2. Il utilise un mélange d'experts, avec environ 21 milliards de paramètres au total et à peu près 3,6 milliards actifs par token. C'est assez léger pour tourner sur un seul GPU grand public avec 16 GB de mémoire ou plus. C'était le but : un modèle de raisonnement utilisable pour les développeurs et les amateurs, sans matériel de niveau serveur. Il a obtenu 85,3 au MMLU au lancement, un bon résultat pour sa classe de taille, et il traite le code, les maths et le raisonnement général assez près de son grand frère, malgré une empreinte bien plus petite. Sous licence Apache 2.0, on peut faire du fine-tuning et le redistribuer librement. Il est disponible via Hugging Face, Together AI et l'API d'OpenAI pour les équipes qui veulent une option gérée plutôt que l'auto-hébergement.
