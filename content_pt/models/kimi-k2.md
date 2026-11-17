---
title: 'Kimi K2'
name: 'Kimi K2'
slug: 'kimi-k2'
subtitle: "Modelo-base original de pesos abertos da geração K2 da Moonshot"
description: "Modelo-base original de pesos abertos da geração K2 da Moonshot"
company: 'moonshot-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 7
release_date: '2025-07-11'
param_count: '1T (32B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.2
api_available: true
humaneval_score: 85.0
lmarena_score: 1340
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: '611eb2c97d06'
---

Kimi K2 é o modelo-base original da geração K2 da Moonshot AI, lançado em julho de 2025 como um dos maiores modelos de linguagem de pesos abertos disponíveis na época. Usa uma arquitetura de mistura de especialistas com cerca de 1 trilhão de parâmetros totais e 32 bilhões ativos por token, e aceita uma janela de contexto de 128.000 tokens. A Moonshot o desenvolveu para casos de uso com agentes, como chamadas de ferramentas e execução de tarefas em várias etapas, em vez de priorizar apenas o chat; em benchmarks de programação como a variante multilíngue HumanEval, MultiPL-E, ele chegou perto dos melhores modelos fechados disponíveis naquele verão. Os pesos são lançados sob uma licença MIT modificada, permitindo que empresas baixem, ajustem e hospedem o modelo em vez de usar a API da Moonshot. Ele serviu de base para lançamentos posteriores da Moonshot, incluindo K2.5, K2.6 e K2.7 Code.
