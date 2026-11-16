---
title: 'DBRX Instruct'
name: 'DBRX Instruct'
slug: 'dbrx-instruct'
subtitle: "Variante ajustée pour les instructions du modèle DBRX à poids ouverts de Databricks"
description: "Variante ajustée pour les instructions du modèle DBRX à poids ouverts de Databricks"
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 4
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
tags: [llm, open-weight, instruction-tuned, self-hosted]
extra_model_types: ['Code']
i18n_source: '2f1996df20fb'
---

DBRX Instruct est la version ajustée par fine-tuning, prête pour le chat, du modèle DBRX de Databricks, sortie en mars 2024 en même temps que le modèle de base. Il utilise un mélange d'experts à grain fin, avec 132 milliards de paramètres au total, dont seulement 36 milliards sont actifs pour un token donné. Il a été entraîné sur 12 billions de tokens de texte et de code. Databricks l'a réglé pour le suivi d'instructions et la conversation à plusieurs tours. Au lancement, l'entreprise indiquait qu'il dépassait GPT-3.5 au MMLU (73,7 % contre 70,0 %) et sur HumanEval (70,1 % contre 48,1 %). La fenêtre de contexte est de 32 000 tokens. Il est distribué sous la Databricks Open Model License, qui permet un usage commercial avec quelques restrictions pour les très grands déploiements. On le fait tourner sur la plateforme de Databricks, ou en auto-hébergeant les poids depuis Hugging Face.
