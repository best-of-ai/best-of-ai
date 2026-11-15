---
title: 'GPT-OSS-120B'
name: 'GPT-OSS-120B'
slug: 'gpt-oss-120b'
subtitle: 'Erstes Open-Weight-Modell von OpenAI seit GPT-2, das bei vielen Reasoning-Benchmarks mit o4-mini mithält'
description: 'Erstes Open-Weight-Modell von OpenAI seit GPT-2, das bei vielen Reasoning-Benchmarks mit o4-mini mithält'
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 8
release_date: '2025-08-05'
param_count: '117B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 90.0
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Together AI', 'Azure AI Foundry']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: 'caa1902f73b4'
---

GPT-OSS-120B ist ein Schlussfolgerungsmodell mit offenen Gewichten, das OpenAI am 5. August 2025 veröffentlichte. Es war die erste offene Modellveröffentlichung des Unternehmens seit GPT-2 im Jahr 2019. Die Mixture-of-Experts-Transformerarchitektur umfasst 117 Milliarden Parameter insgesamt, aber nur etwa 5,1 Milliarden aktive pro Token. Dadurch kann das Modell Schlussfolgerungsaufgaben auf einer einzelnen leistungsstarken GPU ausführen, statt auf GPU-Clustern, die dichte Modelle ähnlicher Größe benötigen würden. Bei der Veröffentlichung erreichte es rund 90 Punkte bei MMLU und lag damit bei vielen Benchmarks für Schlussfolgern und Programmierung im selben Bereich wie OpenAIs o4-mini. Es steht unter Apache 2.0, sodass Unternehmen es ohne Nutzungsbeschränkungen selbst hosten und feinabstimmen können. OpenAI entwickelte es als Konkurrenz zu offenen Veröffentlichungen von Meta, Mistral und chinesischen Laboren wie DeepSeek und Alibaba Qwen, die bei offenen Gewichten den Takt vorgaben, während OpenAI geschlossen blieb. Verfügbar ist es über Hugging Face, Together AI, Azure AI Foundry und OpenAIs API – sowohl zum Selbsthosten als auch als verwalteter Dienst.
