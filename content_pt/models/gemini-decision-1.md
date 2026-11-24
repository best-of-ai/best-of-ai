---
title: 'Gemini Decision 1'
name: 'Gemini Decision 1'
slug: 'gemini-decision-1'
subtitle: "Modelo não generativo do Google que pontua opções e devolve confiança em vez de texto"
description: "Modelo não generativo do Google que pontua opções e devolve confiança em vez de texto"
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/'
price: 'Paid'
rank: 6
release_date: '2026-11-11'
param_count: 'Undisclosed'
context_window_tokens: 256000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Gemini API', 'Google AI Studio']
date: '2026-11-24'
tags: [classification, decision-model, multimodal, api]
i18n_source: '1bbd28f7737a'
---

O Gemini Decision 1 é um modelo por trás da Decisions API do Google, lançada em 11 de novembro de 2026, que não escreve texto. Ele pontua opções em uma única passada e devolve uma probabilidade e uma confiança para cada uma. Lida com perguntas de sim ou não, múltipla escolha com 2 a 255 opções e pontuação ordenada por rubrica, com até 1.000 perguntas em uma única solicitação. As entradas podem ser texto, imagens, áudio, vídeo e PDFs, de até 256.000 tokens.

O Google cita latência de ponta a ponta de 150 a 250 milissegundos. O preço é de US$ 0,10 por milhão de tokens de entrada e nada pela saída, e o AI Studio tem um plano sem custo para prototipagem. O Google diz que ele é quase cinco vezes mais barato que o Gemini 3.5 Flash-Lite no mesmo conjunto de testes. O ID do modelo é gemini-decision-1, e as integrações estão sendo liberadas no OpenRouter, LangChain, Vercel e LiteLLM.
