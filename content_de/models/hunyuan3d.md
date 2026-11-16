---
title: 'Hunyuan3D'
name: 'Hunyuan3D'
slug: 'hunyuan3d'
subtitle: 'Offenes Modell von Tencent zur Generierung von 3D-Objekten aus Text oder Bildern'
description: 'Offenes Modell von Tencent zur Generierung von 3D-Objekten aus Text oder Bildern'
company: 'tencent'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/Tencent/Hunyuan3D-2'
price: 'Free'
rank: 5
release_date: '2025-01-21'
param_count: '2.6B (shape) + 1.3B (texture)'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [3d-generation, open-weight, api]
i18n_source: '07d08c139e5b'
---
Hunyuan3D ist ein System von Tencent mit offenen Gewichten, das Texteingaben oder Referenzbilder in 3D-Objekte umwandelt. Die verbreitete Version 2.0 wurde im Januar 2025 veröffentlicht. Die Aufgabe ist auf zwei Modelle aufgeteilt: Ein Formgenerator mit 2,6 Milliarden Parametern auf Basis eines Flow-Diffusion-Transformers erzeugt ein untexturiertes Netz. Anschließend trägt ein Texturmodell mit 1,3 Milliarden Parametern hochauflösende PBR-Materialien darauf auf. Durch diese Aufteilung kann sich der Formgenerator auf Geometrie konzentrieren, während das Texturmodell Farbe, Lichtreaktion und Oberflächendetails bearbeitet. Tencent veröffentlichte die Gewichte auf Hugging Face und GitHub unter der Hunyuan-Lizenz. So können Spielestudios und 3D-Künstler Objekte lokal generieren, statt dafür eine kostenpflichtige API zu nutzen. Hunyuan3D konkurriert mit offenen und teilweise offenen 3D-Generatoren wie TripoSR und TripoSG von Stability AI. Spätere Versionen (2.1 und 2.5) verbesserten Texturtreue und Geometriedetails weiter.
