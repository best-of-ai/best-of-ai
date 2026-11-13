---
title: 'BitNet b1.58'
name: 'BitNet b1.58'
slug: 'bitnet-b1-58'
subtitle: "Le modèle de recherche de Microsoft qui tient des performances de LLM compétitives avec des poids ternaires à 1,58 bit"
description: "Le modèle de recherche de Microsoft qui tient des performances de LLM compétitives avec des poids ternaires à 1,58 bit"
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BitNet'
price: 'Free'
rank: 6
release_date: '2024-02-27'
param_count: '2B (2B4T release)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, research, efficiency]
i18n_source: '4d1b2822f6ff'
---

BitNet b1.58 est une ligne de recherche de Microsoft sur des modèles de langage à poids ternaires : chaque poids est limité à -1, 0 ou 1, au lieu des flottants habituels en 16 ou 32 bits. L'article d'origine, « The Era of 1-bit LLMs », est paru en février 2024. Il montrait que des modèles entraînés nativement ainsi, plutôt que quantifiés après coup, pouvaient égaler des modèles en pleine précision comme Llama 2 à des tailles comparables, tout en réduisant nettement la mémoire et l'énergie d'inférence. En avril 2025, Microsoft a enchaîné avec BitNet b1.58 2B4T, un checkpoint ouvert de 2 milliards de paramètres entraîné sur 4 billions de tokens. Hors embeddings, son empreinte mémoire tourne autour de 0,4 GB, bien en dessous de modèles de taille proche comme Gemma 3 1B ou MiniCPM 2B. Les poids et le code d'inférence sont sur GitHub et Hugging Face, sous licence MIT. Le projet compte moins pour dépasser d'autres modèles sur les benchmarks que pour montrer qu'un entraînement à 1 bit fonctionne, sans grosse perte de performance. C'est ce qui importe pour faire tourner des modèles capables sur un téléphone ou un appareil en périphérie.
