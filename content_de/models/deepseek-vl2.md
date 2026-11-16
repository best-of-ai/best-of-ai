---
title: 'DeepSeek-VL2'
name: 'DeepSeek-VL2'
slug: 'deepseek-vl2'
subtitle: 'Offenes Vision-Language-Mixture-of-Experts-Modell von DeepSeek'
description: 'Offenes Vision-Language-Mixture-of-Experts-Modell von DeepSeek'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-12-13'
param_count: '27B (4.5B active)'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'DeepSeek License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
i18n_source: 'f06b4bb46852'
---
DeepSeek-VL2 ist eine Familie von Vision-Language-Modellen, die DeepSeek am 13. Dezember 2024 als Nachfolger des Anfang desselben Jahres erschienenen DeepSeek-VL veröffentlichte. Sie umfasst drei Größen: Tiny, Small und VL2 mit insgesamt 3B, 16B und 27B Parametern sowie jeweils 1B, 2,8B und 4,5B aktiven Parametern. Zum Einsatz kommen dieselbe DeepSeekMoE- und Multi-head-Latent-Attention-Architektur wie bei den Sprachmodellen von DeepSeek. Durch dynamisches Kacheln kann das Modell hochauflösende Bilder mit unterschiedlichen Seitenverhältnissen verarbeiten, ohne Details zu verlieren. Das hilft unter anderem beim Lesen umfangreicher Dokumente, Diagramme und Screenshots.

Die Mixture-of-Experts-Architektur ermöglicht starke Ergebnisse bei visueller Fragebeantwortung, OCR und visueller Verankerung, während die Inferenz im Verhältnis zur Gesamtzahl der Parameter kostengünstig bleibt, da pro Eingabe nur wenige Experten aktiviert werden. Alle drei Größen wurden mit offenen Gewichten veröffentlicht. DeepSeek-VL2 gehörte damit zu den leistungsfähigeren offenen multimodalen Modellfamilien seiner Zeit.
