---
title: 'InternLM2'
name: 'InternLM2'
slug: 'internlm2'
subtitle: "Modelo de base de pesos abertos do Shanghai AI Lab, com forte capacidade de contexto longo e raciocínio"
description: "Modelo de base de pesos abertos do Shanghai AI Lab, com forte capacidade de contexto longo e raciocínio"
company: 'shanghai-ai-lab'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-01-17'
param_count: '20B'
context_window_tokens: 200000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.7
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, long-context]
i18n_source: 'e91b498370ff'
---

O InternLM2 é um modelo de linguagem de pesos abertos do Shanghai AI Laboratory, lançado em 17 de janeiro de 2024 nos tamanhos 7B e 20B, junto com variantes de chat correspondentes. Ambos os tamanhos aceitam uma janela de contexto de 200.000 tokens, obtida por um processo de treinamento que começa com sequências de 4 mil tokens e as amplia gradualmente para 32 mil e além; o modelo apresenta bom desempenho em testes de agulha no palheiro com documentos longos nesse comprimento. A variante de chat 20B obtém 67,7 no MMLU, superando vários modelos abertos de tamanho semelhante na época do lançamento. O InternLM2 foi treinado em um grande corpus multilíngue, com destaque para inglês e chinês, e foi apresentado como modelo de base de uso geral para raciocínio, programação e tarefas de contexto longo antes de o Shanghai AI Lab substituí-lo pelo InternLM2.5 no fim daquele ano. É lançado sob a licença Apache 2.0 e distribuído pelo Hugging Face e pelo repositório InternLM no GitHub.
