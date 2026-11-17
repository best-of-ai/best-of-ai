---
title: 'DeepSeek V3.2'
name: 'DeepSeek V3.2'
slug: 'deepseek-v3-2'
subtitle: 'Atualização do V3.1 da DeepSeek, baseada em um novo mecanismo de atenção esparsa'
description: 'Atualização do V3.1 da DeepSeek, baseada em um novo mecanismo de atenção esparsa'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-12-01'
param_count: '685B (MoE)'
context_window_tokens: 163840
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.21
output_price_usd_per_m: 0.32
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'd6a4a3b7b4f4'
---

O DeepSeek V3.2 é uma atualização do V3.1, detalhada publicamente em 1º de dezembro de 2025 após uma prévia experimental em setembro. Introduz a DeepSeek Sparse Attention, um mecanismo de atenção esparsa granular que reduz o custo de treinamento e inferência sem perder qualidade em tarefas com contexto longo. A variante principal Speciale tem cerca de 685 bilhões de parâmetros em uma arquitetura de mistura de especialistas. A janela de contexto é de 163.840 tokens, com até 64 mil tokens de saída. A DeepSeek relata resultados equivalentes a medalhas de ouro nas provas da Olimpíada Internacional de Matemática e da Olimpíada Internacional de Informática de 2025. A API custa cerca de US$ 0,21 por milhão de tokens de entrada e US$ 0,32 por milhão de saída, cerca da metade do preço do V3.1-Terminus, especialmente na decodificação com contexto longo. Como o restante da linha DeepSeek, é publicado sob a licença MIT, com pesos no Hugging Face, e serviu de base para o V4-Pro na primavera seguinte.