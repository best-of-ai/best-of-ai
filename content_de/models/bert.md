---
title: 'BERT'
name: 'BERT'
slug: 'bert'
subtitle: 'Bidirektionaler Encoder von Google aus dem Jahr 2018, der die NLP-Forschung neu prägte'
description: 'Bidirektionaler Encoder von Google aus dem Jahr 2018, der die NLP-Forschung neu prägte'
company: 'google'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://github.com/google-research/bert'
price: 'Free'
rank: 6
release_date: '2018-10-11'
param_count: '340M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, nlp, legacy]
i18n_source: '9489893b9c63'
---

BERT (Bidirectional Encoder Representations from Transformers) ist ein Sprachmodell, das Google Research im Oktober 2018 veröffentlichte und das den Ansatz des Fachgebiets zum Vortraining für NLP-Aufgaben veränderte. Anders als frühere Modelle, die Text von links nach rechts lasen, wird BERT mit maskierter Wortvorhersage und Satzfolgenvorhersage trainiert. So bildet es Repräsentationen, die den Kontext gleichzeitig aus beiden Richtungen berücksichtigen. Google veröffentlichte zwei Hauptgrößen: BERT-base mit 110 Millionen und BERT-large mit 340 Millionen Parametern. Beide haben eine Grenze von 512 Tokens. Die Gewichte wurden unter Apache 2.0 auf GitHub und später Hugging Face frei zugänglich gemacht. Feinabgestimmte BERT-Versionen stellten bei der Veröffentlichung Rekorde in elf NLP-Benchmarks auf, darunter Fragenbeantwortung und natürlichsprachliches Schlussfolgern. Schnell wurde es zum Standard-Basismodell für Aufgaben wie Klassifizierung, Erkennung benannter Entitäten und Suchranking. Neuere Encoder wie RoBERTa und DeBERTa sowie nachfolgende Embedding-Modelle haben es größtenteils abgelöst. Dennoch zählt es zu den meistzitierten NLP-Arbeiten und seine Architektur liegt vielen späteren Encoder-Systemen zugrunde.
