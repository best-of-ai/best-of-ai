---
title: 'Qwen4-Max'
name: 'Qwen4-Max'
slug: 'qwen4-max'
subtitle: "Le modèle propriétaire phare d'Alibaba pour l'API Qwen et sa plateforme cloud"
description: "Le modèle propriétaire phare d'Alibaba pour l'API Qwen et sa plateforme cloud"
company: 'alibaba'
model_type: 'Language'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Paid'
rank: 8
release_date: '2026-07-11'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.20
output_price_usd_per_m: 4.80
api_available: true
mmlu_score: 88.0
lmarena_score: 1352
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Alibaba Cloud', 'Qwen Chat', 'API']
date: '2026-07-19'
tags: [llm, proprietary, api, multimodal]
i18n_source: 'd9ca0c4f1096'
---

Qwen4-Max est le modèle propriétaire de plus haut palier d'Alibaba, au-dessus de la famille Qwen3 à poids ouverts que l'entreprise continue de publier sur Hugging Face. Contrairement à ceux-là, Qwen4-Max est fermé et n'est accessible que par l'API d'Alibaba Cloud, Qwen Chat ou des plateformes partenaires, à 1,20 $ par million de tokens d'entrée et 4,80 $ par million de tokens de sortie. Il prend du texte et de l'image en entrée, a une fenêtre de contexte d'un million de tokens, et Alibaba le place directement face à GPT-5.6 et Gemini 3.5 Pro dans ses propres comparaisons de benchmarks.

La coupure entre les modèles Qwen3 ouverts et le Qwen4-Max fermé reprend un schéma sur lequel d'autres labos se sont alignés : publier des poids de taille moyenne, assez capables, pour que les développeurs s'en emparent, et garder pour une API payante le plus grand modèle, le plus cher à entraîner. Alibaba s'appuie là-dessus pour étendre Qwen bien au-delà de la Chine, surtout auprès des développeurs sur Hugging Face qui font du fine-tuning sur les sorties ouvertes, mais passent encore au palier Max en production quand il leur faut la marge de raisonnement en plus.
