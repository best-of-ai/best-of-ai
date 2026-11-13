---
title: 'DeepSeek-VL2'
name: 'DeepSeek-VL2'
slug: 'deepseek-vl2'
subtitle: "Le modèle vision-langage à mélange d'experts et à poids ouverts de DeepSeek"
description: "Le modèle vision-langage à mélange d'experts et à poids ouverts de DeepSeek"
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-12-13'
param_count: '27B (4.5B active)'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'DeepSeek License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
i18n_source: 'f06b4bb46852'
---

DeepSeek-VL2 est une famille de modèles vision-langage que DeepSeek a publiée le 13 décembre 2024, dans la suite du DeepSeek-VL original sorti plus tôt la même année. Elle existe en trois tailles, Tiny, Small et le VL2 complet, avec 3B, 16B et 27B de paramètres au total et 1B, 2,8B et 4,5B de paramètres actifs, sur la même architecture DeepSeekMoE et Multi-head Latent Attention que les modèles de langage de DeepSeek. Un tuilage dynamique lui permet de traiter des images haute résolution de ratios variés sans perdre de détail, ce qui aide pour lire des documents denses, des graphiques et des captures d'écran.

Le mélange d'experts permet à DeepSeek-VL2 de bien tenir sur les benchmarks de question-réponse visuelle, d'OCR et d'ancrage visuel, tout en gardant une inférence peu coûteuse au regard du nombre total de paramètres, puisque seule une petite fraction des experts s'active pour une entrée donnée. Les trois tailles ont été publiées avec des poids ouverts, ce qui faisait de DeepSeek-VL2 l'une des familles de modèles multimodaux ouverts les plus capables du moment.
