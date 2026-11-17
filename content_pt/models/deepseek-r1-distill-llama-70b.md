---
title: 'DeepSeek-R1-Distill-Llama-70B'
name: 'DeepSeek-R1-Distill-Llama-70B'
slug: 'deepseek-r1-distill-llama-70b'
subtitle: 'Destilação das trilhas de raciocínio do DeepSeek-R1 em Llama, a maior variante destilada'
description: 'Destilação das trilhas de raciocínio do DeepSeek-R1 em Llama, a maior variante destilada'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-R1'
price: 'Free'
rank: 6
release_date: '2025-01-20'
param_count: '70B'
context_window_tokens: 131072
modality: [text]
open_weight: true
license: 'Llama 3.3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: '875e7d1cacd9'
---

O DeepSeek-R1-Distill-Llama-70B é um modelo de raciocínio destilado, lançado pela DeepSeek junto com o DeepSeek-R1 em janeiro de 2025. Em vez de treinar um modelo de raciocínio do zero, a DeepSeek ajustou o Llama 3.3 70B Instruct da Meta com trilhas de raciocínio geradas pelo modelo R1 completo, transferindo boa parte de sua capacidade de resolução de problemas em cadeia de pensamento para uma arquitetura menor e mais barata de executar. É a maior das seis variantes destiladas publicadas pela DeepSeek, que abrangem modelos base Qwen e Llama de 1,5B a 70B parâmetros. No lançamento, marcou 70,0% de pass@1 no AIME 2024 e 94,5% no MATH-500, muito acima de modelos gerais como GPT-4o e Claude 3.5 Sonnet nos mesmos benchmarks matemáticos. Tem janela de contexto de 128 mil tokens, herdada do Llama 3.3, e é distribuído sob a licença comunitária do Llama 3.3, com pesos no Hugging Face e acesso a APIs hospedadas por provedores como Together AI.