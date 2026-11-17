---
title: 'ELMo'
name: 'ELMo'
slug: 'elmo'
subtitle: 'Modelo de representação contextual profunda de palavras da AI2, anterior à era dos transformers'
description: 'Modelo de representação contextual profunda de palavras da AI2, anterior à era dos transformers'
company: 'allen-institute-for-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://allenai.org/allennlp/software/elmo'
price: 'Free'
rank: 5
release_date: '2018-02-15'
param_count: '93.6M'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['AllenNLP']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: 'b789397d7327'
---

ELMo, sigla de Embeddings from Language Models, foi desenvolvido pelo Allen Institute for AI e pela Universidade de Washington e lançado em fevereiro de 2018. É descrito no artigo “Deep Contextualized Word Representations”, de Matthew Peters, Mark Neumann e coautores. Em vez de atribuir a cada palavra um vetor fixo, como faziam embeddings anteriores, como word2vec e GloVe, o ELMo processa uma frase com uma LSTM bidirecional e gera uma representação de cada palavra conforme o contexto. Assim, a mesma palavra recebe vetores diferentes conforme seu uso. Treinado com cerca de um bilhão de palavras, melhorou resultados em seis tarefas de PLN da época, incluindo perguntas e respostas e reconhecimento de entidades nomeadas, quando incorporado a modelos existentes como recurso. O ELMo é anterior à arquitetura transformer e foi amplamente substituído pelo BERT e seus sucessores em cerca de um ano, mas é citado como um dos modelos que estabeleceu as representações contextuais de palavras como abordagem padrão em PLN.