---
title: 'Fuyu-8B'
name: 'Fuyu-8B'
slug: 'fuyu-8b'
subtitle: 'Multimodales Open-Weight-Modell von Adept für die Wahrnehmung durch digitale Agenten.'
description: 'Multimodales Open-Weight-Modell von Adept für die Wahrnehmung durch digitale Agenten.'
company: 'adept-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.adept.ai/blog/fuyu-8b'
price: 'Free'
rank: 3
release_date: '2023-10-17'
param_count: '8B'
context_window_tokens: 16000
modality: [text, image]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, multimodal, open-weight, agentic]
i18n_source: 'f65d9839efe1'
---

Fuyu-8B ist ein multimodales Modell von Adept AI, veröffentlicht im Oktober 2023. Es wurde speziell für digitale Agenten entwickelt, die Bildschirme sehen und bedienen müssen, nicht als allgemeiner Chatbot. Adept nutzte eine vereinfachte Architektur: Bildausschnitte werden direkt in einen gewöhnlichen Transformer mit reinem Decoder eingespeist, ohne separaten Bildencoder. So kann das Modell Bilder in ihrer ursprünglichen Auflösung verarbeiten, statt alle auf eine feste Größe zu skalieren. Das ist für Adepts Anwendungsfall wichtig: UI-Elemente, Schaltflächen und Text müssen in nativer Auflösung erkannt werden, um Fragen zu Bildschirmfotos, Diagrammen und Grafiken zu beantworten und einzelne Elemente auf dem Bildschirm zu lokalisieren. Adept veröffentlichte das Modell mit acht Milliarden Parametern unter CC-BY-NC-Lizenz auf Hugging Face. Es darf kostenlos genutzt und verändert, aber nicht kommerziell eingesetzt werden. Fuyu-8B war als kleinere öffentliche Vorschau des Modells hinter Adepts eigenem Produkt gedacht, nicht als separates Angebot. Es unterstützt ein Kontextfenster von 16.000 Tokens. Nach der Übernahme von Adept wechselte 2024 ein großer Teil des Teams zu Amazon; Fuyu-8B bleibt eine Momentaufnahme dieser agentenorientierten Forschung.
