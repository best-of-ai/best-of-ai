---
title: 'InstructGPT'
name: 'InstructGPT'
slug: 'instructgpt'
subtitle: 'OpenAIs Modell von 2022, das RLHF-Instruktionsabstimmung im großen Maßstab einführte'
description: 'OpenAIs Modell von 2022, das RLHF-Instruktionsabstimmung im großen Maßstab einführte'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/instruction-following/'
price: 'Paid'
rank: 5
release_date: '2022-01-27'
param_count: '175B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [API]
runs_at_home: false
platforms: ['API']
date: '2026-07-16'
tags: [llm, foundation-model, legacy, rlhf]
i18n_source: 'e5b0714c6a82'
---
InstructGPT ist die feinabgestimmte Version von GPT-3, die OpenAI in der Arbeit „Training Language Models to Follow Instructions with Human Feedback“ von Ouyang et al. beschrieb. OpenAI kündigte sie im Januar 2022 an und veröffentlichte die vollständige Arbeit im März auf arXiv. Das Team entwickelte das Modell in drei Schritten: Zuerst verfassten menschliche Annotatoren Beispiele für gute Antworten, mit denen GPT-3 feinabgestimmt wurde. Danach bewerteten Menschen mehrere Modellausgaben. Schließlich trainierte das Team anhand dieser Bewertungen ein Reward-Modell, das mithilfe von Reinforcement Learning die weitere Feinabstimmung steuerte. OpenAI trainierte drei Größen mit 1,3B, 6B und 175B Parametern. Alle übernahmen das Kontextfenster von 2048 Tokens aus GPT-3.

Das meistzitierte Ergebnis der Arbeit: Menschliche Bewertende bevorzugten die Ausgaben des InstructGPT-Modells mit 1,3B Parametern gegenüber dem GPT-3-Basismodell mit 175B Parametern, obwohl das kleinere Modell hundertmal weniger Parameter hatte. Das zeigte, dass Abstimmung anhand menschlichen Feedbacks für erwünschte Antworten wichtiger sein kann als reine Modellgröße. Zugleich gingen schädliche und falsche Ausgaben zurück, ohne dass die allgemeinen Fähigkeiten wesentlich litten. Die hier entwickelte Methode – Reinforcement Learning from Human Feedback (RLHF) – wurde zum Standard, um aus einem rohen Sprachmodell einen nutzbaren Assistenten zu machen. Weniger als ein Jahr später führte sie direkt zu ChatGPT.
