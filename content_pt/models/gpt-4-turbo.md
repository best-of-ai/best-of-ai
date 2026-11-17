---
title: 'GPT-4 Turbo'
name: 'GPT-4 Turbo'
slug: 'gpt-4-turbo'
subtitle: 'GPT-4 Turbo é a atualização do GPT-4 lançada pela OpenAI em novembro de 2023 e anunciada na primeira conferência da empresa para desenvolvedores.'
description: 'GPT-4 Turbo é a atualização do GPT-4 lançada pela OpenAI em novembro de 2023 e anunciada na primeira conferência da empresa para desenvolvedores.'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/new-models-and-developer-products-announced-at-devday/'
price: 'Paid'
rank: 6
release_date: '2023-11-06'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 10
output_price_usd_per_m: 30
api_available: true
mmlu_score: 86.5
humaneval_score: 87.1
lmarena_score: 1250
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['ChatGPT', 'Azure OpenAI', 'API']
date: '2026-07-16'
tags: [llm, foundation-model, api]
extra_model_types: ['Code']
i18n_source: 'dfca7bbe4eb9'
---

GPT-4 Turbo é a atualização do GPT-4 lançada pela OpenAI em novembro de 2023 e anunciada na primeira conferência da empresa para desenvolvedores. Manteve o nível de capacidade subjacente do GPT-4, mas ampliou a janela de contexto para 128.000 tokens, acrescentou uma data-limite de conhecimento em abril de 2023 e reduziu o preço para US$ 10 por milhão de tokens de entrada e US$ 30 por milhão de tokens de saída, bem abaixo das tarifas do GPT-4 original. Obteve 86,5% no MMLU e 87,1% no HumanEval, além de passar a aceitar imagens, permitindo que desenvolvedores enviassem imagens junto com texto na mesma solicitação.

A janela de contexto maior tinha uma ressalva prática: testes independentes constataram que a qualidade da atenção caía visivelmente após cerca de 32.000 tokens, então a janela completa de 128K funcionava melhor na teoria do que no uso intensivo com documentos longos. Ainda assim, o GPT-4 Turbo se tornou o modelo da classe GPT-4 padrão para desenvolvedores de API durante boa parte de 2024. Ficava disponível diretamente pela OpenAI, pelo Azure OpenAI e no ChatGPT, até que o GPT-4o o substituiu como opção recomendada mais tarde naquele ano.
