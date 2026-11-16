---
title: 'DeepSeek Coder V2'
name: 'DeepSeek Coder V2'
slug: 'deepseek-coder-v2'
subtitle: "Modèle à mélange d'experts de DeepSeek, à poids ouverts et spécialisé dans le code"
description: "Modèle à mélange d'experts de DeepSeek, à poids ouverts et spécialisé dans le code"
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2024-06-17'
param_count: '236B (21B active)'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'MIT'
api_available: true
humaneval_score: 90.2
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '5e8d9823340f'
---

DeepSeek-Coder-V2 est le modèle de code de deuxième génération de DeepSeek, sorti en juin 2024. C'est un mélange d'experts, avec 236 milliards de paramètres au total et 21 milliards actifs par token. La fenêtre de contexte passe à 128 000 tokens, très au-dessus des 16 000 du DeepSeek-Coder d'origine, et la couverture va de 86 à 338 langages de programmation. Sur HumanEval, il a obtenu 90,2 %. DeepSeek présentait alors ce score comme un rapprochement avec des modèles fermés comme GPT-4 Turbo sur les tâches de code. Il progressait aussi, par rapport à son prédécesseur, sur les benchmarks de raisonnement général et de maths. Contrairement à la licence plus restrictive du DeepSeek-Coder d'origine, DeepSeek-Coder-V2 est sous licence MIT, donc utilisable librement pour des projets commerciaux. Les poids sont sur Hugging Face, avec un accès API via la plateforme de DeepSeek.
