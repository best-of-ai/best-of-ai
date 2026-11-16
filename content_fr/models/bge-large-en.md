---
title: 'BGE-large-en'
name: 'BGE-large-en'
slug: 'bge-large-en'
subtitle: "Le modèle d'embeddings général de BAAI, très utilisé pour la recherche en anglais"
description: "Le modèle d'embeddings général de BAAI, très utilisé pour la recherche en anglais"
company: 'baai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/BAAI/bge-large-en-v1.5'
price: 'Free'
rank: 6
release_date: '2023-09-15'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, api]
i18n_source: 'f70b29aa405b'
---

BGE-large-en-v1.5 est un modèle d'embeddings de texte de BAAI, la Beijing Academy of Artificial Intelligence, publié en septembre 2023 comme mise à jour du BGE-large-en d'origine, sorti quelques semaines plus tôt. Il compte 335 millions de paramètres, produit des embeddings de dimension 1 024 et traite des séquences jusqu'à 512 tokens. Il se place donc dans la même classe de taille que d'autres encodeurs à l'échelle de BERT, plutôt que parmi les modèles d'embeddings plus gros, à base de décodeur, venus ensuite. La mise à jour v1.5 a surtout corrigé un problème de distribution des scores de similarité de la version d'origine, et elle a amélioré la qualité de la recherche sans préfixe d'instruction propre à la tâche, un point rugueux de la v1. BAAI l'a publié sous licence MIT. Il est devenu l'un des modèles d'embeddings ouverts les plus utilisés pour la recherche en anglais et les pipelines RAG, surtout parce qu'il était gratuit, rapide à faire tourner, et bien placé sur le benchmark MTEB au regard de sa taille. Des modèles BAAI plus gros et plus capables, comme BGE-M3, sont arrivés depuis, mais il reste un choix courant pour une recherche auto-hébergée légère.
