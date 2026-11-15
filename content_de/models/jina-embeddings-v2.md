---
title: 'Jina Embeddings v2'
name: 'Jina Embeddings v2'
slug: 'jina-embeddings-v2'
subtitle: 'Embedding-Modell von Jina AI, das bei seiner Veröffentlichung durch ein Kontextfenster von 8K Tokens auffiel'
description: 'Embedding-Modell von Jina AI, das bei seiner Veröffentlichung durch ein Kontextfenster von 8K Tokens auffiel'
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/news/jina-embeddings-2-the-best-solution-for-embedding-long-documents/'
price: 'Free'
rank: 5
release_date: '2023-10-30'
param_count: '137M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Jina API']
date: '2026-07-16'
tags: [embedding, open-weight, api, legacy]
i18n_source: '9b381be032d7'
---
Jina Embeddings v2 ist ein Text-Embedding-Modell von Jina AI und wurde im Oktober 2023 veröffentlicht. Es erschien in zwei Hauptgrößen: einer Small-Version mit 33 Millionen und einer Base-Version mit 137 Millionen Parametern. Beide basieren auf einer angepassten BERT-Architektur, die ALiBi-Positionskodierung statt standardmäßiger Positionsembeddings verwendet. Dadurch verarbeitet das Modell Sequenzen mit bis zu 8192 Tokens. Das war für ein offenes Embedding-Modell damals ungewöhnlich und ließ es bei der Suche in langen Dokumenten mit OpenAIs proprietärem text-embedding-ada-002 konkurrieren, obwohl es deutlich kleiner war. Das Modell steht unter Apache 2.0 und kann lokal betrieben oder über die API von Jina genutzt werden. Inzwischen wurde es von jina-embeddings-v3 abgelöst, das mehrsprachige Unterstützung und aufgabenspezifische Adapter ergänzt. Version 2 wird für englischsprachige Retrieval-Aufgaben weiterhin genutzt, wenn die kleinere Größe von Vorteil ist.
