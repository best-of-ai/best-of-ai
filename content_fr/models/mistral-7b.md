---
title: 'Mistral 7B'
name: 'Mistral 7B'
slug: 'mistral-7b'
subtitle: "Le premier modèle compact à poids ouverts de Mistral, qui a dépassé des rivaux plus gros"
description: "Le premier modèle compact à poids ouverts de Mistral, qui a dépassé des rivaux plus gros"
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/announcing-mistral-7b/'
price: 'Free'
rank: 6
release_date: '2023-09-27'
param_count: '7B'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 60.1
humaneval_score: 30.5
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
extra_model_types: ['Code']
i18n_source: 'c7cb93d8e531'
---

Mistral 7B est le modèle qui a fait connaître Mistral AI. Il est sorti le 27 septembre 2023, premier modèle public de la startup française. À 7 milliards de paramètres, il était assez petit pour tourner sur un seul GPU grand public, et il a pourtant battu Llama 2 13B sur chaque benchmark testé par Mistral, et même dépassé Llama 2 34B sur plusieurs tâches de raisonnement et de code, avec 60,1 % au MMLU et 30,5 % sur HumanEval. Il utilise la grouped-query attention et la sliding-window attention pour garder une inférence rapide et économe en mémoire, sur une fenêtre de contexte de 32 000 tokens.

Mistral l'a publié sous licence Apache 2.0, sans restriction d'usage, ce qui était rare pour un modèle de cette qualité à l'époque et l'a aidé à se répandre vite dans la communauté open source, via Hugging Face et des outils comme Ollama et llama.cpp. Il est devenu une base courante pour des fine-tunes et des fusions, et ce succès a installé Mistral AI comme un concurrent sérieux de Meta et d'OpenAI, quelques mois après la création de l'entreprise.
