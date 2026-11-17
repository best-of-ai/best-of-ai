---
title: 'DeepSeek-V2'
name: 'DeepSeek-V2'
slug: 'deepseek-v2'
subtitle: 'Modelo de mistura de especialistas da DeepSeek de 2024 que reduziu os preços de API em relação aos concorrentes'
description: 'Modelo de mistura de especialistas da DeepSeek de 2024 que reduziu os preços de API em relação aos concorrentes'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-05-06'
param_count: '236B (21B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'DeepSeek License'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
mmlu_score: 78.5
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
i18n_source: '988dda9730f9'
---

O DeepSeek-V2 é um modelo de linguagem de mistura de especialistas lançado em maio de 2024, com 236 bilhões de parâmetros totais e 21 bilhões ativos por token. Sua principal contribuição técnica foi a Multi-head Latent Attention, um método para comprimir o cache de chave e valor. Isso reduziu bastante o uso de memória e permitiu processar muito mais tokens por segundo do que o modelo denso DeepSeek 67B anterior no mesmo hardware. Treinado com 8,1 trilhões de tokens e janela de contexto de 128 mil, teve resultados competitivos em benchmarks MMLU e de programação contra outros modelos abertos da época.

O que tornou o V2 notável não foi apenas a arquitetura, mas também o preço: a DeepSeek lançou sua API por uma fração do que cobravam os concorrentes chineses e ocidentais, iniciando uma rodada de cortes de preços que comentaristas chamaram de “guerra de preços”. As técnicas MLA e DeepSeekMoE introduzidas aqui foram usadas em todos os modelos DeepSeek posteriores, incluindo V3 e R1, fazendo do V2 a base arquitetônica dos lançamentos de fronteira da empresa.