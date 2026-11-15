---
title: 'Jamba 1.5 Large'
name: 'Jamba 1.5 Large'
slug: 'jamba-1-5-large'
subtitle: 'Das hybride Transformer-Mamba-Modell von AI21 für sehr lange Kontexte'
description: 'Das hybride Transformer-Mamba-Modell von AI21 für sehr lange Kontexte'
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 5
release_date: '2024-08-22'
param_count: '398B (94B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 2
output_price_usd_per_m: 8
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: '53e8093cdb62'
---
Jamba 1.5 Large ist das Spitzenmodell der Jamba-Familie von AI21 Labs und erschien am 22. August 2024. Es nutzt eine hybride Architektur, die Transformer-Attention-Blöcke und Mamba-Zustandsraumschichten in einem Mixture-of-Experts-Aufbau kombiniert. Insgesamt hat es 398 Milliarden Parameter, von denen bei der Inferenz nur 94 Milliarden aktiv sind. Dadurch kann es ein Kontextfenster von 256.000 Tokens verarbeiten – eines der längsten, die damals ein offen lizenziertes Modell bot –, während Speicherbedarf und Inferenzkosten geringer bleiben als bei einem gleich leistungsfähigen dichten Transformer. Über die API von AI21 kostet es 2 US-Dollar pro Million Eingabetokens und 8 US-Dollar pro Million Ausgabetokens. Außerdem wird es auf Hugging Face und AWS Bedrock unter der Jamba Open Model License von AI21 bereitgestellt. Es richtet sich an Unternehmensaufgaben wie die Analyse langer Dokumente, Zusammenfassungen und Retrieval-Augmented Generation und konkurriert in diesem Bereich mit Modellen wie Mixtral 8x22B und Command R+.
