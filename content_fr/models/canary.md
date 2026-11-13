---
title: 'Canary'
name: 'Canary'
slug: 'canary'
subtitle: 'Le modèle multilingue de reconnaissance vocale et de traduction de NVIDIA'
description: 'Le modèle multilingue de reconnaissance vocale et de traduction de NVIDIA'
company: 'nvidia'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://huggingface.co/nvidia/canary-1b'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '1B'
modality: [audio, text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['NVIDIA NIM', 'Hugging Face']
date: '2026-07-16'
tags: [speech-recognition, open-weight, multilingual]
i18n_source: 'ad7707d7cc9a'
---

Canary est une famille de modèles de parole de l'équipe NeMo de NVIDIA. Le principal, Canary-1B, est sorti en avril 2024. Contrairement à un modèle ASR typique, qui ne fait que transcrire l'audio, Canary fait à la fois la reconnaissance vocale et la traduction de la parole pour l'anglais, le français, l'allemand et l'espagnol : il convertit l'audio parlé en texte dans la même langue, ou le traduit vers une autre. Il combine un encodeur FastConformer et un décodeur transformer, une architecture que NVIDIA a réglée pour tirer une bonne précision d'un modèle relativement petit. À sa sortie, il a pris la tête du classement Open ASR de Hugging Face, devant des concurrents plusieurs fois plus gros.

NVIDIA distribue Canary-1B via Hugging Face et son framework NeMo pour un usage auto-hébergé, et aussi via NVIDIA NIM comme API hébergée. Le Canary-1B d'origine est publié sous licence CC-BY-NC 4.0, ce qui le réserve à un usage non commercial. NVIDIA a depuis publié de nouvelles variantes, dont Canary-1B-Flash et Canary-1B-v2, sous la licence plus permissive CC-BY-4.0, avec une autorisation commerciale explicite et une inférence plus rapide.
