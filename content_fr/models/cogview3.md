---
title: 'CogView3'
name: 'CogView3'
slug: 'cogview3'
subtitle: "Modèle texte-vers-image de Zhipu, en relay diffusion"
description: "Modèle texte-vers-image de Zhipu, en relay diffusion"
company: 'zhipu-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogView3'
price: 'Free'
rank: 5
release_date: '2024-09-29'
param_count: '3B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: 'e06af9d7cbba'
---

CogView3 est un modèle texte-vers-image de Zhipu AI et de l'université Tsinghua, décrit dans un article de mars 2024 et publié en open source sur Hugging Face en septembre 2024. Il repose sur la relay diffusion, une approche en cascade : un étage de base de 3 milliards de paramètres génère une image basse résolution en 512x512, puis un second étage réinjecte du bruit dans cette image avant une passe de diffusion de super-résolution plus courte, au lieu de conditionner le second étage directement sur la sortie basse résolution, comme le faisaient les anciens modèles en cascade. Zhipu indique que CogView3 dépasse Stable Diffusion XL dans les évaluations humaines, avec une large marge, tout en ne demandant qu'environ la moitié du temps d'inférence. Une version distillée atteint cette qualité avec environ un dixième des pas d'inférence de SDXL. Le modèle et le code sont sous Apache 2.0. Zhipu a enchaîné avec CogView-3Plus, une variante plus grande à transformeur de diffusion dans la même famille, et une version hébergée via l'API Zhipu pour les développeurs qui ne veulent pas le faire tourner eux-mêmes.
