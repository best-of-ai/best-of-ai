---
title: 'Nemotron 5'
name: 'Nemotron 5'
slug: 'nemotron-5'
subtitle: "Modelo de pesos abertos da NVIDIA ajustado para inferência eficiente em seu próprio hardware"
description: "Modelo de pesos abertos da NVIDIA ajustado para inferência eficiente em seu próprio hardware"
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/nemotron'
price: 'Free'
rank: 6
release_date: '2026-07-10'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'NVIDIA Open Model License'
api_available: true
mmlu_score: 82.0
humaneval_score: 80.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'NVIDIA NIM', 'NGC']
date: '2026-07-19'
tags: [llm, open-weight, self-hosted, efficiency]
i18n_source: '528d47e90cc1'
---

Nemotron 5 dá continuidade à linha de modelos de pesos abertos da NVIDIA, desenvolvidos menos para liderar tabelas de classificação e mais para demonstrar o bom desempenho dos modelos nas próprias GPUs e na pilha de inferência da empresa. É um modelo denso de 70 bilhões de parâmetros, com janela de contexto de 128.000 tokens, distribuído sob a NVIDIA Open Model License e preparado para implantação com um clique por meio dos microsserviços NVIDIA NIM, além de downloads comuns do Hugging Face.

Desde o Nemotron-4 340B, a NVIDIA usa a linha Nemotron para demonstrar técnicas como poda e destilação, que reduzem modelos sem comprometer sua qualidade, e o Nemotron 5 mantém esse foco. O tamanho 70B foi escolhido especificamente para caber em uma única H100 ou em um par de GPUs de consumo com quantização razoável. A proposta central da NVIDIA aqui é a pilha de hardware e software por trás do modelo, não o modelo em si.
