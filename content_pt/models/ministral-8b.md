---
title: Ministral 8B
name: Ministral 8B
slug: ministral-8b
subtitle: Modelo compacto da Mistral desenvolvido para execução em dispositivos e
  ambientes de borda
description: Modelo compacto da Mistral desenvolvido para execução em dispositivos
  e ambientes de borda
company: mistral-ai
model_type: Language
logo_url: ''
product_url: https://mistral.ai/news/ministraux/
price: Free
rank: 4
release_date: '2024-10-16'
param_count: 8B
context_window_tokens: 128000
modality:
- text
open_weight: true
license: Mistral Research License
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0.1
api_available: true
mmlu_score: 65.0
access_methods:
- Self-hosted
- API
runs_at_home: true
platforms:
- Hugging Face
- API
date: '2026-07-16'
tags:
- llm
- open-weight
- small-model
- on-device
i18n_source: '5f9757c587f7'
---
O Ministral 8B é um modelo de 8 bilhões de parâmetros lançado pela Mistral AI em outubro de 2024 como parte de “Les Ministraux”, uma dupla de modelos pequenos voltados à execução em dispositivos e ambientes de borda, junto com o menor Ministral 3B. Ele usa atenção de janela deslizante intercalada para oferecer contexto de 128.000 tokens apesar do tamanho reduzido. A Mistral o posicionou em comparação com modelos de porte semelhante, como Llama 3.1 8B e Gemma 2 9B, alegando melhores resultados em benchmarks de conhecimento, raciocínio e multilinguismo dentro dessa categoria.

A Mistral o lançou sob a Mistral Research License, que permite uso gratuito para pesquisa e testes, mas exige uma licença comercial para implantação em produção. Isso difere dos termos totalmente abertos da Apache 2.0 do Mistral 7B. O modelo é voltado a desenvolvedores de aplicativos para celulares, laptops e outros dispositivos com recursos limitados, como assistentes locais, tradução e agentes leves, nos quais executar um modelo de tamanho completo não é viável.
