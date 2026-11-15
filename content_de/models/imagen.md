---
title: 'Imagen'
name: 'Imagen'
slug: 'imagen'
subtitle: 'Ursprüngliches Text-zu-Bild-Diffusionsmodell von Google, gemeinsam mit Parti als Forschungsvorschau vorgestellt'
description: 'Ursprüngliches Text-zu-Bild-Diffusionsmodell von Google, gemeinsam mit Parti als Forschungsvorschau vorgestellt'
company: 'google-deepmind'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://imagen.research.google/'
price: 'Paid'
rank: 6
release_date: '2022-05-24'
param_count: 'Undisclosed'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, research, legacy]
i18n_source: '6e5bc6e9c169'
---

Imagen ist Googles ursprüngliches Text-zu-Bild-Diffusionsmodell. Es wurde in der Arbeit „Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding“ beschrieben, die im Mai 2022 auf arXiv erschien. Ein großes eingefrorenes Sprachmodell, T5, wird mit einer Kaskade aus Diffusionsmodellen kombiniert: Ein Basismodell erzeugt ein kleines Bild mit 64 × 64 Pixeln. Zwei Superauflösungsstufen skalieren es anschließend auf 256 × 256 und 1.024 × 1.024 Pixel hoch. Die zentrale Erkenntnis der Arbeit war, dass ein größerer Textencoder die Bildqualität und Prompttreue stärker verbesserte als ein größeres Bilddiffusionsnetzwerk. Dieses Ergebnis beeinflusste spätere Text-zu-Bild-Systeme in der gesamten Branche. Imagen erzielte im COCO-Benchmark trotz fehlenden Trainings mit COCO-Daten einen damals führenden FID-Wert von 7,27.

Google veröffentlichte Imagen nie als öffentliches Produkt. Es blieb eine Forschungsvorschau, die zusammen mit dem autoregressiven Modell Parti gezeigt und mit OpenAIs wenige Monate zuvor gestarteter DALL-E 2 verglichen wurde. Name und Entwicklungslinie lebten in den kommerziellen Modellen Imagen 2, 3 und 4 weiter. Sie bauten auf demselben Diffusionsansatz auf, ergänzten aber Produktionsinfrastruktur, Sicherheitsfilter und API-Zugriff, die dem ursprünglichen Forschungsmodell fehlten.
