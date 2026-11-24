---
title: 'Gemini Decision 1'
name: 'Gemini Decision 1'
slug: 'gemini-decision-1'
subtitle: "Le modèle non génératif de Google qui note des options et renvoie un niveau de confiance plutôt que du texte"
description: "Le modèle non génératif de Google qui note des options et renvoie un niveau de confiance plutôt que du texte"
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/'
price: 'Paid'
rank: 6
release_date: '2026-11-11'
param_count: 'Undisclosed'
context_window_tokens: 256000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Gemini API', 'Google AI Studio']
date: '2026-11-24'
tags: [classification, decision-model, multimodal, api]
i18n_source: '1bbd28f7737a'
---

Gemini Decision 1 est un modèle derrière l'API Decisions de Google, lancée le 11 novembre 2026, qui n'écrit pas de texte. Il note des options en une seule passe avant et renvoie une probabilité et un niveau de confiance pour chacune. Il gère les questions oui/non, les choix multiples de 2 à 255 options et la notation ordonnée selon une grille, avec jusqu'à 1 000 questions dans une même requête. Les entrées peuvent être du texte, des images, de l'audio, de la vidéo et des PDF, jusqu'à 256 000 tokens.

Google annonce une latence de bout en bout de 150 à 250 millisecondes. Le tarif est de 0,10 $ par million de tokens d'entrée et rien pour la sortie, et AI Studio propose une offre sans frais pour le prototypage. Google dit qu'il est près de cinq fois moins cher que Gemini 3.5 Flash-Lite sur la même suite. L'ID du modèle est gemini-decision-1, et les intégrations arrivent sur OpenRouter, LangChain, Vercel et LiteLLM.
