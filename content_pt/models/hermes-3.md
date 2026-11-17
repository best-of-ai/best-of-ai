---
title: 'Hermes 3'
name: 'Hermes 3'
slug: 'hermes-3'
subtitle: 'Hermes 3 é um modelo de linguagem de pesos abertos criado pela Nous Research sobre o modelo-base Llama 3.1 405B da Meta.'
description: 'Hermes 3 é um modelo de linguagem de pesos abertos criado pela Nous Research sobre o modelo-base Llama 3.1 405B da Meta.'
company: 'nous-research'
model_type: 'Language'
logo_url: ''
product_url: 'https://nousresearch.com/hermes3/'
price: 'Free'
rank: 4
release_date: '2024-08-27'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fine-tune, self-hosted]
i18n_source: 'b20d0dae77b1'
---

Hermes 3 é um modelo de linguagem de pesos abertos criado pela Nous Research sobre o modelo-base Llama 3.1 405B da Meta. A Nous o lançou em agosto de 2024 como ajuste fino de todos os parâmetros, não como adaptador leve, com o objetivo de devolver mais controle ao usuário por meio de direcionamento com prompts de sistema, uso de ferramentas por agentes e longas cadeias de raciocínio. Está disponível em três tamanhos (8B, 70B e 405B), treinados principalmente com dados sintéticos selecionados pela Nous, e aceita saídas estruturadas e chamadas de função o bastante para funcionar como backend direto de agentes. Em benchmarks públicos, iguala ou supera o ajuste Instruct do próprio Llama 3.1 da Meta em tarefas como ARC, HellaSwag e IFEval, algo notável para um ajuste comunitário que compete com o lançamento oficial do fornecedor. Como os pesos são abertos sob a licença Llama 3.1, desenvolvedores podem hospedar o modelo completo 405B ou executá-lo por provedores de inferência terceirizados, em vez de depender de uma API proprietária.
