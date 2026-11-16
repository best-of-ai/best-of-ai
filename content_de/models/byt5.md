---
title: 'ByT5'
name: 'ByT5'
slug: 'byt5'
subtitle: 'Die tokenfreie Google-Variante von T5, die direkt mit Rohbytes arbeitet'
description: 'Die tokenfreie Google-Variante von T5, die direkt mit Rohbytes arbeitet'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2105.13626'
price: 'Free'
rank: 4
release_date: '2021-05-28'
param_count: '13B'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, research]
i18n_source: 'e8007dd611dd'
---
ByT5 ist eine Variante von Googles Text-zu-Text-Modell T5, die Google Research Mitte 2021 veröffentlichte. Sie verzichtet vollständig auf Tokenisierung und verarbeitet UTF-8-Rohbytes direkt. Übliche Sprachmodelle zerlegen Text mithilfe eines Tokenizers in Subword-Tokens aus einem festen Vokabular. Das funktioniert für Sprachen und Schriftsysteme gut, auf die das Vokabular zugeschnitten ist, verarbeitet jedoch seltene Wörter, Schreibfehler und weniger verbreitete Sprachen oft schlecht. ByT5 umgeht dieses Problem, indem es jede Eingabe als Bytefolge behandelt. Sein Vokabular umfasst dadurch nur einige Hundert mögliche Werte statt Zehntausende Subword-Tokens.

Der Nachteil: Bytefolgen sind für denselben Text deutlich länger als Tokenfolgen. ByT5 benötigt daher tiefere Encoder und mehr Rechenleistung pro Eingabe, um bei Standardbenchmarks mit tokenbasierten Modellen mitzuhalten. Google veröffentlichte eine Modellfamilie bis ByT5-XXL mit rund 13 Milliarden Parametern. Alle Checkpoints sind unter Apache 2.0 offen auf Hugging Face verfügbar. Besonders gut schnitt das Modell bei verrauschten Texten, Transliteration und mehrsprachigen Aufgaben mit ressourcenarmen Schriftsystemen ab. In der Forschung zu tokenfreier und zeichenbasierter Modellierung dient es daher als wichtiger Bezugspunkt, obwohl die meisten Produktionsmodelle wegen ihrer Effizienz weiterhin Tokens verwenden.
