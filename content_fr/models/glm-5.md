---
title: 'GLM-5'
name: 'GLM-5'
slug: 'glm-5'
subtitle: "Le modèle frontier à poids ouverts de Zhipu, entraîné entièrement sur du hardware Huawei national"
description: "Le modèle frontier à poids ouverts de Zhipu, entraîné entièrement sur du hardware Huawei national"
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-02-11'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 203000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.57
output_price_usd_per_m: 1.92
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
i18n_source: 'd5e3911c0704'
---

GLM-5 est le modèle frontier à poids ouverts de Zhipu AI, publié le 11 février 2026 comme un quasi-doublement d'échelle par rapport à GLM-4.5, de 355 milliards à environ 744 milliards de paramètres au total, en gardant autour de 40 milliards actifs par token dans son mélange d'experts. Il sort avec une fenêtre de contexte de 203 000 tokens, bien en deçà du million de tokens que son successeur GLM-5.2 ajouterait quatre mois plus tard, et Zhipu l'a entraîné entièrement sur des puces Huawei Ascend avec le framework MindSpore, et non sur du hardware Nvidia. Le tarif de l'API commence à 0,57 $ par million de tokens d'entrée et 1,92 $ par million de tokens de sortie, via la plateforme de Zhipu et l'API WaveSpeed. Il est sorti sous licence MIT, et la couverture de l'époque l'a présenté comme le premier modèle de classe frontier d'un labo chinois construit sur du hardware entièrement national.
