---
title: 'Imagen'
name: 'Imagen'
slug: 'imagen'
subtitle: 'Imagen é o modelo original de difusão de texto para imagem do Google Research, descrito no artigo “Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding”, publicado no arXiv em maio de 2022.'
description: 'Imagen é o modelo original de difusão de texto para imagem do Google Research, descrito no artigo “Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding”, publicado no arXiv em maio de 2022.'
company: 'google-deepmind'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://imagen.research.google/'
price: 'Paid'
rank: 6
release_date: '2022-05-24'
param_count: 'Undisclosed'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, research, legacy]
i18n_source: '6e5bc6e9c169'
---

Imagen é o modelo original de difusão de texto para imagem do Google Research, descrito no artigo “Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding”, publicado no arXiv em maio de 2022. Ele combina um grande modelo de linguagem congelado, o T5, com uma sequência de modelos de difusão: um modelo-base que gera uma imagem pequena de 64 × 64 pixels, seguida de duas etapas de super-resolução que a ampliam primeiro para 256 × 256 e depois para 1024 × 1024. A principal conclusão do artigo foi que ampliar o codificador de texto melhorava a qualidade da imagem e a aderência ao comando mais que ampliar a própria rede de difusão de imagens, resultado que influenciou sistemas posteriores de texto para imagem em todo o setor. O Imagen informou uma pontuação FID de ponta de 7,27 no benchmark COCO, apesar de nunca ter sido treinado com dados do COCO.

O Google nunca lançou o Imagen como produto público. Ele permaneceu como prévia de pesquisa, apresentado junto com o modelo autorregressivo Parti e comparado ao DALL-E 2 da OpenAI, lançado alguns meses antes. O nome e a linhagem continuaram nos modelos comerciais Imagen 2, 3 e 4, que mantiveram a mesma abordagem de difusão e acrescentaram infraestrutura de produção, filtros de segurança e acesso por API, ausentes no modelo de pesquisa original.
