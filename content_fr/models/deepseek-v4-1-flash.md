---
title: 'DeepSeek-V4.1-Flash'
name: 'DeepSeek-V4.1-Flash'
slug: 'deepseek-v4-1-flash'
subtitle: "La suite moins chère de V4-Flash, capable de vision, avec une tarification de pointe par paliers"
description: "La suite moins chère de V4-Flash, capable de vision, avec une tarification de pointe par paliers"
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/quick_start/pricing/'
price: 'Paid'
rank: 7
release_date: '2026-09-10'
param_count: '552B (MoE)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.15
output_price_usd_per_m: 0.60
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-09-18'
tags: [llm, multimodal, api, cost-efficient, moe]
i18n_source: '9bfa801c726b'
---

DeepSeek a sorti V4.1-Flash le 10 septembre 2026, un modèle de mélange d'experts de 552 milliards de paramètres, avec vision native et une fenêtre de contexte de 1 048 576 tokens, qui va jusqu'à 393 216 tokens en sortie. Les tarifs suivent un découpage heures de pointe et heures creuses : hors pointe, 0,003 $ par million de tokens en entrée en cas de cache hit, 0,15 $ en cas de cache miss, et 0,60 $ par million de tokens en sortie. Aux heures de pointe (matins de semaine, UTC), les tarifs sont exactement le double.

Cette tarification par paliers reprend le réflexe habituel de DeepSeek : casser fortement les prix des API occidentales pendant les fenêtres de faible demande, pour attirer les traitements par lots et les charges peu sensibles à la latence, tout en facturant assez aux heures de pointe pour gérer la capacité.
