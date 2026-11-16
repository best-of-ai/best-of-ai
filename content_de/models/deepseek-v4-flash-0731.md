---
title: 'DeepSeek-V4-Flash-0731'
name: 'DeepSeek-V4-Flash-0731'
slug: 'deepseek-v4-flash-0731'
subtitle: 'MIT-lizenziertes 284B-MoE-Modell von DeepSeek, für leistungsfähigere agentische Programmierung neu trainiert'
description: 'MIT-lizenziertes 284B-MoE-Modell von DeepSeek, für leistungsfähigere agentische Programmierung neu trainiert'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2026-07-31'
param_count: '284B (13B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-08-09'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: '247907c6207f'
---

DeepSeek-V4-Flash-0731 verlässt die Vorschauphase und geht als nachtrainierter Checkpoint in eine öffentliche Beta. Die Ankündigung erfolgte am 31. Juli 2026 im API-Änderungsprotokoll des Unternehmens. Die Architektur entspricht dem Modell vom April: ein Mixture-of-Experts-Entwurf mit 284 Milliarden Parametern, 13 Milliarden aktiven Parametern pro Token, einem gemeinsamen Experten, 256 gerouteten Experten und einem Kontextfenster von einer Million Tokens. Geändert wurde das Nachtraining: DeepSeek stimmte das Modell gezielt auf Programmierung, agentische Werkzeugnutzung und Schlussfolgern ab. Die API unterstützt nun nativ das Responses-Format und funktioniert direkt mit Codex. Das Modell bleibt unter MIT-Lizenz ohne Zugangsbeschränkung, sodass Teams es kommerziell selbst hosten können. Bei 3-Bit-Quantisierung werden etwa 110 GB Speicher benötigt; für volle Genauigkeit ist ein 4x-GB300-Knoten nötig. Die API bleibt günstig: 0,14 US-Dollar pro Million Eingabetokens und 0,28 US-Dollar pro Million Ausgabetokens.
