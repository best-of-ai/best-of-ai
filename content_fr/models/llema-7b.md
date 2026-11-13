---
title: 'Llemma 7B'
name: 'Llemma 7B'
slug: 'llema-7b'
subtitle: "Modèle ouvert d'EleutherAI, préentraîné en continu sur des textes de maths et de sciences"
description: "Modèle ouvert d'EleutherAI, préentraîné en continu sur des textes de maths et de sciences"
company: 'eleuther-ai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://huggingface.co/EleutherAI/llemma_7b'
price: 'Free'
rank: 4
release_date: '2023-10-16'
param_count: '7B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Llama 2 Community License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [reasoning, math, open-weight]
i18n_source: 'c5b46b531dbb'
---

Llemma 7B est un modèle de langage centré sur les maths d'EleutherAI, sorti en octobre 2023 en poursuivant le préentraînement par-dessus Code Llama 7B, plutôt qu'en partant de zéro. EleutherAI l'a entraîné davantage sur Proof-Pile-2, un mélange de 200 milliards de tokens d'articles de maths, de preuves formelles et de texte web chargé en maths, donc il se spécialise dans le raisonnement mathématique en chaîne de pensée et peut appeler des outils comme Python ou des prouveurs de théorèmes formels pour résoudre des problèmes. Il existe en 7B et en 34B, et les deux figuraient parmi les modèles de maths ouvertement disponibles les plus solides au moment de la sortie. Comme il hérite de ses poids de base de Code Llama, il porte la Llama 2 Community License plutôt qu'une licence pleinement permissive, ce qui limite certains usages commerciaux par rapport à des licences comme Apache 2.0.
