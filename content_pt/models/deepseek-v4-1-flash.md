---
title: 'DeepSeek-V4.1-Flash'
name: 'DeepSeek-V4.1-Flash'
slug: 'deepseek-v4-1-flash'
subtitle: 'Versão mais barata do V4-Flash, com visão e preços diferenciados nos horários de pico'
description: 'Versão mais barata do V4-Flash, com visão e preços diferenciados nos horários de pico'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/quick_start/pricing/'
price: 'Paid'
rank: 7
release_date: '2026-09-10'
param_count: '552B (MoE)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.15
output_price_usd_per_m: 0.60
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-09-18'
tags: [llm, multimodal, api, cost-efficient, moe]
i18n_source: '9bfa801c726b'
---

A DeepSeek lançou o V4.1-Flash em 10 de setembro de 2026. É um modelo de mistura de especialistas com 552 bilhões de parâmetros, suporte nativo a visão e janela de contexto de 1.048.576 tokens, com até 393.216 tokens de saída. Os preços variam conforme o horário de pico: fora do pico, custam US$ 0,003 por milhão de tokens de entrada em caso de acerto no cache, US$ 0,15 em caso de falha e US$ 0,60 por milhão de tokens de saída. Nos horários de pico, em manhãs de dias úteis no horário UTC, os preços dobram.

A tarifa diferenciada segue a estratégia habitual da DeepSeek: reduzir bastante os preços de API ocidentais em períodos de baixa demanda para atrair cargas em lote e que não exigem baixa latência, mantendo preços de pico suficientes para gerenciar a capacidade.