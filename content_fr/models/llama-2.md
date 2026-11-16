---
title: 'Llama 2'
name: 'Llama 2'
slug: 'llama-2'
subtitle: "Sortie à poids ouverts de Meta en 2023, qui a lancé l'écosystème des LLM ouverts"
description: "Sortie à poids ouverts de Meta en 2023, qui a lancé l'écosystème des LLM ouverts"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2023-07-18'
param_count: '70B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
mmlu_score: 68.9
humaneval_score: 29.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '69c51717a945'
---

Llama 2 est la gamme de modèles de langage à poids ouverts de deuxième génération chez Meta, sortie le 18 juillet 2023 en 7B, 13B et 70B, avec des versions chat de chacune. Il a été entraîné sur 2 billions de tokens et prend en charge une fenêtre de contexte de 4 096 tokens, modeste aux standards plus tardifs, mais compétitive à son lancement. Le modèle 70B a obtenu 68,9 au MMLU, proche de GPT-3.5, même s'il restait loin derrière en génération de code, avec seulement 29,9 au HumanEval contre 48,1 pour GPT-3.5. Ce qui comptait plus que les scores bruts, c'était la licence : Meta autorisait un usage commercial pour la plupart des entreprises, ce qui a fait de Llama 2 le premier modèle à poids ouverts vraiment assez bon pour construire des produits, et il a lancé la vague de variantes ajustées, de versions quantifiées et de modèles dérivés qui peuplent maintenant Hugging Face. Les poids se téléchargent encore librement des années plus tard, même si Meta a depuis sorti Llama 3 et Llama 4.
