---
title: 'Florence-2'
name: 'Florence-2'
slug: 'florence-2'
subtitle: "Modelo compacto de visão fundamental da Microsoft para legendagem, detecção e segmentação em um único modelo"
description: "Modelo compacto de visão fundamental da Microsoft para legendagem, detecção e segmentação em um único modelo"
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.microsoft.com/en-us/research/publication/florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks/'
price: 'Free'
rank: 6
release_date: '2024-06-15'
param_count: '0.77B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Azure AI Foundry']
date: '2026-07-16'
tags: [computer-vision, open-weight, multimodal]
i18n_source: '9791d240cd8e'
---

O Florence-2 é um modelo fundamental de visão lançado pelo Microsoft Research em junho de 2024, criado para realizar legendagem, detecção de objetos, segmentação e aterramento visual em um único modelo, sem precisar de um modelo separado para cada tarefa. Ele usa prompts: a mesma rede pode produzir uma legenda, um conjunto de caixas delimitadoras ou uma máscara de segmentação, dependendo da instrução em texto, por meio de uma arquitetura unificada sequência a sequência. A Microsoft lançou dois tamanhos: uma versão base de 230 milhões de parâmetros e uma versão large de 770 milhões, ambas pequenas em comparação com modelos visão-linguagem típicos. O treinamento usou o FLD-5B, conjunto interno da Microsoft com cerca de 126 milhões de imagens e 5,4 bilhões de anotações. Isso permite que um modelo tão pequeno iguale ou supere modelos especializados maiores em tarefas como legendagem no COCO e compreensão de expressões de referência. A Microsoft publicou os pesos sob licença MIT no Hugging Face e também oferece o modelo pelo Azure AI Foundry, tornando-o popular entre equipes que querem recursos de visão sem executar um LLM multimodal grande.
