---
title: 'GPT-4o Realtime'
name: 'GPT-4o Realtime'
slug: 'gpt-4o-realtime'
subtitle: "Variante parole vers parole de GPT-4o, à faible latence, pour la voix en direct"
description: "Variante parole vers parole de GPT-4o, à faible latence, pour la voix en direct"
company: 'openai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://openai.com/index/introducing-the-realtime-api/'
price: 'Paid'
rank: 7
release_date: '2024-10-01'
param_count: 'Undisclosed'
context_window_tokens: 32000
modality: [audio, text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 5
output_price_usd_per_m: 20
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['API', 'ChatGPT Advanced Voice']
date: '2026-07-16'
tags: [voice, multimodal, api, real-time]
i18n_source: '507fc668616b'
---

GPT-4o Realtime est une variante parole vers parole de GPT-4o qu'OpenAI a présentée via sa Realtime API le 1er octobre 2024. Au lieu du pipeline habituel, qui transcrit l'audio en texte, le passe dans un modèle de langage, puis resynthétise la parole, il traite l'audio de bout en bout, en natif, sur une connexion WebSocket ou WebRTC. Ça réduit le délai qui rendait les bots vocaux précédents peu naturels. Il fait tourner l'Advanced Voice Mode de ChatGPT et permet de construire des agents téléphoniques, des assistants vocaux et des outils de traduction en direct qui répondent en moins d'une seconde. Le modèle a une fenêtre de contexte de 32 000 tokens et facture 5 $ par million de tokens texte d'entrée et 20 $ par million de tokens texte de sortie, avec des tarifs à part, plus élevés, pour les tokens audio. Il concurrence l'API Gemini Live de Google et plusieurs startups vocales qui empilent une transcription de classe Whisper et un modèle de langage. Ce qui le distingue, c'est l'architecture à un seul modèle et à faible latence, plutôt qu'un pipeline recollé.
