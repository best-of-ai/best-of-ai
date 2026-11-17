---
title: 'ESM-2'
name: 'ESM-2'
slug: 'esm-2'
subtitle: "Modelo de linguagem de proteínas da Meta usado para prever estruturas a partir de sequências"
description: "Modelo de linguagem de proteínas da Meta usado para prever estruturas a partir de sequências"
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/protein-folding-esmfold-metagenomics/'
price: 'Free'
rank: 6
release_date: '2022-10-31'
param_count: '15B'
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [science, biology, open-weight]
i18n_source: '603d0e8b688e'
---

O ESM-2 é um modelo de linguagem de proteínas da Meta AI, lançado em outubro de 2022 e treinado com cerca de 250 milhões de sequências proteicas, sem etapa de alinhamento de múltiplas sequências. Há vários tamanhos, até 15 bilhões de parâmetros, o maior modelo de linguagem de proteínas na época do lançamento. A Meta observou que, à medida que o modelo cresce, suas representações internas passam a codificar informações sobre a estrutura tridimensional das proteínas, sem ter sido explicitamente treinado para isso. Essa propriedade alimenta o ESMFold, sistema de previsão estrutural da Meta, que processa uma sequência de proteínas pelo ESM-2 e converte diretamente a representação resultante em coordenadas atômicas. Assim, dispensa os bancos de dados de alinhamento usados por ferramentas como o AlphaFold e torna a previsão estrutural muito mais rápida. A Meta publicou os pesos abertamente e usou o ESM-2 para criar o ESM Metagenomic Atlas, banco de dados público de estruturas previstas para centenas de milhões de proteínas antes não caracterizadas.
