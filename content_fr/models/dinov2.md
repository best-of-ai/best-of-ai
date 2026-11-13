---
title: 'DINOv2'
name: 'DINOv2'
slug: 'dinov2'
subtitle: "Le modèle de vision auto-supervisé de Meta, qui produit des caractéristiques d'image générales sans étiquettes"
description: "Le modèle de vision auto-supervisé de Meta, qui produit des caractéristiques d'image générales sans étiquettes"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/dino-v2-computer-vision-self-supervised-learning/'
price: 'Free'
rank: 6
release_date: '2023-04-17'
param_count: '1.1B'
modality: [image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [computer-vision, open-weight, self-supervised]
i18n_source: '35d54331b555'
---

DINOv2 est un modèle de vision par ordinateur que Meta AI a publié en avril 2023, entraîné entièrement sans étiquettes sur un jeu de données sélectionné de 142 millions d'images, appelé LVD-142M. Au lieu d'apprendre à classer des images dans des catégories prédéfinies, il apprend des caractéristiques visuelles générales par distillation auto-supervisée. Ces caractéristiques marchent bien sur un large éventail de tâches en aval, classification d'images, estimation de profondeur, segmentation et recherche, souvent sans aucun fine-tuning. Le plus grand modèle publié compte 1,1 milliard de paramètres.

Comme ces caractéristiques se transfèrent bien telles quelles, DINOv2 est devenu un backbone courant pour d'autres systèmes de vision, y compris en imagerie médicale, où les données étiquetées manquent. Meta a publié le code et les poids du modèle sous licence Apache 2.0, puis a enchaîné avec DINOv3. DINOv2 reste largement utilisé comme extracteur de caractéristiques visuelles généraliste.
