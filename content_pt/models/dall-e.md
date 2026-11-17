---
title: 'DALL-E'
name: 'DALL-E'
slug: 'dall-e'
subtitle: 'Modelo original de geração de imagens a partir de texto da OpenAI, de 2021'
description: 'Modelo original de geração de imagens a partir de texto da OpenAI, de 2021'
company: 'openai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://openai.com/index/dall-e/'
price: 'Paid'
rank: 5
release_date: '2021-01-05'
param_count: '12B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, legacy]
i18n_source: '69880ba7eb3a'
---

O DALL-E é o modelo original de texto para imagem da OpenAI, apresentado em janeiro de 2021 como uma variante do GPT-3 com 12 bilhões de parâmetros, treinada para gerar imagens a partir de legendas em texto. Ele tratava a geração de imagens como um problema de previsão de sequências: um autoencoder variacional discreto convertia imagens em tokens, e um transformer autorregressivo aprendia a prever esses tokens a partir de um prompt. Depois, um modelo CLIP classificava as imagens resultantes. Foi treinado com cerca de 250 milhões de pares de texto e imagem coletados na internet e conseguia gerar imagens plausíveis de combinações de conceitos que nunca haviam sido vistas juntas, como uma poltrona em forma de abacate. O DALL-E nunca foi lançado como produto público: a OpenAI o manteve como prévia de pesquisa e depois o substituiu pelo DALL-E 2, baseado em difusão, que produzia imagens mais nítidas com uma fração dos parâmetros.