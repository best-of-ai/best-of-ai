---
title: 'DBRX'
name: 'DBRX'
slug: 'dbrx'
subtitle: 'Modelo de mistura de especialistas com pesos abertos da Databricks'
description: 'Modelo de mistura de especialistas com pesos abertos da Databricks'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 5
release_date: '2024-03-27'
param_count: '132B (36B active)'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Databricks Open Model License'
api_available: true
mmlu_score: 73.7
humaneval_score: 70.1
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Databricks']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: 'c49f11ecc44d'
---

O DBRX é o grande modelo de linguagem de pesos abertos da Databricks, lançado em março de 2024 como modelo base do DBRX Instruct, ajustado para instruções. É um modelo de mistura de especialistas granular com 132 bilhões de parâmetros totais e 36 bilhões ativos por token, treinado do zero com 12 trilhões de tokens de texto e código usando a própria pilha de treinamento Mosaic AI da Databricks. No lançamento, a Databricks afirmou que ele superava outros modelos abertos da época, incluindo Llama 2 70B e Mixtral, em benchmarks como MMLU e HumanEval. A empresa o apresentou como prova de que uma companhia focada em negócios podia treinar um modelo de base competitivo sem o orçamento de pesquisa de um grande laboratório. Tem janela de contexto de 32 mil tokens e é publicado sob a Databricks Open Model License, com pesos disponíveis no Hugging Face para hospedagem própria ou na infraestrutura de serviço da Databricks.