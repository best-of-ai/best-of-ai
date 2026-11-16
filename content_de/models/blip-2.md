---
title: 'BLIP-2'
name: 'BLIP-2'
slug: 'blip-2'
subtitle: 'Effizienterer Nachfolger von BLIP von Salesforce, der das Vision-Language-Pretraining mit eingefrorenen Encodern startet'
description: 'Effizienterer Nachfolger von BLIP von Salesforce, der das Vision-Language-Pretraining mit eingefrorenen Encodern startet'
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/LAVIS/tree/main/projects/blip2'
price: 'Free'
rank: 6
release_date: '2023-01-30'
param_count: '3.7B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '8456e2d29321'
---
BLIP-2 ist ein Vision-Language-Modell, das Salesforce Research im Januar 2023 veröffentlichte. Es beruht auf einem besonderen Effizienztrick: Statt einen großen Bildencoder und ein Sprachmodell gemeinsam von Grund auf zu trainieren, bleiben beide vortrainierten Modelle eingefroren und nur ein leichter Verbinder namens Q-Former wird trainiert. Dieser Q-Former umfasst rund 188 Millionen trainierbare Parameter – weniger als zwei Prozent des Gesamtmodells. Dadurch ließ sich BLIP-2 viel günstiger trainieren als vergleichbare Vision-Language-Modelle seiner Zeit und erzielte dennoch gute Ergebnisse bei Bildbeschreibungen und visueller Fragebeantwortung. Salesforce veröffentlichte mehrere Varianten, die den Q-Former mit unterschiedlichen eingefrorenen Sprachmodellen kombinieren, darunter OPT-Versionen mit 2,7 und 6,7 Milliarden Parametern sowie Flan-T5-Versionen mit bis zu 11 Milliarden Parametern. So konnten Nutzer:innen Leistung und Rechenaufwand gegeneinander abwägen. Code und Gewichte stehen auf GitHub und Hugging Face unter der MIT-Lizenz als Teil von Salesforces LAVIS-Bibliothek bereit. Der populär gewordene Ansatz aus eingefrorenen Encodern und leichtem Verbinder beeinflusste spätere multimodale Modelle, die Bildverarbeitung ebenfalls an vorhandene Sprachmodelle anfügten, statt alles gemeinsam zu trainieren.
