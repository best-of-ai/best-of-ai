---
title: 'Dolly 2.0'
name: 'Dolly 2.0'
slug: 'dolly-2-0'
subtitle: 'Primeiro modelo da Databricks totalmente aberto e utilizável comercialmente para seguir instruções'
description: 'Primeiro modelo da Databricks totalmente aberto e utilizável comercialmente para seguir instruções'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm'
price: 'Free'
rank: 5
release_date: '2023-04-12'
param_count: '12B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: '24b60e23db79'
---

O Dolly 2.0 é um modelo de linguagem de 12 bilhões de parâmetros para seguir instruções, lançado pela Databricks em 12 de abril de 2023 com base no modelo Pythia da EleutherAI. O que o tornou notável não foi sua capacidade bruta — bem inferior ao GPT-3.5 na época —, mas sua licença: a Databricks publicou como código aberto os pesos, o código de treinamento e um novo conjunto de dados de instruções chamado databricks-dolly-15k, todos liberados para uso comercial. Os 15 mil exemplos foram escritos do zero por cerca de 5 mil funcionários da Databricks, especificamente para evitar restrições de licença de conjuntos de dados criados a partir de respostas da OpenAI, usadas por modelos abertos anteriores ajustados para instruções.

A Databricks apresentou o Dolly 2.0 como prova de que era possível criar e compartilhar um modelo útil de seguimento de instruções sem termos restritivos, numa época em que a maioria dos modelos abertos de capacidade comparável tinha licenças apenas para pesquisa. Já não compete com modelos modernos ajustados para instruções, mas foi um exemplo inicial e influente de alternativa totalmente aberta a chatbots comerciais fechados.