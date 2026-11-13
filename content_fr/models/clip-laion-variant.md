---
title: 'CLIP (LAION variant)'
name: 'CLIP (LAION variant)'
slug: 'clip-laion-variant'
subtitle: "Réentraînement à poids ouverts de CLIP par LAION, modèle d'embeddings vision-langage"
description: "Réentraînement à poids ouverts de CLIP par LAION, modèle d'embeddings vision-langage"
company: 'laion'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://laion.ai/'
price: 'Free'
rank: 4
release_date: '2022-09-15'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, vision, self-hosted]
i18n_source: '40efbd85bd2a'
---

Cette variante de CLIP est un réentraînement à poids ouverts de l'architecture CLIP d'origine d'OpenAI, produit par LAION et distribué via le projet open_clip, et non par OpenAI. Elle s'appuie sur le vision transformer ViT-L/14, compte environ 428 millions de paramètres, et a été entraînée sur LAION-2B, le sous-ensemble anglais de 2 milliards de paires image-texte du jeu plus large LAION-5B, sur 384 GPU A100 du supercalculateur JUWELS. Comme le CLIP d'origine, elle place images et texte dans un espace d'embeddings commun. On peut donc faire de la classification d'images zero-shot, de la recherche image-texte et de la recherche par similarité, sans fine-tuning propre à la tâche. Elle atteint environ 75,3 % de précision zero-shot sur ImageNet-1k. Les poids sont publiés sous une licence ouverte et hébergés sur Hugging Face, et elle est devenue un remplacement courant des checkpoints CLIP fermés d'OpenAI dans les pipelines open source de recherche d'images, de légendage et d'art génératif, y compris comme encodeur de texte dans plusieurs variantes de Stable Diffusion.
