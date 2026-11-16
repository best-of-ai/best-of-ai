---
title: 'GPT-J'
name: 'GPT-J'
slug: 'gpt-j'
subtitle: 'Frühes Open-Weight-Modell von EleutherAI im GPT-3-Stil.'
description: 'Frühes Open-Weight-Modell von EleutherAI im GPT-3-Stil.'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 3
release_date: '2021-06-04'
param_count: '6B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '3c03d602f92a'
---

GPT-J ist ein Sprachmodell mit sechs Milliarden Parametern, das EleutherAI am 9. Juni 2021 veröffentlichte. Es gehörte zu den ersten überzeugenden offenen Nachbildungen der GPT-3-Architektur, während OpenAI GPT-3 hinter einer kostenpflichtigen API hielt. Trainiert wurde es auf The Pile, dem 825-GB-Textdatensatz von EleutherAI. Die Mesh-Transformer-JAX-Bibliothek parallelisierte das Training über TPU-Pods statt GPUs. Mit 28 Schichten und einem Kontextfenster von 2.048 Tokens war es deutlich kleiner als die größte GPT-3-Variante, bewältigte aber Textgenerierung, Fragenbeantwortung und Codevervollständigung gut genug, um zur Standardreferenz für offene NLP-Forschung zu werden. Es erschien unter Apache 2.0, sodass alle es ohne OpenAIs Nutzungsbeschränkungen herunterladen, feinabstimmen und bereitstellen konnten. Dadurch wurde es eine beliebte Grundlage früher offener Chatbot-Projekte. Inzwischen haben GPT-NeoX-20B und spätere Modelle GPT-J abgelöst; es bleibt jedoch ein häufig zitierter Bezugspunkt dafür, wie die Open-Source-Community in der GPT-3-Ära zu geschlossenen Laboren aufschloss.
