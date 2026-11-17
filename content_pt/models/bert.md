---
title: 'BERT'
name: 'BERT'
slug: 'bert'
subtitle: "Codificador bidirecional do Google de 2018 que transformou a pesquisa em PLN"
description: "Codificador bidirecional do Google de 2018 que transformou a pesquisa em PLN"
company: 'google'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://github.com/google-research/bert'
price: 'Free'
rank: 6
release_date: '2018-10-11'
param_count: '340M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, nlp, legacy]
i18n_source: '9489893b9c63'
---

BERT (Representações de Codificadores Bidirecionais de Transformers) é um modelo de linguagem publicado pelo Google Research em outubro de 2018 que mudou a forma como a área abordava o pré-treinamento para tarefas de PLN. Ao contrário de modelos anteriores, que liam o texto da esquerda para a direita, o BERT é treinado para prever palavras mascaradas e a frase seguinte, o que lhe permite criar representações que usam o contexto simultaneamente nas duas direções. O Google lançou dois tamanhos principais: BERT-base, com 110 milhões de parâmetros, e BERT-large, com 340 milhões, ambos com limite de 512 tokens, e disponibilizou os pesos gratuitamente sob a licença Apache 2.0 no GitHub e, mais tarde, no Hugging Face. No lançamento, versões ajustadas do BERT estabeleceram novos recordes em onze benchmarks diferentes de PLN, incluindo resposta a perguntas e inferência em linguagem natural, e ele rapidamente se tornou o modelo-base padrão para ajustes finos em tarefas como classificação, reconhecimento de entidades nomeadas e ordenação de resultados de busca. Em grande parte, foi substituído por modelos codificadores mais recentes, como RoBERTa e DeBERTa, e pelos modelos de embeddings que vieram depois, mas continua sendo um dos artigos mais citados em PLN, e sua arquitetura sustenta grande parte dos sistemas posteriores baseados em codificadores.
