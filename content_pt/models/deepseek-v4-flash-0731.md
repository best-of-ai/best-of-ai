---
title: 'DeepSeek-V4-Flash-0731'
name: 'DeepSeek-V4-Flash-0731'
slug: 'deepseek-v4-flash-0731'
subtitle: 'Modelo MoE de 284B da DeepSeek, com licença MIT e retreinado para programação agêntica mais avançada'
description: 'Modelo MoE de 284B da DeepSeek, com licença MIT e retreinado para programação agêntica mais avançada'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2026-07-31'
param_count: '284B (13B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-08-09'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: '247907c6207f'
---

O DeepSeek-V4-Flash-0731 saiu da prévia e entrou em beta público como um checkpoint retreinado após o treinamento, anunciado no registro de alterações da API da empresa em 31 de julho de 2026. A arquitetura permanece igual à estreia do modelo em abril: mistura de especialistas com 284 bilhões de parâmetros, 13 bilhões ativos por token, um especialista compartilhado e 256 especialistas roteados, além de uma janela de contexto de 1 milhão de tokens. A mudança está no pipeline de pós-treinamento: a DeepSeek ajustou o modelo para programação, uso agêntico de ferramentas e raciocínio. A API agora oferece suporte nativo ao formato Responses e funciona com o Codex sem configuração adicional. O modelo continua sob licença MIT e sem restrições de acesso, permitindo hospedagem comercial própria. São necessários cerca de 110 GB de memória com quantização de 3 bits ou um nó 4x GB300 para precisão total. Os preços de API continuam baixos: US$ 0,14 por milhão de tokens de entrada e US$ 0,28 por milhão de saída.