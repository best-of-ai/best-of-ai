---
title: 'DeepSeek-Coder-33B'
name: 'DeepSeek-Coder-33B'
slug: 'deepseek-coder-33b'
subtitle: 'Modelo de programação principal anterior da DeepSeek, que precedeu o DeepSeek-Coder-V2'
description: 'Modelo de programação principal anterior da DeepSeek, que precedeu o DeepSeek-Coder-V2'
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-Coder'
price: 'Free'
rank: 6
release_date: '2023-11-02'
param_count: '33B'
context_window_tokens: 16384
modality: [text, code]
open_weight: true
license: 'DeepSeek License'
api_available: true
humaneval_score: 79.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-07-16'
tags: [code, open-weight, api, legacy]
i18n_source: 'e1d443d0e69c'
---

O DeepSeek-Coder-33B é um modelo de linguagem voltado a código que a DeepSeek lançou em novembro de 2023, antes de ficar conhecida por seus modelos posteriores de raciocínio. Foi treinado do zero com 2 trilhões de tokens, principalmente de código e linguagem natural, tem janela de contexto de 16 mil tokens e treinamento no nível de projetos, o que permite raciocinar sobre vários arquivos em vez de apenas trechos isolados. A versão ajustada para instruções marcou 79,3% de pass@1 no HumanEval no lançamento, superando a maioria dos modelos abertos de código da época e chegando perto do GPT-3.5 em benchmarks de programação. Oferece preenchimento fill-in-the-middle para editores de código e cobre muitas linguagens de programação. A DeepSeek o sucedeu pelo DeepSeek-Coder-V2, maior e baseado em mistura de especialistas, mas o modelo 33B continua disponível no Hugging Face para hospedagem própria.