---
title: 'Granite 3.0'
name: 'Granite 3.0'
slug: 'granite-3-0'
subtitle: "La famille de modèles à poids ouverts d'IBM pour les secteurs régulés"
description: "La famille de modèles à poids ouverts d'IBM pour les secteurs régulés"
company: 'ibm'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2024-10-21'
param_count: '2B, 8B (dense); 1B, 3B (MoE)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 65.5
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'IBM watsonx']
date: '2026-07-16'
tags: [llm, open-weight, enterprise, self-hosted]
i18n_source: '2ebc701cde02'
---

Granite 3.0 est la troisième génération de modèles de langage ouverts d'IBM, sortie le 21 octobre 2024 pour des usages en entreprise comme le service client, la cybersécurité et les pipelines RAG. La gamme comprend des modèles denses de 2B et 8B, entraînés sur 12 billions de tokens, plus des variantes en mélange d'experts de 1B et 3B. Le tout est sous licence Apache 2.0 : on peut faire du fine-tuning et les déployer commercialement sans restriction. IBM a placé Granite 3.0 face à des modèles de taille proche chez Meta et Mistral, avec des scores compétitifs ou meilleurs sur des benchmarks de raisonnement, de code et de maths, tout en gardant des modèles assez petits pour tourner à bas coût sur des GPU standards. La sortie initiale avait une fenêtre de contexte de 4 000 tokens, ensuite étendue à 128 000 dans la mise à jour Granite 3.1 de décembre 2024. Granite 3.0 est disponible via Hugging Face, Ollama et la plateforme watsonx d'IBM. Il sert de base aux modèles Granite Guardian, Code et Vision.
