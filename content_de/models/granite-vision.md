---
title: 'Granite Vision'
name: 'Granite Vision'
slug: 'granite-vision'
subtitle: 'IBMs kompaktes Vision-Language-Modell zum Verständnis von Dokumenten und Diagrammen'
description: 'IBMs kompaktes Vision-Language-Modell zum Verständnis von Dokumenten und Diagrammen'
company: 'ibm'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2025-02-26'
param_count: '2B'
context_window_tokens: 16384
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, enterprise]
i18n_source: 'a32ea768a093'
---
Granite Vision ist das kompakte Vision-Language-Modell von IBM. Es erschien im Februar 2025 als Teil des Granite-3.2-Updates und wurde speziell für das visuelle Verständnis von Dokumenten statt für allgemeine Bilddialoge entwickelt. Mit zwei Milliarden Parametern liest es Tabellen, Diagramme, Infografiken, Plots und gescannte Dokumente und wandelt sie in strukturierte Texte um. Es richtet sich an Benchmarks wie DocVQA und ChartQA, bei denen es laut IBM mit offenen Modellen konkurriert, die ein Vielfaches seiner Größe haben. Der geringe Ressourcenbedarf ist beabsichtigt: IBM entwickelte das Modell für alltägliche Unternehmensaufgaben wie das Auslesen von Rechnungen oder die Datenextraktion aus Berichten, bei denen ein großes multimodales Modell unpraktisch oder zu teuer wäre. Es unterstützt ein Kontextfenster von 16K Tokens, steht unter Apache 2.0 mit offenen Gewichten und ist über Hugging Face und IBM watsonx verfügbar. Spätere Versionen (3.3 sowie die Vision-Varianten von Granite 4.0) bauen auf demselben dokumentenorientierten Entwurf auf.
