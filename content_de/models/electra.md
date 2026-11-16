---
title: 'ELECTRA'
name: 'ELECTRA'
slug: 'electra'
subtitle: 'Pretraining-Ansatz von Google mit höherer Stichprobeneffizienz und einem Ziel zur Erkennung ersetzter Tokens'
description: 'Pretraining-Ansatz von Google mit höherer Stichprobeneffizienz und einem Ziel zur Erkennung ersetzter Tokens'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2003.10555'
price: 'Free'
rank: 6
release_date: '2020-03-23'
param_count: '335M'
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
i18n_source: 'f5cba0d29eb6'
---

ELECTRA ist eine Methode zum Vortraining von Text-Encodern, die Forschende von Google und Stanford in einer 2020 auf der ICLR veröffentlichten Arbeit vorstellten, zusammen mit einer Reihe darauf trainierter Modelle. Anders als beim Masked-Language-Modeling von BERT, bei dem das Modell zufällig ausgeblendete Wörter vorhersagt, trainiert ELECTRA einen kleinen Generator, der Tokens durch plausible Alternativen ersetzt. Ein Diskriminator erkennt anschließend, welche Tokens ausgetauscht wurden. Dieses Verfahren zur Erkennung ersetzter Tokens liefert für jedes Token einer Sequenz ein Lernsignal statt nur für maskierte Wörter und macht das Vortraining dadurch deutlich effizienter.

Die größte veröffentlichte Version, ELECTRA-Large, hat 335 Millionen Parameter und erzielte GLUE-Werte auf Augenhöhe mit RoBERTa und XLNet, benötigte aber nur ein Viertel ihres Vortrainingsaufwands. Bei gleichem Rechenbudget übertraf sie diese Modelle sogar. Google veröffentlichte Code und Gewichte unter Apache 2.0. Die kleineren Varianten ELECTRA-Small und ELECTRA-Base wurden zu beliebten Optionen für Teams, die BERT-Genauigkeit ohne dessen Trainingskosten wollten.
