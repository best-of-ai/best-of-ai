---
title: 'ByT5'
name: 'ByT5'
slug: 'byt5'
subtitle: "Variante do T5 sem tokens do Google que opera diretamente sobre bytes brutos"
description: "Variante do T5 sem tokens do Google que opera diretamente sobre bytes brutos"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2105.13626'
price: 'Free'
rank: 4
release_date: '2021-05-28'
param_count: '13B'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, research]
i18n_source: 'e8007dd611dd'
---

ByT5 é uma variante do modelo de texto para texto T5 do Google, publicada pelo Google Research em meados de 2021 e conhecida por eliminar completamente a tokenização e operar diretamente com bytes UTF-8 brutos. Modelos de linguagem padrão dividem o texto em tokens de subpalavras usando um vocabulário fixo criado por um tokenizador. Isso funciona bem para os idiomas e sistemas de escrita considerados na criação desse vocabulário, mas tende a lidar mal com palavras raras, erros de grafia e idiomas menos comuns. O ByT5 contorna esse problema tratando cada entrada como uma sequência de bytes e usando um vocabulário com apenas algumas centenas de valores possíveis, em vez de dezenas de milhares de tokens de subpalavras.

A desvantagem é que as sequências de bytes são muito mais longas que sequências de tokens para o mesmo texto, então o ByT5 precisa de codificadores mais profundos e de mais computação por entrada para igualar modelos baseados em tokens nos benchmarks padrão. O Google lançou uma família de tamanhos ByT5 até o ByT5-XXL, com cerca de 13 bilhões de parâmetros, e disponibilizou todos os checkpoints abertamente no Hugging Face sob a licença Apache 2.0. O modelo teve desempenho especialmente bom com textos ruidosos, transliteração e tarefas multilíngues com sistemas de escrita de poucos recursos, tornando-se uma referência útil em pesquisas sobre modelagem sem tokenização e em nível de caractere, embora a maioria dos modelos de produção continue usando tokens por sua eficiência.
