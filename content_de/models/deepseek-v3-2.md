---
title: 'DeepSeek V3.2'
name: 'DeepSeek V3.2'
slug: 'deepseek-v3-2'
subtitle: 'Update V3.1 von DeepSeek mit einem neuen Mechanismus für Sparse Attention'
description: 'Update V3.1 von DeepSeek mit einem neuen Mechanismus für Sparse Attention'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-12-01'
param_count: '685B (MoE)'
context_window_tokens: 163840
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.21
output_price_usd_per_m: 0.32
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'd6a4a3b7b4f4'
---

DeepSeek V3.2 ist DeepSeeks Aktualisierung von V3.1, die am 1. Dezember 2025 öffentlich vorgestellt wurde, nach einer experimentellen Vorschau im September. Neu ist DeepSeek Sparse Attention, ein fein abgestufter sparsamer Attention-Mechanismus, der Trainings- und Inferenzkosten senkt und die Qualität bei Aufgaben mit langem Kontext erhält. Die Spitzenvariante Speciale umfasst rund 685 Milliarden Parameter in einer Mixture-of-Experts-Architektur. Das Kontextfenster umfasst 163.840 Tokens, die Ausgabe bis zu 64.000 Tokens. DeepSeek berichtet von Ergebnissen auf Goldmedaillenniveau bei den Aufgaben der Internationalen Mathematik-Olympiade und der Internationalen Informatik-Olympiade 2025. Die API kostet rund 0,21 US-Dollar pro Million Eingabetokens und 0,32 US-Dollar pro Million Ausgabetokens – etwa die Hälfte des Preises von V3.1-Terminus, insbesondere bei der Dekodierung langer Kontexte. Wie der Rest der DeepSeek-Reihe steht das Modell unter MIT-Lizenz; Gewichte gibt es auf Hugging Face. Im darauffolgenden Frühjahr diente es als Basis für DeepSeek V4-Pro.
