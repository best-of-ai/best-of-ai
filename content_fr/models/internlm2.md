---
title: 'InternLM2'
name: 'InternLM2'
slug: 'internlm2'
subtitle: "Modèle de fondation à poids ouverts du Shanghai AI Lab, solide en long contexte et en raisonnement"
description: "Modèle de fondation à poids ouverts du Shanghai AI Lab, solide en long contexte et en raisonnement"
company: 'shanghai-ai-lab'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-01-17'
param_count: '20B'
context_window_tokens: 200000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.7
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, long-context]
i18n_source: 'e91b498370ff'
---

InternLM2 est un modèle de langage à poids ouverts du Shanghai AI Laboratory, sorti le 17 janvier 2024 en 7B et 20B, avec des variantes chat correspondantes. Les deux tailles prennent en charge une fenêtre de contexte de 200 000 tokens, obtenue par un entraînement qui commence sur des séquences de 4K tokens et s'étend peu à peu à 32K et au-delà. Le modèle tient bien sur les tests d'aiguille dans une botte de foin pour les longs documents, à cette longueur. La variante chat 20B obtient 67,7 au MMLU, devant plusieurs modèles ouverts de taille proche au moment de la sortie. InternLM2 a été entraîné sur un grand corpus multilingue, avec une force particulière en anglais et en chinois, et il était présenté comme un modèle de fondation généraliste pour le raisonnement, le code et les tâches en long contexte, avant que le Shanghai AI Lab le remplace par InternLM2.5 plus tard dans l'année. Il est sous licence Apache 2.0, distribué via Hugging Face et le dépôt GitHub InternLM.
