---
title: 'ELECTRA'
name: 'ELECTRA'
slug: 'electra'
subtitle: 'Abordagem de pré-treinamento do Google mais eficiente em amostras, baseada na detecção de tokens substituídos'
description: 'Abordagem de pré-treinamento do Google mais eficiente em amostras, baseada na detecção de tokens substituídos'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2003.10555'
price: 'Free'
rank: 6
release_date: '2020-03-23'
param_count: '335M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: 'f5cba0d29eb6'
---

O ELECTRA é um método de pré-treinamento de codificadores de texto apresentado por pesquisadores do Google e de Stanford em um artigo publicado para a ICLR 2020, junto com uma família de modelos pré-treinados. Em vez do objetivo de modelagem de linguagem mascarada do BERT, no qual o modelo prevê palavras ocultadas aleatoriamente, o ELECTRA treina um pequeno gerador para substituir alguns tokens por alternativas plausíveis e um discriminador para identificar quais foram trocados. O objetivo de “detecção de tokens substituídos” fornece sinal de aprendizado para cada token da sequência, e não apenas para os mascarados, tornando o pré-treinamento muito mais eficiente em amostras.

A maior versão publicada, ELECTRA-Large, tem 335 milhões de parâmetros e obteve pontuações GLUE competitivas com RoBERTa e XLNet, usando um quarto do custo computacional de pré-treinamento. Com o mesmo orçamento de computação, superou esses modelos. O Google publicou o código e os pesos sob a licença Apache 2.0. As versões menores ELECTRA-Small e ELECTRA-Base tornaram-se populares entre equipes que buscavam precisão no nível do BERT sem o custo de treinamento equivalente.