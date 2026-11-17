---
title: 'Falcon 40B'
name: 'Falcon 40B'
slug: 'falcon-40b'
subtitle: "Modelo aberto anterior do TII, que liderou rankings antes do Falcon 180B"
description: "Modelo aberto anterior do TII, que liderou rankings antes do Falcon 180B"
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 4
release_date: '2023-05-25'
param_count: '40B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
mmlu_score: 82.7
humaneval_score: 76.3
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '109766ee6da4'
---

O Falcon 40B é um modelo de linguagem causal apenas decodificador, com 40 bilhões de parâmetros, lançado pelo Technology Innovation Institute em maio de 2023. Foi treinado com cerca de 1 trilhão de tokens do RefinedWeb, grande conjunto de dados da web selecionado e filtrado pelo próprio TII, combinado com alguns corpora adicionais. No lançamento, liderou o Open LLM Leaderboard do Hugging Face entre modelos de código aberto, com pontuações de 82,7 no MMLU e 76,3 no HumanEval, à frente de contemporâneos como MPT e RedPajama e competitivo com o Llama 2 70B, maior, da Meta em vários benchmarks. A arquitetura usa atenção multiquery e FlashAttention para reduzir o custo de inferência em relação ao tamanho. O TII publicou o modelo sob Apache 2.0, sem royalties — uma escolha excepcionalmente permissiva para um modelo dessa escala na época —, o que ajudou sua adoção empresarial, inclusive sua disponibilidade no AWS SageMaker JumpStart. O Falcon 40B foi substituído pelo Falcon 180B e pela família Falcon 3; sua janela de contexto de 2.048 tokens também é pequena diante dos modelos atuais.
