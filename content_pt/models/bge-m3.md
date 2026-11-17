---
title: 'BGE-M3'
name: 'BGE-M3'
slug: 'bge-m3'
subtitle: "Modelo multilíngue de embeddings de pesos abertos e múltiplas granularidades da BAAI"
description: "Modelo multilíngue de embeddings de pesos abertos e múltiplas granularidades da BAAI"
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

BGE-M3 é um modelo de embeddings de texto da BAAI, descrito em um artigo publicado em fevereiro de 2024. O nome se refere a três capacidades simultâneas: multilinguismo em mais de 100 idiomas, processamento em várias escalas de entradas de até 8.192 tokens e multifuncionalidade, pois produz vetores densos, pesos lexicais esparsos e vetores de tokens no estilo ColBERT em uma única passagem direta. Ele tem 568 milhões de parâmetros, um número modesto diante de grandes modelos de linguagem, mas foi treinado especificamente para recuperação de informação, não para geração. Essa combinação permitiu que alcançasse resultados de ponta na época nos benchmarks multilíngues MIRACL e interlinguístico MKQA, pois um único modelo podia substituir os sistemas separados de recuperação densa e esparsa antes necessários. A BAAI o publicou sob a licença MIT no Hugging Face, e ele é amplamente usado em fluxos de geração aumentada por recuperação que precisam pesquisar documentos em vários idiomas ou documentos mais longos que o limite de 512 tokens comum nos primeiros modelos de embeddings baseados em BERT.
