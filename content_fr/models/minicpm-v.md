---
title: 'MiniCPM-V'
name: 'MiniCPM-V'
slug: 'minicpm-v'
subtitle: "Modèle multimodal pour l'edge d'OpenBMB, capable de tâches de vision au niveau de GPT-4V sur un téléphone"
description: "Modèle multimodal pour l'edge d'OpenBMB, capable de tâches de vision au niveau de GPT-4V sur un téléphone"
company: 'openbmb'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM-V'
price: 'Free'
rank: 5
release_date: '2024-05-20'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, small-model, on-device]
i18n_source: '83a16a62bccc'
---

MiniCPM-V est une gamme de modèles vision-langage à poids ouverts d'OpenBMB, un labo de recherche issu de l'université Tsinghua, construite pour faire tourner la compréhension de la vision et de la vidéo sur des téléphones et d'autres appareils aux ressources limitées, plutôt que d'exiger un GPU de serveur. La sortie de mai 2024, MiniCPM-Llama3-V 2.5, associe une base Llama3 de 8 milliards de paramètres à un encodeur de vision SigLip, et annonce une performance en OCR, en raisonnement multi-images et en questions-réponses visuelles générales qui égale ou dépasse GPT-4V sur plusieurs benchmarks publics, tout en tournant entièrement hors ligne sur un téléphone.

OpenBMB a continué d'itérer sur la série depuis, avec des versions plus tardives comme MiniCPM-V 4.5 et 4.6 qui réduisent encore le nombre de paramètres tout en améliorant la précision, dans un mouvement plus large qui réduit l'écart entre les petits modèles multimodaux sur l'appareil et des modèles bien plus grands hébergés dans le cloud. Les modèles sont sous licence Apache 2.0 sur Hugging Face et GitHub, visés vers les développeurs qui ont besoin d'une IA multimodale hors ligne, qui préserve la vie privée, sur du hardware grand public.
