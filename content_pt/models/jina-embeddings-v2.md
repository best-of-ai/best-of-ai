---
title: 'Jina Embeddings v2'
name: 'Jina Embeddings v2'
slug: 'jina-embeddings-v2'
subtitle: "Modelo de embeddings da Jina AI, notável pela janela de contexto de 8 mil tokens no lançamento"
description: "Modelo de embeddings da Jina AI, notável pela janela de contexto de 8 mil tokens no lançamento"
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

O Jina Embeddings v2 é um modelo de embeddings de texto da Jina AI, lançado em outubro de 2023. Veio em dois tamanhos principais: uma versão pequena de 33 milhões de parâmetros e uma versão base de 137 milhões, ambas construídas sobre uma arquitetura BERT modificada que usa codificação posicional ALiBi em vez de embeddings posicionais padrão. Essa escolha permitiu processar sequências de até 8.192 tokens, algo incomum para um modelo aberto de embeddings na época, e competir com o text-embedding-ada-002 proprietário da OpenAI na recuperação de documentos longos, apesar de ser muito menor. O modelo é lançado sob a licença Apache 2.0 e pode ser executado localmente ou acessado pela API da Jina. Desde então foi sucedido pelo jina-embeddings-v3, que acrescenta suporte multilíngue e adaptadores específicos por tarefa; ainda assim, o v2 continua sendo usado em tarefas de recuperação em inglês nas quais seu tamanho menor é uma vantagem.
