---
title: 'GTE-large'
name: 'GTE-large'
slug: 'gte-large'
subtitle: 'GTE-large é um modelo de embeddings de texto da Alibaba DAMO Academy, publicado no Hugging Face em meados de 2023 como parte da família General Text Embeddings (GTE), junto com as variantes menores GTE-base e GTE-small.'
description: 'GTE-large é um modelo de embeddings de texto da Alibaba DAMO Academy, publicado no Hugging Face em meados de 2023 como parte da família General Text Embeddings (GTE), junto com as variantes menores GTE-base e GTE-small.'
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

GTE-large é um modelo de embeddings de texto da Alibaba DAMO Academy, publicado no Hugging Face em meados de 2023 como parte da família General Text Embeddings (GTE), junto com as variantes menores GTE-base e GTE-small. É um codificador no estilo BERT com 335 milhões de parâmetros, treinado com aprendizado contrastivo em várias etapas sobre uma ampla combinação de textos da web e de domínios específicos. Produz vetores de 1.024 dimensões para entradas de até 512 tokens. O modelo é destinado a recuperação de informação, busca semântica, agrupamento e reordenação de resultados. No lançamento, teve bom desempenho no ranking do benchmark MTEB em relação a outros modelos abertos de embeddings de tamanho semelhante e concorreu diretamente com modelos do tipo BGE e E5 de outros laboratórios chineses. GTE-large tem pesos abertos sob Apache 2.0, roda facilmente em uma única GPU ou CPU durante a inferência e é distribuído pelo Hugging Face e pela Alibaba Cloud. Tornou-se uma escolha padrão comum para equipes que criam fluxos RAG e querem um modelo de embeddings compacto sem depender de API.
