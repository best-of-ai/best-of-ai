---
title: 'Kosmos-2'
name: 'Kosmos-2'
slug: 'kosmos-2'
subtitle: "Modelo multimodal fundamentado da Microsoft que associa linguagem a regiões específicas de imagens"
description: "Modelo multimodal fundamentado da Microsoft que associa linguagem a regiões específicas de imagens"
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/microsoft/unilm/tree/master/kosmos-2'
price: 'Free'
rank: 5
release_date: '2023-06-26'
param_count: '1.6B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '327b99415fef'
---

Kosmos-2 é um modelo multimodal da Microsoft Research, publicado em junho de 2023, com cerca de 1,6 bilhão de parâmetros. Seu diferencial é a fundamentação: em vez de apenas descrever uma imagem em texto, ele associa frases da resposta a caixas delimitadoras específicas na imagem, de modo que uma frase sobre “um cachorro” ou “a cadeira à esquerda” aponte para os pixels exatos a que se refere. A Microsoft o treinou no GrIT, um grande conjunto de dados de pares imagem-texto fundamentados criado para esse fim, combinado com corpora multimodais gerais, e o avaliou em compreensão de expressões referenciais, fundamentação de frases e tarefas padrão de visão-linguagem. Kosmos-2 foi uma publicação de pesquisa, não um produto, destinada a mostrar que a fundamentação podia ser aprendida de ponta a ponta dentro de um modelo de linguagem, em vez de ser adicionada com um detector separado. O código e os pesos estão abertos no GitHub e Hugging Face sob a licença MIT, e o trabalho contribuiu para pesquisas multimodais posteriores da Microsoft, inclusive partes das linhas Florence e Phi de visão-linguagem.
