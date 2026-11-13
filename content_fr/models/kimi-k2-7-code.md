---
title: 'Kimi K2.7 Code'
name: 'Kimi K2.7 Code'
slug: 'kimi-k2-7-code'
subtitle: "Modèle de code agentique à poids ouverts de Moonshot, réglé pour les outils et les tâches longues"
description: "Modèle de code agentique à poids ouverts de Moonshot, réglé pour les outils et les tâches longues"
company: 'moonshot-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-06-12'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.95
output_price_usd_per_m: 4.0
api_available: true
humaneval_score: 90.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: '7d2adc3dc4a7'
---

Kimi K2.7 Code est le modèle de Moonshot AI centré sur le code, sorti en juin 2026 comme version spécialisée par-dessus Kimi K2.6. Il garde la même architecture de mélange d'experts à 1 billion de paramètres, avec environ 32 milliards de paramètres actifs et une fenêtre de contexte de 256 000 tokens, mais le modèle est ajusté spécifiquement pour le code sur un long horizon et la décomposition de tâches agentiques. Moonshot annonce des gains d'environ 22 % sur son Kimi Code Bench v2, 11 % sur Program Bench et 31,5 % sur MLS Bench Lite par rapport à K2.6, avec environ 30 % de tokens de raisonnement en moins par tâche, ce qui baisse le coût effectif dans une boucle d'agent. Le modèle tourne toujours en mode thinking et ne propose pas de repli sans ce mode, et il accepte du texte, de l'image et de la vidéo en plus du code. Les poids sont ouverts sur Hugging Face, et l'API de Moonshot le tarife bien en dessous de concurrents fermés comme Claude Opus et GPT-5.5, en entrée comme en sortie.
