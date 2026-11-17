---
title: 'DeepFloyd IF'
name: 'DeepFloyd IF'
slug: 'deepfloyd-if'
subtitle: 'Modelo de geração de imagens em espaço de pixels, sem espaço latente, desenvolvido pelo laboratório DeepFloyd apoiado pela Stability'
description: 'Modelo de geração de imagens em espaço de pixels, sem espaço latente, desenvolvido pelo laboratório DeepFloyd apoiado pela Stability'
company: 'stability-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://stability.ai/news/deepfloyd-if-text-to-image-model'
price: 'Free'
rank: 5
release_date: '2023-04-28'
param_count: '4.3B'
modality: [text, image]
open_weight: true
license: 'Stability Community License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [image-generation, open-weight, legacy]
i18n_source: 'e6c34510f10f'
---

O DeepFloyd IF é um modelo de texto para imagem lançado em abril de 2023 pelo DeepFloyd, laboratório de pesquisa apoiado pela Stability AI. Adota uma abordagem diferente da difusão no espaço latente do Stable Diffusion: opera diretamente no espaço de pixels, em uma sequência de três módulos. Primeiro gera uma imagem de baixa resolução, 64 × 64, e depois amplia a imagem em etapas até 1024 × 1024. Isso lhe deu uma boa reputação por renderizar texto legível nas imagens, tarefa que modelos de difusão latente da época frequentemente executavam mal. O DeepFloyd treinou três tamanhos do módulo base; o maior tem 4,3 bilhões de parâmetros. O pipeline completo foi publicado como prévia de pesquisa não comercial sob uma licença Stability Community, não uma licença totalmente aberta. Nunca se tornou um produto popular como o Stable Diffusion, mas seus resultados com texto influenciaram modelos comerciais posteriores.