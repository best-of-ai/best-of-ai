---
title: 'CLIP (LAION variant)'
name: 'CLIP (LAION variant)'
slug: 'clip-laion-variant'
subtitle: "Modelo CLIP de embeddings visão-linguagem retreinado pela LAION e com pesos abertos"
description: "Modelo CLIP de embeddings visão-linguagem retreinado pela LAION e com pesos abertos"
company: 'laion'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://laion.ai/'
price: 'Free'
rank: 4
release_date: '2022-09-15'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, vision, self-hosted]
i18n_source: '40efbd85bd2a'
---

Esta variante do CLIP é um retreinamento com pesos abertos da arquitetura CLIP original da OpenAI, produzido pela LAION e distribuído pelo projeto open_clip, não pela própria OpenAI. Usa a base de vision transformer ViT-L/14, tem cerca de 428 milhões de parâmetros e foi treinada no LAION-2B, subconjunto em inglês com 2 bilhões de pares imagem-texto do conjunto maior LAION-5B, usando 384 GPUs A100 no supercomputador JUWELS. Como o CLIP original, mapeia imagens e textos para um espaço compartilhado de embeddings, permitindo classificação de imagens sem exemplos, recuperação imagem-texto e busca por similaridade sem ajuste fino específico para cada tarefa. Alcança cerca de 75,3% de precisão sem exemplos no ImageNet-1k. Como os pesos são publicados sob licença aberta e hospedados no Hugging Face, tornou-se substituto direto comum dos checkpoints fechados do CLIP da OpenAI em projetos abertos de busca de imagens, legendagem e geração de arte, inclusive como encoder de texto em várias variantes do Stable Diffusion.
