---
title: 'BLOOMZ'
name: 'BLOOMZ'
slug: 'bloomz'
subtitle: 'Une variante de BLOOM ajustée sur des instructions, entraînée à en suivre d''une langue à l''autre'
description: 'Une variante de BLOOM ajustée sur des instructions, entraînée à en suivre d''une langue à l''autre'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/bigscience/bloomz'
price: 'Free'
rank: 5
release_date: '2022-11-03'
param_count: '176B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'RAIL License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual, legacy]
i18n_source: '9dff7db95770'
---

BLOOMZ est la version de BLOOM ajustée sur des instructions par BigScience, publiée fin 2022 par fine-tuning du modèle de base à 176 milliards de paramètres sur xP3, un grand ensemble de tâches multilingues formulées comme des instructions en langage naturel. Le but était la généralisation d'une langue à l'autre : BLOOMZ a surtout été ajusté sur des instructions en anglais, mais il suivait des consignes dans des langues qu'il n'avait jamais vues associées à des instructions pendant le fine-tuning, pourvu que cette langue soit apparue dans le préentraînement d'origine de BLOOM. C'était l'une des premières démonstrations publiques que le suivi d'instructions se transfère d'une langue à l'autre, sans ajustement séparé pour chacune.

Comme BLOOM, BLOOMZ garde la fenêtre de contexte de 2 048 tokens et l'architecture transformer dense du modèle de base, et il sort sous la même licence RAIL, qui autorise un large usage avec une liste d'applications interdites. Il intéresse aujourd'hui surtout les chercheurs qui étudient l'ajustement multilingue sur des instructions, plutôt que comme modèle de chat en production. Des modèles ouverts plus récents, eux aussi ajustés sur des instructions, offrent une meilleure qualité et des fenêtres de contexte bien plus grandes, pour un coût de calcul similaire ou plus bas.
