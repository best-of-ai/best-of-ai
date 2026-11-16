---
title: 'Gato'
name: 'Gato'
slug: 'gato'
subtitle: 'DeepMinds einzelner Generalist-Agent, trainiert mit Text, Bildern und Robotersteuerung'
description: 'DeepMinds einzelner Generalist-Agent, trainiert mit Text, Bildern und Robotersteuerung'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/a-generalist-agent/'
price: 'Paid'
rank: 5
release_date: '2022-05-12'
param_count: '1.18B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, generalist-agent]
i18n_source: '7358d84afc22'
---
Gato ist ein einzelnes neuronales Netz, das DeepMind im Mai 2022 vorstellte. Mit denselben Gewichten kann es mehr als 600 verschiedene Aufgaben bewältigen: Atari-Spiele spielen, Bilder beschreiben, Textgespräche führen und einen echten Roboterarm beim Stapeln von Blöcken steuern. Statt für jede Aufgabe ein eigenes Modell zu trainieren, wandelte DeepMind alle Eingaben – darunter Text, Bilder, Gelenkdrehmomente und Tastendrücke – in eine gemeinsame Tokenfolge um und trainierte darauf einen einzelnen Transformer. Die Architektur ähnelt einem großen Sprachmodell, wobei Tokens neben Wörtern auch Aktionen und Sensordaten darstellen.

Mit 1,18 Milliarden Parametern ist Gato im Vergleich zu GPT-3 mit 175 Milliarden Parametern klein. Bei jeder einzelnen Aufgabe bleibt es hinter spezialisierten Modellen zurück. Bemerkenswert war der Nachweis, dass ein einziges Netz überhaupt brauchbare Leistungen über so unterschiedliche Modalitäten und Steuerungsaufgaben hinweg erbringen kann. DeepMind beschrieb Gato als Forschungsschritt in Richtung vielseitigerer Agenten, nicht als Produkt. Das Modell wurde weder öffentlich veröffentlicht noch über eine API angeboten.
