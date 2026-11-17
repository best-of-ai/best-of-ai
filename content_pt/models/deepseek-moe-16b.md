---
title: 'DeepSeek-MoE-16B'
name: 'DeepSeek-MoE-16B'
slug: 'deepseek-moe-16b'
subtitle: 'Modelo inicial de mistura de especialistas granular da DeepSeek, que influenciou suas arquiteturas MoE posteriores'
description: 'Modelo inicial de mistura de especialistas granular da DeepSeek, que influenciou suas arquiteturas MoE posteriores'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-MoE'
price: 'Free'
rank: 5
release_date: '2024-01-11'
param_count: '16.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'DeepSeek License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
i18n_source: '61ec60299e14'
---

Lançado em janeiro de 2024, o DeepSeek-MoE-16B foi uma das primeiras tentativas da DeepSeek de criar uma arquitetura granular de mistura de especialistas. Suas escolhas de design foram levadas aos modelos V2 e V3 posteriores da empresa. O modelo tem 16,4 bilhões de parâmetros totais, mas apenas cerca de 2,8 bilhões ativos por token. Isso é obtido por duas técnicas descritas no artigo: dividir os especialistas em unidades menores e mais especializadas e reservar um conjunto de especialistas compartilhados, sempre ativados, para captar conhecimento comum. Treinado do zero com 2 trilhões de tokens em inglês e chinês, alcançou desempenho comparável ao DeepSeek 7B denso e ao Llama 2 7B, usando cerca de 40% da computação necessária para inferência desses modelos. Tem janela de contexto de 4.096 tokens e foi lançado sob a licença aberta da DeepSeek para uso próprio, sobretudo como demonstração de pesquisa em especialização de especialistas, não como produto para produção.