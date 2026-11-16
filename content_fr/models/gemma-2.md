---
title: 'Gemma 2'
name: 'Gemma 2'
slug: 'gemma-2'
subtitle: "La famille de modèles à poids ouverts de la génération précédente chez Google"
description: "La famille de modèles à poids ouverts de la génération précédente chez Google"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 6
release_date: '2024-06-27'
param_count: '27B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 75.2
humaneval_score: 51.8
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted]
extra_model_types: ['Code']
i18n_source: '4b34b113fc55'
---

Gemma 2 est la deuxième génération de la famille de modèles à poids ouverts de Google, issue des mêmes recherches que Gemini, mais publiée pour que chacun puisse la télécharger et la faire tourner. Google a lancé les versions à 9 milliards et 27 milliards de paramètres le 27 juin 2024, puis, plus tard, une version plus petite à 2 milliards de paramètres, prévue pour les ordinateurs portables et les téléphones. Le 27B a été ajusté pour tenir face à des modèles de plus du double de sa taille, et le 9B a dépassé Llama 3 8B et d'autres modèles ouverts de taille proche sur plusieurs benchmarks au lancement, avec 75,2 sur MMLU et 51,8 sur HumanEval.

Google distribue les poids de Gemma 2 sur Hugging Face et Kaggle pour l'auto-hébergement, et le propose aussi via Google AI Studio et Vertex AI à ceux qui préfèrent ne pas le faire tourner eux-mêmes. Il sort sous la licence Gemma propre à Google, qui permet un usage commercial mais comporte des restrictions d'usage, au lieu d'une licence pleinement permissive comme Apache 2.0. Google a depuis publié Gemma 3 comme génération plus récente, donc Gemma 2 est maintenant l'option de la génération précédente dans la gamme, gardée pour la compatibilité et pour les équipes déjà construites dessus.
