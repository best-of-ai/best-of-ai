---
title: 'GPT-OSS-120B'
name: 'GPT-OSS-120B'
slug: 'gpt-oss-120b'
subtitle: "La première sortie à poids ouverts d'OpenAI depuis GPT-2, au niveau d'o4-mini sur beaucoup de benchmarks de raisonnement"
description: "La première sortie à poids ouverts d'OpenAI depuis GPT-2, au niveau d'o4-mini sur beaucoup de benchmarks de raisonnement"
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 8
release_date: '2025-08-05'
param_count: '117B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 90.0
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Together AI', 'Azure AI Foundry']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: 'caa1902f73b4'
---

GPT-OSS-120B est un modèle de raisonnement à poids ouverts qu'OpenAI a publié le 5 août 2025, sa première sortie de modèle ouvert depuis GPT-2 en 2019. Il utilise un transformer en mélange d'experts : 117 milliards de paramètres au total, mais seulement environ 5,1 milliards actifs par token. Ça lui permet de faire tourner des charges lourdes en raisonnement sur un seul GPU haut de gamme, au lieu des grappes multi-GPU qu'exigeraient des modèles denses de taille comparable. Il a obtenu environ 90 au MMLU au lancement, dans la même zone qu'o4-mini d'OpenAI sur beaucoup de benchmarks de raisonnement et de code. Il sort sous licence Apache 2.0, donc une entreprise peut l'auto-héberger, faire du fine-tuning et l'exécuter sans restrictions d'usage. OpenAI l'a construit pour concurrencer les sorties ouvertes de Meta, de Mistral et de labos chinois comme DeepSeek et l'équipe Qwen d'Alibaba, qui donnaient le rythme des modèles à poids ouverts pendant qu'OpenAI restait fermé. Il est disponible via Hugging Face, Together AI, Azure AI Foundry, et l'API d'OpenAI, pour qui veut à la fois l'auto-hébergement ouvert et un hébergement géré.
