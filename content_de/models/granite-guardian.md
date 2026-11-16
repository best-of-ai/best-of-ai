---
title: 'Granite Guardian'
name: 'Granite Guardian'
slug: 'granite-guardian'
subtitle: 'IBMs Sicherheits- und Risikoerkennungsmodell zum Filtern schädlicher Eingaben und Ausgaben von LLMs'
description: 'IBMs Sicherheits- und Risikoerkennungsmodell zum Filtern schädlicher Eingaben und Ausgaben von LLMs'
company: 'ibm'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2024-10-21'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [safety, open-weight, enterprise]
i18n_source: '6ce71d1a9d0a'
---
Granite Guardian ist eine Familie von Sicherheitsmodellen von IBM. Sie ergänzt ein primäres LLM und markiert riskante Eingaben oder Antworten, bevor diese Nutzer oder Anwendungen erreichen. Die Familie erschien im Oktober 2024 zusammen mit Granite 3.0 in Größen mit 2B und 8B Parametern. Beide Varianten wurden von den Granite-Instruct-Basismodellen feinabgestimmt statt von Grund auf trainiert. Sie prüfen auf Risiken aus IBMs AI Risk Atlas, darunter Jailbreak-Versuche, vulgäre Sprache, soziale Voreingenommenheit und halluzinierte Tool-Aufrufe oder Retrieval-Ergebnisse in agentischen Abläufen. Für Teams mit strengeren Latenz- oder Kostengrenzen bietet IBM außerdem eine deutlich kleinere HAP-Variante (Hate, Abuse, Profanity) mit 38 Millionen Parametern. Granite Guardian steht unter Apache 2.0 mit offenen Gewichten zur Verfügung und wird über Hugging Face, Ollama, NVIDIA und watsonx verbreitet. Spätere Aktualisierungen, darunter Version 3.3 und 4.1 mit Unterstützung für nutzerdefinierte Bewertungskriterien, übertrugen denselben Ansatz auf neuere Granite-Basismodelle.
