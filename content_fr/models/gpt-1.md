---
title: 'GPT-1'
name: 'GPT-1'
slug: 'gpt-1'
subtitle: "Le modèle d'article d'origine d'OpenAI en 2018, qui a introduit l'architecture GPT"
description: "Le modèle d'article d'origine d'OpenAI en 2018, qui a introduit l'architecture GPT"
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/language-unsupervised/'
price: 'Free'
rank: 5
release_date: '2018-06-11'
param_count: '117M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [llm, legacy, foundation-model]
i18n_source: '99d5a246579a'
---

GPT-1 est le premier Generative Pre-trained Transformer d'OpenAI, présenté dans un article de juin 2018 intitulé « Improving Language Understanding by Generative Pre-Training ». Il avait 117 millions de paramètres et a été entraîné sur BookCorpus, un ensemble de romans non publiés, avec une fenêtre de contexte de 512 tokens. L'idée de base était simple : préentraîner un Transformer sur du texte brut, sans étiquettes, puis faire le fine-tuning du même modèle sur des tâches précises, comme la réponse à des questions ou l'implication textuelle.

Cette approche a dépassé les architectures faites pour une tâche sur 9 des 12 benchmarks où OpenAI l'a testée, et c'était le vrai sujet de l'article. GPT-1 n'a jamais été un produit. C'était la preuve qu'un préentraînement génératif suivi d'un fine-tuning pouvait battre des modèles construits et entraînés à part pour chaque tâche. Ce résultat a fixé le schéma qu'OpenAI a ensuite agrandi, de GPT-2 à GPT-3 et à tout ce qui a suivi.
