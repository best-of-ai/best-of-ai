---
title: 'Gemini Embedding'
name: 'Gemini Embedding'
slug: 'gemini-embedding'
subtitle: "Le modèle d'embeddings de texte unifié de Google, construit à partir de Gemini"
description: "Le modèle d'embeddings de texte unifié de Google, construit à partir de Gemini"
company: 'google-deepmind'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://ai.google.dev/gemini-api/docs/embeddings'
price: 'Freemium'
rank: 5
release_date: '2025-03-07'
param_count: 'Undisclosed'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Google Vertex AI']
date: '2026-07-16'
tags: [embedding, retrieval, api]
i18n_source: '8ad624583fe8'
---

Gemini Embedding est le modèle d'embeddings de texte de Google, issu de la famille Gemini et passé en disponibilité générale via l'API Gemini à partir de mars 2025. Il convertit un texte en une seule représentation vectorielle, que les développeurs utilisent pour la recherche, le clustering, la classification et le RAG. Il remplace les anciens modèles d'embeddings séparés de Google par un seul modèle unifié, entraîné sur plus de 100 langues, plus du code. Il gère le Matryoshka Representation Learning : on peut donc tronquer l'embedding par défaut vers des tailles plus petites, comme 768 ou 256 dimensions, pour économiser le stockage, sans rien réentraîner.

À sa sortie, il a pris la tête du classement multilingue MTEB, avec une marge nette sur le modèle juste derrière. Google a depuis prolongé la gamme, dont une version plus récente qui ajoute le support natif des images, de l'audio et de la vidéo, à côté du texte, dans le même espace vectoriel. On y accède par l'API Gemini et Vertex AI, et il est tarifé au token d'entrée, comme les autres modèles Gemini de Google.
