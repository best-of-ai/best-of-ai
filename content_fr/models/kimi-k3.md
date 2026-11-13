---
title: 'Kimi K3'
name: 'Kimi K3'
slug: 'kimi-k3'
subtitle: "Modèle à poids ouverts de 2,8 billions de paramètres de Moonshot, le plus grand modèle ouvert livré à ce jour"
description: "Modèle à poids ouverts de 2,8 billions de paramètres de Moonshot, le plus grand modèle ouvert livré à ce jour"
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-07-16'
param_count: '2.8T (MoE)'
context_window_tokens: 1000000
modality: [text, image, video]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 3
output_price_usd_per_m: 15
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-08-09'
tags: [llm, open-weight, multimodal, reasoning, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: 'bf5cebe9bf5c'
---

Kimi K3 est la plus grande sortie de Moonshot AI à ce jour, un mélange d'experts de 2,8 billions de paramètres que l'entreprise présente comme le plus grand modèle à poids ouverts livré par qui que ce soit jusqu'ici. Il lit le texte, les images et la vidéo nativement, porte une fenêtre de contexte d'un million de tokens, et tourne dans un mode thinking toujours actif, sans voie rapide séparée. Moonshot a tarifé l'accès API à 3 $ par million de tokens d'entrée (0,30 $ en cas de cache hit) et 15 $ par million de tokens de sortie, bien en dessous des grands modèles fermés des labos occidentaux. Les poids complets sont arrivés sur Hugging Face peu après l'annonce du 16 juillet, en quantification MXFP4, ce qui ramène le téléchargement à environ 1,4 TB, assez petit pour qu'une installation d'auto-hébergement sérieuse tourne sans cluster dédié.
