---
title: 'DeepSeek-R1-Distill-Qwen-32B'
name: 'DeepSeek-R1-Distill-Qwen-32B'
slug: 'deepseek-r1-distill-qwen-32b'
subtitle: "Distillation sur base Qwen des traces de raisonnement de DeepSeek-R1, dans un plus petit modèle ouvert"
description: "Distillation sur base Qwen des traces de raisonnement de DeepSeek-R1, dans un plus petit modèle ouvert"
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-R1'
price: 'Free'
rank: 6
release_date: '2025-01-20'
param_count: '32B'
context_window_tokens: 131072
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: '3cf96c55115c'
---

DeepSeek-R1-Distill-Qwen-32B est un modèle dense de 32 milliards de paramètres. DeepSeek l'a construit en ajustant Qwen2.5-32B sur des traces de raisonnement produites par le modèle DeepSeek-R1 complet. Au lieu d'entraîner un plus petit modèle depuis zéro, DeepSeek a distillé les sorties en chaîne de pensée de R1 dans plusieurs modèles de base, et la version Qwen 32B s'est avérée la plus forte du lot. Elle a dépassé o1-mini d'OpenAI sur des benchmarks de maths, de code et de sciences, malgré une taille assez modeste. C'est ainsi devenu l'un des premiers modèles ouverts assez petits pour tourner sur un seul GPU haut de gamme, tout en montrant une vraie capacité de raisonnement. Les poids sont sous licence MIT, avec le reste de la famille R1. Le modèle est largement repris en miroir sur Hugging Face, et servi par des fournisseurs d'inférence comme Together AI et Groq.

Il occupe un créneau précis : les équipes qui veulent un raisonnement pas à pas du style de R1, sans payer le modèle complet de 671B ni l'héberger. Comme c'est un transformeur dense classique, et non un mélange d'experts, il est aussi plus simple à ajuster par fine-tuning et à déployer que les sorties phares de DeepSeek.
