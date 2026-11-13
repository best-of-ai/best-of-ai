---
title: 'Gopher'
name: 'Gopher'
slug: 'gopher'
subtitle: "Le modèle de recherche de DeepMind à 280 milliards de paramètres, qui a nourri les lois d'échelle de Chinchilla"
description: "Le modèle de recherche de DeepMind à 280 milliards de paramètres, qui a nourri les lois d'échelle de Chinchilla"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/'
price: 'Paid'
rank: 6
release_date: '2021-12-08'
param_count: '280B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 60.0
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
i18n_source: 'adb1e7eb1bf4'
---

Gopher est un modèle de langage de 280 milliards de paramètres que DeepMind a entraîné et décrit dans un article de décembre 2021, au sein d'une étude sur la façon dont la performance évolue avec la taille. Il a été entraîné sur MassiveText, un corpus de 10,5 téraoctets, et évalué à côté de cinq modèles plus petits, de 44 millions à 7 milliards de paramètres, pour voir comment la capacité progressait avec l'échelle. Sur le benchmark MMLU, Gopher a obtenu 60 % en five-shot, un saut net par rapport aux modèles antérieurs de l'époque.

DeepMind n'a jamais publié Gopher, ni au public ni via une API : il servait uniquement de modèle de recherche. Ce qui en reste surtout vient de l'analyse suivante, publiée comme l'article Chinchilla, qui s'est appuyée sur Gopher et ses modèles frères pour montrer que la plupart des grands modèles de langage de cette période étaient sous-entraînés par rapport à leur nombre de paramètres. Ce résultat a, pendant des années, changé la façon dont les labos répartissaient le calcul entre la taille du modèle et les données d'entraînement.
