---
title: 'DINOv2'
name: 'DINOv2'
slug: 'dinov2'
subtitle: 'Selbstüberwachtes Bildmodell von Meta, das allgemeine Bildmerkmale ohne Labels erzeugt'
description: 'Selbstüberwachtes Bildmodell von Meta, das allgemeine Bildmerkmale ohne Labels erzeugt'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/dino-v2-computer-vision-self-supervised-learning/'
price: 'Free'
rank: 6
release_date: '2023-04-17'
param_count: '1.1B'
modality: [image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [computer-vision, open-weight, self-supervised]
i18n_source: '35d54331b555'
---

DINOv2 ist ein Computer-Vision-Modell, das Meta AI im April 2023 veröffentlichte. Es wurde vollständig ohne Labels auf einem kuratierten Datensatz mit 142 Millionen Bildern namens LVD-142M trainiert. Statt Bilder vordefinierten Kategorien zuzuordnen, lernt es durch selbstüberwachte Destillation allgemeine visuelle Merkmale. Diese funktionieren bei vielen Folgeaufgaben gut – Bildklassifizierung, Tiefenschätzung, Segmentierung und Retrieval – oft ganz ohne Feinabstimmung. Das größte veröffentlichte Modell umfasst 1,1 Milliarden Parameter.

Da sich die Merkmale direkt auf andere Aufgaben übertragen lassen, wurde DINOv2 zu einer verbreiteten Grundlage für weitere Computer-Vision-Systeme, auch in Bereichen wie medizinischer Bildgebung mit wenigen gelabelten Daten. Meta veröffentlichte Code und Gewichte unter Apache 2.0. Später folgte DINOv3, doch DINOv2 wird weiterhin häufig als universeller Extraktor visueller Merkmale eingesetzt.
