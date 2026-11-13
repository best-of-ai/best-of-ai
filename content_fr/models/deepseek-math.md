---
title: 'DeepSeek-Math'
name: 'DeepSeek-Math'
slug: 'deepseek-math'
subtitle: "Modèle à poids ouverts de DeepSeek, spécialisé dans le raisonnement mathématique"
description: "Modèle à poids ouverts de DeepSeek, spécialisé dans le raisonnement mathématique"
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 4
release_date: '2024-02-05'
param_count: '7B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, math, reasoning]
i18n_source: 'f4c27d033105'
---

DeepSeekMath est un modèle de 7 milliards de paramètres que DeepSeek a construit pour le raisonnement mathématique. Il est sorti en février 2024, initialisé à partir de DeepSeek-Coder-Base. L'entraînement a porté sur 120 milliards de tokens liés aux maths, tirés du web, avec de la langue naturelle et du code. Il a obtenu 51,7 % sur le benchmark MATH de niveau compétition, sans calculatrice ni outil externe. À l'époque, ce résultat approchait celui de modèles fermés bien plus gros, comme Gemini-Ultra et GPT-4. DeepSeek l'a publié en variante de base, en variante ajustée pour les instructions et en variante ajustée par apprentissage par renforcement. La version RL a été entraînée avec Group Relative Policy Optimization, un algorithme introduit dans cet article et réutilisé ensuite pour DeepSeek-R1. La fenêtre de contexte est de 4 096 tokens. Le modèle vise les chercheurs et les développeurs qui travaillent sur le tutorat en maths, la démonstration de théorèmes et le raisonnement quantitatif, pas le chat généraliste.
