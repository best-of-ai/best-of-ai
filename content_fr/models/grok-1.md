---
title: 'Grok-1'
name: 'Grok-1'
slug: 'grok-1'
subtitle: "Premier modèle de xAI, ensuite publié à poids ouverts sous Apache 2.0"
description: "Premier modèle de xAI, ensuite publié à poids ouverts sous Apache 2.0"
company: 'xai'
model_type: 'Language'
logo_url: ''
product_url: 'https://x.ai/blog/grok-os'
price: 'Free'
rank: 5
release_date: '2023-11-04'
param_count: '314B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: '1027c6ce5f38'
---

Grok-1 est le premier grand modèle de langage de xAI, construit par le labo d'IA d'Elon Musk et d'abord proposé aux abonnés X Premium+ à partir de novembre 2023. C'est un modèle de mélange d'experts de 314 milliards de paramètres, avec 8 experts et un routage top-2 : environ un quart seulement des poids s'active pour un token donné. La fenêtre de contexte est de 8 192 tokens. Le 17 mars 2024, xAI a publié en open source les poids du modèle de base et l'architecture, sous licence Apache 2.0, ce qui faisait de Grok-1 le plus grand modèle MoE à poids ouverts disponible publiquement à l'époque. La sortie ne contenait que les poids préentraînés bruts, pas une version ajustée pour les instructions ni prête pour le chat. Le modèle a donc surtout été repris par des chercheurs et des équipes d'infrastructure, pas par les utilisateurs finaux. xAI l'a entraîné sur une pile maison en JAX et Rust, plutôt que sur PyTorch, et le préentraînement était terminé en octobre 2023, avant que Grok-2 ne le remplace plus tard en 2024.
