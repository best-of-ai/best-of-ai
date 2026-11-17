---
title: 'BTLM-3B'
name: 'BTLM-3B'
slug: 'btlm-3b'
subtitle: "Modelo compacto de pesos abertos da Cerebras, ajustado para superar o esperado por sua quantidade de parâmetros"
description: "Modelo compacto de pesos abertos da Cerebras, ajustado para superar o esperado por sua quantidade de parâmetros"
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/btlm-3b-8b-7b-parameter-performance-in-a-3-billion-parameter-model'
price: 'Free'
rank: 4
release_date: '2023-07-24'
param_count: '3B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model]
i18n_source: '2c4fad8daa2c'
---

BTLM-3B-8K é um modelo de linguagem de 3 bilhões de parâmetros criado pela Cerebras em parceria com a Opentensor Foundation e treinado nos sistemas CS-2 em escala de wafer da Cerebras. Anunciado no verão de 2023, foi projetado com um objetivo específico: igualar a qualidade de modelos de 7 bilhões de parâmetros e continuar pequeno o suficiente para rodar em celulares e dispositivos com pouca memória. A Cerebras informa que, após quantização, o BTLM-3B ocupa cerca de 3 GB de memória e roda em hardware como iPhone, Google Pixel e até Raspberry Pi, com desempenho semelhante ao de modelos 7B contemporâneos, como RedPajama-INCITE-7B, em benchmarks comuns.

O modelo foi treinado com 627 bilhões de tokens do conjunto de dados SlimPajama, menos do que vários modelos concorrentes de 3B usaram na época, e emprega embeddings posicionais ALiBi para oferecer uma janela de contexto nativa de 8.192 tokens, com extrapolação razoável além desse limite. A Cerebras publicou o BTLM-3B sob a licença Apache 2.0, permitindo uso comercial gratuito. Por um breve período, foi considerado o modelo aberto de 3B com melhor desempenho, antes de modelos pequenos mais recentes da Microsoft, do Google e de outras empresas o superarem.
