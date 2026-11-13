---
title: 'Qwen3.8-Flash-Next'
name: 'Qwen3.8-Flash-Next'
slug: 'qwen3-8-flash-next'
subtitle: "L'aperçu à poids ouverts, par Alibaba, de l'architecture Qwen4 de prochaine génération"
description: "L'aperçu à poids ouverts, par Alibaba, de l'architecture Qwen4 de prochaine génération"
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-26'
param_count: '125B (6B active)'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-09-05'
tags: [llm, open-weight, multimodal, moe, apache-2.0, cost-efficient]
i18n_source: '6dac4a7632ca'
---

Alibaba a publié Qwen3.8-Flash-Next en open source le 26 août 2026, pour donner aux développeurs un premier aperçu de l'architecture Qwen4 avant la famille complète. C'est un modèle multimodal à mélange d'experts, avec un backbone de 125 milliards de paramètres mais seulement 6 milliards actifs par token, plus une table d'embeddings de n-grammes de 51 milliards de paramètres et un module de prédiction multi-tokens de 4 milliards de paramètres. Le contexte va en natif jusqu'à 262 144 tokens et s'étend à un million. Alibaba dit qu'il dépasse l'ancien Qwen3.7-Plus, surtout sur le code et les tâches de bureau, tout en coûtant environ neuf fois moins à entraîner et environ douze fois moins à faire tourner. Un checkpoint standard et un checkpoint FP8 sont sortis au lancement.
