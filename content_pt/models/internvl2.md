---
title: 'InternVL2'
name: 'InternVL2'
slug: 'internvl2'
subtitle: "Família aberta de modelos visão-linguagem do Shanghai AI Lab, competitiva com modelos multimodais proprietários"
description: "Família aberta de modelos visão-linguagem do Shanghai AI Lab, competitiva com modelos multimodais proprietários"
company: 'shanghai-ai-lab'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/OpenGVLab/InternVL'
price: 'Free'
rank: 6
release_date: '2024-07-04'
param_count: '76B (flagship; family spans 1B-108B)'
context_window_tokens: 8192
modality: [text, image, video]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '75f0788941ee'
---

O InternVL2 é uma família de modelos abertos de visão e linguagem do OpenGVLab, do Shanghai AI Laboratory, lançada em 4 de julho de 2024, com tamanhos de 1B até uma configuração principal de 108B (76B InternViT + Llama 3 70B). Os modelos combinam o codificador visual InternViT com uma arquitetura de linguagem, e a maior configuração, InternVL2-Llama3-76B, obteve 62,0% no benchmark MMMU, igualando o GPT-4o na época e superando outros modelos multimodais abertos em tarefas de compreensão de documentos e gráficos, como DocVQA e ChartQA. Além de imagens estáticas, o InternVL2 processa vídeo por amostragem de quadros e raciocínio sobre eles, e aceita múltiplas imagens para tarefas com documentos e comparações. Foi lançado sob a licença MIT, com pesos no Hugging Face, e na época era uma das alternativas abertas mais fortes a sistemas fechados como GPT-4o e Gemini. O Shanghai AI Lab lançou depois o InternVL2.5, em dezembro de 2024, elevando o maior modelo para mais de 70% no MMMU.
