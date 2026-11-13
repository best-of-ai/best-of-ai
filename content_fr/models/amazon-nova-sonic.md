---
title: 'Amazon Nova Sonic'
name: 'Amazon Nova Sonic'
slug: 'amazon-nova-sonic'
subtitle: "Le modèle parole vers parole d'Amazon, pour des agents vocaux conversationnels en temps réel"
description: "Le modèle parole vers parole d'Amazon, pour des agents vocaux conversationnels en temps réel"
company: 'amazon'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/speech/'
price: 'Freemium'
rank: 6
release_date: '2025-04-08'
param_count: 'Undisclosed'
context_window_tokens: 300000
modality: [audio, text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [voice, audio, api, real-time]
i18n_source: '1cbaa750f79c'
---

Amazon Nova Sonic est un modèle parole vers parole qu'Amazon a annoncé en avril 2025. Il réunit la compréhension et la génération de la parole dans un seul modèle, au lieu d'enchaîner des systèmes séparés de speech-to-text, de langage et de text-to-speech. On y accède par une API de streaming bidirectionnel sur Amazon Bedrock. Il prend en charge une fenêtre de contexte de 300 000 tokens, et il est fait pour des agents vocaux en temps réel qui doivent écouter, raisonner et répondre avec une parole au son naturel et une faible latence. L'appel d'outils et l'ancrage sur des connaissances sont aussi pris en charge : un agent vocal bâti sur Sonic peut appeler des fonctions externes ou aller chercher une information au milieu de la conversation.

Amazon a présenté Sonic comme une alternative moins coûteuse à l'assemblage de pipelines ASR, LLM et TTS séparés, et comme un concurrent de l'API Realtime d'OpenAI et des modèles audio natifs de Google, pour les assistants vocaux et les bots de service client. Amazon a ensuite sorti Nova 2 Sonic, avec davantage de langues et une fenêtre de contexte plus large, mais le Sonic d'origine reste disponible sur Bedrock pour les charges d'agents vocaux déjà en place.
