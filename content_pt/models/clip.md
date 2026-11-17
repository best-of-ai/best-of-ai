---
title: 'CLIP'
name: 'CLIP'
slug: 'clip'
subtitle: "Modelo contrastivo fundamental de imagem e texto da OpenAI, base de grande parte da IA multimodal moderna"
description: "Modelo contrastivo fundamental de imagem e texto da OpenAI, base de grande parte da IA multimodal moderna"
company: 'openai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://openai.com/index/clip/'
price: 'Free'
rank: 8
release_date: '2021-01-05'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy, foundation-model]
i18n_source: 'bc970f441b1f'
---

O CLIP (Contrastive Language-Image Pre-training) é um modelo lançado pela OpenAI em janeiro de 2021 que aprende a associar imagens a descrições em texto. Foi treinado com 400 milhões de pares imagem-texto coletados da internet, usando um objetivo contrastivo que aproxima embeddings de imagens e textos correspondentes e afasta pares incompatíveis. A maior variante publicada usa o vision transformer ViT-L/14 junto com um transformer de texto de 63 milhões de parâmetros, totalizando cerca de 428 milhões de parâmetros. Em vez de ser treinado para uma única tarefa, o CLIP aprende um espaço geral de embeddings conjuntos de imagens e textos, permitindo classificar imagens sem exemplos ao compará-las com um conjunto de rótulos em texto, sem ajuste fino específico.

O impacto real do CLIP veio depois do lançamento, não de resultados de destaque em benchmarks. Seus encoders de imagem e texto se tornaram a base de muitos sistemas posteriores, incluindo o pipeline de geração de imagens do DALL-E 2, o condicionamento de texto do Stable Diffusion e inúmeras ferramentas de busca e recuperação de imagens. Meta, Salesforce e outros laboratórios lançaram variantes e versões ajustadas do CLIP, mas os pesos originais da OpenAI, publicados sob licença MIT no GitHub e no Hugging Face, continuam sendo um ponto de partida comum para projetos multimodais anos depois.
