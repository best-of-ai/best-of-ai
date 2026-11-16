---
title: 'Flamingo'
name: 'Flamingo'
slug: 'flamingo'
subtitle: 'Vision-Language-Modell von DeepMind, das multimodales Few-Shot-Reasoning maßgeblich prägte'
description: 'Vision-Language-Modell von DeepMind, das multimodales Few-Shot-Reasoning maßgeblich prägte'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/tackling-multiple-tasks-with-a-single-visual-language-model/'
price: 'Paid'
rank: 6
release_date: '2022-04-29'
param_count: '80B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, vision, research]
i18n_source: '98bf1c585f2e'
---

Flamingo ist ein Vision-Language-Modell, das DeepMind im April 2022 veröffentlichte. Es verarbeitet Bilder, Videos und Text gemeinsam und beantwortet offene Fragen dazu, nachdem es nur wenige Beispiele gesehen hat. Als Basis dient Chinchilla, DeepMinds Sprachmodell mit 70 Milliarden Parametern. Hinzu kommen Bild-Encoder und Cross-Attention-Schichten, über die die Textgenerierung visuelle Eingaben berücksichtigt. Das Gesamtmodell umfasst dadurch rund 80 Milliarden Parameter. Zentral war Few-Shot-Lernen für Vision-Language-Aufgaben: Statt für jeden neuen Datensatz feinabgestimmt zu werden, konnte Flamingo wenige Beispiele im Prompt erhalten und daraus verallgemeinern – ähnlich wie GPT-3 bei Text. Bei der Veröffentlichung übertraf es frühere Few-Shot-Ansätze in 16 Benchmarks, darunter Bildbeschriftung, visuelle Fragenbeantwortung und visueller Dialog. DeepMind veröffentlichte Flamingo weder als Produkt noch als öffentliche API. Das Modell blieb Forschung, beeinflusste aber spätere multimodale Systeme, etwa offene Neuimplementierungen wie OpenFlamingo und Entwurfsentscheidungen in nachfolgenden multimodalen Google-Modellen.
