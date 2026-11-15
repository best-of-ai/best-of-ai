---
title: 'MiniCPM'
name: 'MiniCPM'
slug: 'minicpm'
subtitle: 'Das effiziente kleine Modell von OpenBMB, ausgelegt für Smartphones und Edge-Geräte'
description: 'Das effiziente kleine Modell von OpenBMB, ausgelegt für Smartphones und Edge-Geräte'
company: 'openbmb'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM'
price: 'Free'
rank: 5
release_date: '2024-02-01'
param_count: '2.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, on-device]
i18n_source: '0dcdb45ddc3c'
---
MiniCPM ist ein Sprachmodell mit 2,4 Milliarden Parametern, das OpenBMB im Februar 2024 veröffentlichte. Es wurde für den Betrieb auf Smartphones und anderen Edge-Geräten entwickelt, auf denen ein vollwertiges Modell mit 7B oder 13B Parametern zu schwer wäre. Trotz seiner geringen Größe erreicht es laut OpenBMB bei allgemeinen Benchmarks nahezu Mistral 7B und übertrifft größere Modelle wie Llama 2 13B und Falcon 40B bei mehreren Aufgaben, insbesondere beim Verständnis chinesischer Sprache, bei Mathematik und Programmierung. Eine separate Langkontextvariante, MiniCPM-2B-128k, erweitert das Kontextfenster für dokumentenintensive Anwendungen auf 128.000 Tokens.

Das Modell steht unter Apache 2.0 mit offenen Gewichten auf Hugging Face bereit. Es richtet sich an Entwickler, die Offline- oder kostengünstige Anwendungen mit knappen Speicher- und Rechenbudgets erstellen möchten. Es bildete die Grundlage für die späteren multimodalen MiniCPM-V-Modelle von OpenBMB und prägte den Fokus des Labors auf effiziente KI direkt auf dem Gerät als Alternative zur immer weiteren Skalierung.
