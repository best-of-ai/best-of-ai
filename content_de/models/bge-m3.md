---
title: 'BGE-M3'
name: 'BGE-M3'
slug: 'bge-m3'
subtitle: 'Mehrsprachiges Embedding-Modell von BAAI mit offenen Gewichten und mehreren Granularitätsstufen'
description: 'Mehrsprachiges Embedding-Modell von BAAI mit offenen Gewichten und mehreren Granularitätsstufen'
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
BGE-M3 ist ein Text-Embedding-Modell von BAAI, das in einer im Februar 2024 veröffentlichten Arbeit beschrieben wurde. Der Name verweist auf drei Eigenschaften: Mehrsprachigkeit mit über 100 Sprachen, mehrere Eingabegranularitäten bis zu 8192 Tokens und mehrere Funktionen. In einem einzigen Durchlauf erzeugt das Modell dichte Vektoren, sparsame lexikalische Gewichte und Tokenvektoren im ColBERT-Stil. Es hat 568 Millionen Parameter – wenig im Vergleich zu großen LLMs –, wurde jedoch gezielt für Retrieval statt für Generierung trainiert. Dadurch erzielte es damals Spitzenwerte beim mehrsprachigen MIRACL- und beim sprachübergreifenden MKQA-Benchmark. Ein einziges Modell konnte so separate dichte und sparsame Retrieval-Systeme ersetzen. BAAI veröffentlichte es unter MIT-Lizenz auf Hugging Face. Es kommt häufig in RAG-Pipelines zum Einsatz, die Dokumente in mehreren Sprachen oder längere Texte durchsuchen müssen, welche die bei früheren BERT-Embedding-Modellen übliche Grenze von 512 Tokens überschreiten.
