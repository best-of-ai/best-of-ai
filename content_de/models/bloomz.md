---
title: 'BLOOMZ'
name: 'BLOOMZ'
slug: 'bloomz'
subtitle: 'Eine instruction-tuned Variante von BLOOM, trainiert darauf, sprachübergreifende Anweisungen zu befolgen'
description: 'Eine instruction-tuned Variante von BLOOM, trainiert darauf, sprachübergreifende Anweisungen zu befolgen'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/bigscience/bloomz'
price: 'Free'
rank: 5
release_date: '2022-11-03'
param_count: '176B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'RAIL License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual, legacy]
i18n_source: '9dff7db95770'
---

BLOOMZ ist die instruction-tuned Variante von BLOOM, die BigScience Ende 2022 veröffentlichte. Dafür wurde das Basismodell mit 176 Milliarden Parametern anhand von xP3 feinabgestimmt, einer umfangreichen Sammlung mehrsprachiger Aufgaben in Form natürlichsprachlicher Anweisungen. Im Mittelpunkt stand die sprachübergreifende Generalisierung: BLOOMZ wurde überwiegend mit englischen Anweisungen abgestimmt, konnte aber auch Anweisungen in Sprachen befolgen, die während des Fine-Tunings nicht mit Anweisungen verknüpft waren – sofern diese Sprachen im ursprünglichen BLOOM-Pretraining vorkamen. Das war eine der ersten öffentlichen Demonstrationen dafür, dass sich Instruction-Following-Fähigkeiten auf andere Sprachen übertragen lassen, ohne jede Sprache separat abstimmen zu müssen.

Wie BLOOM behält BLOOMZ das Kontextfenster von 2048 Tokens und die dichte Transformer-Architektur des Basismodells bei. Es wird unter derselben RAIL-Lizenz veröffentlicht, die eine breite Nutzung mit einer Liste verbotener Anwendungen erlaubt. Heute ist es vor allem für Forschende interessant, die mehrsprachiges Instruction-Tuning untersuchen, und weniger als Produktions-Chatmodell: Neuere offene instruction-tuned Modelle bieten eine bessere Qualität und deutlich größere Kontextfenster bei ähnlichem oder geringerem Rechenaufwand.
