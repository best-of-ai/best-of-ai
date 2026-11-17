---
title: 'Llama Guard 3'
name: 'Llama Guard 3'
slug: 'llama-guard-3'
subtitle: "Classificador de segurança de pesos abertos da Meta para moderar entradas e saídas de LLMs"
description: "Classificador de segurança de pesos abertos da Meta para moderar entradas e saídas de LLMs"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 4
release_date: '2024-07-23'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, safety, self-hosted]
i18n_source: 'f0c740f9e81b'
---

Llama Guard 3 é o classificador de segurança da Meta, lançado em julho de 2024 junto com o Llama 3.1 e substituindo o Llama Guard 2 como modelo de moderação recomendado pela Meta. Construído sobre uma base Llama 3.1 8B, amplia o antecessor com três novas categorias de risco, elevando a taxonomia total a 14, e melhora a cobertura de moderação multilíngue. Como o Llama Guard 2, ele integra um fluxo de processamento em vez de atuar como assistente independente: lê um prompt ou a resposta de um modelo e retorna uma classificação de seguro ou inseguro, além da categoria violada. Tem pesos abertos sob a Llama 3.1 Community License e é amplamente usado por empresas que implantam LLMs de código aberto e precisam de uma camada de moderação sem depender de uma API de terceiros.
