---
title: 'Fuyu-8B'
name: 'Fuyu-8B'
slug: 'fuyu-8b'
subtitle: "Le modèle multimodal à poids ouverts d'Adept, conçu pour la perception des agents numériques"
description: "Le modèle multimodal à poids ouverts d'Adept, conçu pour la perception des agents numériques"
company: 'adept-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.adept.ai/blog/fuyu-8b'
price: 'Free'
rank: 3
release_date: '2023-10-17'
param_count: '8B'
context_window_tokens: 16000
modality: [text, image]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, multimodal, open-weight, agentic]
i18n_source: 'f65d9839efe1'
---

Fuyu-8B est un modèle multimodal publié par Adept AI en octobre 2023, conçu pour des agents numériques qui doivent voir des écrans et agir dessus, plutôt que pour servir de chatbot généraliste. Adept l'a construit autour d'une architecture simplifiée : les patchs d'image vont directement dans un transformer décodeur seul standard, sans encodeur d'image séparé, ce qui lui permet d'accepter les images à la résolution où elles arrivent, au lieu de tout redimensionner à une taille fixe. Ça compte pour le cas d'usage d'Adept, qui doit lire des éléments d'interface, des boutons et du texte à la résolution native pour répondre à des questions sur des captures d'écran, des graphiques et des schémas, et pour localiser des éléments précis à l'écran. Adept a publié le modèle de 8 milliards de paramètres sur Hugging Face sous licence CC-BY-NC, donc libre d'usage et de modification, mais pas à des fins commerciales, et le présente comme un aperçu public plus petit du modèle qui fait tourner son propre produit, plutôt qu'une offre entièrement à part. Il prend en charge une fenêtre de contexte de 16K tokens. Adept a depuis été racheté, une grande partie de l'équipe étant passée chez Amazon en 2024, ce qui laisse Fuyu-8B comme un instantané de cette direction de recherche tournée vers les agents.
