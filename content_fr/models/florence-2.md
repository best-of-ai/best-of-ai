---
title: 'Florence-2'
name: 'Florence-2'
slug: 'florence-2'
subtitle: 'Le modèle de fondation visuel compact de Microsoft, pour les légendes, la détection et la segmentation en un seul modèle'
description: 'Le modèle de fondation visuel compact de Microsoft, pour les légendes, la détection et la segmentation en un seul modèle'
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.microsoft.com/en-us/research/publication/florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks/'
price: 'Free'
rank: 6
release_date: '2024-06-15'
param_count: '0.77B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Azure AI Foundry']
date: '2026-07-16'
tags: [computer-vision, open-weight, multimodal]
i18n_source: '9791d240cd8e'
---

Florence-2 est un modèle de fondation pour la vision, publié par Microsoft Research en juin 2024, conçu pour les légendes, la détection d'objets, la segmentation et l'ancrage visuel dans un seul modèle, au lieu d'un modèle distinct par tâche. Il fonctionne par prompt : le même réseau peut produire une légende, un ensemble de boîtes englobantes ou un masque de segmentation selon l'instruction textuelle qu'on lui donne, avec une architecture séquence vers séquence unifiée. Microsoft l'a publié en deux tailles, une base à 230 millions de paramètres et une version large à 770 millions, toutes deux minuscules à côté des modèles vision-langage habituels. Il a été entraîné sur FLD-5B, un jeu de données interne de Microsoft d'environ 126 millions d'images et 5,4 milliards d'annotations, ce qui permet à un modèle aussi petit d'égaler ou de dépasser des modèles spécialisés plus grands sur des tâches comme les légendes COCO et la compréhension d'expressions référentielles. Microsoft a publié les poids sous licence MIT sur Hugging Face et le propose aussi via Azure AI Foundry, ce qui en fait un choix courant pour les équipes qui veulent de la vision sans faire tourner un grand LLM multimodal.
