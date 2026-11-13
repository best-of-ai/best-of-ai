---
title: 'Gato'
name: 'Gato'
slug: 'gato'
subtitle: "L'agent généraliste unique de DeepMind, entraîné sur le texte, les images et le contrôle robotique"
description: "L'agent généraliste unique de DeepMind, entraîné sur le texte, les images et le contrôle robotique"
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/a-generalist-agent/'
price: 'Paid'
rank: 5
release_date: '2022-05-12'
param_count: '1.18B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, generalist-agent]
i18n_source: '7358d84afc22'
---

Gato est un seul réseau de neurones, présenté par DeepMind en mai 2022, dont le même jeu de poids peut traiter plus de 600 tâches : jouer à des jeux Atari, légender des images, tenir une conversation en texte et commander un vrai bras robot pour empiler des blocs. Au lieu d'entraîner un modèle distinct par tâche, DeepMind a sérialisé chaque entrée, qu'il s'agisse de texte, d'images, de couples articulaires ou de pressions de boutons, en une seule séquence plate de tokens, et a entraîné un seul transformer sur tout cela d'un coup, avec une architecture proche d'un grand modèle de langage, mais où les tokens représentent aussi des actions et des données de capteurs, pas seulement des mots.

Avec 1,18 milliard de paramètres, Gato est minuscule à côté des 175 milliards de GPT-3, et sur une tâche donnée il reste derrière les spécialistes conçus seulement pour elle. Ce qui comptait, c'était de montrer qu'un seul réseau pouvait faire un travail correct sur des modalités et des problèmes de commande aussi différents. DeepMind le décrivait comme une étape de recherche vers des agents plus généralistes, pas comme un produit, et Gato n'a jamais été publié ni proposé via une API.
