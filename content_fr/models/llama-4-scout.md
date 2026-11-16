---
title: 'Llama 4 Scout'
name: 'Llama 4 Scout'
slug: 'llama-4-scout'
subtitle: "Palier Llama 4 plus petit et plus rapide de Meta, avec une fenêtre de contexte de 10 millions de tokens"
description: "Palier Llama 4 plus petit et plus rapide de Meta, avec une fenêtre de contexte de 10 millions de tokens"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2025-04-05'
param_count: '109B (17B active)'
context_window_tokens: 10000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 80.5
lmarena_score: 1290
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, self-hosted]
i18n_source: 'a01f39772dca'
---

Llama 4 Scout est le petit frère de la sortie Llama 4 de Meta en avril 2025, un mélange d'experts de 109 milliards de paramètres au total et 17 milliards actifs par token, répartis sur 16 experts. Son trait marquant est la longueur de contexte : Scout prend en charge jusqu'à 10 millions de tokens, bien au-delà de ce que proposaient les autres modèles ouvertement disponibles au lancement, ce qui convient à des tâches comme résumer une base de code entière ou une longue collection de documents en une seule passe. Comme Maverick, il est nativement multimodal et entraîné pour traiter texte et images ensemble. Meta a positionné Scout comme une option plus rapide et moins chère, qui dépasse quand même des modèles comme Gemma 3 et Gemini 2.0 Flash-Lite sur les benchmarks publics, et il tourne sur un seul GPU H100 une fois quantifié, ce qui l'a rendu courant pour les déploiements auto-hébergés.
