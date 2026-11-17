---
title: 'Gemini Embedding'
name: 'Gemini Embedding'
slug: 'gemini-embedding'
subtitle: 'Gemini Embedding é o modelo de embeddings de texto do Google, desenvolvido a partir da família Gemini e disponibilizado de forma geral pela API Gemini a partir de março de 2025.'
description: 'Gemini Embedding é o modelo de embeddings de texto do Google, desenvolvido a partir da família Gemini e disponibilizado de forma geral pela API Gemini a partir de março de 2025.'
company: 'google-deepmind'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://ai.google.dev/gemini-api/docs/embeddings'
price: 'Freemium'
rank: 5
release_date: '2025-03-07'
param_count: 'Undisclosed'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Google Vertex AI']
date: '2026-07-16'
tags: [embedding, retrieval, api]
i18n_source: '8ad624583fe8'
---

Gemini Embedding é o modelo de embeddings de texto do Google, desenvolvido a partir da família Gemini e disponibilizado de forma geral pela API Gemini a partir de março de 2025. Ele converte texto em uma única representação vetorial que desenvolvedores usam para busca, agrupamento, classificação e geração aumentada por recuperação, substituindo os modelos de embeddings separados anteriores do Google por um modelo unificado, treinado com mais de 100 idiomas e também com código. Ele aceita Matryoshka Representation Learning, permitindo que o desenvolvedor reduza o embedding padrão para dimensões menores, como 768 ou 256, para economizar armazenamento sem retreinamento.

No lançamento, liderou por ampla margem o ranking multilíngue MTEB, superando o segundo melhor modelo. Desde então, o Google continuou ampliando a linha, incluindo uma versão mais recente que acrescenta suporte nativo a imagens, áudio e vídeo, além de texto, no mesmo espaço vetorial. O acesso é pela API Gemini e pelo Vertex AI, e o preço é calculado por token de entrada, como nos outros modelos Gemini do Google.
