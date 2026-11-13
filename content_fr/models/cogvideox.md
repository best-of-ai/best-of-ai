---
title: 'CogVideoX'
name: 'CogVideoX'
slug: 'cogvideox'
subtitle: "Famille de modèles texte-vers-vidéo à poids ouverts de Zhipu"
description: "Famille de modèles texte-vers-vidéo à poids ouverts de Zhipu"
company: 'zhipu-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogVideo'
price: 'Free'
rank: 6
release_date: '2024-08-27'
param_count: '5B'
modality: [text, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [video-generation, open-weight, api]
i18n_source: '892ae410997f'
---

CogVideoX est le modèle texte-vers-vidéo à poids ouverts de Zhipu AI, construit avec le labo KEG de l'université Tsinghua et sorti en août 2024 comme successeur du projet CogVideo d'origine. Il existe en variantes 2B et 5B, avec un VAE causal 3D pour la compression spatiale et temporelle, et un transformeur à expert adaptive LayerNorm. Il gère le texte-vers-vidéo, l'image-vers-vidéo et la continuation d'une vidéo à partir d'une seule image ou d'un prompt. Le modèle 5B produit des séquences jusqu'à 10 secondes, jusqu'à 768p et 16 images par seconde. Zhipu a ensuite sorti une mise à jour CogVideoX-1.5 en novembre 2024, avec des sorties plus longues et de plus haute résolution. Les poids sont sous Apache 2.0 et hébergés sur Hugging Face, et Zhipu sert aussi les modèles via sa propre API. CogVideoX fonctionne donc comme modèle ouvert auto-hébergé et comme service hébergé, un peu comme Stability AI et Runway placent leurs générateurs de vidéo.
