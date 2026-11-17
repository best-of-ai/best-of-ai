---
title: 'Arctic'
name: 'Arctic'
slug: 'arctic'
subtitle: "Modelo aberto da Snowflake voltado a empresas e otimizado para SQL e RAG"
description: "Modelo aberto da Snowflake voltado a empresas e otimizado para SQL e RAG"
company: 'snowflake-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.snowflake.com/en/blog/arctic-open-efficient-foundation-language-models-snowflake/'
price: 'Free'
rank: 4
release_date: '2024-04-24'
param_count: '480B (17B active)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Snowflake Cortex']
date: '2026-07-16'
tags: [llm, open-weight, enterprise, self-hosted]
i18n_source: '083cf9082048'
---

Arctic é um modelo de linguagem lançado pela Snowflake em abril de 2024, criado para tarefas empresariais como geração de SQL, programação e seguimento de instruções, em vez de conversa de uso geral. Ele usa uma arquitetura de mistura de especialistas com 480 bilhões de parâmetros no total distribuídos por 128 especialistas, mas apenas cerca de 17 bilhões ficam ativos para cada token, o que reduz os custos de inferência em relação a modelos densos de escala semelhante. A Snowflake lançou checkpoints base e instruct sob a licença Apache 2.0, permitindo hospedá-los por conta própria ou executá-los pelo Snowflake Cortex. No benchmark Spider de texto para SQL, obteve cerca de 79% de precisão, e a Snowflake o apresentou como uma forma de levar modelos abertos capazes para data warehouses sem enviar consultas a uma API de terceiros. Ele troca uma janela de contexto mais curta, de 4K, e menor capacidade de conversa geral por forte desempenho nas tarefas empresariais específicas para as quais foi criado.
