---
title: 'Gemini 2.5 Flash'
name: 'Gemini 2.5 Flash'
slug: 'gemini-2-5-flash'
subtitle: "Faixa Gemini de baixa latência e custo eficiente do Google"
description: "Faixa Gemini de baixa latência e custo eficiente do Google"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 7
release_date: '2025-04-17'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 84.0
humaneval_score: 82.0
lmarena_score: 1290
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, low-latency, multimodal, api]
i18n_source: 'd2ed515fd5c9'
---

O Gemini 2.5 Flash é a faixa econômica do Google na geração 2.5, lançada como prévia em abril de 2025 e disponibilizada em geral no mês seguinte. É o primeiro modelo Flash criado desde o início com pensamento visível integrado: ele pode raciocinar passo a passo sobre um problema antes de responder, e os desenvolvedores podem definir um “orçamento de pensamento” para equilibrar a qualidade da resposta com a latência e o custo. Ele recebe texto, imagem e áudio e tem a mesma janela de contexto de um milhão de tokens de seu irmão Pro.

O Google cobra US$ 0,30 por milhão de tokens de entrada e US$ 2,50 por milhão de tokens de saída, com os tokens de pensamento cobrados pela tarifa de saída, e oferece também a variante Flash-Lite, mais enxuta, para cargas de trabalho ainda mais baratas e simples. Ele obtém cerca de 83% no MMLU-Pro e apresenta bom desempenho em benchmarks de programação e matemática para seu preço, tornando-se a recomendação padrão do Google para aplicações de alto volume que não precisam da profundidade de raciocínio do Pro.
