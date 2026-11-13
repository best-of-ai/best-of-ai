---
title: 'ALBERT'
name: 'ALBERT'
slug: 'albert'
subtitle: "La variante de BERT par Google, avec partage de paramètres, pensée pour l'efficacité à grande échelle"
description: "La variante de BERT par Google, avec partage de paramètres, pensée pour l'efficacité à grande échelle"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1909.11942'
price: 'Free'
rank: 6
release_date: '2019-09-26'
param_count: '223M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: '4c3c3afa8529'
---

ALBERT (A Lite BERT) est un modèle de représentation du langage que Google Research et le Toyota Technological Institute ont publié en septembre 2019, dans la suite de BERT. Deux astuces réduisent les paramètres, une paramétrisation factorisée des embeddings et le partage des paramètres d'une couche à l'autre, ce qui fait chuter fortement le nombre de paramètres tout en gardant une précision proche de modèles bien plus gros. La plus grande configuration, ALBERT-xxlarge, autour de 223 millions de paramètres, en a environ 18 fois moins que BERT-large, s'entraîne plus vite et a établi, à la sortie, de nouveaux meilleurs scores sur GLUE, SQuAD 2.0 et RACE.

Comme BERT, ALBERT est un modèle à encodeur seul, prévu pour des tâches de compréhension comme la classification, la réponse aux questions et la compréhension de texte, plutôt que pour la génération libre, et il limite l'entrée à 512 tokens par séquence. Google a publié le code et les poids préentraînés en accès ouvert, et le modèle est devenu une base courante pour la recherche en NLP et les systèmes en production au début des années 2020, avant que les modèles génératifs à décodeur seul ne prennent l'essentiel de l'attention dans le domaine.
