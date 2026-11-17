---
title: 'Qwen4-Max'
name: 'Qwen4-Max'
slug: 'qwen4-max'
subtitle: "Modelo proprietário principal da Alibaba para sua API Qwen e plataforma de nuvem"
description: "Modelo proprietário principal da Alibaba para sua API Qwen e plataforma de nuvem"
company: 'alibaba'
model_type: 'Language'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Paid'
rank: 8
release_date: '2026-07-11'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.20
output_price_usd_per_m: 4.80
api_available: true
mmlu_score: 88.0
lmarena_score: 1352
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Alibaba Cloud', 'Qwen Chat', 'API']
date: '2026-07-19'
tags: [llm, proprietary, api, multimodal]
i18n_source: 'd9ca0c4f1096'
---

Qwen4-Max é o modelo proprietário de ponta da Alibaba, acima da família Qwen3 de pesos abertos que a empresa continua lançando no Hugging Face. Ao contrário deles, Qwen4-Max é fechado e acessível somente pela API da Alibaba Cloud, pelo Qwen Chat ou por plataformas parceiras, ao preço de US$ 1,20 por milhão de tokens de entrada e US$ 4,80 por milhão de tokens de saída. Aceita entrada de texto e imagem, tem uma janela de contexto de 1 milhão de tokens e a Alibaba o posiciona diretamente contra GPT-5.6 e Gemini 3.5 Pro em suas próprias comparações de benchmarks.

A divisão entre os modelos Qwen3 abertos e o Qwen4-Max fechado espelha um padrão adotado por outros laboratórios: oferecer pesos capazes de porte médio para conquistar desenvolvedores, reservando o maior modelo, mais caro de treinar, para uma API paga. A Alibaba tem usado essa abordagem para expandir o alcance do Qwen muito além da China, especialmente entre desenvolvedores no Hugging Face que ajustam os lançamentos abertos, mas recorrem à faixa Max em produção quando precisam de maior capacidade de raciocínio.
