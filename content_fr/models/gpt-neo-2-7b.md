---
title: 'GPT-Neo 2.7B'
name: 'GPT-Neo 2.7B'
slug: 'gpt-neo-2-7b'
subtitle: "Le premier modèle ouvert de style GPT-3 d'EleutherAI, avant GPT-J et GPT-NeoX"
description: "Le premier modèle ouvert de style GPT-3 d'EleutherAI, avant GPT-J et GPT-NeoX"
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/EleutherAI/gpt-neo-2.7B'
price: 'Free'
rank: 4
release_date: '2021-03-21'
param_count: '2.7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: '8f6eeabfc72f'
---

GPT-Neo 2.7B est le modèle de langage de 2,7 milliards de paramètres d'EleutherAI, sorti le 21 mars 2021, avec des versions plus petites de 125M et 1,3B, comme premiers modèles publics du groupe. Il reprend l'architecture de GPT-3 avec la bibliothèque mesh-tensorflow, et a été entraîné sur the Pile pendant environ 420 milliards de tokens. La fenêtre de contexte est de 2 048 tokens, et la génération de texte général est comparable aux plus petits paliers GPT-3 d'OpenAI à l'époque. EleutherAI l'a publié sous licence Apache 2.0 justement parce qu'OpenAI n'avait pas rendu GPT-3 téléchargeable. Chercheurs et amateurs s'en sont servis pour tout, des chatbots aux outils d'écriture, dans les mois avant l'arrivée de GPT-J et de GPT-NeoX-20B, plus gros. Il précède ces deux sorties et n'a plus surtout qu'un intérêt historique. Il tourne encore sans peine sur un seul GPU grand public, ce qui l'a gardé en usage dans des projets aux ressources limitées, bien après l'arrivée de modèles ouverts plus grands.
