---
title: 'Imagen'
name: 'Imagen'
slug: 'imagen'
subtitle: "Modèle de diffusion texte-vers-image d'origine de Google, présenté avec Parti comme aperçu de recherche"
description: "Modèle de diffusion texte-vers-image d'origine de Google, présenté avec Parti comme aperçu de recherche"
company: 'google-deepmind'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://imagen.research.google/'
price: 'Paid'
rank: 6
release_date: '2022-05-24'
param_count: 'Undisclosed'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, research, legacy]
i18n_source: '6e5bc6e9c169'
---

Imagen est le modèle de diffusion texte-vers-image d'origine de Google Research, décrit dans un article intitulé « Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding » et déposé sur arXiv en mai 2022. Il associe un grand modèle de langage gelé, T5, à une cascade de modèles de diffusion : un modèle de base qui génère une petite image en 64x64, puis deux étages de super-résolution qui la portent à 256x256, puis à 1024x1024. Le résultat central de l'article était qu'agrandir l'encodeur de texte améliorait la qualité d'image et l'alignement au prompt plus qu'agrandir le réseau de diffusion d'images lui-même, un résultat qui a influencé les systèmes texte-vers-image suivants dans le secteur. Imagen a annoncé un score FID état de l'art de 7,27 sur le benchmark COCO, sans jamais s'être entraîné sur les données COCO.

Google n'a jamais sorti Imagen comme produit public. Il est resté un aperçu de recherche, montré aux côtés du modèle autorégressif Parti et comparé à DALL-E 2 d'OpenAI, sorti quelques mois plus tôt. Le nom et la lignée ont continué dans les modèles d'images commerciaux suivants de Google, Imagen 2, 3 et 4, qui reprennent la même approche de diffusion, mais ajoutent l'infrastructure de production, le filtrage de sécurité et l'accès API qui manquaient au modèle de recherche d'origine.
