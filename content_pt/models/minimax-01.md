---
title: MiniMax-01
name: MiniMax-01
slug: minimax-01
subtitle: Modelo de pesos abertos da MiniMax, lançado em 2025, com janela de contexto
  de 4 milhões de tokens
description: Modelo de pesos abertos da MiniMax, lançado em 2025, com janela de contexto
  de 4 milhões de tokens
company: minimax-ai
model_type: Language
logo_url: ''
product_url: https://www.minimaxi.com/
price: Free
rank: 6
release_date: '2025-01-15'
param_count: 456B (45.9B active)
context_window_tokens: 4000000
modality:
- text
open_weight: true
license: Apache 2.0
input_price_usd_per_m: 0.2
output_price_usd_per_m: 1.1
api_available: true
access_methods:
- API
- Self-hosted
runs_at_home: true
platforms:
- Hugging Face
- API
date: '2026-07-16'
tags:
- llm
- open-weight
- long-context
- mixture-of-experts
extra_model_types:
- Multimodal
i18n_source: '7af458104dd5'
---
MiniMax-01 é uma família de modelos de pesos abertos lançada em janeiro de 2025 pelo laboratório chinês de IA MiniMax. Ela combina um modelo de texto (MiniMax-Text-01) e um modelo de linguagem e visão (MiniMax-VL-01), ambos baseados na mesma arquitetura híbrida. A família usa uma arquitetura de mistura de especialistas com 456 bilhões de parâmetros totais e cerca de 45,9 bilhões ativos por token, combinando Lightning Attention com atenção softmax convencional para tornar sequências muito longas viáveis do ponto de vista computacional. Seu principal destaque é o tamanho do contexto: o modelo aceita entradas de até 4 milhões de tokens, muito acima do suportado pela maioria dos concorrentes na época; versões hospedadas via API geralmente oferecem uma janela de 1 milhão de tokens.

A MiniMax lançou os pesos sob a licença Apache 2.0 no Hugging Face e também oferece o modelo por sua API, a US$ 0,20 por milhão de tokens de entrada e US$ 1,10 por milhão de tokens de saída, abaixo dos preços da maioria dos modelos de ponta ocidentais. Entre os usos pretendidos estão a análise de documentos longos, fluxos de trabalho agênticos prolongados e raciocínio sobre bases de código, nos quais o limite está no tamanho do contexto, não no número bruto de parâmetros.
