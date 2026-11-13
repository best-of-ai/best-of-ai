---
title: 'MiniMax M3'
name: 'MiniMax M3'
slug: 'minimax-m3'
subtitle: "Premier modèle à poids ouverts qui combine un code de niveau frontière, un contexte d'un million de tokens et une multimodalité native"
description: "Premier modèle à poids ouverts qui combine un code de niveau frontière, un contexte d'un million de tokens et une multimodalité native"
company: 'minimax-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.minimaxi.com/'
price: 'Free'
rank: 8
release_date: '2026-06-01'
param_count: '428B (23B active)'
context_window_tokens: 1000000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 1.2
api_available: true
lmarena_score: 1340
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, coding]
extra_model_types: ['Code']
i18n_source: 'b89f089ecadf'
---

MiniMax M3 est un modèle à mélange d'experts et à poids ouverts que MiniMax a publié en juin 2026, avec les poids sur Hugging Face dès le 7 juin. Il compte environ 428 milliards de paramètres au total, dont à peu près 23 milliards actifs par token, répartis sur 256 experts à grain fin. MiniMax le présente comme le premier modèle à poids ouverts qui associe une capacité de code de niveau frontière, une fenêtre de contexte d'un million de tokens et une entrée multimodale native, sur le texte, les images et la vidéo. Le labo annonce 59 % sur SWE-Bench Pro et 66 % sur Terminal-Bench 2.1, des benchmarks faits pour le code et les tâches d'agent qui durent, plutôt que pour des questions isolées.

Son architecture vise à garder l'inférence en long contexte peu coûteuse : MiniMax indique que le coût de calcul par token à 1 million de tokens n'est qu'une fraction de celui de la génération précédente, avec un préremplissage et un décodage tous les deux plusieurs fois plus rapides. Il sort sous Apache 2.0, au tarif de 0,30 $ par million de tokens d'entrée et 1,20 $ par million de tokens de sortie via l'API de MiniMax. Ça le place comme une alternative ouverte moins chère aux modèles de code fermés de niveau frontière, pour les développeurs qui construisent des agents de code autonomes et des outils qui travaillent sur de grandes bases de code.
