---
title: 'Kimi-VL'
name: 'Kimi-VL'
slug: 'kimi-vl'
subtitle: "Modèle vision-langage à poids ouverts de Moonshot"
description: "Modèle vision-langage à poids ouverts de Moonshot"
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 4
release_date: '2025-04-10'
param_count: '16B (2.8B active)'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
extra_model_types: ['Reasoning']
i18n_source: 'edae211c40fc'
---

Kimi-VL est le modèle vision-langage à poids ouverts de Moonshot AI, sorti en avril 2025. Il utilise un mélange d'experts de 16 milliards de paramètres au total, mais seulement environ 2,8 milliards actifs dans son décodeur de langage, ce qui garde l'inférence peu chère par rapport à sa capacité. Le modèle associe ce décodeur à MoonViT, un encodeur de vision à résolution native qui peut lire des images en très haute résolution sans les réduire d'abord, et il gère une fenêtre de contexte de 128 000 tokens pour les longs documents et les vidéos. Kimi-VL vise des tâches de type agent, comme naviguer sur un écran d'ordinateur (il s'en sort bien sur OSWorld), ainsi que l'OCR, le raisonnement mathématique à partir d'images et la comparaison de plusieurs images. Moonshot a aussi sorti une variante Kimi-VL-Thinking, entraînée par apprentissage par renforcement sur des données de chaîne de pensée, qui étend le raisonnement du modèle de base sur des horizons plus longs.
