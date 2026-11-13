---
title: 'CLIP'
name: 'CLIP'
slug: 'clip'
subtitle: "Modèle contrastif image-texte fondateur d'OpenAI, derrière une grande partie de l'IA multimodale actuelle"
description: "Modèle contrastif image-texte fondateur d'OpenAI, derrière une grande partie de l'IA multimodale actuelle"
company: 'openai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://openai.com/index/clip/'
price: 'Free'
rank: 8
release_date: '2021-01-05'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy, foundation-model]
i18n_source: 'bc970f441b1f'
---

CLIP (Contrastive Language-Image Pre-training) est un modèle qu'OpenAI a publié en janvier 2021 pour associer des images à des descriptions en texte. Il a été entraîné sur 400 millions de paires image-texte prises sur internet, avec un objectif contrastif qui rapproche les embeddings d'une image et d'un texte qui vont ensemble, et éloigne les paires qui ne correspondent pas. La plus grande variante publiée, bâtie sur un vision transformer ViT-L/14 associé à un transformeur de texte de 63 millions de paramètres, totalise environ 428 millions de paramètres. Au lieu d'être entraîné pour une seule tâche étroite, CLIP apprend un espace d'embeddings commun, à usage général, pour les images et le texte. Il peut ainsi classer des images en zero-shot, en comparant une image à un ensemble d'étiquettes textuelles, sans fine-tuning propre à la tâche.

L'effet réel de CLIP est venu après la sortie, pas des scores de benchmark mis en avant. Ses encodeurs d'image et de texte sont devenus la base d'une série de systèmes plus tardifs, dont le pipeline de génération d'images de DALL-E 2, le conditionnement par le texte de Stable Diffusion, et d'innombrables outils de recherche et de récupération d'images. Meta, Salesforce et d'autres labos ont publié leurs propres variantes et ajustements de CLIP, mais les poids d'origine d'OpenAI, sous licence MIT sur GitHub et Hugging Face, restent un point de départ courant pour les projets multimodaux, même des années après la publication.
