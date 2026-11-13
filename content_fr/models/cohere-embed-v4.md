---
title: 'Cohere Embed v4'
name: 'Cohere Embed v4'
slug: 'cohere-embed-v4'
subtitle: "Modèle d'embeddings multimodal le plus récent de Cohere, pour le texte, les images et les documents mixtes"
description: "Modèle d'embeddings multimodal le plus récent de Cohere, pour le texte, les images et les documents mixtes"
company: 'cohere'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://cohere.com/blog/embed-4'
price: 'Paid'
rank: 6
release_date: '2025-04-15'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.12
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Cohere API']
date: '2026-07-16'
tags: [embedding, multimodal, api]
i18n_source: 'edb96743b450'
---

Cohere Embed v4 est le modèle d'embeddings multimodal de Cohere, sorti en avril 2025 comme successeur d'Embed v3. Contrairement à son prédécesseur, il accepte du texte, des images et des documents mixtes dans un seul appel, et il produit une représentation vectorielle unifiée. Une capture de page PDF, une diapositive ou un tableau peuvent donc être indexés directement à côté du texte brut, sans conversion en texte au préalable. La fenêtre de contexte va jusqu'à 128 000 tokens, bien au-delà des modèles d'embeddings d'OpenAI et de Voyage, et les embeddings Matryoshka sont proposés en 256, 512, 1 024 ou 1 536 dimensions, pour arbitrer entre stockage et précision. Le tarif est de 0,12 $ par million de tokens de texte et de 0,47 $ par million de tokens d'image via l'API Cohere. Le modèle est aussi disponible sur Amazon Bedrock et Azure AI. Cohere le destine à la recherche documentaire en entreprise et aux systèmes RAG qui doivent traiter du contenu scanné ou mis en forme visuellement, pas seulement du texte brut.
