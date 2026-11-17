---
title: 'BLIP-2'
name: 'BLIP-2'
slug: 'blip-2'
subtitle: "Sucessor mais eficiente do BLIP da Salesforce, que inicia o pré-treinamento visão-linguagem com codificadores congelados"
description: "Sucessor mais eficiente do BLIP da Salesforce, que inicia o pré-treinamento visão-linguagem com codificadores congelados"
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/LAVIS/tree/main/projects/blip2'
price: 'Free'
rank: 6
release_date: '2023-01-30'
param_count: '3.7B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '8456e2d29321'
---

BLIP-2 é um modelo de visão e linguagem publicado pelo Salesforce Research em janeiro de 2023, construído em torno de um recurso específico de eficiência: em vez de treinar do zero um grande codificador de imagens e um modelo de linguagem em conjunto, ele congela um codificador de imagens pré-treinado e um modelo de linguagem pré-treinado, treinando apenas um conector leve entre eles, chamado Q-Former. O Q-Former tem cerca de 188 milhões de parâmetros treináveis, menos de 2% do total do modelo, o que tornou o BLIP-2 muito mais barato de treinar que modelos de visão e linguagem comparáveis da época, mantendo bons resultados em legendagem de imagens e respostas visuais a perguntas. O Salesforce lançou várias variantes que combinam o Q-Former com diferentes modelos de linguagem congelados, incluindo versões baseadas em OPT, com 2,7B e 6,7B parâmetros, e em Flan-T5, com até 11B parâmetros, permitindo que usuários escolham entre capacidade e custo computacional. O código e os pesos estão no GitHub e no Hugging Face sob a licença MIT como parte da biblioteca LAVIS do Salesforce. A abordagem que popularizou, com codificadores congelados e um conector leve, influenciou modelos multimodais posteriores que também adicionam capacidades visuais a modelos de linguagem existentes em vez de treinar tudo em conjunto.
