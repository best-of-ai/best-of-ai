---
title: 'Llama 3.1 405B'
name: 'Llama 3.1 405B'
slug: 'llama-3-1-405b'
subtitle: "Maior modelo denso de pesos abertos da Meta, competitivo com modelos de fronteira fechados"
description: "Maior modelo denso de pesos abertos da Meta, competitivo com modelos de fronteira fechados"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2024-07-23'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
mmlu_score: 88.6
humaneval_score: 89.0
lmarena_score: 1265
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, foundation-model]
extra_model_types: ['Code']
i18n_source: 'c720dd46ff12'
---

Llama 3.1 405B é o maior modelo da Meta na série Llama 3.1, lançado em 23 de julho de 2024 como Transformer denso de 405 bilhões de parâmetros, e não como arquitetura de mistura de especialistas. Aceita uma janela de contexto de 128.000 tokens e obteve 88,6 no MMLU e 89,0 no HumanEval, colocando-o na mesma faixa do GPT-4 em benchmarks de conhecimento e programação. Foi o primeiro modelo de pesos abertos a igualar de fato um modelo de fronteira fechado, em vez de ficar uma geração atrás; a Meta o lançou junto com versões menores de 70B e 8B, treinadas da mesma maneira, para que desenvolvedores pudessem escolher o equilíbrio entre qualidade e custo. Está disponível para hospedagem própria pelo Hugging Face e para inferência hospedada na Together AI, Fireworks, AWS Bedrock, Azure e Google Cloud, com provedores cobrando bem menos que por modelos fechados equivalentes, pois a Meta não cobra pelos pesos. O Llama 3.1 405B reforçou o argumento da Meta de que um modelo aberto podia estar na fronteira, em vez de ser apenas uma alternativa mais barata e fraca.
