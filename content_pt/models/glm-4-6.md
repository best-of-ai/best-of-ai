---
title: 'GLM-4.6'
name: 'GLM-4.6'
slug: 'glm-4-6'
subtitle: 'GLM-4.6 é o modelo aberto de categoria econômica da Zhipu (Z.ai), lançado em 30 de setembro de 2025 como atualização do GLM-4.5.'
description: 'GLM-4.6 é o modelo aberto de categoria econômica da Zhipu (Z.ai), lançado em 30 de setembro de 2025 como atualização do GLM-4.5.'
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2025-09-30'
param_count: '355B (MoE, ~32B active)'
context_window_tokens: 200000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 1.75
api_available: true
humaneval_score: 85.0
lmarena_score: 1320
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '89b99962ef6e'
---

GLM-4.6 é o modelo aberto de categoria econômica da Zhipu (Z.ai), lançado em 30 de setembro de 2025 como atualização do GLM-4.5. Ele usa uma arquitetura de mistura de especialistas com aproximadamente 355 bilhões de parâmetros no total e cerca de 32 bilhões ativos por token. Sua janela de contexto aumentou de 128.000 para 200.000 tokens para permitir sessões mais longas com agentes. O modelo processa texto, imagens e código, e a Zhipu o ajustou especificamente para uso de ferramentas em assistentes de programação como Claude Code, Cline e Roo Code.

Em benchmarks de programação, o modelo fica entre os melhores do grupo de pesos abertos, lidera o LiveCodeBench v6 e tem resultados competitivos com DeepSeek-V3.1-Terminus e Claude Sonnet 4 em várias tarefas com agentes. Seu principal atrativo é o preço: por bem menos de um dólar por milhão de tokens de entrada, custa muito menos que a maioria dos modelos proprietários principais e continua sendo útil para trabalho real de programação. Por isso, aparece com frequência em ferramentas de desenvolvimento auto-hospedadas e baseadas em API.
