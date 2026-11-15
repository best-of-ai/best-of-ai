---
title: 'GTE-large'
name: 'GTE-large'
slug: 'gte-large'
subtitle: 'Alibabas allgemeines Text-Embedding-Modell für Retrieval und semantische Ähnlichkeit'
description: 'Alibabas allgemeines Text-Embedding-Modell für Retrieval und semantische Ähnlichkeit'
company: 'alibaba'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/thenlper/gte-large'
price: 'Free'
rank: 5
release_date: '2023-08-07'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud']
date: '2026-07-16'
tags: [embedding, open-weight, api]
i18n_source: '25ba91e27698'
---
GTE-large ist ein Text-Embedding-Modell der DAMO Academy von Alibaba. Es wurde Mitte 2023 auf Hugging Face als Teil der Familie General Text Embeddings (GTE) zusammen mit den kleineren Varianten GTE-base und GTE-small veröffentlicht. Der BERT-ähnliche Encoder mit 335 Millionen Parametern wurde mit mehrstufigem kontrastivem Lernen anhand einer breiten Mischung aus Web- und Fachdaten trainiert. Er erzeugt Vektoren mit 1024 Dimensionen aus Eingaben mit bis zu 512 Tokens. Das Modell ist für Retrieval, semantische Suche, Clustering und Reranking gedacht. Bei seiner Veröffentlichung erzielte es auf der MTEB-Bestenliste gute Ergebnisse im Vergleich zu offenen Embedding-Modellen ähnlicher Größe und konkurrierte direkt mit den Modellen der Reihen BGE und E5 anderer chinesischer Labore. GTE-large steht unter Apache 2.0 mit offenen Gewichten, läuft bei der Inferenz problemlos auf einer einzelnen GPU oder CPU und wird über Hugging Face und Alibaba Cloud verbreitet. Es ist eine häufige Standardwahl für Teams, die RAG-Pipelines ohne Abhängigkeit von einer API entwickeln möchten.
