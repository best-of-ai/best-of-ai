---
title: 'DeepSeek-MoE-16B'
name: 'DeepSeek-MoE-16B'
slug: 'deepseek-moe-16b'
subtitle: "Premier mélange d'experts à grain fin de DeepSeek, qui a nourri ses architectures MoE suivantes"
description: "Premier mélange d'experts à grain fin de DeepSeek, qui a nourri ses architectures MoE suivantes"
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-MoE'
price: 'Free'
rank: 5
release_date: '2024-01-11'
param_count: '16.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
i18n_source: '61ec60299e14'
---

DeepSeek-MoE-16B, sorti en janvier 2024, était le premier essai de DeepSeek d'un mélange d'experts à grain fin, et ses choix de conception ont été repris dans les modèles V2 et V3. Il a 16,4 milliards de paramètres au total, mais seulement environ 2,8 milliards actifs par token. Ça vient de deux techniques décrites dans l'article : découper les experts en unités plus petites et plus spécialisées, et isoler un ensemble d'experts partagés qui s'activent toujours, pour capter le savoir commun. Entraîné depuis zéro sur 2 billions de tokens anglais et chinois, il a atteint un niveau comparable aux modèles denses DeepSeek 7B et Llama 2 7B, avec à l'inférence environ 40 % seulement du calcul que ces modèles demandent. La fenêtre de contexte est de 4 096 tokens. Il est sorti sous la licence ouverte de DeepSeek, pour un usage auto-hébergé, surtout comme démonstration de recherche sur la spécialisation des experts, pas comme une sortie pensée pour la production.
