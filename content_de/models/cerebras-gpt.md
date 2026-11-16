---
title: 'Cerebras-GPT'
name: 'Cerebras-GPT'
slug: 'cerebras-gpt'
subtitle: 'Vollständig offene Modellfamilie von Cerebras, trainiert auf Chips im Wafermaßstab.'
description: 'Vollständig offene Modellfamilie von Cerebras, trainiert auf Chips im Wafermaßstab.'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models'
price: 'Free'
rank: 3
release_date: '2023-03-28'
param_count: '13B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fully-open, self-hosted]
i18n_source: 'ff8674011b4e'
---
Cerebras-GPT ist eine Modellfamilie mit Größen von 111 Millionen bis 13 Milliarden Parametern. Cerebras trainierte sie auf eigenen wafergroßen CS-2-Systemen und veröffentlichte sie im März 2023. Im Mittelpunkt stand weniger das Übertreffen von Benchmarks als Offenheit: Cerebras veröffentlichte Gewichte, Trainingscode und einen ausführlichen technischen Bericht zu Hyperparametern und Skalierungsverhalten jeder Modellgröße. Dabei orientierte sich das Unternehmen an rechenoptimalen Trainingsrezepten ähnlich denen von Chinchilla. So wurde Cerebras-GPT zu einer der umfassender dokumentierten offenen Modellfamilien seiner Zeit und bot Forschenden eine saubere, reproduzierbare Grundlage zur Untersuchung von Skalierungsgesetzen.

Alle Cerebras-GPT-Checkpoints stehen unter Apache 2.0 auf Hugging Face bereit und können kostenlos kommerziell und wissenschaftlich genutzt werden. Die Modelle verwenden eine weitgehend übliche GPT-Architektur mit einem Kontextfenster von 2.048 Tokens. Gemessen an den Standards von 2023 war ihre reine Leistungsfähigkeit im Vergleich zu Modellen wie LLaMA eher begrenzt, denn Cerebras priorisierte transparentes, reproduzierbares Training gegenüber maximaler Benchmark-Leistung. Heute wird die Familie vor allem in Forschungsarbeiten zu Skalierungsgesetzen und als Beispiel dafür zitiert, wie ein KI-Hardwareunternehmen seine Chips durch Training und Veröffentlichung einer vollständigen Modellreihe demonstriert.
