---
title: 'GPT-NeoX-20B'
name: 'GPT-NeoX-20B'
slug: 'gpt-neox-20b'
subtitle: 'Das Modell mit offenen Gewichten von EleutherAI, einer der größten öffentlichen Checkpoints seiner Zeit'
description: 'Das Modell mit offenen Gewichten von EleutherAI, einer der größten öffentlichen Checkpoints seiner Zeit'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 4
release_date: '2022-04-14'
param_count: '20B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
i18n_source: '3f0cef2ef3c0'
---
GPT-NeoX-20B ist ein Sprachmodell mit 20 Milliarden Parametern, das EleutherAI im April 2022 nach etwa einem Jahr Entwicklung ankündigte. Es basiert auf dem eigenen GPT-NeoX-Trainingsframework der Gruppe, das Megatron und DeepSpeed nutzt. Bei der Veröffentlichung war es das größte dichte autoregressive Sprachmodell mit öffentlich herunterladbaren Gewichten. Es wurde mit dem Pile und einem Kontextfenster von 2048 Tokens trainiert. Auf EleutherAIs eigenem Evaluierungsframework lag es bei den meisten gängigen NLP-Benchmarks zwischen Curie und Davinci von OpenAI. Bei einem Test mit einem Beispiel zur Lösung mathematischer Textaufgaben übertraf es GPT-3 mit 175B Parametern. Das Team hob dies als Hinweis darauf hervor, dass die Qualität der Trainingsdaten ebenso wichtig wie die reine Modellgröße ist. Das Modell wurde unter Apache 2.0 über Hugging Face veröffentlicht und bot Forschenden einen großen, einsehbaren Checkpoint zum Untersuchen und Fine-Tuning ohne geschlossene API. GPT-NeoX-20B wurde inzwischen von viel größeren und effizienteren offenen Modellen überholt, blieb aber als eine der Referenz-Codebasen der Open-Source-LLM-Forschung einflussreich.
