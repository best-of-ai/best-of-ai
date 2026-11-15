---
title: 'Kimi K2.6'
name: 'Kimi K2.6'
slug: 'kimi-k2-6'
subtitle: 'Offenes Modell von Moonshot für lang laufende agentische Aufgaben und Tool-Nutzung'
description: 'Offenes Modell von Moonshot für lang laufende agentische Aufgaben und Tool-Nutzung'
company: 'moonshot-ai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-04-20'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.6
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 88.0
humaneval_score: 87.0
lmarena_score: 1355
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, agentic, reasoning, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'f4220c32edb6'
---

Kimi K2.6 ist Moonshot AIs Spitzenmodell mit offenen Gewichten. Es erschien im April 2026 als Nachfolger des ursprünglichen Kimi K2. Das Mixture-of-Experts-Modell umfasst eine Billion Parameter insgesamt und aktiviert pro Token rund 32 Milliarden. Es wird nativ in INT4 ausgeliefert, was die Inferenzkosten senkt, und unterstützt ein Kontextfenster von 262.144 Tokens. Das Modell richtet sich an lang andauernde agentische Arbeit: Moonshot entwickelte es für die Orchestrierung mehrerer Agenten, stundenlange Programmieraufgaben ohne menschliches Eingreifen und native multimodale Eingaben statt nachträglich ergänzter Bilderkennung. Unabhängige Bewertungen von Artificial Analysis führen es als stärkstes verfügbares Modell mit offenen Gewichten. Bei Aufgaben wie SWE-Bench Pro und Humanity's Last Exam liegt es nur wenige Punkte hinter geschlossenen Spitzenmodellen von OpenAI und Anthropic, kostet pro Token aber nur einen Bruchteil. Die Gewichte stehen unter einer angepassten MIT-Lizenz; das Modell kann heruntergeladen und selbst gehostet werden.
