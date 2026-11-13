---
title: 'Mathstral'
name: 'Mathstral'
slug: 'mathstral'
subtitle: "Modèle de Mistral spécialisé en maths, dérivé de Mistral 7B"
description: "Modèle de Mistral spécialisé en maths, dérivé de Mistral 7B"
company: 'mistral-ai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://mistral.ai/news/mathstral/'
price: 'Free'
rank: 5
release_date: '2024-07-16'
param_count: '7B'
context_window_tokens: 32768
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [reasoning, math, open-weight]
i18n_source: '9a59b8ca351d'
---

Mathstral est un modèle de 7 milliards de paramètres que Mistral AI a sorti en juillet 2024, construit sur la base Mistral 7B et ajusté spécifiquement pour le raisonnement en maths et en STEM. Il est issu d'une collaboration avec Project Numina, un groupe centré sur l'avancée des modèles de maths ouverts, et il est sorti en même temps que Codestral Mamba, comme l'un des deux modèles « miniatures » spécialisés de cette semaine-là. Sur le benchmark MATH, il obtient 56,6 %, et près de 69 % avec un vote majoritaire sur plusieurs échantillons, et il atteint 63,5 % au MMLU, ce qui le place devant la plupart des autres modèles de la classe 7B sur les tâches de raisonnement quantitatif.

Mistral a publié Mathstral sous licence Apache 2.0, donc on peut le télécharger, l'ajuster par fine-tuning et le faire tourner en local sans restriction. Il vise les chercheurs et les développeurs qui ont besoin d'un petit modèle auto-hébergeable pour des problèmes de maths en plusieurs étapes, des applications de tutorat, ou comme base pour un fine-tuning supplémentaire, plutôt que pour le chat généraliste.
