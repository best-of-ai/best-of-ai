---
title: 'CogView3'
name: 'CogView3'
slug: 'cogview3'
subtitle: "Modelo de texto para imagem da Zhipu baseado em difusão em cascata"
description: "Modelo de texto para imagem da Zhipu baseado em difusão em cascata"
company: 'zhipu-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogView3'
price: 'Free'
rank: 5
release_date: '2024-09-29'
param_count: '3B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: 'e06af9d7cbba'
---

O CogView3 é um modelo de texto para imagem da Zhipu AI e da Universidade Tsinghua, descrito em um artigo de pesquisa de março de 2024 e disponibilizado em código aberto no Hugging Face em setembro de 2024. Ele usa difusão em cascata: uma etapa base de 3 bilhões de parâmetros gera uma imagem de baixa resolução de 512 × 512; uma segunda etapa adiciona ruído à imagem e executa uma passagem mais curta de difusão para super-resolução, em vez de se condicionar diretamente na saída de baixa resolução, como faziam modelos em cascata anteriores. A Zhipu afirma que o CogView3 supera bastante o Stable Diffusion XL em avaliações humanas e precisa de cerca de metade do tempo de inferência. Uma versão destilada alcança qualidade semelhante usando aproximadamente um décimo das etapas de inferência do SDXL. O modelo e o código são publicados sob Apache 2.0. Depois, a Zhipu lançou o CogView-3Plus, uma variante maior com transformer de difusão da mesma família, e uma versão hospedada pela API da Zhipu para desenvolvedores que preferem não executá-lo por conta própria.
