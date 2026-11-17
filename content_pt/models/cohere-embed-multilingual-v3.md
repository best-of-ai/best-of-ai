---
title: 'Cohere Embed Multilingual v3'
name: 'Cohere Embed Multilingual v3'
slug: 'cohere-embed-multilingual-v3'
subtitle: "Modelo de embeddings da Cohere, ajustado para recuperação em mais de 100 idiomas"
description: "Modelo de embeddings da Cohere, ajustado para recuperação em mais de 100 idiomas"
company: 'cohere'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://cohere.com/blog/introducing-embed-v3'
price: 'Paid'
rank: 6
release_date: '2023-11-02'
param_count: 'Undisclosed'
context_window_tokens: 512
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Cohere API']
date: '2026-07-16'
tags: [embedding, api, multilingual]
i18n_source: '5c2674ca56c9'
---

O Cohere Embed Multilingual v3 é um modelo de embeddings de texto lançado pela Cohere em novembro de 2023 para busca, geração aumentada por recuperação e tarefas de similaridade semântica em mais de 100 idiomas. Ele recebe textos de até 512 tokens e, por padrão, gera um vetor de 1.024 dimensões; também oferece embeddings menores, de 384 ou 768 dimensões, para equipes que querem buscas mais rápidas ou menor custo de armazenamento. A Cohere o treinou junto com o modelo irmão apenas para inglês, Embed English v3, e apresentou ambos como melhorias em relação à versão 2: eles ponderam trechos de acordo com sua provável relevância, e não apenas pela similaridade, reduzindo resultados de recuperação ruidosos em pipelines RAG. O preço pela API da Cohere é US$ 0,10 por milhão de tokens. O modelo também é distribuído pelos marketplaces da AWS, Azure e Oracle Cloud. Desde então, a Cohere lançou modelos Embed v4 mais novos; alguns provedores de nuvem, como a Oracle, já listam a versão 3 como legada ou descontinuada, embora ela continue disponível pela API da Cohere e no Hugging Face.
