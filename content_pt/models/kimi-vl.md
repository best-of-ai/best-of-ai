---
title: 'Kimi-VL'
name: 'Kimi-VL'
slug: 'kimi-vl'
subtitle: "Modelo visão-linguagem de pesos abertos da Moonshot"
description: "Modelo visão-linguagem de pesos abertos da Moonshot"
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 4
release_date: '2025-04-10'
param_count: '16B (2.8B active)'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
extra_model_types: ['Reasoning']
i18n_source: 'edae211c40fc'
---

Kimi-VL é o modelo visão-linguagem de pesos abertos da Moonshot AI, lançado em abril de 2025. Usa uma arquitetura de mistura de especialistas com 16 bilhões de parâmetros no total, mas apenas cerca de 2,8 bilhões ativos no decodificador de linguagem, o que mantém a inferência barata em relação à capacidade. O modelo combina esse decodificador com o MoonViT, um codificador visual de resolução nativa capaz de ler imagens de resolução extremamente alta sem reduzi-las primeiro, e processa uma janela de contexto de 128.000 tokens para documentos e vídeos longos. Kimi-VL se destina a tarefas no estilo de agentes, como navegar pela tela de um computador (tem bom desempenho no OSWorld), além de OCR, raciocínio matemático a partir de imagens e comparação de várias imagens. A Moonshot também lançou a variante Kimi-VL-Thinking, treinada com aprendizado por reforço em dados de cadeia de pensamento, que amplia o raciocínio do modelo-base para horizontes mais longos.
