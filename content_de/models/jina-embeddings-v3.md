---
title: 'jina-embeddings-v3'
name: 'jina-embeddings-v3'
slug: 'jina-embeddings-v3'
subtitle: 'Open-Weight-mehrsprachiges Embedding-Modell von Jina AI.'
description: 'Open-Weight-mehrsprachiges Embedding-Modell von Jina AI.'
company: 'jina-ai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://jina.ai/embeddings/'
price: 'Free'
rank: 4
release_date: '2024-09-18'
param_count: '570M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [embedding, open-weight, retrieval, multilingual]
i18n_source: '881f6947c894'
---

jina-embeddings-v3 ist Jina AIs mehrsprachiges Text-Embedding-Modell, veröffentlicht im September 2024. Es hat 570 Millionen Parameter, unterstützt 89 Sprachen und verarbeitet dank rotierender Positions-Embeddings bis zu 8.192 Tokens. Aufgabenspezifische LoRA-Adapter decken Anwendungsfälle wie Anfrage-Dokument-Retrieval, Clustering, Klassifizierung und Textabgleich ab. So lässt sich ein einziger Gewichtsbestand für unterschiedliche Aufgaben anpassen, ohne das Modell vollständig neu zu trainieren. Matryoshka Representation Learning ermöglicht außerdem, die standardmäßige Ausgabedimension von 1.024 auf bis zu 32 zu kürzen und dabei den Großteil der Retrieval-Qualität zu erhalten. Im MTEB-Benchmark übertraf v3 laut Jina AI bei englischen Aufgaben proprietäre Embeddings von OpenAI und Cohere sowie multilingual-e5-large-instruct bei mehrsprachigen Aufgaben. Es steht unter CC BY-NC 4.0: Forschung und Evaluierung sind kostenlos, kommerzieller Einsatz in großem Umfang erfordert jedoch eine Lizenz.
