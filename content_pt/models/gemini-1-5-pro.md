---
title: 'Gemini 1.5 Pro'
name: 'Gemini 1.5 Pro'
slug: 'gemini-1-5-pro'
subtitle: "Modelo do Google de 2024 que introduziu a janela de contexto de 1 milhão de tokens"
description: "Modelo do Google de 2024 que introduziu a janela de contexto de 1 milhão de tokens"
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 6
release_date: '2024-02-15'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.25
output_price_usd_per_m: 5
api_available: true
mmlu_score: 85.9
humaneval_score: 71.9
lmarena_score: 1260
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, multimodal, long-context, api, legacy]
extra_model_types: ['Code']
i18n_source: 'eceffcd944e2'
---

O Gemini 1.5 Pro foi o modelo que introduziu janelas de contexto de um milhão de tokens em uma API convencional. Lançado pelo Google em fevereiro de 2024, chegou à disponibilidade geral em maio daquele ano. Ele lê texto, imagens, áudio e vídeo em um único prompt, e o Google demonstrou que podia manter em contexto uma hora inteira de vídeo ou centenas de páginas de documentos de uma só vez, muito além do que GPT-4 ou Claude ofereciam na época. Ele usa uma arquitetura de mistura de especialistas, que, segundo o Google, permitiu igualar ou superar o Gemini 1.0 Ultra, maior, na maioria dos benchmarks, com custo de execução menor.

O Google reduziu o preço do 1.5 Pro duas vezes em 2024, chegando a cerca de US$ 1,25 por milhão de tokens de entrada e US$ 5 por milhão de tokens de saída para prompts com menos de 128.000 tokens. Ele obteve cerca de 85,9 no MMLU e 71,9 no HumanEval, e tornou-se o modelo de produção padrão do Google durante a maior parte de 2024, por meio do app Gemini, Vertex AI e Gemini API. Em 2025, o Google o substituiu como carro-chefe pelo Gemini 2.5 Pro, embora o 1.5 Pro continue disponível pela API para integrações existentes.
