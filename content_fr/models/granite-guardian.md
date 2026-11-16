---
title: 'Granite Guardian'
name: 'Granite Guardian'
slug: 'granite-guardian'
subtitle: "Le modèle de sécurité d'IBM pour filtrer les entrées et sorties à risque d'un LLM"
description: "Le modèle de sécurité d'IBM pour filtrer les entrées et sorties à risque d'un LLM"
company: 'ibm'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2024-10-21'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [safety, open-weight, enterprise]
i18n_source: '6ce71d1a9d0a'
---

Granite Guardian est la famille de modèles de sécurité d'IBM. Elle se place à côté d'un LLM principal et signale les prompts ou les réponses à risque avant qu'ils n'atteignent un utilisateur ou une application. Elle est sortie avec Granite 3.0 en octobre 2024, en 2B et en 8B. Les deux tailles sont ajustées par fine-tuning à partir des modèles instruct Granite de base, pas entraînées depuis zéro. Elle vérifie les dommages listés dans l'AI Risk Atlas d'IBM : tentatives de jailbreak, vulgarité, biais sociaux, violence, et appels d'outils ou résultats de recherche hallucinés dans des flux de travail agentiques. IBM livre aussi une variante HAP (haine, abus, vulgarité) bien plus petite, de 38 millions de paramètres, pour les équipes qui ont besoin de garde-fous avec moins de latence ou un budget plus serré. Granite Guardian est à poids ouverts sous Apache 2.0, et distribué via Hugging Face, Ollama, NVIDIA et watsonx. Des mises à jour plus tardives, dont une 3.3 et une 4.1 qui accepte des critères de jugement définis par l'utilisateur, ont étendu la même approche aux modèles de base Granite plus récents.
