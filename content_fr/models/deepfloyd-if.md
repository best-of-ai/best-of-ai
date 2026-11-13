---
title: 'DeepFloyd IF'
name: 'DeepFloyd IF'
slug: 'deepfloyd-if'
subtitle: "Modèle texte-vers-image en espace pixel (non latent), du labo DeepFloyd soutenu par Stability"
description: "Modèle texte-vers-image en espace pixel (non latent), du labo DeepFloyd soutenu par Stability"
company: 'stability-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://stability.ai/news/deepfloyd-if-text-to-image-model'
price: 'Free'
rank: 5
release_date: '2023-04-28'
param_count: '4.3B'
modality: [text, image]
open_weight: true
license: 'Stability Community License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [image-generation, open-weight, legacy]
i18n_source: 'e6c34510f10f'
---

DeepFloyd IF est un modèle texte-vers-image sorti en avril 2023 par DeepFloyd, un labo de recherche soutenu par Stability AI. Il ne suit pas la diffusion en espace latent de Stable Diffusion : il travaille directement dans l'espace des pixels, sur une cascade de trois modules. Il génère d'abord une image en 64x64, puis la suréchantillonne par étapes jusqu'à 1024x1024. Ça lui a valu une réputation solide pour le texte lisible à l'intérieur des images, une tâche que les modèles de diffusion latente de cette époque rataient souvent. DeepFloyd a entraîné trois tailles du module de base, la plus grande à 4,3 milliards de paramètres. Le pipeline complet est sorti en aperçu de recherche non commercial, sous une Stability Community License, et non sous une licence pleinement ouverte. Il n'est jamais devenu un produit grand public comme Stable Diffusion, mais ses résultats sur le texte ont influencé des modèles commerciaux plus tardifs, qui ont corrigé la même faiblesse.
