---
title: 'BGE-large-en'
name: 'BGE-large-en'
slug: 'bge-large-en'
subtitle: "Modelo geral de embeddings da BAAI amplamente usado para recuperação em inglês"
description: "Modelo geral de embeddings da BAAI amplamente usado para recuperação em inglês"
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

BGE-large-en-v1.5 é um modelo de embeddings de texto da BAAI, a Beijing Academy of Artificial Intelligence, lançado em setembro de 2023 como atualização do modelo BGE-large-en original, publicado algumas semanas antes. Ele tem 335 milhões de parâmetros, produz embeddings de 1.024 dimensões e processa sequências de até 512 tokens, colocando-o na mesma categoria de tamanho de outros modelos codificadores na escala do BERT, em vez dos modelos de embeddings maiores baseados em decodificadores que vieram depois. A atualização v1.5 corrigiu principalmente um problema na distribuição das pontuações de similaridade da versão original e melhorou a qualidade da recuperação de informação quando usada sem um prefixo de instrução específico para a tarefa, uma limitação da versão v1. A BAAI o publicou sob a licença MIT, e ele se tornou um dos modelos abertos de embeddings mais usados em recuperação de informação em inglês e fluxos RAG, em grande parte por ser gratuito, rápido de executar e ter bons resultados no benchmark MTEB em relação ao seu tamanho. Desde então, juntaram-se a ele modelos maiores e mais capazes da BAAI, como BGE-M3, mas continua sendo uma opção padrão comum para recuperação de informação leve e auto-hospedada.
