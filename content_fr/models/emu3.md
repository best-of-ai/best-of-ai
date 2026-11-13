---
title: 'Emu3'
name: 'Emu3'
slug: 'emu3'
subtitle: "Le modèle de prédiction du token suivant de BAAI, qui unifie génération et compréhension de texte, d'image et de vidéo"
description: "Le modèle de prédiction du token suivant de BAAI, qui unifie génération et compréhension de texte, d'image et de vidéo"
company: 'baai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://baai-agents.github.io/Emu3/'
price: 'Free'
rank: 5
release_date: '2024-09-27'
param_count: '8B'
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, research]
extra_model_types: ['Image Generation']
i18n_source: '6fd97391d2f7'
---

Emu3 est un modèle multimodal à poids ouverts de la Beijing Academy of Artificial Intelligence, publié en septembre 2024, construit autour d'une seule idée : traiter le texte, les images et la vidéo comme des séquences de tokens discrets, et entraîner un seul transformer à prédire le token suivant sur les trois, sans composant de diffusion ni composant de type CLIP à part. BAAI l'a publié comme modèle de 8 milliards de paramètres en variantes Chat et Gen, l'une ajustée pour la compréhension vision-langage, l'autre pour la génération. Malgré cette conception simplifiée à un seul objectif, BAAI a indiqué qu'Emu3 dépassait des modèles ouverts spécialisés établis de l'époque, dont SDXL pour la génération d'images et LLaVA-1.6 pour la compréhension vision-langage. Le projet précède le plus grand modèle Emu3.5 de BAAI, publié fin 2025, qui pousse la même approche de prédiction du token suivant jusqu'à 34 milliards de paramètres.
