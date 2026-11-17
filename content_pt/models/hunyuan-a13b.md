---
title: 'Hunyuan-A13B'
name: 'Hunyuan-A13B'
slug: 'hunyuan-a13b'
subtitle: 'Hunyuan-A13B é um modelo de linguagem de mistura de especialistas com pesos abertos da Tencent, lançado em junho de 2025 com 80 bilhões de parâmetros no total, mas apenas 13 bilhões ativos por token, mantendo o custo de inferência próximo ao de um modelo denso muito menor.'
description: 'Hunyuan-A13B é um modelo de linguagem de mistura de especialistas com pesos abertos da Tencent, lançado em junho de 2025 com 80 bilhões de parâmetros no total, mas apenas 13 bilhões ativos por token, mantendo o custo de inferência próximo ao de um modelo denso muito menor.'
company: 'tencent'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 4
release_date: '2025-06-27'
param_count: '80B (13B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, mixture-of-experts]
i18n_source: '1fc3c97bd4e4'
---

Hunyuan-A13B é um modelo de linguagem de mistura de especialistas com pesos abertos da Tencent, lançado em junho de 2025 com 80 bilhões de parâmetros no total, mas apenas 13 bilhões ativos por token, mantendo o custo de inferência próximo ao de um modelo denso muito menor. Aceita nativamente uma janela de contexto de 256K, embora muitas configurações auto-hospedadas a limitem para caber na memória da GPU. O modelo oferece um projeto de modo duplo que permite alternar entre respostas rápidas e raciocínio passo a passo mais lento para problemas difíceis de matemática, ciência e programação. A Tencent publicou os pesos no Hugging Face sob sua própria licença Hunyuan, e o modelo também está disponível pela API da Tencent Cloud para equipes que não querem executá-lo por conta própria. Ele concorre com outros modelos abertos eficientes de raciocínio MoE, como lançamentos menores da DeepSeek e o Qwen do Alibaba, privilegiando a eficiência dos parâmetros ativos em vez da contagem bruta de parâmetros.
