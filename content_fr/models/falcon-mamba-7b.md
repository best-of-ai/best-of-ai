---
title: 'Falcon Mamba 7B'
name: 'Falcon Mamba 7B'
slug: 'falcon-mamba-7b'
subtitle: "Le modèle à poids ouverts de TII, construit sur l'architecture Mamba à espace d'états"
description: "Le modèle à poids ouverts de TII, construit sur l'architecture Mamba à espace d'états"
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 3
release_date: '2024-08-12'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'TII Falcon Mamba 7B License 1.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, hybrid-architecture, self-hosted]
i18n_source: '117aa18c3953'
---

Falcon Mamba 7B, publié par le Technology Innovation Institute en août 2024, a été le premier modèle de langage ouvert 7B solide construit entièrement sur l'architecture Mamba à espace d'états, plutôt que sur l'attention des transformers. Comme il n'a pas de mécanisme d'attention, l'usage mémoire et la vitesse d'inférence restent constants quand les séquences générées s'allongent, contrairement aux transformers dont le calcul augmente avec la longueur du contexte. TII l'a entraîné par étapes, en poussant la prise en charge effective du contexte de 2 048 à 8 192 tokens. Dans les comparaisons de benchmarks, il égalait ou dépassait des modèles transformer de taille proche, dont Mistral 7B et Llama 3.1 8B de Meta, et faisait mieux que d'autres modèles non transformer comme RecurrentGemma 9B et RWKV-v6. TII distribue les poids sur Hugging Face sous sa propre licence Falcon Mamba, pour les chercheurs et les développeurs qui veulent une alternative aux architectures à attention, sur des charges de longues séquences.
