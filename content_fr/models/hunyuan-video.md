---
title: 'Hunyuan Video'
name: 'Hunyuan Video'
slug: 'hunyuan-video'
subtitle: "Modèle de génération texte-vers-vidéo à poids ouverts de Tencent"
description: "Modèle de génération texte-vers-vidéo à poids ouverts de Tencent"
company: 'tencent'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://aivideo.hunyuan.tencent.com/'
price: 'Free'
rank: 6
release_date: '2024-12-03'
param_count: '13B'
modality: [text, video]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [video-generation, open-weight, text-to-video]
i18n_source: '840cb7f4cbbc'
---

HunyuanVideo est le modèle de génération vidéo à poids ouverts de Tencent, sorti en décembre 2024 avec environ 13 milliards de paramètres, ce qui en faisait alors le plus grand modèle vidéo ouvert disponible. Il génère des extraits texte-vers-vidéo et image-vers-vidéo jusqu'à environ 720p et cinq secondes, avec un suivi du prompt et une qualité de mouvement que des tests ont comparés favorablement à des modèles fermés comme Runway Gen-3 et Kling. Tencent a publié le code complet d'entraînement et d'inférence, ainsi que les poids préentraînés, sur GitHub et Hugging Face, sous une licence qui autorise un usage commercial dans la plupart des juridictions. C'était inhabituel pour un modèle de cette échelle à la sortie. Les poids ouverts permettent aux chercheurs et aux studios de l'ajuster (fine-tuning) pour des styles ou des sujets précis, plutôt que de passer seulement par une API. Tencent a ensuite enchaîné avec HunyuanVideo-1.5, un modèle plus petit de 8,3 milliards de paramètres qui atteint une qualité comparable avec moins de calcul.
