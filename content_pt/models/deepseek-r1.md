---
title: 'DeepSeek R1'
name: 'DeepSeek R1'
slug: 'deepseek-r1'
subtitle: 'Modelo de raciocínio da DeepSeek que igualou modelos de fronteira fechados em matemática e programação'
description: 'Modelo de raciocínio da DeepSeek que igualou modelos de fronteira fechados em matemática e programação'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-01-20'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.19
api_available: true
mmlu_score: 90.8
humaneval_score: 92.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, chain-of-thought]
i18n_source: 'fa3b02ee20e3'
---

O DeepSeek R1 é um modelo de raciocínio lançado pelo laboratório chinês DeepSeek em 20 de janeiro de 2025. Usa uma arquitetura de mistura de especialistas com 671 bilhões de parâmetros, dos quais 37 bilhões são ativados por token. Foi treinado parcialmente com aprendizado por reforço em larga escala, em vez de depender apenas de ajuste fino supervisionado, o que o levou a resolver problemas passo a passo antes de responder. No lançamento, igualou o o1 da OpenAI em benchmarks de matemática, programação e ciências, marcando 90,8 no MMLU e chegando perto do topo dos modelos da época em problemas no estilo AIME e Codeforces. Foi publicado com pesos abertos sob a licença MIT e preços de API muito inferiores aos do o1.

O lançamento causou repercussão além dos círculos habituais de pesquisa em IA: o aplicativo da DeepSeek chegou brevemente ao topo da App Store dos EUA, e a notícia de que um laboratório chinês relativamente pequeno treinou um modelo de raciocínio de fronteira por uma fração do custo usual abalou as ações de IA. O R1 está disponível pela API e interface de chat da DeepSeek. Seus pesos abertos também permitem hospedá-lo por conta própria; eles estão amplamente espelhados no Hugging Face e disponíveis em provedores de inferência terceirizados.