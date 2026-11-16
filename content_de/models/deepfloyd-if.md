---
title: 'DeepFloyd IF'
name: 'DeepFloyd IF'
slug: 'deepfloyd-if'
subtitle: 'Ein Text-zu-Bild-Modell im Pixelraum (ohne latenten Raum) des von Stability unterstützten DeepFloyd-Labs'
description: 'Ein Text-zu-Bild-Modell im Pixelraum (ohne latenten Raum) des von Stability unterstützten DeepFloyd-Labs'
company: 'stability-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://stability.ai/news/deepfloyd-if-text-to-image-model'
price: 'Free'
rank: 5
release_date: '2023-04-28'
param_count: '4.3B'
modality: [text, image]
open_weight: true
license: 'Stability Community License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [image-generation, open-weight, legacy]
i18n_source: 'e6c34510f10f'
---
DeepFloyd IF ist ein Text-zu-Bild-Modell, das DeepFloyd, ein von Stability AI unterstütztes Forschungslabor, im April 2023 veröffentlichte. Anders als Stable Diffusion arbeitet es mit Diffusion direkt im Pixelraum statt im latenten Raum. Die Generierung läuft über eine Kaskade aus drei Modulen: Zunächst entsteht ein Bild mit niedriger Auflösung von 64 × 64 Pixeln, das anschließend schrittweise auf 1024 × 1024 Pixel hochskaliert wird. Dadurch kann das Modell besonders gut lesbaren Text in Bilder einfügen – eine Aufgabe, an der latente Diffusionsmodelle jener Zeit oft scheiterten. DeepFloyd trainierte drei Größen des Basismoduls; die größte hat 4,3 Milliarden Parameter. Die gesamte Pipeline wurde als nicht kommerzielle Forschungsvorschau unter der Stability Community License veröffentlicht und nicht unter einer vollständig offenen Lizenz. Das Modell wurde nicht so verbreitet wie Stable Diffusion, doch seine Ergebnisse bei der Texterzeugung beeinflussten spätere kommerzielle Modelle.
