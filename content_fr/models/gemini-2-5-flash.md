---
title: 'Gemini 2.5 Flash'
name: 'Gemini 2.5 Flash'
slug: 'gemini-2-5-flash'
subtitle: 'Le palier Gemini de Google, à faible latence et peu coûteux'
description: 'Le palier Gemini de Google, à faible latence et peu coûteux'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 7
release_date: '2025-04-17'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 84.0
humaneval_score: 82.0
lmarena_score: 1290
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, low-latency, multimodal, api]
i18n_source: 'd2ed515fd5c9'
---

Gemini 2.5 Flash est le palier économique de la génération 2.5 chez Google, sorti en préversion en avril 2025 et passé en disponibilité générale le mois suivant. C'est le premier modèle Flash conçu dès le départ avec une réflexion visible : il peut raisonner étape par étape avant de répondre, et les développeurs peuvent fixer un « thinking budget » pour arbitrer entre qualité de la réponse, latence et coût. Il prend du texte, de l'image et de l'audio en entrée, et a la même fenêtre d'un million de tokens que son frère Pro.

Google le tarife à 0,30 $ par million de tokens en entrée et 2,50 $ par million de tokens en sortie, les tokens de réflexion étant facturés au tarif de sortie, et propose une variante Flash-Lite encore plus dépouillée pour des charges plus simples et encore moins chères. Il tourne autour de 83 % au MMLU-Pro et se défend bien sur les benchmarks de programmation et de maths par rapport à son prix, ce qui en fait la recommandation par défaut de Google pour les applications à fort volume qui n'ont pas besoin de la profondeur de raisonnement de Pro.
