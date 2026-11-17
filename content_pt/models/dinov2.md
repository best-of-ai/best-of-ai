---
title: 'DINOv2'
name: 'DINOv2'
slug: 'dinov2'
subtitle: 'Modelo de visão autossupervisionado da Meta que extrai características gerais de imagens sem rótulos'
description: 'Modelo de visão autossupervisionado da Meta que extrai características gerais de imagens sem rótulos'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/dino-v2-computer-vision-self-supervised-learning/'
price: 'Free'
rank: 6
release_date: '2023-04-17'
param_count: '1.1B'
modality: [image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [computer-vision, open-weight, self-supervised]
i18n_source: '35d54331b555'
---

O DINOv2 é um modelo de visão computacional lançado pela Meta AI em abril de 2023. Foi treinado sem rótulos em um conjunto de dados selecionado de 142 milhões de imagens chamado LVD-142M. Em vez de aprender a classificar imagens em categorias predefinidas, aprende características visuais gerais por destilação autossupervisionada. Essas características funcionam bem em diversas tarefas posteriores — classificação de imagens, estimativa de profundidade, segmentação e recuperação — muitas vezes sem ajuste fino. O maior modelo publicado tem 1,1 bilhão de parâmetros.

Como suas características são transferidas bem sem ajustes adicionais, o DINOv2 tornou-se uma base comum para outros sistemas de visão computacional, inclusive em áreas como imagens médicas, nas quais há poucos dados rotulados. A Meta publicou o código e os pesos sob a licença Apache 2.0 e lançou depois o DINOv3. Ainda assim, o DINOv2 continua amplamente usado como extrator visual de características de uso geral.