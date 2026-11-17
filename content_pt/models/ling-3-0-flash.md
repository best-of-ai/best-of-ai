---
title: 'Ling-3.0-Flash'
name: 'Ling-3.0-Flash'
slug: 'ling-3-0-flash'
subtitle: "Modelo de raciocínio eficiente de pesos abertos da Ant Group, criado para agentes de IA em produção"
description: "Modelo de raciocínio eficiente de pesos abertos da Ant Group, criado para agentes de IA em produção"
company: 'ant-group'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.antgroup.com'
price: 'Free'
rank: 6
release_date: '2026-07-23'
param_count: '124B (5.1B active)'
context_window_tokens: 262144
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.075
output_price_usd_per_m: 0.22
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'OpenRouter']
date: '2026-08-09'
tags: [llm, open-weight, reasoning, agentic, mixture-of-experts, efficiency]
extra_model_types: ['Code']
i18n_source: '368f5f371b66'
---

Ling-3.0-Flash é o lançamento mais recente da linha Ling da Ant Group, focada em eficiência. Desenvolvido pelo laboratório InclusionAI e apresentado em 23 de julho de 2026, é um modelo de base de raciocínio híbrido para cargas de trabalho de agentes de IA em produção. É um modelo de mistura de especialistas com 124 bilhões de parâmetros, dos quais apenas cerca de 5,1 bilhões são ativados por token; oferece nativamente uma janela de contexto de 256.000 tokens, expansível até 1 milhão, e, segundo a Ant, iguala ou supera modelos com duas a três vezes mais parâmetros em benchmarks de raciocínio, seguimento de instruções e contexto longo. Um sistema hierárquico de cache em nível de cluster reduz de 60% a 80% o tempo até o primeiro token em conversas longas. A Ant definiu o preço da API própria em US$ 0,075 por milhão de tokens de entrada e US$ 0,22 por milhão de tokens de saída, entre as tarifas mais baixas medidas para um modelo com pontuação de 38 ou mais no Artificial Analysis Intelligence Index, e lançou os pesos no Hugging Face sob licença MIT.
