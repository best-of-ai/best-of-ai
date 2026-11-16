---
title: 'Amazon Nova Micro'
name: 'Amazon Nova Micro'
slug: 'amazon-nova-micro'
subtitle: "Le palier Nova d'Amazon le plus rapide et le moins cher, pour les tâches de texte simples"
description: "Le palier Nova d'Amazon le plus rapide et le moins cher, pour les tâches de texte simples"
company: 'amazon'
model_type: 'Language'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 5
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.035
output_price_usd_per_m: 0.14
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, low-cost, api]
i18n_source: '8a91538f6295'
---

Amazon Nova Micro est le plus petit et le moins cher des modèles de la gamme Nova d'Amazon, annoncé en décembre 2024 avec le reste de la famille et disponible via Amazon Bedrock. Il ne traite que le texte, en entrée comme en sortie, avec une fenêtre de contexte de 128 000 tokens. Le tarif est de 0,035 $ par million de tokens en entrée et de 0,14 $ par million de tokens en sortie. C'est la réponse d'Amazon aux modèles légers du type GPT-4o mini et Gemini Flash-Lite. Amazon l'a conçu pour des charges à fort volume, sensibles à la latence, comme la classification de texte, l'extraction simple et la logique de routage dans des pipelines d'agents plus larges.

Comme il laisse de côté toute compréhension d'image ou de vidéo, Nova Micro tourne plus vite et moins cher que Lite et Pro, ses voisins multimodaux, au prix de ne pas pouvoir traiter une entrée visuelle. Le fine-tuning et la distillation de modèles sont pris en charge sur Bedrock : on peut l'entraîner sur les sorties d'un modèle plus gros pour se rapprocher de la qualité de ce modèle sur des tâches étroites, pour une fraction du coût.
