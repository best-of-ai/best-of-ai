---
title: 'Claude Haiku 4.5'
name: 'Claude Haiku 4.5'
slug: 'claude-haiku-4-5'
subtitle: "Modelo mais rápido e barato da geração atual da Anthropic"
description: "Modelo mais rápido e barato da geração atual da Anthropic"
company: 'anthropic'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.anthropic.com/news/claude-haiku-4-5'
price: 'Paid'
rank: 7
release_date: '2025-10-15'
param_count: 'Undisclosed'
context_window_tokens: 200000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1
output_price_usd_per_m: 5
api_available: true
mmlu_score: 85.0
humaneval_score: 84.0
lmarena_score: 1310
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'API']
date: '2026-07-16'
tags: [llm, foundation-model, low-latency, api]
extra_model_types: ['Reasoning', 'Code']
i18n_source: '54e445dc32ed'
---

O Claude Haiku 4.5 é o modelo mais rápido e barato da geração atual da Anthropic, lançado em 15 de outubro de 2025. É o primeiro modelo Haiku a incluir pensamento estendido, uso do computador e compreensão de contexto, recursos antes disponíveis apenas nos modelos Sonnet e Opus maiores da Anthropic. No SWE-bench Verified, alcança cerca de 73,3%, poucos pontos abaixo dos 77,2% do Claude Sonnet 4.5, apesar de custar um terço: US$ 1 por milhão de tokens de entrada e US$ 5 por milhão de saída, contra US$ 3/US$ 15 do Sonnet. Isso o torna uma opção prática para executar muitos agentes em paralelo ou lidar com tarefas de alto volume em que Sonnet ou Opus seriam desnecessariamente caros. Ele lê texto e imagens e compartilha a janela de contexto de 200 mil tokens usada no restante da linha Claude atual.
