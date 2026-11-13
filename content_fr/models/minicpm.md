---
title: 'MiniCPM'
name: 'MiniCPM'
slug: 'minicpm'
subtitle: "Petit modèle économe d'OpenBMB, conçu pour bien tourner sur les téléphones et les appareils en périphérie"
description: "Petit modèle économe d'OpenBMB, conçu pour bien tourner sur les téléphones et les appareils en périphérie"
company: 'openbmb'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM'
price: 'Free'
rank: 5
release_date: '2024-02-01'
param_count: '2.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, on-device]
i18n_source: '0dcdb45ddc3c'
---

MiniCPM est un modèle de langage de 2,4 milliards de paramètres qu'OpenBMB a sorti en février 2024, construit pour bien tourner sur les téléphones et d'autres appareils en périphérie, là où un modèle complet de 7B ou 13B serait trop lourd. Malgré sa petite taille, OpenBMB indiquait qu'il se place près de Mistral 7B sur les benchmarks généraux, et devant des modèles plus grands comme Llama 2 13B et Falcon 40B sur plusieurs tâches, en particulier la compréhension du chinois, les maths et le code. Une variante séparée pour le long contexte, MiniCPM-2B-128k, étend la fenêtre de contexte à 128 000 tokens pour les usages chargés en documents.

Le modèle est à poids ouverts sous licence Apache 2.0 et distribué via Hugging Face, visé vers les développeurs qui construisent des applications hors ligne ou peu coûteuses et ont besoin d'un modèle capable qui tient dans des budgets mémoire et calcul serrés. Il est devenu la base des modèles multimodaux MiniCPM-V suivants d'OpenBMB, et il a aidé à fixer l'orientation du labo : une IA économe, sur l'appareil, comme alternative au fait de tout faire grossir.
