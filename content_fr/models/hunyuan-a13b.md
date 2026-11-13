---
title: 'Hunyuan-A13B'
name: 'Hunyuan-A13B'
slug: 'hunyuan-a13b'
subtitle: "Modèle de raisonnement à mélange d'experts et à poids ouverts de Tencent"
description: "Modèle de raisonnement à mélange d'experts et à poids ouverts de Tencent"
company: 'tencent'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 4
release_date: '2025-06-27'
param_count: '80B (13B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, mixture-of-experts]
i18n_source: '1fc3c97bd4e4'
---

Hunyuan-A13B est le modèle de langage à mélange d'experts et à poids ouverts de Tencent, sorti en juin 2025 avec 80 milliards de paramètres au total, mais seulement 13 milliards actifs par token, ce qui garde le coût d'inférence proche de celui d'un modèle dense bien plus petit. Il prend en charge nativement une fenêtre de contexte de 256K, même si beaucoup de déploiements auto-hébergés la plafonnent plus bas pour tenir dans la mémoire GPU. Le modèle a deux modes : une réponse rapide, et un raisonnement pas à pas, plus lent, pour les problèmes plus durs de maths, de sciences et de code. Tencent a publié les poids sur Hugging Face sous sa propre licence Hunyuan, et le modèle est aussi disponible via l'API de Tencent Cloud pour les équipes qui ne veulent pas le faire tourner elles-mêmes. Il se place face à d'autres modèles de raisonnement MoE ouverts et efficaces, comme les plus petites sorties de DeepSeek et Qwen d'Alibaba, davantage sur l'efficacité en paramètres actifs que sur le nombre brut de paramètres.
