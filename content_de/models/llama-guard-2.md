---
title: 'Llama Guard 2'
name: 'Llama Guard 2'
slug: 'llama-guard-2'
subtitle: 'Metas früheres Klassifizierungsmodell für Inhaltssicherheit, Vorgänger von Llama Guard 3'
description: 'Metas früheres Klassifizierungsmodell für Inhaltssicherheit, Vorgänger von Llama Guard 3'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-llama-3/'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [safety, open-weight, legacy]
i18n_source: '1ec3f0456e4e'
---
Llama Guard 2 ist ein Modell zur Klassifizierung der Inhaltssicherheit, das Meta im April 2024 zusammen mit Llama 3 veröffentlichte. Es basiert auf Llama 3 mit 8B Parametern und ist kein Chatmodell für allgemeine Zwecke. Es prüft sowohl Eingaben an ein Sprachmodell als auch dessen Ausgaben und kennzeichnet Inhalte aus elf Gefahrenkategorien der MLCommons-Taxonomie, darunter Gewalt, Hassrede und sexuelle Inhalte. Entwickler setzen es als Schutzschicht vor oder hinter ein anderes LLM in einer Pipeline ein, statt damit direkt Antworten zu generieren. Meta hat es inzwischen durch Llama Guard 3 ersetzt. Für Teams, die es bereits produktiv einsetzen, ist es weiterhin unter der Llama 3 Community License auf Hugging Face verfügbar.
