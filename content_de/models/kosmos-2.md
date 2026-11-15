---
title: 'Kosmos-2'
name: 'Kosmos-2'
slug: 'kosmos-2'
subtitle: 'Multimodales Modell von Microsoft, das Sprache mit bestimmten Bildbereichen verknüpft'
description: 'Multimodales Modell von Microsoft, das Sprache mit bestimmten Bildbereichen verknüpft'
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/microsoft/unilm/tree/master/kosmos-2'
price: 'Free'
rank: 5
release_date: '2023-06-26'
param_count: '1.6B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '327b99415fef'
---
Kosmos-2 ist ein multimodales Modell von Microsoft Research, das im Juni 2023 veröffentlicht wurde und etwa 1,6 Milliarden Parameter hat. Sein besonderes Merkmal ist visuelle Verankerung: Statt ein Bild nur in Text zu beschreiben, verknüpft es Textstellen in der Ausgabe mit bestimmten Begrenzungsrahmen im Bild. So verweist eine Aussage über „einen Hund“ oder „den Stuhl links“ auf die genauen Bildpixel. Microsoft trainierte das Modell mit GrIT, einem eigens dafür entwickelten umfangreichen Datensatz verankerter Bild-Text-Paare, kombiniert mit allgemeinen multimodalen Korpora. Bewertet wurde es unter anderem bei Aufgaben zum Verständnis referenzieller Ausdrücke, zur Verankerung von Textstellen und bei gängigen Vision-Language-Aufgaben. Kosmos-2 war eine Forschungsarbeit und kein Produkt. Sie sollte zeigen, dass sich visuelle Verankerung direkt in einem Sprachmodell erlernen lässt, statt sie mit einem separaten Detektor nachzurüsten. Code und Gewichte stehen auf GitHub und Hugging Face unter MIT-Lizenz bereit. Die Arbeit floss in spätere multimodale Forschung von Microsoft ein, darunter Teile der Vision-Language-Reihen Florence und Phi.
