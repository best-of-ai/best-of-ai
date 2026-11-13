---
title: 'Jamba Large 1.6'
name: 'Jamba Large 1.6'
slug: 'jamba-large-1-6'
subtitle: "Modèle phare hybride transformeur-Mamba d'AI21, mis à jour"
description: "Modèle phare hybride transformeur-Mamba d'AI21, mis à jour"
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 4
release_date: '2025-03-06'
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
i18n_source: '7f46269a09c0'
---

Jamba Large 1.6 est le modèle de langage phare d'AI21 Labs, construit sur une architecture hybride qui combine des couches d'attention de transformeur et des couches Mamba à espace d'états. AI21 l'a sorti en mars 2025 dans la famille Jamba 1.6, à côté d'un plus petit Jamba Mini 1.6. Le modèle a 398 milliards de paramètres au total, dont seulement 94 milliards actifs à l'inférence grâce à un mélange d'experts, ce qui limite le coût de calcul tout en prenant en charge une fenêtre de contexte de 256 000 tokens. AI21 le destine aux clients entreprises qui doivent traiter de longs documents, des contrats ou des bases de code sans envoyer les données à un tiers, puisque le modèle est disponible en déploiement auto-hébergé comme via une API. Dans les benchmarks d'AI21, Jamba Large 1.6 a dépassé des modèles ouverts de Meta, Mistral et Cohere sur un ensemble de tâches, et il tourne nettement plus vite que des transformeurs denses de taille proche, parce que les couches Mamba traitent les longues séquences de façon plus économe.
