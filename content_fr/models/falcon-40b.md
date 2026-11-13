---
title: 'Falcon 40B'
name: 'Falcon 40B'
slug: 'falcon-40b'
subtitle: 'Le modèle à poids ouverts antérieur de TII, en tête des leaderboards avant Falcon 180B'
description: 'Le modèle à poids ouverts antérieur de TII, en tête des leaderboards avant Falcon 180B'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 4
release_date: '2023-05-25'
param_count: '40B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
mmlu_score: 82.7
humaneval_score: 76.3
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '109766ee6da4'
---

Falcon 40B est un modèle de langage à décodeur causal seul, de 40 milliards de paramètres, publié par le Technology Innovation Institute en mai 2023. Il a été entraîné sur environ 1 billion de tokens de RefinedWeb, un grand jeu de données web que TII a lui-même sélectionné et filtré, combiné à quelques corpus supplémentaires choisis. Au lancement, il a pris la tête du Hugging Face Open LLM Leaderboard parmi les modèles open source, avec 82,7 au MMLU et 76,3 au HumanEval, devant des modèles de la même époque comme MPT et RedPajama, et au niveau du plus grand Llama 2 70B de Meta sur plusieurs benchmarks. L'architecture utilise l'attention multiquery et FlashAttention pour garder le coût d'inférence bas par rapport à la taille. TII l'a publié sous licence Apache 2.0 sans redevances, un choix inhabituellement permissif pour un modèle de cette échelle à l'époque, ce qui a aidé une adoption précoce en entreprise, dont la disponibilité sur AWS SageMaker JumpStart. Falcon 40B a depuis été remplacé par Falcon 180B et la famille Falcon 3, et sa fenêtre de contexte de 2 048 tokens paraît petite à côté des modèles actuels.
