---
title: 'ELECTRA'
name: 'ELECTRA'
slug: 'electra'
subtitle: "L'approche de préentraînement de Google, plus économe en exemples, avec un objectif de détection de tokens remplacés"
description: "L'approche de préentraînement de Google, plus économe en exemples, avec un objectif de détection de tokens remplacés"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2003.10555'
price: 'Free'
rank: 6
release_date: '2020-03-23'
param_count: '335M'
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
i18n_source: 'f5cba0d29eb6'
---

ELECTRA est une méthode de préentraînement d'encodeurs de texte, présentée par des chercheurs de Google et de Stanford dans un article pour ICLR 2020, avec une famille de modèles préentraînés construits avec elle. Au lieu de l'objectif de modélisation de langage masqué de BERT, où le modèle prédit des mots cachés au hasard, ELECTRA entraîne un petit générateur à remplacer certains tokens par des alternatives plausibles, et un discriminateur à repérer quels tokens ont été échangés. Cet objectif de replaced token detection donne au modèle un signal d'apprentissage sur chaque token de la séquence, pas seulement sur les tokens masqués, ce qui rend le préentraînement bien plus économe en exemples.

La plus grande version publiée, ELECTRA-Large, compte 335 millions de paramètres et a atteint des scores GLUE compétitifs avec RoBERTa et XLNet, avec un quart de leur calcul de préentraînement. À budget de calcul égal, elle les a dépassés nettement. Google a publié le code et les poids sous licence Apache 2.0, et les variantes plus petites ELECTRA-Small et ELECTRA-Base sont devenues des choix courants pour les équipes qui voulaient la précision de BERT sans le coût d'entraînement de BERT.
