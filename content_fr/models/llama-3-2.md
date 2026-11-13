---
title: 'Llama 3.2'
name: 'Llama 3.2'
slug: 'llama-3-2'
subtitle: "Première génération Llama de Meta avec des paliers vision et pour l'appareil"
description: "Première génération Llama de Meta avec des paliers vision et pour l'appareil"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2024-09-25'
param_count: '90B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Llama 3.2 Community License'
api_available: true
mmlu_score: 86.0
lmarena_score: 1250
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, self-hosted]
extra_model_types: ['Reasoning']
i18n_source: '70c7f383bbf6'
---

Llama 3.2 est la sortie de Meta de septembre 2024 qui a d'abord amené la vision dans la gamme Llama, à côté d'un ensemble de petits modèles texte seuls, faits pour les téléphones et les appareils en périphérie. La variante vision phare, en 90B, associe une base de texte Llama 3.1 à un encodeur d'images entraîné sur environ six milliards de paires image-texte : il peut lire des graphiques, légender des photos et répondre à des questions sur une image, en plus des prompts texte. Meta a aussi livré des modèles légers 1B et 3B dans la même famille, prévus pour tourner en local sur du hardware mobile plutôt que dans un centre de données. Sur les benchmarks de raisonnement, le modèle 90B se place près de Llama 3.1 70B tout en ajoutant l'entrée multimodale, et il est distribué sous la Llama 3.2 Community License, avec les poids sur Hugging Face.
