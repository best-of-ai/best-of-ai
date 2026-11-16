---
title: 'Gemini Nano'
name: 'Gemini Nano'
slug: 'gemini-nano'
subtitle: "Le palier Gemini sur appareil de Google, intégré à Pixel et à Android"
description: "Le palier Gemini sur appareil de Google, intégré à Pixel et à Android"
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 4
release_date: '2023-12-06'
param_count: '3.25B'
context_window_tokens: 8192
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Android', 'Chrome']
date: '2026-07-16'
tags: [llm, on-device, small-model]
i18n_source: '6991c4c972f9'
---

Gemini Nano est le plus petit palier de la famille Gemini de Google, conçu pour tourner entièrement sur un téléphone plutôt que d'appeler un serveur. Google l'a annoncé avec Gemini Pro et Ultra le 6 décembre 2023, et l'a d'abord livré sur le Pixel 8 Pro, où il fait tourner des fonctions sur l'appareil comme Smart Reply dans les apps de messagerie, le résumé d'appels et les résumés de l'app Recorder. Il existe en quelques tailles, environ 1,8 milliard et 3,25 milliards de paramètres, quantifié pour tenir dans les limites de mémoire et de NPU d'un téléphone, et il fonctionne entièrement hors ligne, sans que les données quittent l'appareil.

Comme il tourne en local, Nano échange de la capacité brute contre de la vitesse, de la confidentialité et un coût marginal nul par requête, et sa fenêtre de contexte utilisable est bien plus petite que celle des modèles côté serveur de Google. Depuis le lancement, Google a étendu le support à d'autres Pixel et, par des partenariats, aux Samsung Galaxy. Il expose Nano aux développeurs Android tiers via le système AICore et les API ML Kit GenAI, et non par une API cloud publique.
