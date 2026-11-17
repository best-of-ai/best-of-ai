---
title: 'Cerebras-GPT'
name: 'Cerebras-GPT'
slug: 'cerebras-gpt'
subtitle: "Família de modelos totalmente abertos da Cerebras, treinados em seus chips em escala de wafer"
description: "Família de modelos totalmente abertos da Cerebras, treinados em seus chips em escala de wafer"
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models'
price: 'Free'
rank: 3
release_date: '2023-03-28'
param_count: '13B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fully-open, self-hosted]
i18n_source: 'ff8674011b4e'
---

O Cerebras-GPT é uma família de modelos de linguagem com tamanhos de 111 milhões a 13 bilhões de parâmetros, treinada pela Cerebras em seus próprios sistemas CS-2 em escala de wafer e lançada em março de 2023. O objetivo do projeto era menos superar benchmarks e mais promover abertura: a Cerebras publicou os pesos, o código de treinamento e um relatório técnico detalhado com hiperparâmetros e comportamento de escala de cada tamanho da família, seguindo receitas de treinamento otimizadas para computação, semelhantes às usadas no Chinchilla. Isso tornou o Cerebras-GPT uma das famílias de modelos abertos mais bem documentadas da época, útil a pesquisadores que buscavam uma referência limpa e reproduzível para estudar leis de escala.

Todos os checkpoints do Cerebras-GPT são publicados sob Apache 2.0 e hospedados no Hugging Face, gratuitos para uso comercial e em pesquisa. Os modelos usam uma arquitetura padrão no estilo GPT e uma janela de contexto de 2.048 tokens. Pelos padrões de 2023, sua capacidade bruta era modesta em comparação com modelos como LLaMA, pois a Cerebras priorizou um treinamento transparente e reproduzível, em vez de maximizar o desempenho em benchmarks. Hoje, a família é citada sobretudo em pesquisas sobre leis de escala e como exemplo de uma empresa de hardware de IA demonstrando seus próprios chips ao treinar e abrir uma linha completa de modelos.
