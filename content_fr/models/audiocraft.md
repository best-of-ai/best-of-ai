---
title: 'AudioCraft'
name: 'AudioCraft'
slug: 'audiocraft'
subtitle: "Le framework open source de Meta, pour la musique et les effets sonores"
description: "Le framework open source de Meta, pour la musique et les effets sonores"
company: 'meta-ai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/audiocraft-musicgen-audiogen-encodec-generative-ai-audio/'
price: 'Free'
rank: 6
release_date: '2023-08-02'
param_count: '300M-3.3B (MusicGen), 1.5B (AudioGen)'
modality: [audio, text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['GitHub']
date: '2026-07-16'
tags: [audio, open-weight, music-generation]
i18n_source: '0ed2f655dea3'
---

AudioCraft est une bibliothèque de code que Meta a publiée en août 2023. Elle regroupe trois modèles audio génératifs : MusicGen pour la génération de musique à partir de texte, AudioGen pour les effets sonores d'ambiance, et EnCodec, le codec audio neuronal dont les deux autres se servent pour découper les formes d'onde en tokens. MusicGen existe en plusieurs tailles (300M, 1,5B et 3,3B de paramètres), avec des variantes qui peuvent aussi suivre une mélodie en plus d'un prompt texte, tandis qu'AudioGen est livré en modèle de 1,5B de paramètres, entraîné sur des effets sonores plutôt que sur de la musique. Meta a publié le code et les poids sous licence MIT, ce qui a fait d'AudioCraft l'une des premières boîtes à outils entièrement ouvertes pour la génération audio à partir de texte, à l'inverse de systèmes fermés comme ceux de Google. Les plus petits checkpoints tournent sur un seul GPU grand public, et la bibliothèque est devenue une base courante pour les projets open source de génération musicale et pour la recherche sur la synthèse audio que l'on peut diriger.
