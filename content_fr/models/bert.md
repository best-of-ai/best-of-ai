---
title: 'BERT'
name: 'BERT'
slug: 'bert'
subtitle: "L'encodeur bidirectionnel de Google, en 2018, qui a réorienté la recherche en NLP"
description: "L'encodeur bidirectionnel de Google, en 2018, qui a réorienté la recherche en NLP"
company: 'google'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://github.com/google-research/bert'
price: 'Free'
rank: 6
release_date: '2018-10-11'
param_count: '340M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, nlp, legacy]
i18n_source: '9489893b9c63'
---

BERT (Bidirectional Encoder Representations from Transformers) est un modèle de langage que Google Research a publié en octobre 2018, et il a changé la façon dont le domaine abordait le préentraînement pour les tâches de NLP. Contrairement aux modèles plus anciens, qui lisaient le texte de gauche à droite, BERT s'entraîne sur la prédiction de mots masqués et la prédiction de la phrase suivante. Il peut ainsi construire des représentations qui s'appuient sur le contexte des deux sens à la fois. Google a publié deux tailles principales, BERT-base à 110 millions de paramètres et BERT-large à 340 millions, toutes deux limitées à 512 tokens, et a rendu les poids libres sous Apache 2.0, d'abord sur GitHub puis sur Hugging Face. Des versions de BERT ajustées par fine-tuning ont établi de nouveaux records sur onze benchmarks de NLP distincts au lancement, dont la réponse aux questions et l'inférence en langage naturel, et le modèle est vite devenu la base standard à ajuster pour la classification, la reconnaissance d'entités nommées et le classement en recherche. Des encodeurs plus récents, comme RoBERTa et DeBERTa, et les modèles d'embeddings venus ensuite l'ont en grande partie remplacé. Il reste pourtant l'un des articles les plus cités en NLP, et son architecture est sous une grande part des systèmes à encodeur qui ont suivi.
