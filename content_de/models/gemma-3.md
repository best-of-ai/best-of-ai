---
title: 'Gemma 3'
name: 'Gemma 3'
slug: 'gemma-3'
subtitle: 'Modellfamilie von Google mit offenen Gewichten, entwickelt auf Grundlage der Gemini-Forschung'
description: 'Modellfamilie von Google mit offenen Gewichten, entwickelt auf Grundlage der Gemini-Forschung'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 7
release_date: '2025-03-12'
param_count: '27B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 78.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
i18n_source: '053632cde4ac'
---

Gemma 3 ist die dritte Generation offener Google-Modelle und basiert auf Forschung und Technologie des Gemini-2.0-Projekts. Es gibt vier Größen: 1B, 4B, 12B und 27B Parameter, jeweils als Basis- und instruktionsoptimierter Checkpoint. Die Modelle mit 4B, 12B und 27B Parametern verarbeiten Text und Bilder; das 1B-Modell nur Text. Alle Größen unterstützen mehr als 140 Sprachen, darunter mehr als 35 mit guter sofortiger Unterstützung. Die größeren Modelle haben ein Kontextfenster von 128.000 Tokens – deutlich mehr als Gemma 2 mit 8.192.

Google positioniert Gemma 3 als klein genug für einen einzelnen GPU- oder TPU-Host und zugleich konkurrenzfähig mit deutlich größeren geschlossenen Modellen bei Standardbenchmarks. Die 27B-Variante übertrifft Berichten zufolge Gemini 1.5 Pro in mehreren Tests; unabhängige Bewertungen setzen sie deutlich vor Gemma 2 27B. Da die Gewichte unter der Gemma-Lizenz heruntergeladen werden können, nutzen Entwickler:innen das Modell lokal, zur Feinabstimmung und für Edge-Anwendungen, bei denen Daten nicht an eine gehostete API gesendet werden können.
