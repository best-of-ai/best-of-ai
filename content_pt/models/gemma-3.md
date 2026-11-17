---
title: 'Gemma 3'
name: 'Gemma 3'
slug: 'gemma-3'
subtitle: 'Gemma 3 é a terceira geração de modelos de pesos abertos do Google, criada com pesquisa e tecnologia do projeto Gemini 2.0.'
description: 'Gemma 3 é a terceira geração de modelos de pesos abertos do Google, criada com pesquisa e tecnologia do projeto Gemini 2.0.'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 7
release_date: '2025-03-12'
param_count: '27B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 78.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
i18n_source: '053632cde4ac'
---

Gemma 3 é a terceira geração de modelos de pesos abertos do Google, criada com pesquisa e tecnologia do projeto Gemini 2.0. Está disponível em quatro tamanhos — 1B, 4B, 12B e 27B parâmetros — cada um como checkpoint base e versão ajustada para seguir instruções. Os modelos 4B, 12B e 27B aceitam texto e imagens, enquanto o 1B aceita somente texto. Todos processam mais de 140 idiomas e oferecem bom suporte imediato a mais de 35 deles. Os modelos maiores têm contexto de até 128.000 tokens, um grande aumento em relação aos 8.192 tokens do Gemma 2.

O Google posiciona o Gemma 3 como pequeno o bastante para rodar em um único host de GPU ou TPU, mas ainda capaz de competir com modelos fechados muito maiores em benchmarks padrão. Segundo relatos, a variante 27B supera o Gemini 1.5 Pro em várias avaliações, e testes independentes a colocam bem à frente do Gemma 2 27B anterior. Como os pesos podem ser baixados sob a licença Gemma, desenvolvedores o usam para implantação local, ajuste fino e aplicações de borda em que não é possível enviar dados para uma API hospedada.
