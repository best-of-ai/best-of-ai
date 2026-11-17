---
title: 'Kimi K2.6'
name: 'Kimi K2.6'
slug: 'kimi-k2-6'
subtitle: "Modelo de pesos abertos da Moonshot criado para tarefas longas com agentes e uso de ferramentas"
description: "Modelo de pesos abertos da Moonshot criado para tarefas longas com agentes e uso de ferramentas"
company: 'moonshot-ai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-04-20'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.6
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 88.0
humaneval_score: 87.0
lmarena_score: 1355
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, agentic, reasoning, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'f4220c32edb6'
---

Kimi K2.6 é o modelo principal de pesos abertos da Moonshot AI, lançado em abril de 2026 como sucessor do Kimi K2 original. É um modelo de mistura de especialistas com 1 trilhão de parâmetros, ativando cerca de 32 bilhões por token, fornecido nativamente em INT4 para baratear a inferência e com janela de contexto de 262.144 tokens. O modelo foi criado para trabalhos longos com agentes: a Moonshot o projetou em torno da orquestração multiagente, sessões de programação que duram horas sem intervenção humana e entrada multimodal nativa, em vez de visão adicionada posteriormente. Avaliações independentes da Artificial Analysis o classificam como o modelo de pesos abertos mais forte disponível, a poucos pontos de sistemas fechados de fronteira da OpenAI e Anthropic em tarefas como SWE-Bench Pro e Humanity's Last Exam, cobrando uma fração do preço por token desses sistemas. A Moonshot lança os pesos sob uma licença MIT modificada, permitindo que qualquer pessoa baixe e hospede o modelo em vez de depender da API própria da Moonshot.
