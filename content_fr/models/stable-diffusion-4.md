---
title: 'Stable Diffusion 4'
name: 'Stable Diffusion 4'
slug: 'stable-diffusion-4'
subtitle: "Le modèle de diffusion texte-vers-image à poids ouverts suivant, chez Stability AI"
description: "Le modèle de diffusion texte-vers-image à poids ouverts suivant, chez Stability AI"
company: 'stability-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://stability.ai/'
price: 'Free'
rank: 7
release_date: '2026-07-15'
param_count: '12B'
modality: [text, image]
open_weight: true
license: 'Stability AI Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Stability API']
date: '2026-07-19'
tags: [image-generation, open-weight, text-to-image, diffusion, self-hosted]
i18n_source: '14d55cb2be7c'
---

Stable Diffusion 4 est la première grande mise à jour de la gamme chez Stability AI depuis SD 3.5, fin 2024. Le modèle passe à 12 milliards de paramètres et améliore le suivi du prompt et le rendu du texte dans les images, deux faiblesses de longue date face à des concurrents fermés comme Midjourney et Imagen. Il sort sous la même Stability AI Community License que SD 3.5, gratuit pour les particuliers et les petites entreprises, avec une licence payante obligatoire au-dessus d'un seuil de chiffre d'affaires.

Les poids sont sur Hugging Face comme d'habitude, les versions quantifiées tournent sur un seul GPU grand public, et Stability propose aussi une inférence hébergée via sa propre API pour les équipes qui ne veulent pas gérer l'infrastructure. SD4 arrive alors que Stability subit une vraie pression de FLUX et d'autres modèles d'images ouverts, qui ont entamé son avance. La sortie s'appuie beaucoup sur l'écosystème de fine-tuning de la communauté (LoRAs, ControlNets, checkpoints personnalisés), qui a gardé Stable Diffusion comme choix par défaut pour la génération d'images à poids ouverts, malgré une concurrence plus forte.
