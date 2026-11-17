---
title: 'DeepSeek-R1-Distill-Qwen-32B'
name: 'DeepSeek-R1-Distill-Qwen-32B'
slug: 'deepseek-r1-distill-qwen-32b'
subtitle: 'Destilação das trilhas de raciocínio do DeepSeek-R1 em um modelo aberto menor baseado em Qwen'
description: 'Destilação das trilhas de raciocínio do DeepSeek-R1 em um modelo aberto menor baseado em Qwen'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-R1'
price: 'Free'
rank: 6
release_date: '2025-01-20'
param_count: '32B'
context_window_tokens: 131072
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: '3cf96c55115c'
---

O DeepSeek-R1-Distill-Qwen-32B é um modelo denso de 32 bilhões de parâmetros que a DeepSeek criou ajustando o Qwen2.5-32B com trilhas de raciocínio geradas pelo modelo DeepSeek-R1 completo. Em vez de treinar um modelo menor do zero, a DeepSeek destilou as respostas em cadeia de pensamento do R1 em vários modelos base; a versão Qwen 32B acabou sendo a mais forte do grupo. Superou o o1-mini da OpenAI em benchmarks de matemática, programação e ciências, apesar do tamanho relativamente modesto. Foi um dos primeiros modelos abertos pequenos o suficiente para rodar em uma única GPU de alto desempenho e ainda demonstrar capacidade real de raciocínio. Os pesos são publicados sob a licença MIT junto com o restante da família R1 e estão amplamente disponíveis no Hugging Face e por provedores de inferência como Together AI e Groq.

Ele atende a um caso específico: equipes que querem raciocínio passo a passo no estilo R1 sem pagar pelo modelo completo de 671B nem hospedá-lo. Como é um transformer denso padrão, e não um modelo de mistura de especialistas, também é mais simples de ajustar e implantar que os principais lançamentos da DeepSeek.