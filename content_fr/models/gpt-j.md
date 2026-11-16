---
title: 'GPT-J'
name: 'GPT-J'
slug: 'gpt-j'
subtitle: "Un des premiers modèles à poids ouverts de style GPT-3, par EleutherAI"
description: "Un des premiers modèles à poids ouverts de style GPT-3, par EleutherAI"
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 3
release_date: '2021-06-04'
param_count: '6B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '3c03d602f92a'
---

GPT-J est un modèle de langage de 6 milliards de paramètres qu'EleutherAI a publié le 9 juin 2021. C'était l'une des premières réplications ouvertes crédibles de l'architecture de GPT-3, à une époque où OpenAI gardait GPT-3 derrière une API payante. Il a été entraîné sur the Pile, le jeu de données texte de 825 GB d'EleutherAI, avec la bibliothèque Mesh Transformer JAX, pour paralléliser l'entraînement sur des pods de TPU plutôt que sur des GPU. Avec 28 couches et une fenêtre de contexte de 2 048 tokens, il était nettement plus petit que la plus grande configuration de GPT-3, mais il gérait assez bien la génération de texte, les questions-réponses et la complétion de code pour devenir une base de référence courante en recherche NLP open source. Il est sorti sous licence Apache 2.0 : on pouvait le télécharger, faire du fine-tuning et le déployer sans les restrictions d'usage d'OpenAI, ce qui en a fait une base fréquente des premiers chatbots ouverts. GPT-J a depuis été dépassé par GPT-NeoX-20B et par des modèles ouverts plus tardifs, mais il reste souvent cité pour la façon dont la communauté open source a rattrapé les labos fermés pendant l'ère GPT-3.
