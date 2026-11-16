---
title: 'Hunyuan Large'
name: 'Hunyuan Large'
slug: 'hunyuan-large'
subtitle: "Modèle à mélange d'experts et à poids ouverts de Tencent"
description: "Modèle à mélange d'experts et à poids ouverts de Tencent"
company: 'tencent'
model_type: 'Language'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 5
release_date: '2024-11-05'
param_count: '389B (52B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts]
i18n_source: '12052bfcac4f'
---

Hunyuan-Large est le modèle de langage à mélange d'experts et à poids ouverts de Tencent, sorti en novembre 2024 avec 389 milliards de paramètres au total et 52 milliards activés par token. Tencent le présentait au lancement comme le plus grand modèle MoE ouvert à base de Transformer disponible alors. Il prend en charge une fenêtre de contexte de 256K et a été entraîné sur un mélange de données synthétiques et réelles, pour améliorer le raisonnement, le code et le rappel en long contexte par rapport aux modèles Hunyuan denses plus anciens de Tencent. L'entreprise a publié un rapport technique avec les poids, qui détaille ses choix de routage d'experts et de montée en échelle des données, et a sorti le modèle sur Hugging Face sous la licence Hunyuan pour l'auto-hébergement, avec un accès API via Tencent Cloud. Il est en concurrence directe avec d'autres grandes sorties MoE ouvertes de cette période, dont DeepSeek-V2 et la famille Mixtral de Mistral, par la taille de son pool d'experts rapportée au coût en paramètres actifs.
