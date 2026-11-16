---
title: 'BGE-large-en'
name: 'BGE-large-en'
slug: 'bge-large-en'
subtitle: 'Weit verbreitetes allgemeines Embedding-Modell der BAAI für englischsprachigen Information Retrieval'
description: 'Weit verbreitetes allgemeines Embedding-Modell der BAAI für englischsprachigen Information Retrieval'
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

BGE-large-en-v1.5 ist ein Texte-Embedding-Modell von BAAI (Beijing Academy of Artificial Intelligence), das im September 2023 als Aktualisierung des wenige Wochen zuvor veröffentlichten BGE-large-en erschien. Es hat 335 Millionen Parameter, erzeugt Embeddings mit 1.024 Dimensionen und verarbeitet Sequenzen bis zu 512 Tokens. Damit entspricht es eher der Größenklasse von BERT-Encodern als den späteren größeren, decoderbasierten Embedding-Modellen. Die Version 1.5 korrigierte vor allem ein Problem mit der Verteilung von Ähnlichkeitswerten der ursprünglichen Veröffentlichung und verbesserte die Retrieval-Qualität, wenn kein aufgabenspezifischer Instruktionspräfix verwendet wurde – eine Schwäche der ersten Version. BAAI veröffentlichte das Modell unter MIT-Lizenz. Es wurde eines der meistgenutzten offenen Embedding-Modelle für englischsprachiges Retrieval und RAG-Pipelines, vor allem weil es kostenlos, schnell ausführbar und gemessen an seiner Größe im MTEB-Benchmark leistungsfähig war. Inzwischen kamen größere und leistungsfähigere BAAI-Modelle wie BGE-M3 hinzu; BGE-large-en-v1.5 bleibt jedoch eine verbreitete Standardwahl für leichtgewichtiges, selbst gehostetes Retrieval.
