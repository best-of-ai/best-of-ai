---
title: 'DistilBERT'
name: 'DistilBERT'
slug: 'distilbert'
subtitle: 'Verdichtete Version von BERT von Hugging Face, 40 Prozent kleiner bei Erhalt des Großteils der Leistung'
description: 'Verdichtete Version von BERT von Hugging Face, 40 Prozent kleiner bei Erhalt des Großteils der Leistung'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1910.01108'
price: 'Free'
rank: 7
release_date: '2019-10-02'
param_count: '66M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, small-model]
i18n_source: '4bb37eb28b4c'
---

DistilBERT ist eine komprimierte Version von Googles BERT, die Hugging Face im Oktober 2019 veröffentlichte. Beim sogenannten Knowledge Distillation lernt ein kleineres Schülermodell während des Vortrainings, die Ausgaben des größeren BERT-Lehrermodells nachzuahmen. Mit 66 Millionen Parametern ist es 40 Prozent kleiner als BERT-base und läuft rund 60 Prozent schneller, behält aber etwa 97 Prozent der BERT-Leistung in der GLUE-Benchmark-Suite. Bei Aufgaben wie Fragenbeantwortung mit SQuAD und IMDb-Stimmungsklassifizierung liegt es trotz der Größenreduzierung nur wenige Punkte hinter dem vollständigen BERT.

Die Arbeit „DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter“ zählt zu den meistzitierten NLP-Publikationen. Das Modell wurde zur Standardwahl für Teams, die Sprachverständnis auf BERT-Niveau mit begrenzter Hardware – etwa Mobilgeräten – benötigen. Es steht unter Apache 2.0 und gehört auch Jahre nach der Veröffentlichung zu den meistgeladenen Modellen auf Hugging Face.
