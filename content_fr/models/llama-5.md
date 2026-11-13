---
title: 'Llama 5'
name: 'Llama 5'
slug: 'llama-5'
subtitle: "Prochain modèle phare multimodal à poids ouverts de Meta, pour l'appareil comme pour le centre de données"
description: "Prochain modèle phare multimodal à poids ouverts de Meta, pour l'appareil comme pour le centre de données"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 9
release_date: '2026-07-14'
param_count: '520B (24B active)'
context_window_tokens: 2000000
modality: [text, image, audio]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 89.5
humaneval_score: 90.0
lmarena_score: 1381
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock', 'Azure AI Foundry']
date: '2026-07-19'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
i18n_source: '47cdfc96510e'
---

Llama 5 est la suite de la gamme Llama 4 de l'an dernier chez Meta, à nouveau livré comme mélange d'experts, mais monté à 520 milliards de paramètres au total, avec 24 milliards actifs par token. Le plus grand saut est la fenêtre de contexte de 2 millions de tokens, le double de ce que proposait Llama 4 Maverick, que Meta destine à des tâches comme ingérer des bases de code entières ou de longues transcriptions vidéo en une seule passe. Il gère le texte, l'image et l'audio en entrée nativement, plutôt que d'ajouter des encodeurs sur une base texte seule, et Meta dit qu'il devance de peu Gemini 3.5 Pro et GPT-5.6 sur plusieurs benchmarks ouverts, tout en restant économe grâce au routage clairsemé des experts.

Comme pour les sorties Llama précédentes, les poids sont ouverts sous la Llama 4 Community License et disponibles tout de suite sur Hugging Face, avec des partenaires d'hébergement comme Together AI, AWS Bedrock et Azure AI Foundry qui proposent une inférence managée pour les équipes qui ne veulent pas le faire tourner elles-mêmes. Meta continue de refuser les droits commerciaux complets aux entreprises au-dessus d'un certain seuil d'utilisateurs, la même réserve appliquée depuis Llama 2.
