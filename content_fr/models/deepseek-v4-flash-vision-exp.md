---
title: 'DeepSeek-V4-Flash-Vision-Exp'
name: 'DeepSeek-V4-Flash-Vision-Exp'
slug: 'deepseek-v4-flash-vision-exp'
subtitle: "La variante multimodale expérimentale de V4-Flash, pour la lecture de documents et de graphiques"
description: "La variante multimodale expérimentale de V4-Flash, pour la lecture de documents et de graphiques"
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/news/news260821/'
price: 'Paid'
rank: 6
release_date: '2026-08-21'
param_count: '284B (MoE, 13B active)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.22
output_price_usd_per_m: 0.66
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-08-31'
tags: [multimodal, vision, api, document-understanding, mixture-of-experts]
i18n_source: '1264f839812e'
---

DeepSeek a publié DeepSeek-V4-Flash-Vision-Exp le 21 août 2026 comme variante expérimentale à entrée image de DeepSeek-V4-Flash, le modèle de mélange d'experts sparse de 284 milliards de paramètres au total et 13 milliards actifs par token. Il égale le V4-Flash texte seul sur les tâches agentiques et de raisonnement, et ajoute la compréhension d'images, visée vers la lecture de documents et de graphiques, la réponse à des questions visuelles et les flux de travail d'agents qui mêlent texte et images. Les images peuvent passer en données base64 inline, par URL, ou via la Files API de DeepSeek. Le modèle tokenise chaque image à 384 tokens, bien en dessous de ce que les modèles GPT et Claude utilisent en général par image.

Sur les benchmarks internes d'agents multimodaux de DeepSeek, l'entreprise indique que V4-Flash-Vision-Exp comble une grande partie de l'écart avec l'Opus-4.8 d'Anthropic sur les tâches qui demandent de raisonner à partir d'une entrée visuelle, un saut net par rapport au V4-Flash texte seul. Il est tarifé à 0,22 $ par million de tokens en entrée et 0,66 $ par million de tokens en sortie, avec un tarif plus bas à part pour l'entrée en cache, et il n'est disponible que via l'API DeepSeek, le temps que l'entreprise recueille des retours avant une sortie qui ne soit plus expérimentale.
