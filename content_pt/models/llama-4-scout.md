---
title: 'Llama 4 Scout'
name: 'Llama 4 Scout'
slug: 'llama-4-scout'
subtitle: "Faixa Llama 4 menor e mais rápida da Meta, com janela de contexto de 10M de tokens"
description: "Faixa Llama 4 menor e mais rápida da Meta, com janela de contexto de 10M de tokens"
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2025-04-05'
param_count: '109B (17B active)'
context_window_tokens: 10000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 80.5
lmarena_score: 1290
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, self-hosted]
i18n_source: 'a01f39772dca'
---

Llama 4 Scout é o irmão menor do lançamento Llama 4 da Meta em abril de 2025: um modelo de mistura de especialistas com 109 bilhões de parâmetros totais e 17 bilhões ativos por token, distribuídos por 16 especialistas. Seu destaque é o comprimento do contexto: Scout aceita até 10 milhões de tokens, muito além do oferecido por outros modelos abertamente disponíveis no lançamento, o que o torna adequado a tarefas como resumir uma base de código inteira ou uma coleção longa de documentos em uma única passagem. Assim como Maverick, é multimodal nativamente e foi treinado para processar texto e imagens juntos. A Meta posicionou Scout como opção mais rápida e barata que ainda supera modelos como Gemma 3 e Gemini 2.0 Flash-Lite em benchmarks públicos; quantizado, funciona em uma única GPU H100, o que o tornou popular em implantações autogerenciadas.
