---
title: 'Claude 3.5 Haiku'
name: 'Claude 3.5 Haiku'
slug: 'claude-3-5-haiku'
subtitle: "Modelo rápido e acessível da Anthropic que iguala o Claude 3 Opus anterior em alguns benchmarks"
description: "Modelo rápido e acessível da Anthropic que iguala o Claude 3 Opus anterior em alguns benchmarks"
company: 'anthropic'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.anthropic.com/claude/haiku'
price: 'Paid'
rank: 6
release_date: '2024-11-04'
param_count: 'Undisclosed'
context_window_tokens: 200000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.8
output_price_usd_per_m: 4
api_available: true
humaneval_score: 88.1
lmarena_score: 1240
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'API']
date: '2026-07-16'
tags: [llm, low-latency, foundation-model, api]
extra_model_types: ['Code']
i18n_source: '43df5415f16a'
---

O Claude 3.5 Haiku é o modelo rápido e de baixo custo da família Claude 3.5 da Anthropic, lançado em outubro de 2024 junto com uma versão atualizada do Claude 3.5 Sonnet. A Anthropic o criou para substituir o Claude 3 Haiku como opção mais rápida e barata da linha, reduzindo ao mesmo tempo boa parte da diferença de capacidade em relação a modelos maiores. Em avaliações de programação como o SWE-bench Verified, o Claude 3.5 Haiku teve desempenho competitivo com o Claude 3.5 Sonnet original e superou vários modelos maiores disponíveis no lançamento. A Anthropic informou uma pontuação de 88,1% no HumanEval para geração de código.

O modelo mantém a janela de contexto de 200 mil tokens padrão da linha Claude 3.5. Seu preço é US$ 0,80 por milhão de tokens de entrada e US$ 4 por milhão de saída, o que o tornou um dos modelos próximos da fronteira mais baratos quando foi lançado. Ele se destina a usos de alto volume e sensíveis à latência, como atendimento ao cliente, moderação de conteúdo e extração de dados, nos quais velocidade e custo por chamada importam mais do que obter o máximo de qualidade em raciocínio. Está disponível pela API da Anthropic, no claude.ai e em plataformas de nuvem, incluindo AWS Bedrock.
