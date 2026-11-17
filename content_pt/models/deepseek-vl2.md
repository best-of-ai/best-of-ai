---
title: 'DeepSeek-VL2'
name: 'DeepSeek-VL2'
slug: 'deepseek-vl2'
subtitle: 'Modelo de visão e linguagem de mistura de especialistas com pesos abertos da DeepSeek'
description: 'Modelo de visão e linguagem de mistura de especialistas com pesos abertos da DeepSeek'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-12-13'
param_count: '27B (4.5B active)'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'DeepSeek License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
i18n_source: 'f06b4bb46852'
---

O DeepSeek-VL2 é uma família de modelos de visão e linguagem lançada em 13 de dezembro de 2024, sucessora do DeepSeek-VL original. Tem três tamanhos — Tiny, Small e VL2 completo — com 3B, 16B e 27B de parâmetros totais e, respectivamente, 1B, 2,8B e 4,5B de parâmetros ativos. Usa as mesmas arquiteturas DeepSeekMoE e Multi-head Latent Attention dos modelos de linguagem da DeepSeek. Um método de divisão dinâmica em blocos permite processar imagens de alta resolução e diferentes proporções sem perder detalhes, o que ajuda na leitura de documentos densos, gráficos e capturas de tela.

A arquitetura de mistura de especialistas proporciona bom desempenho em perguntas e respostas visuais, OCR e localização visual, mantendo baixo o custo de inferência em relação ao total de parâmetros, pois apenas uma pequena parte dos especialistas é ativada para cada entrada. Os três tamanhos foram publicados com pesos abertos, tornando o DeepSeek-VL2 uma das famílias multimodais abertas mais capazes disponíveis na época.