---
title: Megatron-Turing NLG
name: Megatron-Turing NLG
slug: megatron-turing-nlg
subtitle: Modelo de pesquisa de 530B parâmetros da NVIDIA e da Microsoft, um dos maiores
  LLMs densos de sua época
description: Modelo de pesquisa de 530B parâmetros da NVIDIA e da Microsoft, um dos
  maiores LLMs densos de sua época
company: nvidia
model_type: Language
logo_url: ''
product_url: https://developer.nvidia.com/megatron-turing-natural-language-generation
price: Paid
rank: 5
release_date: '2021-10-11'
param_count: 530B
modality:
- text
open_weight: false
license: Proprietary
api_available: false
access_methods:
- Research
runs_at_home: false
platforms:
- Research
date: '2026-07-16'
tags:
- llm
- research
- legacy
extra_model_types:
- Reasoning
i18n_source: '06b0502910e0'
---
O Megatron-Turing NLG é um modelo de linguagem transformer denso, com 530 bilhões de parâmetros, treinado em conjunto pela NVIDIA e pela Microsoft e anunciado em outubro de 2021. Na época, era o maior modelo monolítico de linguagem já treinado, sem mistura de especialistas. Sua construção combinou o paralelismo tensorial do Megatron-LM, da NVIDIA, com o paralelismo de pipeline do DeepSpeed e o otimizador ZeRO, da Microsoft, em centenas de GPUs A100. O modelo tem 105 camadas transformer e foi treinado com um corpus de 270 bilhões de tokens, compilado a partir de textos da web, livros e outras fontes selecionadas.

Sua principal função foi demonstrar, em pesquisa e engenharia, até onde poderiam chegar o aumento de escala de modelos densos e o software de treinamento distribuído antes que arquiteturas de mistura de especialistas se tornassem uma opção mais prática para modelos maiores. NVIDIA e Microsoft publicaram resultados em benchmarks de completamento, compreensão de leitura e raciocínio, nos quais ele superou antecessores menores, como GPT-3 e Turing-NLG. O modelo, porém, nunca foi disponibilizado como produto público nem como API.
