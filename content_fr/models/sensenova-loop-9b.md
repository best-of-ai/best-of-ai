---
title: 'SenseNova Loop-9B'
name: 'SenseNova Loop-9B'
slug: 'sensenova-loop-9b'
subtitle: "Le modèle multimodal de 9B à poids ouverts de SenseTime, qui réutilise ses couches en boucle"
description: "Le modèle multimodal de 9B à poids ouverts de SenseTime, qui réutilise ses couches en boucle"
company: 'sensetime'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.sensetime.com/en/news/sensenova-loop-9b-release-20261118-1435'
price: 'Free'
rank: 5
release_date: '2026-11-17'
param_count: '9B (about 14.6B inference-equivalent)'
context_window_tokens: 512000
modality: [text, image]
open_weight: true
license: 'Open weights'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-11-24'
tags: [llm, open-weight, multimodal, small-model, self-hosted]
i18n_source: '842af8c2e04b'
---

SenseNova Loop-9B est la version officielle du modèle multimodal à poids ouverts de SenseTime, publiée le 17 novembre 2026 après une préversion. Il compte environ 9B de paramètres répartis sur 32 couches de décodeur distinctes, qui s'exécutent comme 56 calculs de couche par passe, ce qui donne environ 14,6B de paramètres équivalents à l'inférence. Il accepte du texte et des images, produit du texte et gère jusqu'à 512 000 tokens de contexte.

Les poids en 4 bits font environ 4,9 GB, donc il tient sur du matériel grand public, et une version AWQ officielle est sortie le jour du lancement. SenseTime le dit comparable à Qwen3.8-27B : 41,36 contre 44,60 sur NL2Repo et 65,31 contre 65,01 sur AIDABench. Les poids sont sur Hugging Face sous sensenova/sensenova-loop, avec le code sur GitHub.
