---
title: 'Qwen3.8-27B'
name: 'Qwen3.8-27B'
slug: 'qwen3-8-27b'
subtitle: "Le modèle multimodal à poids ouverts d'Alibaba, taillé pour tourner sur un seul GPU local"
description: "Le modèle multimodal à poids ouverts d'Alibaba, taillé pour tourner sur un seul GPU local"
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-14'
param_count: '27B'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-08-17'
tags: [llm, open-weight, multimodal, single-gpu, apache-2.0, local]
i18n_source: '1e091b27bdc3'
---

L'équipe Qwen d'Alibaba a sorti Qwen3.8-27B le 14 août 2026, avec des poids ouverts tout de suite sous licence Apache 2.0. C'est un modèle dense de 27 milliards de paramètres, pas un mélange d'experts, et il traite le texte, les images et la vidéo, y compris les schémas, les documents et des séquences de plusieurs heures. Le contexte va jusqu'à 262 000 tokens en natif, et peut monter à un million avec la méthode de mise à l'échelle YaRN. Alibaba dit qu'il dépasse le plus gros Qwen3.7-Plus sur le code et les tâches de bureau, et qu'il a affiné sa planification agentique, de quoi finir des tâches en plusieurs étapes avec moins de supervision.

La sortie visait les développeurs qui veulent un modèle capable sur un seul GPU grand public ou de station de travail, plutôt que sur un cluster de datacenter, face à des sorties du même genre, pensées d'abord pour le local, chez Meta et Google. Alibaba a joint au lancement les poids ouverts de Qwen3.8-2.4T-A95B, le modèle de classe Max de la même génération, pour laisser le choix entre cette version légère et un modèle d'échelle frontier prévu pour des charges agentiques plus lourdes.
