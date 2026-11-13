---
title: 'GPT-5'
name: 'GPT-5'
slug: 'gpt-5'
subtitle: "La famille unifiée de modèles de raisonnement et de chat d'OpenAI"
description: "La famille unifiée de modèles de raisonnement et de chat d'OpenAI"
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/gpt-5'
price: 'Paid'
rank: 9
release_date: '2025-08-07'
param_count: 'Undisclosed'
context_window_tokens: 400000
modality: [text, image, audio]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.25
output_price_usd_per_m: 10
api_available: true
mmlu_score: 90.5
lmarena_score: 1390
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['ChatGPT', 'Azure OpenAI', 'API']
date: '2026-07-16'
tags: [llm, reasoning, foundation-model, multimodal, api]
i18n_source: 'ce69b8070709'
---

GPT-5 est le modèle qu'OpenAI a sorti le 7 août 2025. Il réunit la séparation précédente entre modèles de chat rapides (GPT-4o) et modèles de raisonnement lents (la série o) dans un seul système, qui décide seul de la quantité de raisonnement interne dont un prompt a besoin. Au lieu de faire choisir un modèle, ChatGPT et l'API envoient chaque requête vers un mode interne plus léger ou plus lourd. Ça réduit le nombre de choix côté utilisateur, tout en laissant les clients de l'API fixer un effort de raisonnement explicite. Il arrive avec une fenêtre de contexte de 400 000 tokens (272 000 en entrée, 128 000 en sortie), des tarifs d'API de 1,25 $ par million de tokens d'entrée et 10 $ par million de tokens de sortie, et un score d'environ 90 au MMLU, avec de bons résultats sur les benchmarks de code et d'agents au lancement. OpenAI l'a présenté comme un gain de fiabilité et une baisse du taux d'hallucinations, plutôt qu'un bond marqué de capacité brute, face à Gemini 2.5 Pro de Google et aux modèles Claude d'Anthropic de la même période. À la mi-2026, OpenAI était déjà passé à la ligne GPT-5.x, dont la famille GPT-5.6, mais GPT-5 reste disponible dans l'API et dans ChatGPT.
