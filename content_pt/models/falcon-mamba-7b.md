---
title: 'Falcon Mamba 7B'
name: 'Falcon Mamba 7B'
slug: 'falcon-mamba-7b'
subtitle: "Modelo de pesos abertos do TII baseado na arquitetura de espaço de estados Mamba"
description: "Modelo de pesos abertos do TII baseado na arquitetura de espaço de estados Mamba"
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 3
release_date: '2024-08-12'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'TII Falcon Mamba 7B License 1.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, hybrid-architecture, self-hosted]
i18n_source: '117aa18c3953'
---

O Falcon Mamba 7B, lançado pelo Technology Innovation Institute em agosto de 2024, foi o primeiro modelo de linguagem aberto forte de 7B construído inteiramente sobre a arquitetura de espaço de estados Mamba, em vez de atenção transformer. Como não tem mecanismo de atenção, o uso de memória e a velocidade de inferência permanecem constantes conforme as sequências geradas ficam mais longas, ao contrário dos transformers, cuja computação cresce com o comprimento do contexto. O TII o treinou em etapas que ampliaram o contexto efetivo de 2.048 para 8.192 tokens. Em comparações de benchmarks, igualou ou superou modelos transformer de tamanho semelhante, incluindo Mistral 7B e Llama 3.1 8B da Meta, além de superar outros modelos não transformer, como RecurrentGemma 9B e RWKV-v6. O TII distribui os pesos no Hugging Face sob sua própria licença Falcon Mamba, voltada a pesquisadores e desenvolvedores que buscam uma alternativa a arquiteturas baseadas em atenção para cargas de sequências longas.
