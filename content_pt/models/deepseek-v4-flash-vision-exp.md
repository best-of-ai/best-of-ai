---
title: 'DeepSeek-V4-Flash-Vision-Exp'
name: 'DeepSeek-V4-Flash-Vision-Exp'
slug: 'deepseek-v4-flash-vision-exp'
subtitle: 'Variante multimodal experimental do V4-Flash da DeepSeek para compreender documentos e gráficos'
description: 'Variante multimodal experimental do V4-Flash da DeepSeek para compreender documentos e gráficos'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/news/news260821/'
price: 'Paid'
rank: 6
release_date: '2026-08-21'
param_count: '284B (MoE, 13B active)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.22
output_price_usd_per_m: 0.66
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-08-31'
tags: [multimodal, vision, api, document-understanding, mixture-of-experts]
i18n_source: '1264f839812e'
---

A DeepSeek lançou o DeepSeek-V4-Flash-Vision-Exp em 21 de agosto de 2026 como variante experimental com entrada de imagem do DeepSeek-V4-Flash, modelo esparso de mistura de especialistas com 284 bilhões de parâmetros totais e 13 bilhões ativos por token. Mantém o desempenho do V4-Flash somente de texto em tarefas agênticas e de raciocínio e acrescenta compreensão de imagens, voltada a leitura de documentos e gráficos, perguntas e respostas visuais e fluxos agênticos que combinam texto e imagens. As imagens podem ser enviadas como dados base64 em linha, URLs ou pela API Files da DeepSeek. O modelo converte cada imagem em 384 tokens, bem menos do que modelos GPT e Claude costumam usar por imagem.

Em benchmarks internos de agentes multimodais, a DeepSeek afirma que o V4-Flash-Vision-Exp reduziu boa parte da diferença em relação ao Opus-4.8 da Anthropic em tarefas que exigem raciocínio sobre entradas visuais, um avanço importante em relação ao V4-Flash somente de texto. Custa US$ 0,22 por milhão de tokens de entrada e US$ 0,66 por milhão de tokens de saída, com tarifa menor para entradas armazenadas em cache. Continua disponível apenas pela API da DeepSeek enquanto a empresa coleta comentários antes de um lançamento não experimental.