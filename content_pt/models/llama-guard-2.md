---
title: 'Llama Guard 2'
name: 'Llama Guard 2'
slug: 'llama-guard-2'
subtitle: "Modelo anterior de classificação de segurança de conteúdo da Meta, anterior ao Llama Guard 3"
description: "Modelo anterior de classificação de segurança de conteúdo da Meta, anterior ao Llama Guard 3"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-llama-3/'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [safety, open-weight, legacy]
i18n_source: '1ec3f0456e4e'
---

Llama Guard 2 é um classificador de segurança de conteúdo lançado pela Meta junto com o Llama 3 em abril de 2024, baseado no Llama 3 8B, e não criado como modelo de chat de uso geral. Ele verifica tanto os prompts enviados a um modelo de linguagem quanto as respostas geradas, sinalizando conteúdo em 11 categorias de risco da taxonomia MLCommons, que abrangem violência, discurso de ódio e conteúdo sexual. Desenvolvedores o usam como barreira de segurança antes ou depois de outro LLM em um fluxo de processamento, em vez de usá-lo diretamente para gerar respostas. Desde então, a Meta o substituiu pelo Llama Guard 3, mas ele continua disponível no Hugging Face sob a Llama 3 Community License para equipes que já o executam em produção.
