---
title: 'BitNet b1.58'
name: 'BitNet b1.58'
slug: 'bitnet-b1-58'
subtitle: "Modelo de pesquisa da Microsoft que demonstra desempenho competitivo de LLMs com pesos ternários de 1,58 bit"
description: "Modelo de pesquisa da Microsoft que demonstra desempenho competitivo de LLMs com pesos ternários de 1,58 bit"
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BitNet'
price: 'Free'
rank: 6
release_date: '2024-02-27'
param_count: '2B (2B4T release)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, research, efficiency]
i18n_source: '4d1b2822f6ff'
---

BitNet b1.58 é uma linha de pesquisa da Microsoft sobre modelos de linguagem com pesos ternários, ou seja, em que cada peso é limitado a -1, 0 ou 1, em vez dos valores usuais de ponto flutuante de 16 ou 32 bits. O artigo original, “A era dos LLMs de 1 bit”, foi publicado em fevereiro de 2024 e mostrou que modelos treinados nativamente dessa forma, em vez de quantizados depois do treinamento, podiam igualar modelos de precisão completa como Llama 2 em tamanhos comparáveis, reduzindo bastante o uso de memória e a energia de inferência. Em abril de 2025, a Microsoft lançou o BitNet b1.58 2B4T, um checkpoint aberto de 2 bilhões de parâmetros treinado com 4 trilhões de tokens. Sua memória não relacionada a embeddings ocupa cerca de 0,4 GB, muito menos que a de modelos de tamanho semelhante, como Gemma 3 1B ou MiniCPM 2B. Os pesos e o código de inferência estão no GitHub e no Hugging Face sob a licença MIT. O projeto se destaca menos por superar outros modelos em benchmarks e mais por provar que o treinamento de 1 bit funciona sem grande perda de desempenho, algo relevante para executar modelos capazes em celulares ou dispositivos de borda.
