---
title: 'Codestral Mamba'
name: 'Codestral Mamba'
slug: 'codestral-mamba'
subtitle: "Modelo de código da Mistral baseado na arquitetura de espaço de estados Mamba, em vez de transformer"
description: "Modelo de código da Mistral baseado na arquitetura de espaço de estados Mamba, em vez de transformer"
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral-mamba/'
price: 'Free'
rank: 6
release_date: '2024-07-16'
param_count: '7B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.25
output_price_usd_per_m: 0.25
api_available: true
humaneval_score: 75.0
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, api]
i18n_source: '071ce3f5be62'
---

O Codestral Mamba é um modelo de geração de código lançado pela Mistral AI em julho de 2024, notável sobretudo pela arquitetura: em vez do transformer usado por quase todos os outros modelos de código, ele se baseia no Mamba, uma arquitetura de modelo de espaço de estados. Modelos de espaço de estados processam sequências com escala linear, não quadrática, em relação ao comprimento. Assim, a velocidade de inferência não diminui tão acentuadamente conforme o contexto cresce. A Mistral definiu o tamanho em cerca de 7 bilhões de parâmetros e deu ao modelo uma janela de contexto de 256 mil tokens, informando desempenho confiável de recuperação em contexto mesmo nesse comprimento.

No HumanEval, o Codestral Mamba alcança cerca de 75% em pass@1, resultado competitivo com modelos de código transformer muito maiores. É publicado sob a licença Apache 2.0, que permite baixar os pesos, ajustá-los e usá-los comercialmente sem custo. Também está disponível pela API da Mistral por US$ 0,25 por milhão de tokens, tanto de entrada quanto de saída. A Mistral o apresentou como prova de conceito de que arquiteturas de espaço de estados podem igualar transformers em tarefas reais de programação e oferecer inferência mais rápida e barata em usos com contexto longo, como raciocínio sobre grandes repositórios.
