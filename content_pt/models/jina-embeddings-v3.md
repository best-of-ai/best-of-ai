---
title: 'jina-embeddings-v3'
name: 'jina-embeddings-v3'
slug: 'jina-embeddings-v3'
subtitle: "Modelo multilíngue de embeddings da Jina AI com pesos abertos"
description: "Modelo multilíngue de embeddings da Jina AI com pesos abertos"
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

O jina-embeddings-v3 é o modelo multilíngue de embeddings de texto da Jina AI, lançado em setembro de 2024. Tem 570 milhões de parâmetros e oferece suporte a 89 idiomas, com janela de contexto de 8.192 tokens usando embeddings posicionais rotativos. O modelo usa adaptadores LoRA específicos para diferentes usos, como recuperação de consultas e documentos, agrupamento, classificação e correspondência de texto, permitindo adaptar um único conjunto de pesos a tarefas distintas sem retreinamento completo. Também oferece aprendizado de representação Matryoshka, que permite reduzir o embedding de saída, dos 1.024 componentes padrão até apenas 32, mantendo a maior parte da qualidade de recuperação. No benchmark MTEB, a Jina AI informou que o v3 superou embeddings proprietários da OpenAI e Cohere em tarefas de inglês e venceu o multilingual-e5-large-instruct em tarefas multilíngues. É lançado sob a licença CC BY-NC 4.0, que permite uso gratuito em pesquisa e avaliação, mas exige uma licença comercial para uso em produção em escala.
