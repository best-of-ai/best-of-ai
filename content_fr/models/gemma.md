---
title: 'Gemma'
name: 'Gemma'
slug: 'gemma'
subtitle: "La première version Gemma à poids ouverts de Google, issue des mêmes recherches que Gemini"
description: "La première version Gemma à poids ouverts de Google, issue des mêmes recherches que Gemini"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://blog.google/technology/developers/gemma-open-models/'
price: 'Free'
rank: 7
release_date: '2024-02-21'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 64.3
humaneval_score: 32.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Google AI Studio']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: 'b40c9be3f894'
---

Gemma est la première famille de modèles de langage à poids ouverts de Google, publiée en février 2024 et issue des mêmes recherches que celles utilisées dans Gemini. Elle est sortie en deux tailles, 2B et 7B de paramètres, chacune avec un checkpoint de base et un checkpoint ajusté par instructions, entraînés respectivement sur 2 billions et 6 billions de tokens de texte web, de maths et de code. La fenêtre de contexte est modeste : 8 192 tokens, comme les autres modèles de cette époque.

Cette sortie comptait, parce qu'elle donnait aux développeurs un petit modèle vraiment utilisable, à faire tourner sur un seul GPU grand public, voire un ordinateur portable, au lieu de dépendre d'une API. Sa licence autorise l'usage commercial, mais bloque une liste d'applications nuisibles que Google précise, un entre-deux entre des licences pleinement ouvertes comme Apache 2.0 et les conditions fermées de la plupart des modèles propriétaires. Gemma a ensuite été supplanté par Gemma 2 et Gemma 3, mais il a fixé le schéma de nom et de licence que Google suit depuis.
