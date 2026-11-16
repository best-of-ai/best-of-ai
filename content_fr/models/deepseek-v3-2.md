---
title: 'DeepSeek V3.2'
name: 'DeepSeek V3.2'
slug: 'deepseek-v3-2'
subtitle: "La mise à jour de V3.1 par DeepSeek, construite autour d'un nouveau mécanisme d'attention sparse"
description: "La mise à jour de V3.1 par DeepSeek, construite autour d'un nouveau mécanisme d'attention sparse"
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-12-01'
param_count: '685B (MoE)'
context_window_tokens: 163840
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.21
output_price_usd_per_m: 0.32
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'd6a4a3b7b4f4'
---

DeepSeek V3.2 est la mise à jour de V3.1 par DeepSeek, détaillée publiquement le 1er décembre 2025 après une preview expérimentale en septembre. Elle introduit la DeepSeek Sparse Attention, un mécanisme d'attention sparse à grain fin qui réduit le coût d'entraînement et d'inférence tout en gardant la qualité sur les tâches à long contexte. La variante phare Speciale compte environ 685 milliards de paramètres en mélange d'experts. La fenêtre de contexte est de 163 840 tokens, avec jusqu'à 64 000 tokens en sortie, et DeepSeek annonce des résultats de niveau médaille d'or sur les sujets 2025 de l'Olympiade internationale de mathématiques et de l'Olympiade internationale d'informatique. Le tarif de l'API tourne autour de 0,21 $ par million de tokens en entrée et 0,32 $ par million de tokens en sortie, environ la moitié du coût de V3.1-Terminus, surtout pour le décodage en long contexte. Comme le reste de la gamme DeepSeek, il sort sous licence MIT avec les poids sur Hugging Face, et il a servi de base à V4-Pro au printemps suivant.
