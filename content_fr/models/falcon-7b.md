---
title: 'Falcon 7B'
name: 'Falcon 7B'
slug: 'falcon-7b'
subtitle: "Le palier compact de Falcon chez TII, qui a aidé à faire connaître la sortie d'origine"
description: "Le palier compact de Falcon chez TII, qui a aidé à faire connaître la sortie d'origine"
company: 'technology-innovation-institute'
model_type: 'Language'
logo_url: ''
product_url: 'https://falconllm.tii.ae/'
price: 'Free'
rank: 5
release_date: '2023-05-25'
param_count: '7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, legacy]
i18n_source: '61f475ea6988'
---

Falcon 7B est le petit frère de la sortie Falcon d'origine de TII, entraîné sur le même jeu de données RefinedWeb que Falcon 40B, mais dimensionné pour un déploiement moins cher sur un seul GPU. TII l'a entraîné pendant environ deux semaines début 2023 et l'a publié sous la licence permissive Apache 2.0, ce qui permettait de l'utiliser, de le modifier et de le déployer commercialement sans redevances. Ce choix de licence se remarquait à l'époque, car beaucoup de modèles ouverts comparables restaient limités à la recherche. Falcon 7B reprend l'architecture transformer décodeur seul du modèle 40B, avec attention multiquery, mais avec une fenêtre de contexte de 2 048 tokens et moins de calcul, ce qui en a fait un choix courant pour des expériences de fine-tuning et des usages sur l'appareil en 2023 et début 2024. TII est depuis passé aux familles Falcon 3 et Falcon Mamba, et Falcon 7B reste un modèle ancien, encore largement recopié sur Hugging Face.
