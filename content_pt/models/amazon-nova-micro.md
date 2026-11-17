---
title: 'Amazon Nova Micro'
name: 'Amazon Nova Micro'
slug: 'amazon-nova-micro'
subtitle: "Modelo Nova mais rápido e barato da Amazon para tarefas simples com texto"
description: "Modelo Nova mais rápido e barato da Amazon para tarefas simples com texto"
company: 'amazon'
model_type: 'Language'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 5
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.035
output_price_usd_per_m: 0.14
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, low-cost, api]
i18n_source: '8a91538f6295'
---

Amazon Nova Micro é o menor e mais barato modelo da linha Nova da Amazon, anunciado em dezembro de 2024 junto com o restante da família e disponibilizado pelo Amazon Bedrock. Ele processa apenas texto, tanto na entrada quanto na saída, tem uma janela de contexto de 128.000 tokens e custa US$ 0,035 por milhão de tokens de entrada e US$ 0,14 por milhão de tokens de saída. Assim, é a resposta da Amazon a modelos leves como GPT-4o mini e Gemini Flash-Lite. A Amazon o criou para cargas de trabalho de alto volume e sensíveis à latência, como classificação de texto, extração simples e lógica de roteamento em fluxos maiores de agentes.

Como não entende imagens nem vídeos, o Nova Micro funciona com mais rapidez e custa menos que seus modelos multimodais irmãos, Lite e Pro, mas não consegue processar conteúdo visual. Ele aceita ajuste fino e destilação de modelos no Bedrock, permitindo que clientes o treinem com as saídas de um modelo maior e aproximem sua qualidade à daquele modelo em tarefas específicas, por uma fração do custo.
