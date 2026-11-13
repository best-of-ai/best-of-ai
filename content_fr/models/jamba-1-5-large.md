---
title: 'Jamba 1.5 Large'
name: 'Jamba 1.5 Large'
slug: 'jamba-1-5-large'
subtitle: "Modèle hybride transformeur-Mamba d'AI21, fait pour un très long contexte"
description: "Modèle hybride transformeur-Mamba d'AI21, fait pour un très long contexte"
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 5
release_date: '2024-08-22'
param_count: '398B (94B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 2
output_price_usd_per_m: 8
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: '53e8093cdb62'
---

Jamba 1.5 Large est le modèle phare de la famille Jamba chez AI21 Labs, sorti le 22 août 2024. Il utilise une architecture hybride qui mélange des blocs d'attention Transformer et des couches Mamba à espace d'états, dans un mélange d'experts : 398 milliards de paramètres au total, dont seulement 94 milliards actifs à l'inférence. Ce choix lui permet une fenêtre de contexte de 256 000 tokens, parmi les plus longues offertes alors par un modèle sous licence ouverte, tout en gardant la mémoire et le coût d'inférence plus bas qu'un Transformer dense de qualité comparable. AI21 le tarifait à 2 $ par million de tokens d'entrée et 8 $ par million de tokens de sortie via sa propre API. Le modèle est aussi distribué sur Hugging Face et AWS Bedrock, sous la Jamba Open Model License d'AI21. Il vise des charges d'entreprise comme l'analyse de longs documents, le résumé et la génération augmentée par la recherche, face à des modèles comme Mixtral 8x22B et Command R+ sur ce segment.
