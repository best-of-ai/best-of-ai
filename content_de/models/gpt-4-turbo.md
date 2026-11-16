---
title: 'GPT-4 Turbo'
name: 'GPT-4 Turbo'
slug: 'gpt-4-turbo'
subtitle: 'Schnellerer und günstigerer Nachfolger von GPT-4 mit größerem Kontextfenster'
description: 'Schnellerer und günstigerer Nachfolger von GPT-4 mit größerem Kontextfenster'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/new-models-and-developer-products-announced-at-devday/'
price: 'Paid'
rank: 6
release_date: '2023-11-06'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 10
output_price_usd_per_m: 30
api_available: true
mmlu_score: 86.5
humaneval_score: 87.1
lmarena_score: 1250
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['ChatGPT', 'Azure OpenAI', 'API']
date: '2026-07-16'
tags: [llm, foundation-model, api]
extra_model_types: ['Code']
i18n_source: 'dfca7bbe4eb9'
---

GPT-4 Turbo ist OpenAIs Aktualisierung von GPT-4 vom November 2023, vorgestellt auf der ersten Entwicklerkonferenz des Unternehmens. Das Leistungsniveau blieb ähnlich, doch das Kontextfenster wuchs auf 128.000 Tokens. Dazu kamen ein Wissensstichtag im April 2023 und niedrigere Preise: zehn US-Dollar pro Million Eingabetokens und 30 US-Dollar pro Million Ausgabetokens. Das Modell erreicht 86,5 Prozent bei MMLU und 87,1 Prozent bei HumanEval. Außerdem unterstützt es Bildeingaben, sodass Entwickler:innen Bilder zusammen mit Text in derselben Anfrage senden können.

Ein praktischer Vorbehalt betrifft das größere Kontextfenster: Unabhängige Tests stellten fest, dass die Aufmerksamkeit ab etwa 32.000 Tokens deutlich nachließ. Die vollen 128.000 Tokens funktionierten in der Theorie daher besser als bei dichten, langen Dokumenten in der Praxis. Dennoch wurde GPT-4 Turbo 2024 für viele API-Entwickler:innen zum Standardmodell der GPT-4-Klasse. Es war direkt über OpenAI, Azure OpenAI und ChatGPT verfügbar, bis GPT-4o später im Jahr zur empfohlenen Option wurde.
