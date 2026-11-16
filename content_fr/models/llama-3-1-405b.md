---
title: 'Llama 3.1 405B'
name: 'Llama 3.1 405B'
slug: 'llama-3-1-405b'
subtitle: "Plus grand modèle dense à poids ouverts de Meta, au niveau des modèles fermés de premier plan"
description: "Plus grand modèle dense à poids ouverts de Meta, au niveau des modèles fermés de premier plan"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2024-07-23'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
mmlu_score: 88.6
humaneval_score: 89.0
lmarena_score: 1265
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, foundation-model]
extra_model_types: ['Code']
i18n_source: 'c720dd46ff12'
---

Llama 3.1 405B est le plus grand modèle Llama 3.1 de Meta, sorti le 23 juillet 2024 comme transformeur dense de 405 milliards de paramètres, et non un mélange d'experts. Il prend en charge une fenêtre de contexte de 128 000 tokens et a obtenu 88,6 au MMLU et 89,0 au HumanEval, dans la même fourchette que GPT-4 en connaissances comme en code. C'était le premier modèle à poids ouverts à vraiment égaler un modèle fermé de premier plan, plutôt que de rester une génération en retrait, et Meta l'a sorti avec des versions plus petites, 70B et 8B, entraînées de la même façon, pour que les développeurs choisissent un compromis entre qualité et coût. Il est disponible en auto-hébergement via Hugging Face, et en inférence hébergée chez Together AI, Fireworks, AWS Bedrock, Azure et Google Cloud, les fournisseurs le tarifant bien en dessous des modèles fermés équivalents puisque Meta ne fait pas payer les poids. Llama 3.1 405B a poussé l'argument de Meta : un modèle ouvert pouvait se tenir au premier plan, et pas seulement être une alternative moins chère et plus faible.
