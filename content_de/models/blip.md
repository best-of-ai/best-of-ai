---
title: 'BLIP'
name: 'BLIP'
slug: 'blip'
subtitle: 'Vision-Language-Pretraining-Modell von Salesforce für Bildbeschreibungen und Informationsabruf'
description: 'Vision-Language-Pretraining-Modell von Salesforce für Bildbeschreibungen und Informationsabruf'
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/BLIP'
price: 'Free'
rank: 6
release_date: '2022-01-28'
param_count: '223M'
modality: [text, image]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy]
i18n_source: '0a995979513f'
---
BLIP (Bootstrapping Language-Image Pre-training) ist ein Vision-Language-Modell, das Salesforce Research Anfang 2022 vorstellte. Es bewältigt sowohl Aufgaben zum Verstehen von Bildern wie Bildbeschreibungen und visuelle Fragebeantwortung als auch Abrufaufgaben wie die Zuordnung von Bildern zu Text. Beim Training bereinigte ein Bootstrap-Verfahren verrauschte, aus dem Web gesammelte Bildunterschriften: Das Modell erzeugte synthetische Beschreibungen und filterte unpassende Zuordnungen heraus. So erreichte es starke Ergebnisse, ohne sich ausschließlich auf riesige, ungefilterte Datensätze zu stützen. Mit etwa 223 Millionen Parametern ist BLIP klein im Vergleich zu späteren multimodalen Systemen. Es prägte jedoch die Erkenntnis, dass die Qualität von Bildbeschreibungen beim Vortraining ebenso wichtig ist wie deren Menge.

Salesforce veröffentlichte Gewichte und Code von BLIP offen unter einer BSD-Lizenz. Das Modell wurde zu einer verbreiteten Referenz in der Vision-Language-Forschung und zu einer Grundlage für andere Projekte, darunter frühe Versionen der Interrogator-Funktionen von Stable Diffusion. Der Nachfolger BLIP-2 verbesserte die Effizienz, indem er eingefrorene Bildencoder und Sprachmodelle über ein leichtes Verbindungsmodul kombinierte. Das ursprüngliche BLIP wird weiterhin in wissenschaftlicher Arbeit und selbst gehosteten Abläufen eingesetzt, wenn ein kompaktes, gut dokumentiertes Bildbeschreibungsmodell genügt.
