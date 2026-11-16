---
title: 'Ministral 8B'
name: 'Ministral 8B'
slug: 'ministral-8b'
subtitle: "Le modèle compact de Mistral, fait pour le déploiement sur l'appareil et en périphérie"
description: "Le modèle compact de Mistral, fait pour le déploiement sur l'appareil et en périphérie"
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/ministraux/'
price: 'Free'
rank: 4
release_date: '2024-10-16'
param_count: '8B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Mistral Research License'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.1
api_available: true
mmlu_score: 65.0
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, small-model, on-device]
i18n_source: '5f9757c587f7'
---

Ministral 8B est un modèle de 8 milliards de paramètres que Mistral AI a publié en octobre 2024 dans « Les Ministraux », une paire de petits modèles destinés au déploiement sur l'appareil et en périphérie, aux côtés du plus petit Ministral 3B. Il utilise une attention à fenêtre glissante entrelacée pour tenir une fenêtre de contexte de 128 000 tokens malgré sa petite taille. Mistral le plaçait face à des modèles de taille proche, comme Llama 3.1 8B et Gemma 2 9B, en annonçant de meilleurs résultats sur les benchmarks de connaissances, de raisonnement et de multilinguisme dans cette classe.

Mistral l'a publié sous la Mistral Research License, qui autorise l'usage gratuit pour la recherche et les tests, mais exige une licence commerciale pour un déploiement en production, contrairement aux conditions Apache 2.0 entièrement ouvertes de Mistral 7B. Il vise les développeurs qui construisent des applications pour téléphones, ordinateurs portables et autre hardware limité, comme des assistants en local, de la traduction et des agents légers, là où faire tourner un modèle pleine taille n'est pas pratique.
