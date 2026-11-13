---
title: 'Falcon 3'
name: 'Falcon 3'
slug: 'falcon-3'
subtitle: 'La famille de petits modèles efficaces à poids ouverts de TII'
description: 'La famille de petits modèles efficaces à poids ouverts de TII'
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 4
release_date: '2024-12-17'
param_count: '10B'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Falcon License'
api_available: false
mmlu_score: 73.1
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
i18n_source: 'c646be262a46'
---

Falcon 3 est une famille de modèles de langage à poids ouverts du Technology Innovation Institute, à Abou Dhabi, sortie en décembre 2024 en quatre tailles : 1B, 3B, 7B et 10B de paramètres, chacune en versions base et instruct. TII a construit la gamme pour tourner sur du matériel modeste, y compris un seul GPU ou un ordinateur portable, tout en tenant la comparaison avec des modèles ouverts plus grands. Le modèle 10B a pris la tête du leaderboard de Hugging Face pour les modèles sous 13B de paramètres au lancement, avec 73,1 au MMLU et 83,1 au GSM8K, devant les variantes Llama et Gemma comparables à l'époque. La plupart des tailles prennent en charge une fenêtre de contexte de 32K tokens (le modèle 1B est limité à 8K), et TII distribue les poids sur Hugging Face sous sa propre Falcon License, pour un usage auto-hébergé. Falcon 3 suit les sorties Falcon et Falcon Mamba plus anciennes, et marque le virage de TII vers des modèles plus petits, moins chers à faire tourner, plutôt que la course aux nombres de paramètres de frontière.
