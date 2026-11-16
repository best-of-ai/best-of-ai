---
title: 'Hermes 3'
name: 'Hermes 3'
slug: 'hermes-3'
subtitle: "Fine-tune à poids ouverts de Nous Research, axé sur le pilotage et le raisonnement"
description: "Fine-tune à poids ouverts de Nous Research, axé sur le pilotage et le raisonnement"
company: 'nous-research'
model_type: 'Language'
logo_url: ''
product_url: 'https://nousresearch.com/hermes3/'
price: 'Free'
rank: 4
release_date: '2024-08-27'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fine-tune, self-hosted]
i18n_source: 'b20d0dae77b1'
---

Hermes 3 est un modèle de langage à poids ouverts construit par Nous Research au-dessus de la base Llama 3.1 405B de Meta. Nous l'a sorti en août 2024 comme un fine-tune de l'ensemble des paramètres, pas comme un adaptateur léger, pour rendre plus de contrôle à l'utilisateur : pilotage par prompt système, usage agentique d'outils et longues chaînes de raisonnement. Il existe en trois tailles (8B, 70B et 405B), entraînées surtout sur des données synthétiques choisies par Nous, et il gère assez bien la sortie structurée et l'appel de fonctions pour servir de backend d'agent directement utilisable. Sur les benchmarks publics, il égale ou dépasse le réglage Llama 3.1 Instruct de Meta lui-même sur des tâches comme ARC, HellaSwag et IFEval. C'est notable, puisqu'il s'agit d'un fine-tune communautaire face à la sortie officielle du fournisseur. Comme les poids sont ouverts sous la licence Llama 3.1, on peut auto-héberger le modèle 405B complet ou le faire tourner via des fournisseurs d'inférence tiers, plutôt que via une API propriétaire.
