---
title: 'Qwen3.8-Flash-Next'
name: 'Qwen3.8-Flash-Next'
slug: 'qwen3-8-flash-next'
subtitle: "Prévia de pesos abertos da arquitetura Qwen4 de próxima geração da Alibaba"
description: "Prévia de pesos abertos da arquitetura Qwen4 de próxima geração da Alibaba"
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-26'
param_count: '125B (6B active)'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-09-05'
tags: [llm, open-weight, multimodal, moe, apache-2.0, cost-efficient]
i18n_source: '6dac4a7632ca'
---

A Alibaba abriu o código do Qwen3.8-Flash-Next em 26 de agosto de 2026, oferecendo aos desenvolvedores uma prévia da arquitetura Qwen4 antes da família completa de modelos. É um modelo multimodal de mistura de especialistas com arquitetura-base de 125 bilhões de parâmetros, dos quais apenas 6 bilhões ficam ativos por token, além de uma tabela de embeddings n-gram de 51 bilhões de parâmetros e um módulo de predição de múltiplos tokens de 4 bilhões. O contexto nativo chega a 262.144 tokens e pode ser ampliado até um milhão. A Alibaba afirma que supera o antigo Qwen3.7-Plus, especialmente em tarefas de programação e escritório, custando cerca de um nono para treinar e um doze avos para executar. Um checkpoint padrão e outro FP8 foram lançados desde o início.
