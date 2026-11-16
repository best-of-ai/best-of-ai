---
title: 'BGE-M3'
name: 'BGE-M3'
slug: 'bge-m3'
subtitle: "Le modèle d'embeddings à poids ouverts de BAAI, multilingue et à plusieurs granularités"
description: "Le modèle d'embeddings à poids ouverts de BAAI, multilingue et à plusieurs granularités"
company: 'baai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/BAAI/bge-m3'
price: 'Free'
rank: 4
release_date: '2024-02-06'
param_count: '568M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, multilingual, retrieval]
i18n_source: 'dc0d8e73a2f9'
---

BGE-M3 est un modèle d'embeddings de texte de BAAI, décrit dans un article publié en février 2024. Le nom renvoie à trois choses qu'il fait en même temps : le multilinguisme, sur plus de 100 langues, la prise en charge de plusieurs granularités, avec des entrées jusqu'à 8 192 tokens, et plusieurs fonctions de sortie, puisqu'un seul passage avant produit des vecteurs denses, des poids lexicaux creux et des vecteurs de tokens de style ColBERT. Il compte 568 millions de paramètres, ce qui est modeste à côté des grands LLM, mais il est entraîné pour la recherche et non pour la génération. Cette combinaison lui a permis, à l'époque, de placer les meilleurs résultats sur le benchmark multilingue MIRACL et le benchmark translingue MKQA : un seul modèle pouvait remplacer ce qui demandait auparavant des systèmes de recherche dense et creuse séparés. BAAI l'a publié sous licence MIT sur Hugging Face. Il est très utilisé dans les pipelines RAG qui doivent chercher dans des documents en plusieurs langues, ou dans des documents plus longs que la limite de 512 tokens habituelle des modèles d'embeddings plus anciens, à base de BERT.
