---
title: 'Chinchilla'
name: 'Chinchilla'
slug: 'chinchilla'
subtitle: 'Le modèle de recherche de DeepMind en 2022, qui a remis à plat les hypothèses des lois d''échelle pour l''entraînement des LLM'
description: 'Le modèle de recherche de DeepMind en 2022, qui a remis à plat les hypothèses des lois d''échelle pour l''entraînement des LLM'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/'
price: 'Paid'
rank: 4
release_date: '2022-03-29'
param_count: '70B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 67.5
access_methods: [Self-hosted]
runs_at_home: false
platforms: []
date: '2026-07-16'
tags: [llm, research, legacy]
i18n_source: '14414c05c298'
---

Chinchilla est un modèle de langage de recherche que DeepMind a décrit dans un article de mars 2022 sur l'entraînement à l'optimum de calcul. Avec 70 milliards de paramètres, il est bien plus petit que Gopher, le modèle précédent de DeepMind à 280 milliards de paramètres. Pourtant, entraîné sur environ quatre fois plus de données, Chinchilla a battu Gopher, GPT-3 et d'autres modèles plus grands de l'époque sur un large éventail de benchmarks, dont un score MMLU moyen d'environ 67,5 %. Le résultat central de l'article : la plupart des grands modèles de langage jusqu'alors étaient sous-entraînés par rapport à leur taille. Pour un budget de calcul fixe, la taille du modèle et les données d'entraînement doivent croître ensemble, pas seulement la taille du modèle.

Ce résultat, largement connu aujourd'hui comme la loi d'échelle de Chinchilla, a changé la façon dont les laboratoires planifiaient ensuite leurs entraînements. Le domaine s'est orienté vers des modèles plus petits, entraînés sur des jeux de données bien plus grands, au lieu de simplement augmenter le nombre de paramètres. DeepMind n'a jamais publié les poids de Chinchilla ni proposé d'accès public. Il n'existe que comme artefact de recherche décrit dans l'article. Son influence se voit indirectement dans presque tous les grands modèles entraînés depuis, de LLaMA à GPT-4, qui citent tous une mise à l'échelle optimale en calcul dans leur méthode d'entraînement.
