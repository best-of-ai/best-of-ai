---
title: 'InternLM2.5'
name: 'InternLM2.5'
slug: 'internlm2-5'
subtitle: "Geração InternLM atualizada do Shanghai AI Lab, com uso de ferramentas e raciocínio mais fortes"
description: "Geração InternLM atualizada do Shanghai AI Lab, com uso de ferramentas e raciocínio mais fortes"
company: 'shanghai-ai-lab'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-07-03'
param_count: '7B (1.8B and 20B variants also released)'
context_window_tokens: 1000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.8
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, long-context]
i18n_source: '4f1fc404afae'
---

O InternLM2.5 é a continuação do InternLM2 pelo Shanghai AI Laboratory, lançado a partir de 3 de julho de 2024 nos tamanhos 7B e 1.8B, com uma versão 20B adicionada em 1º de agosto de 2024. O modelo de chat 7B obtém 72,8 no MMLU e supera o Llama 3 8B Instruct e o Gemma 2 9B em vários benchmarks de raciocínio e matemática, segundo as avaliações OpenCompass do próprio desenvolvedor. Um checkpoint dedicado 7B-Chat-1M amplia a janela de contexto para um milhão de tokens e consegue localizar fatos específicos em documentos com milhões de tokens em testes de agulha no palheiro, enquanto o modelo padrão 20B chega a 200 mil tokens. A série também acrescenta chamadas de função mais robustas e uso de ferramentas no estilo de agentes em comparação com o InternLM2 original, e todos os pesos são lançados sob a licença Apache 2.0 pelo Hugging Face e pelo repositório InternLM no GitHub.
