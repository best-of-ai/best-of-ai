---
title: 'Gopher'
name: 'Gopher'
slug: 'gopher'
subtitle: 'Gopher é um modelo de linguagem com 280 bilhões de parâmetros que o DeepMind treinou e descreveu em um artigo de dezembro de 2021 como parte de um estudo sobre como o desempenho dos modelos cresce com o tamanho.'
description: 'Gopher é um modelo de linguagem com 280 bilhões de parâmetros que o DeepMind treinou e descreveu em um artigo de dezembro de 2021 como parte de um estudo sobre como o desempenho dos modelos cresce com o tamanho.'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/'
price: 'Paid'
rank: 6
release_date: '2021-12-08'
param_count: '280B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 60.0
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
i18n_source: 'adb1e7eb1bf4'
---

Gopher é um modelo de linguagem com 280 bilhões de parâmetros que o DeepMind treinou e descreveu em um artigo de dezembro de 2021 como parte de um estudo sobre como o desempenho dos modelos cresce com o tamanho. Foi treinado com o MassiveText, um corpus de 10,5 terabytes, e avaliado junto com cinco modelos menores, de 44 milhões a 7 bilhões de parâmetros, para estudar como a capacidade melhorava com a escala. No benchmark MMLU, Gopher obteve 60% em uma configuração de cinco exemplos, um salto expressivo em relação aos modelos anteriores da época.

O DeepMind nunca publicou o Gopher nem o ofereceu por API; ele existiu exclusivamente como instrumento de pesquisa. Seu principal legado veio da análise posterior, publicada como artigo Chinchilla, que usou o Gopher e seus modelos irmãos para mostrar que a maioria dos grandes modelos de linguagem da época tinha sido treinada de forma insuficiente em relação ao número de parâmetros. Essa conclusão reformulou durante anos a forma como os laboratórios distribuíam a computação entre tamanho do modelo e dados de treinamento.
