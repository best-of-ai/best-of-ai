---
title: 'Chameleon'
name: 'Chameleon'
slug: 'chameleon'
subtitle: 'Early-Fusion-Modell von Meta, das Text- und Bild-Tokens nativ kombiniert'
description: 'Early-Fusion-Modell von Meta, das Text- und Bild-Tokens nativ kombiniert'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-fair-research-new-releases/'
price: 'Free'
rank: 6
release_date: '2024-05-16'
param_count: '34B'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'Research-only'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, open-weight]
extra_model_types: ['Image Generation']
i18n_source: '6e820e7a5edb'
---
Chameleon ist ein multimodales Modell von Meta FAIR, das in einer Arbeit vom Mai 2024 beschrieben wurde. Es verarbeitet Text und Bilder von Grund auf gemeinsam, statt einen Vision-Encoder nachträglich an ein Sprachmodell anzuschließen. Viele multimodale Systeme nutzen eine sogenannte späte Fusion: Ein separater Bildencoder speist visuelle Merkmale in ein Sprachmodell ein, das zuvor nur mit Text trainiert wurde. Chameleon quantisiert Bilder dagegen in diskrete Tokens und trainiert von Grund auf mit Sequenzen aus abwechselnden Text- und Bild-Tokens. Dadurch lernt derselbe Transformer, über beide Modalitäten zu schlussfolgern und auch Bilder als Ausgabe zu erzeugen, statt sie nur zu beschreiben.

Meta veröffentlichte zwei Größen, Chameleon-7B und Chameleon-34B. Laut Unternehmen übertraf die 34B-Version Modelle wie Flamingo und IDEFICS bei Bildbeschreibungen und visueller Fragebeantwortung. In paarweisen Präferenztests mit Menschen zu Aufgaben der gemischten Modalitätsgenerierung lag sie zudem auf Augenhöhe mit GPT-4V und Gemini Pro. Die Gewichte sind unter einer reinen Forschungslizenz auf GitHub verfügbar; kommerzielle Nutzung ist daher nicht erlaubt. Meta positionierte Chameleon vor allem als Demonstration des Early-Fusion-Trainings und nicht als Produkt. Ideen daraus flossen in spätere multimodale Llama-Modelle ein, die das Training mit früher Fusion auf eine breitere, kommerziell lizenzierte Modellfamilie ausweiteten.
