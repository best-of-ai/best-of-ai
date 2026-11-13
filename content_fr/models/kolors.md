---
title: 'Kolors'
name: 'Kolors'
slug: 'kolors'
subtitle: "Modèle texte-vers-image à poids ouverts de Kuaishou, solide sur les prompts en chinois"
description: "Modèle texte-vers-image à poids ouverts de Kuaishou, solide sur les prompts en chinois"
company: 'kuaishou'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Kwai-Kolors/Kolors'
price: 'Free'
rank: 5
release_date: '2024-07-06'
param_count: '2.6B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Kuaishou API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: 'b566c88c4748'
---

Kolors est le modèle texte-vers-image à poids ouverts de Kuaishou, sorti en juillet 2024. C'est un modèle de diffusion latente d'environ 2,6 milliards de paramètres, construit sur une architecture U-Net, et il utilise ChatGLM comme encodeur de texte plutôt qu'un encodeur de type CLIP, ce qui lui donne un net avantage pour lire et rendre les prompts en chinois et le texte chinois dans les images. Il génère en résolution native 1024x1024 et prend en charge plusieurs rapports d'aspect. Kuaishou l'a entraîné sur des milliards de paires texte-image et a publié les poids sur GitHub et Hugging Face, gratuitement pour la recherche, avec une inscription séparée pour le déploiement commercial. Aux côtés de modèles comme Flux et Stable Diffusion 3, Kolors est l'un des rares modèles d'image ouverts largement utilisés qui gèrent bien les écritures non latines.
