---
title: 'Granite Vision'
name: 'Granite Vision'
slug: 'granite-vision'
subtitle: "Modèle vision-langage compact d'IBM pour la lecture de documents et de graphiques"
description: "Modèle vision-langage compact d'IBM pour la lecture de documents et de graphiques"
company: 'ibm'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2025-02-26'
param_count: '2B'
context_window_tokens: 16384
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, enterprise]
i18n_source: 'a32ea768a093'
---

Granite Vision est le modèle vision-langage compact d'IBM, sorti avec la mise à jour Granite 3.2 en février 2025 et conçu pour la compréhension de documents visuels, pas pour le chat général sur des images. Avec 2 milliards de paramètres, il lit des tableaux, des graphiques, des infographies, des tracés et des documents scannés, et les rend en texte structuré. Il vise des benchmarks comme DocVQA et ChartQA, où IBM dit qu'il égale des modèles ouverts plusieurs fois plus grands. Le petit format est voulu : IBM l'a conçu pour des charges d'entreprise courantes, comme lire des factures ou extraire des données de rapports, là où faire tourner un grand modèle multimodal n'est ni pratique ni abordable. Il prend en charge une fenêtre de contexte de 16K tokens, est à poids ouverts sous Apache 2.0, et se distribue via Hugging Face et IBM watsonx. Les versions suivantes (3.3 et les variantes vision de Granite 4.0) reprennent le même parti pris pour les documents.
