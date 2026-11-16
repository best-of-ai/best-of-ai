---
title: 'ALBERT'
name: 'ALBERT'
slug: 'albert'
subtitle: 'Parameterteilende BERT-Variante von Google, ausgelegt auf Effizienz im großen Maßstab'
description: 'Parameterteilende BERT-Variante von Google, ausgelegt auf Effizienz im großen Maßstab'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1909.11942'
price: 'Free'
rank: 6
release_date: '2019-09-26'
param_count: '223M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: '4c3c3afa8529'
---

ALBERT (A Lite BERT) ist ein Sprachrepräsentationsmodell, das Google Research und das Toyota Technological Institute im September 2019 als Weiterentwicklung von BERT veröffentlichten. Zwei Methoden zur Reduzierung von Parametern – faktorisierte Embedding-Parametrisierung und Parameterteilung zwischen Schichten – senken die Parameterzahl deutlich, während die Genauigkeit mit wesentlich größeren Modellen mithält. Die größte Variante, ALBERT-xxlarge mit rund 223 Millionen Parametern, hat etwa 18-mal weniger Parameter als BERT-large, trainiert jedoch schneller und erreichte bei der Veröffentlichung neue Bestwerte auf GLUE, SQuAD 2.0 und RACE.

Wie BERT ist ALBERT ein reines Encoder-Modell für Aufgaben zum Textverständnis wie Klassifizierung, Fragenbeantwortung und Leseverständnis, nicht für offene Textgenerierung. Pro Eingabe verarbeitet es höchstens 512 Tokens. Google veröffentlichte Code und vortrainierte Gewichte offen. Anfang der 2020er-Jahre wurde das Modell zu einer verbreiteten Basis für NLP-Forschung und Produktivsysteme, bevor generative Decoder-Modelle den Großteil der Aufmerksamkeit auf sich zogen.
