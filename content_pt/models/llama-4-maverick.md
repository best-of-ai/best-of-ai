---
title: 'Llama 4 Maverick'
name: 'Llama 4 Maverick'
slug: 'llama-4-maverick'
subtitle: "Modelo multimodal principal de mistura de especialistas e pesos abertos da Meta"
description: "Modelo multimodal principal de mistura de especialistas e pesos abertos da Meta"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 8
release_date: '2025-04-05'
param_count: '400B (17B active)'
context_window_tokens: 1000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 86.0
humaneval_score: 85.0
lmarena_score: 1330
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
i18n_source: '1e256fde4e77'
---

Llama 4 Maverick é o modelo principal da Meta no lançamento Llama 4 de abril de 2025, construído como modelo de mistura de especialistas com 400 bilhões de parâmetros totais, mas apenas 17 bilhões ativos por token, distribuídos por 128 especialistas. É multimodal nativamente, treinado para processar texto e imagens em conjunto em vez de acrescentar depois um codificador visual a um modelo de texto, e aceita uma janela de contexto de 1 milhão de tokens. A Meta informou que Maverick supera GPT-4o e Gemini 2.0 Flash em vários benchmarks públicos e iguala DeepSeek V3 em tarefas de raciocínio e programação usando menos da metade dos parâmetros ativos. É distribuído sob a Llama 4 Community License, com pesos no Hugging Face e por provedores de nuvem como AWS Bedrock e Together AI.
