---
title: Mistral Large 3
name: Mistral Large 3
slug: mistral-large-3
subtitle: Modelo de linguagem principal da Mistral, da categoria de ponta
description: Modelo de linguagem principal da Mistral, da categoria de ponta
company: mistral-ai
model_type: Language
logo_url: ''
product_url: https://mistral.ai/news/
price: Freemium
rank: 7
release_date: '2025-12-02'
param_count: 675B (41B active)
context_window_tokens: 256000
modality:
- text
- image
open_weight: true
license: Apache 2.0
input_price_usd_per_m: 0.5
output_price_usd_per_m: 1.5
api_available: true
access_methods:
- API
- Chat UI
- Self-hosted
runs_at_home: true
platforms:
- Le Chat
- Azure AI
- API
- Hugging Face
date: '2026-07-16'
tags:
- llm
- foundation-model
- api
- open-weight
i18n_source: 'b27612444904'
---
O Mistral Large 3 é o principal modelo de linguagem da Mistral AI, lançado em 2 de dezembro de 2025 como parte da linha Mistral 3. Ele usa uma arquitetura esparsa de mistura de especialistas, com 675 bilhões de parâmetros no total e apenas cerca de 41 bilhões ativos por token. Assim, exige aproximadamente o processamento de um modelo denso muito menor, embora aproveite um conjunto bem maior de pesos aprendidos. Recebe texto e imagens, aceita contexto de 256.000 tokens e foi lançado com pesos sob a licença Apache 2.0, uma mudança em relação à abordagem fechada do Mistral Large 2.

No lançamento, o modelo ficou entre os primeiros da categoria de pesos abertos no ranking LMArena. É voltado a desenvolvedores que buscam raciocínio, programação e desempenho multilíngue de ponta sem depender de uma API fechada. Está disponível no assistente Le Chat da Mistral, na API própria, no Azure AI e como pesos para download no Hugging Face, para auto-hospedagem ou fine-tuning. O preço da API ficou bem abaixo do cobrado pela Mistral para o Large 2.
