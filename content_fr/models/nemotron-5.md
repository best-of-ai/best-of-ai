---
title: 'Nemotron 5'
name: 'Nemotron 5'
slug: 'nemotron-5'
subtitle: "Le modèle à poids ouverts de NVIDIA, réglé pour une inférence efficace sur son propre hardware"
description: "Le modèle à poids ouverts de NVIDIA, réglé pour une inférence efficace sur son propre hardware"
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/nemotron'
price: 'Free'
rank: 6
release_date: '2026-07-10'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'NVIDIA Open Model License'
api_available: true
mmlu_score: 82.0
humaneval_score: 80.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'NVIDIA NIM', 'NGC']
date: '2026-07-19'
tags: [llm, open-weight, self-hosted, efficiency]
i18n_source: '528d47e90cc1'
---

Nemotron 5 poursuit la ligne de modèles à poids ouverts de NVIDIA, construits moins pour arriver en tête des classements que pour montrer à quel point les modèles tournent bien sur les GPU et la pile d'inférence de l'entreprise. C'est un modèle dense de 70 milliards de paramètres, avec une fenêtre de contexte de 128 000 tokens, distribué sous la NVIDIA Open Model License et empaqueté pour un déploiement en un clic via les microservices NVIDIA NIM, ainsi qu'en téléchargement simple sur Hugging Face.

Depuis Nemotron-4 340B, NVIDIA se sert de la ligne Nemotron pour montrer des techniques comme l'élagage et la distillation, qui réduisent les modèles sans trop dégrader la qualité, et Nemotron 5 garde ce cap. La taille de 70 milliards a été choisie pour tenir sur un seul H100, ou sur deux GPU grand public avec une quantification raisonnable. L'argument de NVIDIA, ici, c'est surtout la pile hardware et logicielle sous le modèle, pas le modèle lui-même.
