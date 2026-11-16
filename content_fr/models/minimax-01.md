---
title: 'MiniMax-01'
name: 'MiniMax-01'
slug: 'minimax-01'
subtitle: "Modèle à poids ouverts de MiniMax en 2025, avec une fenêtre de contexte de 4 millions de tokens"
description: "Modèle à poids ouverts de MiniMax en 2025, avec une fenêtre de contexte de 4 millions de tokens"
company: 'minimax-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.minimaxi.com/'
price: 'Free'
rank: 6
release_date: '2025-01-15'
param_count: '456B (45.9B active)'
context_window_tokens: 4000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.2
output_price_usd_per_m: 1.1
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, long-context, mixture-of-experts]
extra_model_types: ['Multimodal']
i18n_source: '7af458104dd5'
---

MiniMax-01 est une famille de modèles à poids ouverts que le labo d'IA chinois MiniMax a sortie en janvier 2025, en combinant un modèle de texte (MiniMax-Text-01) et un modèle vision-langage (MiniMax-VL-01) construits sur la même architecture hybride. Il utilise un mélange d'experts de 456 milliards de paramètres au total et environ 45,9 milliards actifs par token, et il mélange Lightning Attention et l'attention softmax classique pour rendre les très longues séquences praticables en calcul. Le trait principal est la longueur de contexte : le modèle peut traiter des entrées jusqu'à 4 millions de tokens, bien au-delà de ce que la plupart des modèles concurrents prenaient en charge alors, tandis que les versions hébergées par API exposent en général une fenêtre d'un million de tokens.

MiniMax a publié les poids sous licence Apache 2.0 sur Hugging Face et propose aussi le modèle via sa propre API, à 0,20 $ par million de tokens d'entrée et 1,10 $ par million de tokens de sortie, en dessous de la plupart des tarifs des grands modèles occidentaux. Il vise des usages comme l'analyse de longs documents, des flux d'agents étendus et le raisonnement à l'échelle d'une base de code, là où la longueur de contexte est le facteur limitant plutôt que le nombre brut de paramètres.
