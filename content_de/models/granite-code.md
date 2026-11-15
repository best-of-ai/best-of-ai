---
title: 'Granite Code'
name: 'Granite Code'
slug: 'granite-code'
subtitle: 'Die Modellfamilie von IBM zur Codegenerierung mit offenen Gewichten'
description: 'Die Modellfamilie von IBM zur Codegenerierung mit offenen Gewichten'
company: 'ibm'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 4
release_date: '2024-05-06'
param_count: '3B, 8B, 20B, 34B'
context_window_tokens: 8192
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'IBM watsonx']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '10f0aa565ad0'
---
Granite Code ist die Familie offener Codemodelle von IBM. Sie erschien im Mai 2024 in vier Größen mit 3B, 8B, 20B und 34B Parametern, jeweils als Basis- und instruction-tuned Version. IBM Research trainierte die Modelle mit etwa drei bis vier Billionen Tokens aus 116 Programmiersprachen. Dabei wurden roher Code und natürliche Sprache über Code gemischt, sodass dieselben Modelle Code generieren, Fehler beheben und Code erklären können. Die Modelle stehen unter Apache 2.0 und lassen sich von Unternehmen ohne Lizenzhürden feinabstimmen und erneut bereitstellen. IBM richtete sie gezielt an Unternehmen, die bei geschlossenen Programmierassistenten Bedenken hatten. Bei der Veröffentlichung zeigten Benchmarks, dass Granite-Code-Modelle andere offene Codemodelle ähnlicher Größe auf HumanEval und verwandten Tests erreichten oder übertrafen. Die Reihe ist auf Hugging Face, über Ollama und auf AWS mit Bedrock und SageMaker verfügbar. Spätere Skalierungsarbeiten erweiterten bei einigen Varianten das Kontextfenster auf 128K Tokens.
