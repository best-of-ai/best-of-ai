---
title: 'GPT-1'
name: 'GPT-1'
slug: 'gpt-1'
subtitle: 'OpenAIs ursprüngliches Modell aus dem Jahr 2018, das die GPT-Architektur einführte'
description: 'OpenAIs ursprüngliches Modell aus dem Jahr 2018, das die GPT-Architektur einführte'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/language-unsupervised/'
price: 'Free'
rank: 5
release_date: '2018-06-11'
param_count: '117M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [llm, legacy, foundation-model]
i18n_source: '99d5a246579a'
---
GPT-1 ist OpenAIs erster Generative Pre-trained Transformer, vorgestellt in der im Juni 2018 veröffentlichten Arbeit „Improving Language Understanding by Generative Pre-Training“. Das Modell hatte 117 Millionen Parameter und wurde mit BookCorpus trainiert, einer Sammlung unveröffentlichter Romane, bei einem Kontextfenster von 512 Tokens. Die Grundidee war einfach: Zunächst wird ein Transformer ohne Labels auf Rohtext vortrainiert, danach wird dasselbe Modell für konkrete Aufgaben wie Fragebeantwortung oder Textimplikation feinabgestimmt.

Dieser Ansatz übertraf auf 9 von 12 getesteten Benchmarks die aufgabenspezifischen Architekturen – das war die zentrale Aussage der Arbeit. GPT-1 selbst war nie ein Produkt, sondern ein Beleg dafür, dass generatives Pretraining mit anschließendem Fine-Tuning Modelle übertreffen kann, die separat für jede Aufgabe entwickelt und trainiert werden. Dieses Ergebnis gab die Vorlage vor, die OpenAI mit GPT-2, GPT-3 und den folgenden Modellen immer weiter skalierte.
