---
title: 'AlphaCode 2'
name: 'AlphaCode 2'
slug: 'alphacode-2'
subtitle: "Le modèle de programmation compétitive de DeepMind, bâti sur Gemini, au niveau des meilleurs participants humains"
description: "Le modèle de programmation compétitive de DeepMind, bâti sur Gemini, au niveau des meilleurs participants humains"
company: 'google-deepmind'
model_type: 'Code'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/alphacode-2-technical-report/'
price: 'Paid'
rank: 6
release_date: '2023-12-06'
param_count: 'Undisclosed'
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [code, research]
i18n_source: 'd985a201f8f1'
---

AlphaCode 2 est le système de programmation compétitive de Google DeepMind, publié comme rapport technique en décembre 2023, en suite du premier AlphaCode. Ce n'est pas un seul modèle : c'est un pipeline construit sur des modèles Gemini ajustés par fine-tuning. Il échantillonne jusqu'à un million de solutions candidates en C++ par problème, puis les filtre par des contrôles sur des tests, un regroupement par comportement et un modèle de score appris, pour n'en garder qu'environ dix en soumission finale. Sur un ensemble de concours Codeforces récents, il a résolu 43 % des problèmes en dix essais, presque le double des 25 % du premier AlphaCode.

DeepMind estimait que ce niveau placerait AlphaCode 2 au 85e centile des participants humains sur Codeforces, entre les rangs « Expert » et « Candidate Master » de la plateforme. Le projet est resté de la recherche, sans produit ni API, et servait surtout à montrer combien un bon modèle de base, plus un échantillonnage massif et un filtrage, peut améliorer les résultats sur des problèmes de code difficiles et vérifiables. C'est un ancêtre direct des techniques de raisonnement et de génération de code ensuite reprises dans les travaux Gemini et AlphaProof de DeepMind.
