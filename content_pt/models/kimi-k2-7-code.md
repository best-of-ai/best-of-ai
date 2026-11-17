---
title: 'Kimi K2.7 Code'
name: 'Kimi K2.7 Code'
slug: 'kimi-k2-7-code'
subtitle: "Modelo de programação com agentes e pesos abertos da Moonshot, ajustado para uso de ferramentas e tarefas prolongadas"
description: "Modelo de programação com agentes e pesos abertos da Moonshot, ajustado para uso de ferramentas e tarefas prolongadas"
company: 'moonshot-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-06-12'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.95
output_price_usd_per_m: 4.0
api_available: true
humaneval_score: 90.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: '7d2adc3dc4a7'
---

Kimi K2.7 Code é o modelo da Moonshot AI voltado à programação, lançado em junho de 2026 como uma versão especializada baseada no Kimi K2.6. Mantém a mesma arquitetura de mistura de especialistas com 1 trilhão de parâmetros, cerca de 32 bilhões ativos, e janela de contexto de 256.000 tokens, mas é ajustado especificamente para programação de longo horizonte e decomposição de tarefas por agentes. A Moonshot relata ganhos de cerca de 22% no Kimi Code Bench v2, 11% no Program Bench e 31,5% no MLS Bench Lite em relação ao K2.6, além de aproximadamente 30% menos tokens de raciocínio por tarefa, reduzindo o custo efetivo de executá-lo em um ciclo de agente. O modelo sempre funciona em modo de pensamento e não oferece alternativa sem pensamento; além de código, aceita entradas de texto, imagem e vídeo. Os pesos estão abertos no Hugging Face, e a API da Moonshot cobra bem menos que concorrentes fechados como Claude Opus e GPT-5.5, tanto pelos tokens de entrada quanto pelos de saída.
