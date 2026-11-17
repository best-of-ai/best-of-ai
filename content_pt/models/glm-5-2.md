---
title: 'GLM-5.2'
name: 'GLM-5.2'
slug: 'glm-5-2'
subtitle: 'GLM-5.2 é o modelo de pesos abertos principal da Zhipu AI, lançado em 13 de junho de 2026 sob a licença MIT.'
description: 'GLM-5.2 é o modelo de pesos abertos principal da Zhipu AI, lançado em 13 de junho de 2026 sob a licença MIT.'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-06-13'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 1.4
output_price_usd_per_m: 4.4
api_available: true
mmlu_score: 91.72
humaneval_score: 88.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
i18n_source: 'd5b4b307c39a'
---

GLM-5.2 é o modelo de pesos abertos principal da Zhipu AI, lançado em 13 de junho de 2026 sob a licença MIT. É um modelo de mistura de especialistas com aproximadamente 744 bilhões de parâmetros no total e cerca de 40 bilhões ativos por token. Sua janela de contexto é de 1 milhão de tokens, muito maior que a janela de 128.000 tokens do antecessor GLM-4.6. A Zhipu o criou especificamente para agentes de programação que executam tarefas de longo horizonte e passou meses treinando-o em cenários de engenharia de software com agentes, em vez de conversa geral.

Nos benchmarks, alcança 91,72% no MMLU, 80,3% no GPQA Diamond e 62,1% no SWE-bench Pro; este último resultado supera os 58,6% informados para GPT-5.5. A Zhipu cobra US$ 1,40 por milhão de tokens de entrada e US$ 4,40 por milhão de tokens de saída pelo acesso à API, uma fração do preço de modelos proprietários comparáveis. A empresa apresenta a combinação de pesos abertos e desempenho em programação como um desafio direto aos modelos de ponta fechados da OpenAI e da Anthropic.
