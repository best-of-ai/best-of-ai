---
title: 'GPT-NeoX-20B'
name: 'GPT-NeoX-20B'
slug: 'gpt-neox-20b'
subtitle: "Le modèle à poids ouverts d'EleutherAI, l'un des plus grands checkpoints publics de son époque"
description: "Le modèle à poids ouverts d'EleutherAI, l'un des plus grands checkpoints publics de son époque"
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 4
release_date: '2022-04-14'
param_count: '20B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
i18n_source: '3f0cef2ef3c0'
---

GPT-NeoX-20B est un modèle de langage de 20 milliards de paramètres qu'EleutherAI a annoncé en avril 2022, après environ un an de travail sur son cadre d'entraînement GPT-NeoX, construit sur Megatron et DeepSpeed. À la sortie, c'était le plus grand modèle de langage autorégressif dense dont les poids étaient téléchargeables publiquement. Il a été entraîné sur the Pile, avec une fenêtre de contexte de 2 048 tokens. Sur le harness d'évaluation d'EleutherAI, il se plaçait entre les modèles Curie et Davinci d'OpenAI sur la plupart des benchmarks NLP standards. En one-shot, sur des problèmes de maths formulés en mots, il battait le GPT-3 complet de 175B sur ce test précis. L'équipe y a vu la preuve que la qualité des données d'entraînement comptait autant que l'échelle brute. Il est sorti sous licence Apache 2.0 via Hugging Face, ce qui donnait aux chercheurs un grand modèle inspectable, à étudier et à ajuster par fine-tuning, sans API fermée. Des modèles ouverts bien plus grands et plus efficaces l'ont depuis dépassé, mais il est resté une référence dans la recherche LLM open source, comme l'une des bases de code d'entraînement sur lesquelles le domaine s'est appuyé.
