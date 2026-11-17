---
title: 'DeepSeek V4-Pro'
name: 'DeepSeek V4-Pro'
slug: 'deepseek-v4-pro'
subtitle: 'Principal modelo aberto de 2026, líder em programação agêntica e raciocínio de nível acadêmico avançado'
description: 'Principal modelo aberto de 2026, líder em programação agêntica e raciocínio de nível acadêmico avançado'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 9
release_date: '2026-04-24'
param_count: '1.6T (49B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 0.87
api_available: true
mmlu_score: 90.0
humaneval_score: 91.0
lmarena_score: 1390
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: '3dcf4ddbbacd'
---

O DeepSeek V4-Pro é o principal modelo da DeepSeek, lançado em 24 de abril de 2026 junto com o menor V4-Flash. É um modelo de mistura de especialistas com 1,6 trilhão de parâmetros totais e 49 bilhões ativos por token. Introduz um mecanismo híbrido de atenção que combina Compressed Sparse Attention e Heavily Compressed Attention, reduzindo bastante a computação de inferência e o tamanho do cache KV em comparação com o V3.2 e permitindo uma janela de contexto de 1 milhão de tokens. O modelo tem um modo “thinking”, para raciocínio passo a passo, e outro sem raciocínio explícito, para respostas rápidas. A DeepSeek afirma que lidera os modelos abertos em benchmarks de matemática, ciências e programação agêntica, com mais de 80% no SWE-bench Verified.

Como o restante da linha, o V4-Pro tem pesos abertos sob licença MIT e preços de API bem abaixo dos modelos fechados comparáveis da OpenAI, Anthropic e Google. É apresentado como a resposta da DeepSeek aos modelos de raciocínio de fronteira dos laboratórios ocidentais no início de 2026. Seu lançamento foi amplamente citado como evidência de que a diferença entre modelos abertos e fechados continua diminuindo.