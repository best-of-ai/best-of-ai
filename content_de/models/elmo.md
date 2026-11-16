---
title: 'ELMo'
name: 'ELMo'
slug: 'elmo'
subtitle: 'Das tief kontextualisierte Wortrepräsentationsmodell von AI2 aus der Zeit vor Transformern'
description: 'Das tief kontextualisierte Wortrepräsentationsmodell von AI2 aus der Zeit vor Transformern'
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
ELMo steht für „Embeddings from Language Models“ und entstand am Allen Institute for AI und an der University of Washington. Es wurde im Februar 2018 veröffentlicht und in der Arbeit „Deep Contextualized Word Representations“ von Matthew Peters, Mark Neumann und weiteren Forschenden beschrieben. Anders als frühere Embedding-Verfahren wie word2vec und GloVe, die jedem Wort einen festen Vektor zuweisen, verarbeitet ELMo einen Satz mit einem bidirektionalen LSTM. Für jedes Wort entsteht so eine Repräsentation, die vom umgebenden Kontext abhängt; dasselbe Wort erhält je nach Verwendung einen anderen Vektor. Das Modell wurde mit ungefähr einer Milliarde Wörtern trainiert und verbesserte damals in sechs NLP-Aufgaben, darunter Fragebeantwortung und Erkennung benannter Entitäten, die Ergebnisse bestehender Modelle, wenn es als Merkmal eingebunden wurde. ELMo erschien vor der Transformer-Architektur und wurde innerhalb von etwa einem Jahr weitgehend von BERT und dessen Nachfolgern abgelöst. Es gilt jedoch weiterhin als eines der Modelle, die kontextuelle Wortrepräsentationen zum Standard in der NLP machten.
