---
title: 'Hunyuan DiT'
name: 'Hunyuan DiT'
slug: 'hunyuan-dit'
subtitle: 'Hunyuan-DiT é o modelo de texto para imagem com pesos abertos da Tencent, baseado em uma arquitetura transformer de difusão, em vez do projeto U-Net usado pela maioria dos modelos de difusão anteriores.'
description: 'Hunyuan-DiT é o modelo de texto para imagem com pesos abertos da Tencent, baseado em uma arquitetura transformer de difusão, em vez do projeto U-Net usado pela maioria dos modelos de difusão anteriores.'
company: 'tencent'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Tencent/HunyuanDiT'
price: 'Free'
rank: 5
release_date: '2024-05-14'
param_count: '1.5B'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: '7a104e51d815'
---

Hunyuan-DiT é o modelo de texto para imagem com pesos abertos da Tencent, baseado em uma arquitetura transformer de difusão, em vez do projeto U-Net usado pela maioria dos modelos de difusão anteriores. A Tencent o publicou em maio de 2024, combinando um transformer de remoção de ruído de 1,5B parâmetros com codificadores de texto CLIP bilíngue e T5 multilíngue, para seguir comandos escritos em chinês ou inglês com fidelidade semelhante. Esse foco bilíngue é seu principal diferencial: a maioria dos modelos abertos de texto para imagem da época processava mal comandos em chinês, e o Hunyuan-DiT foi treinado especificamente para reduzir essa diferença. Gera imagens de 1024 x 1024 e inclui um componente integrado de conversa multimodal que permite refinar uma imagem ao longo de várias interações, sem reescrever todo o comando a cada vez. A Tencent publicou os pesos no Hugging Face e no GitHub sob sua licença Hunyuan e lançou posteriormente a atualização 1.1, que corrigiu a saturação excessiva e os artefatos de marca d’água presentes no checkpoint original.
