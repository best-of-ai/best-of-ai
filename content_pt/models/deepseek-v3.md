---
title: 'DeepSeek V3'
name: 'DeepSeek V3'
slug: 'deepseek-v3'
subtitle: 'Modelo eficiente de mistura de especialistas da DeepSeek, treinado por uma fração do custo dos concorrentes'
description: 'Modelo eficiente de mistura de especialistas da DeepSeek, treinado por uma fração do custo dos concorrentes'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2024-12-26'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.27
output_price_usd_per_m: 1.1
api_available: true
mmlu_score: 88.5
humaneval_score: 82.6
lmarena_score: 1330
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: '3c9c049bbd9a'
---

O DeepSeek V3 é um modelo de mistura de especialistas com 671 bilhões de parâmetros totais e 37 bilhões ativos por token, lançado em 26 de dezembro de 2024. É um modelo base sem raciocínio, construído sobre as mesmas arquiteturas Multi-head Latent Attention e DeepSeekMoE do V2. A DeepSeek afirmou que o treinamento custou cerca de US$ 5,6 milhões em tempo de GPU, muito menos do que laboratórios ocidentais gastavam em modelos comparáveis. Obteve 88,5 no MMLU e 82,6 no HumanEval, ficando próximo do GPT-4o e do Claude 3.5 Sonnet em muitos benchmarks, apesar do baixo custo de treinamento.

O V3 é publicado com pesos abertos sob a licença MIT, e a DeepSeek ofereceu sua API por um preço muito inferior ao de modelos de fronteira concorrentes. Depois, serviu de modelo base para o aprendizado por reforço focado em raciocínio do R1. Sua eficiência de custos virou tema de debate na indústria sobre quanta computação é realmente necessária para alcançar desempenho de fronteira.