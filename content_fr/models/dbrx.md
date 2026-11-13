---
title: 'DBRX'
name: 'DBRX'
slug: 'dbrx'
subtitle: "Modèle à mélange d'experts et à poids ouverts de Databricks"
description: "Modèle à mélange d'experts et à poids ouverts de Databricks"
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 5
release_date: '2024-03-27'
param_count: '132B (36B active)'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Databricks Open Model License'
api_available: true
mmlu_score: 73.7
humaneval_score: 70.1
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Databricks']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: 'c49f11ecc44d'
---

DBRX est le grand modèle de langage à poids ouverts de Databricks, sorti en mars 2024 comme modèle de base de DBRX Instruct, la version ajustée pour les instructions. C'est un mélange d'experts à grain fin, avec 132 milliards de paramètres au total et 36 milliards de paramètres actifs par token, entraîné depuis zéro sur 12 billions de tokens de texte et de code, avec la pile d'entraînement Mosaic AI de Databricks. À la sortie, Databricks indiquait qu'il dépassait d'autres modèles ouverts de l'époque, dont Llama 2 70B et Mixtral, sur des benchmarks comme MMLU et HumanEval. Il était présenté comme la preuve qu'une entreprise tournée vers les clients professionnels pouvait entraîner un modèle de fondation compétitif sans le budget de recherche d'un grand labo. La fenêtre de contexte est de 32 000 tokens. Il est publié sous la Databricks Open Model License, avec les poids sur Hugging Face pour l'auto-hébergement, ou via l'infrastructure de serving de Databricks.
