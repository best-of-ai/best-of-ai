---
title: 'Jamba 1.5 Mini'
name: 'Jamba 1.5 Mini'
slug: 'jamba-1-5-mini'
subtitle: "Modèle hybride compact transformeur-Mamba d'AI21"
description: "Modèle hybride compact transformeur-Mamba d'AI21"
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 4
release_date: '2024-08-22'
param_count: '52B (12B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 0.2
output_price_usd_per_m: 0.4
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: 'e0243c637f6d'
---

Jamba 1.5 Mini est le plus petit modèle de la famille Jamba 1.5 d'AI21 Labs, sorti en même temps que Jamba 1.5 Large le 22 août 2024. Il reprend la même architecture hybride Transformer-Mamba en mélange d'experts, ramenée à 52 milliards de paramètres au total dont 12 milliards actifs, et il garde la même fenêtre de contexte de 256 000 tokens que le grand modèle. Sur le benchmark Arena Hard, il a obtenu 46,1, devant des modèles de taille proche comme Claude 3 Haiku, Mixtral 8x22B et Command R+. AI21 l'a conçu pour des usages métier sensibles à la latence, comme les appels de fonctions, la sortie JSON structurée et la génération ancrée, et le tarife à 0,20 $ par million de tokens d'entrée et 0,40 $ par million de tokens de sortie via son API. Comme Jamba 1.5 Large, il est sous la Jamba Open Model License d'AI21, avec les poids sur Hugging Face et une disponibilité sur AWS Bedrock.
