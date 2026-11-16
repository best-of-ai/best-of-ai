---
title: 'Cerebras-GPT'
name: 'Cerebras-GPT'
slug: 'cerebras-gpt'
subtitle: 'La famille de modèles entièrement ouverts de Cerebras, entraînée sur ses puces à l''échelle du wafer'
description: 'La famille de modèles entièrement ouverts de Cerebras, entraînée sur ses puces à l''échelle du wafer'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models'
price: 'Free'
rank: 3
release_date: '2023-03-28'
param_count: '13B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fully-open, self-hosted]
i18n_source: 'ff8674011b4e'
---

Cerebras-GPT est une famille de modèles de langage, de 111 millions à 13 milliards de paramètres, que Cerebras a entraînée sur ses propres systèmes CS-2 à l'échelle du wafer et publiée en mars 2023. Le but du projet était moins de battre des benchmarks que de miser sur l'ouverture : Cerebras a publié les poids, le code d'entraînement et un rapport technique détaillé, avec les hyperparamètres et le comportement d'échelle pour chaque taille de la famille, en suivant des recettes d'entraînement à l'optimum de calcul, proches de celles derrière Chinchilla. Cerebras-GPT est ainsi devenue l'une des familles de modèles ouverts les plus complètement documentées de son époque, utile aux chercheurs qui voulaient une base propre et reproductible pour étudier les lois d'échelle.

Tous les checkpoints Cerebras-GPT sont publiés sous Apache 2.0 et hébergés sur Hugging Face, libres pour un usage commercial ou de recherche. Les modèles utilisent une architecture de style GPT assez standard, avec une fenêtre de contexte de 2 048 tokens. Aux standards de 2023, leur capacité brute restait modeste à côté de modèles comme LLaMA, parce que Cerebras a privilégié un entraînement transparent et reproductible plutôt que de tirer le maximum des benchmarks. On cite surtout la famille aujourd'hui dans la recherche sur les lois d'échelle, et comme exemple d'une entreprise de hardware d'IA qui montre ses propres puces en entraînant une gamme complète, puis en la publiant en open source.
