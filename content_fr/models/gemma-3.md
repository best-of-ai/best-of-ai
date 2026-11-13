---
title: 'Gemma 3'
name: 'Gemma 3'
slug: 'gemma-3'
subtitle: "La famille de modèles à poids ouverts de Google, issue des recherches Gemini"
description: "La famille de modèles à poids ouverts de Google, issue des recherches Gemini"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 7
release_date: '2025-03-12'
param_count: '27B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 78.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
i18n_source: '053632cde4ac'
---

Gemma 3 est la troisième génération de modèles à poids ouverts de Google, construite avec les recherches et la technique du projet Gemini 2.0. Elle existe en quatre tailles, 1B, 4B, 12B et 27B de paramètres, chacune en checkpoint de base et en version ajustée par instructions. Les modèles 4B, 12B et 27B acceptent le texte et les images, le 1B est seulement texte, et toutes les tailles couvrent plus de 140 langues, avec un bon support dès le départ pour plus de 35 d'entre elles. La longueur de contexte monte à 128 000 tokens pour les plus gros modèles, un grand saut par rapport aux 8 192 tokens de Gemma 2.

Google présente Gemma 3 comme assez petit pour tourner sur un seul hôte GPU ou TPU, tout en restant compétitif face à des modèles fermés bien plus gros sur les benchmarks usuels. La variante 27B dépasserait Gemini 1.5 Pro sur plusieurs évaluations, et des tests indépendants la placent bien devant le Gemma 2 27B précédent. Comme les poids se téléchargent sous la licence Gemma, les développeurs s'en servent pour le déploiement local, le fine-tuning et les applications en périphérie, quand envoyer les données vers une API hébergée n'est pas une option.
