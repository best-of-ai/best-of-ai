---
title: 'BioGPT'
name: 'BioGPT'
slug: 'biogpt'
subtitle: "Modelo generativo de domínio da Microsoft pré-treinado em literatura biomédica"
description: "Modelo generativo de domínio da Microsoft pré-treinado em literatura biomédica"
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BioGPT'
price: 'Free'
rank: 5
release_date: '2022-09-24'
param_count: '347M (base), 1.5B (Large)'
context_window_tokens: 1024
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [healthcare, open-weight, legacy]
i18n_source: 'b08c07fb9738'
---

BioGPT é um modelo de linguagem apresentado pelo Microsoft Research em outubro de 2022, criado especificamente para textos biomédicos, em vez de adaptado posteriormente a partir de um modelo de uso geral. Ele usa uma arquitetura decodificadora no estilo GPT-2, treinada do zero com cerca de 15 milhões de resumos do PubMed, e está disponível em uma versão-base de 347 milhões de parâmetros e na versão BioGPT-Large, de 1,5 bilhão. Como foi treinado desde o início com textos biomédicos, em vez de receber ajuste fino para esse domínio, superou modelos de linguagem de uso geral anteriores em tarefas como extração de relações biomédicas, respostas a perguntas sobre literatura médica e classificação de documentos. A Microsoft publicou ambos os checkpoints sob a licença MIT no Hugging Face e no GitHub, tornando-o um ponto de partida comum para grupos de pesquisa que criam ferramentas de PLN biomédico sem precisar treinar do zero um modelo específico do domínio. Ele antecede a onda de modelos de chat de uso geral ajustados para seguir instruções e não foi atualizado desde então, por isso hoje é usado principalmente como opção leve e auto-hospedável para tarefas restritas com textos biomédicos, em vez de assistente geral.
