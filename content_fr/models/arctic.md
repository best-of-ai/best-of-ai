---
title: 'Arctic'
name: 'Arctic'
slug: 'arctic'
subtitle: "Le modèle à poids ouverts de Snowflake, orienté entreprises, optimisé pour le SQL et le RAG"
description: "Le modèle à poids ouverts de Snowflake, orienté entreprises, optimisé pour le SQL et le RAG"
company: 'snowflake-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.snowflake.com/en/blog/arctic-open-efficient-foundation-language-models-snowflake/'
price: 'Free'
rank: 4
release_date: '2024-04-24'
param_count: '480B (17B active)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Snowflake Cortex']
date: '2026-07-16'
tags: [llm, open-weight, enterprise, self-hosted]
i18n_source: '083cf9082048'
---

Arctic est un grand modèle de langage que Snowflake a publié en avril 2024, conçu pour le travail en entreprise, comme la génération de SQL, la programmation et le suivi d'instructions, plutôt que pour le chat général. Il utilise un mélange d'experts : 480 milliards de paramètres au total, répartis sur 128 experts, mais seulement environ 17 milliards sont actifs pour un token donné, ce qui garde le coût d'inférence plus bas que celui de modèles denses d'échelle comparable. Snowflake a publié les checkpoints base et instruct sous licence Apache 2.0, donc les poids peuvent être auto-hébergés ou exécutés via Snowflake Cortex. Sur le benchmark text-to-SQL Spider, le score tournait autour de 79 % de précision, et Snowflake le présentait comme un moyen d'amener des modèles ouverts capables dans un entrepôt de données sans envoyer les requêtes à une API tierce. Il échange une fenêtre de contexte plus courte, de 4K, et un chat général plus faible, contre de bons résultats sur les tâches entreprise étroites pour lesquelles il a été construit.
