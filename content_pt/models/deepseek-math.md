---
title: 'DeepSeek-Math'
name: 'DeepSeek-Math'
slug: 'deepseek-math'
subtitle: 'Modelo de pesos abertos da DeepSeek especializado em raciocínio matemático'
description: 'Modelo de pesos abertos da DeepSeek especializado em raciocínio matemático'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 4
release_date: '2024-02-05'
param_count: '7B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, math, reasoning]
i18n_source: 'f4c27d033105'
---

O DeepSeekMath é um modelo de 7 bilhões de parâmetros desenvolvido especificamente pela DeepSeek para raciocínio matemático. Lançado em fevereiro de 2024, foi inicializado a partir do DeepSeek-Coder-Base. Foi treinado com 120 bilhões de tokens relacionados à matemática coletados na web, além de linguagem natural e código. No benchmark competitivo MATH, marcou 51,7% sem recorrer a calculadoras ou ferramentas externas, resultado que na época se aproximava de modelos fechados muito maiores, como Gemini-Ultra e GPT-4. A DeepSeek lançou versões base, ajustada para instruções e ajustada por aprendizado por reforço. A versão RL usou Group Relative Policy Optimization, algoritmo apresentado pela empresa nesse artigo e depois reutilizado no DeepSeek-R1. Com janela de contexto de 4.096 tokens, o modelo é voltado a pesquisa e desenvolvimento em tutoria de matemática, demonstração de teoremas e raciocínio quantitativo, não a conversas gerais.