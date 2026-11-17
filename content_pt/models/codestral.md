---
title: 'Codestral'
name: 'Codestral'
slug: 'codestral'
subtitle: "Modelo de geração e conclusão de código da Mistral"
description: "Modelo de geração e conclusão de código da Mistral"
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral/'
price: 'Free'
rank: 6
release_date: '2024-05-29'
param_count: '22B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 0.9
api_available: true
humaneval_score: 81.1
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, code, open-weight, api]
i18n_source: '0c94b2ec4923'
---

O Codestral é o modelo dedicado à geração de código da Mistral AI, lançado inicialmente em maio de 2024 com 22 bilhões de parâmetros. Foi desenvolvido para preenchimento de lacunas e geração de código em várias linguagens. No lançamento, alcançou 81,1% em pass@1 no HumanEval, à frente de modelos maiores como Code Llama 70B e DeepSeek Coder 33B. A versão inicial tinha janela de contexto de 32 mil tokens e foi publicada sob a Mistral AI Non-Production License, que limitava o uso gratuito a pesquisa e testes e exigia uma licença comercial separada para implantação em produção.

Mais tarde, a Mistral ampliou a janela de contexto do Codestral para 256 mil tokens e, em abril de 2026, republicou o modelo sob Apache 2.0, removendo a restrição anterior ao uso comercial e permitindo sua utilização gratuita em IDEs, assistentes de programação e pipelines de CI. O Codestral está disponível como pesos para baixar no Hugging Face e pela API da Mistral, atualmente a US$ 0,30 por milhão de tokens de entrada e US$ 0,90 por milhão de saída. Concorre diretamente com outros modelos abertos de código de médio porte, como Codestral Mamba e Code Llama. A mudança para uma licença permissiva foi amplamente vista como uma alteração significativa no cenário de modelos de programação de código aberto.
