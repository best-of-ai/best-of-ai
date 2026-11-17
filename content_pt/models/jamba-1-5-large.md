---
title: 'Jamba 1.5 Large'
name: 'Jamba 1.5 Large'
slug: 'jamba-1-5-large'
subtitle: "Modelo híbrido transformer-Mamba da AI21, criado para contextos muito longos"
description: "Modelo híbrido transformer-Mamba da AI21, criado para contextos muito longos"
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 5
release_date: '2024-08-22'
param_count: '398B (94B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 2
output_price_usd_per_m: 8
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: '53e8093cdb62'
---

O Jamba 1.5 Large é o modelo principal da família Jamba da AI21 Labs, lançado em 22 de agosto de 2024. Ele usa uma arquitetura híbrida que combina blocos de atenção Transformer com camadas de espaço de estados Mamba em uma configuração de mistura de especialistas, totalizando 398 bilhões de parâmetros, dos quais apenas 94 bilhões ficam ativos durante a inferência. Esse projeto permite processar uma janela de contexto de 256.000 tokens, uma das maiores oferecidas por qualquer modelo de licença aberta na época, mantendo o uso de memória e o custo de inferência abaixo do necessário para um Transformer denso de qualidade comparável. A AI21 definiu o preço em US$ 2 por milhão de tokens de entrada e US$ 8 por milhão de tokens de saída em sua própria API; o modelo também é distribuído pelo Hugging Face e AWS Bedrock sob a Jamba Open Model License da AI21. Ele se destina a cargas de trabalho empresariais como análise de documentos longos, sumarização e geração aumentada por recuperação, competindo nesse segmento com modelos como Mixtral 8x22B e Command R+.
