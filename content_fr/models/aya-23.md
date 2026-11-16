---
title: 'Aya 23'
name: 'Aya 23'
slug: 'aya-23'
subtitle: "Le modèle multilingue à poids ouverts de Cohere For AI, sur 23 langues"
description: "Le modèle multilingue à poids ouverts de Cohere For AI, sur 23 langues"
company: 'cohere'
model_type: 'Language'
logo_url: ''
product_url: 'https://cohere.com/research/aya'
price: 'Free'
rank: 5
release_date: '2024-05-27'
param_count: '35B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual]
i18n_source: '7472f170a470'
---

Aya 23 est une famille de modèles de langage multilingues que Cohere For AI, le labo de recherche de Cohere, a publiée en mai 2024. Elle couvre 23 langues, dont l'arabe, le chinois, l'hindi, le japonais, le russe et l'espagnol, à côté de l'anglais. Deux tailles ont été livrées, 8B et 35B de paramètres, toutes deux construites sur l'architecture Command de Cohere et initialisées à partir d'un checkpoint préentraîné, avant un entraînement multilingue supplémentaire. La version 35B est celle suivie ici. Sa fenêtre de contexte est de 8 192 tokens, pour la recherche d'information et le suivi d'instructions dans des langues d'habitude mal servies par les modèles ouverts centrés sur l'anglais. Cohere a publié les poids sous licence CC-BY-NC 4.0, avec un avenant d'usage acceptable : c'est gratuit pour la recherche et un usage non commercial, mais un accord commercial séparé est nécessaire pour un déploiement en production. Le projet fait suite au premier Aya, centré sur les données et l'évaluation pour 101 langues, en resserrant le périmètre à un plus petit ensemble de langues en échange d'une meilleure qualité dans chacune.
