---
title: 'Chinchilla'
name: 'Chinchilla'
slug: 'chinchilla'
subtitle: "Modelo de pesquisa da DeepMind de 2022 que redefiniu as premissas das leis de escala para treinamento de LLMs"
description: "Modelo de pesquisa da DeepMind de 2022 que redefiniu as premissas das leis de escala para treinamento de LLMs"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/'
price: 'Paid'
rank: 4
release_date: '2022-03-29'
param_count: '70B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 67.5
access_methods: [Self-hosted]
runs_at_home: false
platforms: []
date: '2026-07-16'
tags: [llm, research, legacy]
i18n_source: '14414c05c298'
---

O Chinchilla é um modelo de linguagem de pesquisa descrito pela DeepMind em um artigo de março de 2022 sobre treinamento otimizado para computação. Com 70 bilhões de parâmetros, é muito menor que o modelo Gopher, de 280 bilhões de parâmetros, lançado anteriormente pela DeepMind. Ainda assim, foi treinado com cerca de quatro vezes mais dados e superou o Gopher, o GPT-3 e outros modelos maiores da época em vários benchmarks, incluindo uma pontuação média de aproximadamente 67,5% no MMLU. A principal conclusão do artigo foi que a maioria dos grandes modelos de linguagem até então tinha sido treinada com poucos dados para seu tamanho: com um orçamento fixo de computação, o tamanho do modelo e a quantidade de dados de treinamento devem crescer juntos, em vez de aumentar apenas o modelo.

Esse resultado, hoje conhecido como lei de escala do Chinchilla, mudou a forma como os laboratórios planejavam treinamentos, direcionando a área a modelos menores treinados com conjuntos de dados muito maiores, em vez de simplesmente aumentar a quantidade de parâmetros. A DeepMind nunca publicou os pesos do Chinchilla nem ofereceu acesso público; o modelo existe apenas como objeto de pesquisa descrito no artigo. Sua influência aparece indiretamente em quase todos os grandes modelos treinados desde então, do LLaMA ao GPT-4, que citam a escala otimizada para computação em suas metodologias de treinamento.
