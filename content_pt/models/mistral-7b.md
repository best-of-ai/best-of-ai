---
title: Mistral 7B
name: Mistral 7B
slug: mistral-7b
subtitle: Modelo compacto original de pesos abertos da Mistral, que superou concorrentes
  maiores
description: Modelo compacto original de pesos abertos da Mistral, que superou concorrentes
  maiores
company: mistral-ai
model_type: Language
logo_url: ''
product_url: https://mistral.ai/news/announcing-mistral-7b/
price: Free
rank: 6
release_date: '2023-09-27'
param_count: 7B
context_window_tokens: 32000
modality:
- text
open_weight: true
license: Apache 2.0
api_available: true
mmlu_score: 60.1
humaneval_score: 30.5
access_methods:
- Self-hosted
runs_at_home: true
platforms:
- Hugging Face
- Ollama
date: '2026-07-16'
tags:
- llm
- open-weight
- small-model
- self-hosted
extra_model_types:
- Code
i18n_source: 'c7cb93d8e531'
---
O Mistral 7B colocou a Mistral AI no mapa. Lançado em 27 de setembro de 2023, foi o primeiro modelo público da startup francesa. Com 7 bilhões de parâmetros, era pequeno o bastante para funcionar em uma única GPU de consumo, mas superou o Llama 2 13B em todos os benchmarks avaliados pela Mistral e também venceu o Llama 2 34B em várias tarefas de raciocínio e programação, com pontuações de 60,1% no MMLU e 30,5% no HumanEval. O modelo usa atenção de consulta agrupada e atenção de janela deslizante para manter a inferência rápida e eficiente em memória, com contexto de 32.000 tokens.

A Mistral o lançou sob a licença Apache 2.0, sem restrições de uso, algo incomum para um modelo de qualidade semelhante na época. Isso contribuiu para sua rápida disseminação na comunidade de código aberto pelo Hugging Face e por ferramentas como Ollama e llama.cpp. Ele se tornou uma base comum para fine-tuning e combinações de modelos, e seu sucesso estabeleceu a Mistral AI como concorrente relevante da Meta e da OpenAI poucos meses após a fundação da empresa.
