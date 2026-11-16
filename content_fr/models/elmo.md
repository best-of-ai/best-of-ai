---
title: 'ELMo'
name: 'ELMo'
slug: 'elmo'
subtitle: "Le modèle de représentations de mots contextualisées d'AI2, antérieur à l'ère des transformers"
description: "Le modèle de représentations de mots contextualisées d'AI2, antérieur à l'ère des transformers"
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

ELMo, pour Embeddings from Language Models, est sorti de l'Allen Institute for AI et de l'Université de Washington en février 2018, décrit dans l'article « Deep Contextualized Word Representations » de Matthew Peters, Mark Neumann et leurs coauteurs. Au lieu d'attribuer à chaque mot un seul vecteur fixe, comme le faisaient des embeddings plus anciens tels que word2vec et GloVe, ELMo fait passer un LSTM bidirectionnel sur une phrase et produit pour chaque mot une représentation qui dépend du contexte autour. Le même mot reçoit donc un vecteur différent selon son usage. Entraîné sur environ un milliard de mots, il a amélioré les résultats sur six tâches de NLP de l'époque, dont la question-réponse et la reconnaissance d'entités nommées, une fois branché comme caractéristique dans des modèles existants. ELMo est antérieur à l'architecture transformer et a été largement dépassé par BERT et ses successeurs dans l'année qui a suivi sa sortie, mais on le cite encore comme l'un des modèles qui ont installé les représentations de mots contextualisées comme approche standard en NLP.
