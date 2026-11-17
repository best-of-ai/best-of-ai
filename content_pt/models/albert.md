---
title: 'ALBERT'
name: 'ALBERT'
slug: 'albert'
subtitle: "Variante do BERT com compartilhamento de parâmetros do Google, criada para eficiência em escala"
description: "Variante do BERT com compartilhamento de parâmetros do Google, criada para eficiência em escala"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1909.11942'
price: 'Free'
rank: 6
release_date: '2019-09-26'
param_count: '223M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: '4c3c3afa8529'
---

ALBERT (A Lite BERT) é um modelo de representação de linguagem que o Google Research e o Toyota Technological Institute publicaram em setembro de 2019 como continuação do BERT. Ele usa duas técnicas para reduzir parâmetros — parametrização fatorada de embeddings e compartilhamento de parâmetros entre camadas — e assim reduz bastante o número de parâmetros sem perder competitividade em precisão frente a modelos muito maiores. A configuração maior, ALBERT-xxlarge, com cerca de 223 milhões de parâmetros, tem aproximadamente 18 vezes menos parâmetros que o BERT-large, mas treina mais rápido e, na época do lançamento, estabeleceu novos resultados de ponta em GLUE, SQuAD 2.0 e RACE.

Assim como o BERT, o ALBERT é um modelo somente codificador, voltado a tarefas de compreensão, como classificação, resposta a perguntas e compreensão de leitura, em vez de geração de texto aberto, e limita a entrada a 512 tokens por sequência. O Google disponibilizou abertamente o código e os pesos pré-treinados, e o modelo se tornou uma referência comum em pesquisa de PLN e sistemas de produção no início da década de 2020, antes de os modelos generativos somente decodificadores dominarem a atenção da área.
