---
title: 'DeepSeek LLM 67B'
name: 'DeepSeek LLM 67B'
slug: 'deepseek-llm-67b'
subtitle: 'Primeiro modelo de base denso da DeepSeek com pesos abertos'
description: 'Primeiro modelo de base denso da DeepSeek com pesos abertos'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 4
release_date: '2023-11-29'
param_count: '67B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
mmlu_score: 71.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
i18n_source: 'b8bff96ba077'
---

O DeepSeek LLM 67B é o primeiro modelo de base denso da DeepSeek, lançado em novembro de 2023, antes de a empresa migrar para as arquiteturas de mistura de especialistas usadas nas linhas V2 e V3. É um transformer denso de 67 bilhões de parâmetros, treinado com 2 trilhões de tokens de texto em inglês e chinês. Obteve cerca de 71,9 no MMLU, ficando próximo do Llama 2 70B em benchmarks de conhecimento geral e superando-o em várias tarefas em chinês. Sua janela de contexto de 4.096 tokens é curta para padrões posteriores, refletindo os limites dos treinamentos de 2023. Foi lançado nas versões base e chat sob uma licença DeepSeek permissiva, que permite uso comercial, e serviu de base para modelos posteriores da empresa, mais amplamente usados.