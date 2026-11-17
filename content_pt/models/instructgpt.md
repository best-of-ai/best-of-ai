---
title: 'InstructGPT'
name: 'InstructGPT'
slug: 'instructgpt'
subtitle: 'InstructGPT é a versão ajustada do GPT-3 da OpenAI, descrita no artigo “Training Language Models to Follow Instructions with Human Feedback”, de Ouyang e colaboradores.'
description: 'InstructGPT é a versão ajustada do GPT-3 da OpenAI, descrita no artigo “Training Language Models to Follow Instructions with Human Feedback”, de Ouyang e colaboradores.'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/instruction-following/'
price: 'Paid'
rank: 5
release_date: '2022-01-27'
param_count: '175B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [API]
runs_at_home: false
platforms: ['API']
date: '2026-07-16'
tags: [llm, foundation-model, legacy, rlhf]
i18n_source: 'e5b0714c6a82'
---

InstructGPT é a versão ajustada do GPT-3 da OpenAI, descrita no artigo “Training Language Models to Follow Instructions with Human Feedback”, de Ouyang e colaboradores. A OpenAI o anunciou em janeiro de 2022 e publicou o artigo completo no arXiv em março daquele ano. A equipe o desenvolveu em três etapas: reunir demonstrações de boas respostas escritas por avaliadores humanos e ajustar o GPT-3 com elas; coletar classificações humanas de várias respostas do modelo; e usar essas classificações para treinar um modelo de recompensa que orienta ajustes adicionais por aprendizado por reforço. A OpenAI treinou versões de 1,3B, 6B e 175B parâmetros, todas com a janela de contexto de 2.048 tokens do GPT-3.

O resultado mais citado do artigo é que avaliadores humanos preferiram as respostas do InstructGPT de 1,3B ao GPT-3 base de 175B, embora o modelo menor tivesse cem vezes menos parâmetros. Essa diferença mostrou que o ajuste com feedback humano importava mais que a escala bruta para produzir respostas que as pessoas realmente queriam e reduzia respostas tóxicas e falsas com pouco custo para a capacidade geral. A técnica desenvolvida pela OpenAI — aprendizado por reforço a partir de feedback humano — tornou-se o método padrão para transformar um modelo de linguagem bruto em um assistente utilizável e levou diretamente ao ChatGPT menos de um ano depois.
