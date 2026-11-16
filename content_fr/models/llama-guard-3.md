---
title: 'Llama Guard 3'
name: 'Llama Guard 3'
slug: 'llama-guard-3'
subtitle: "Modèle de classification de sécurité à poids ouverts de Meta, pour modérer l'entrée et la sortie d'un LLM"
description: "Modèle de classification de sécurité à poids ouverts de Meta, pour modérer l'entrée et la sortie d'un LLM"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 4
release_date: '2024-07-23'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, safety, self-hosted]
i18n_source: 'f0c740f9e81b'
---

Llama Guard 3 est le classifieur de sécurité de Meta, sorti en juillet 2024 en même temps que Llama 3.1, et il a remplacé Llama Guard 2 comme modèle de modération recommandé par Meta. Construit sur une base Llama 3.1 8B, il ajoute trois nouvelles catégories de risque par rapport à son prédécesseur, ce qui porte la taxonomie à 14, et il améliore la couverture de modération multilingue. Comme Llama Guard 2, il se place dans un pipeline plutôt que de servir d'assistant autonome : il lit un prompt ou la réponse d'un modèle et renvoie une étiquette safe ou unsafe, plus la catégorie enfreinte. Il est à poids ouverts sous la Llama 3.1 Community License, et il est largement utilisé par les entreprises qui déploient des LLM open source et ont besoin d'une couche de modération sans passer par une API tierce.
