---
title: 'Canary'
name: 'Canary'
slug: 'canary'
subtitle: 'NVIDIAs mehrsprachiges Modell für Spracherkennung und Übersetzung'
description: 'NVIDIAs mehrsprachiges Modell für Spracherkennung und Übersetzung'
company: 'nvidia'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://huggingface.co/nvidia/canary-1b'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '1B'
modality: [audio, text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['NVIDIA NIM', 'Hugging Face']
date: '2026-07-16'
tags: [speech-recognition, open-weight, multilingual]
i18n_source: 'ad7707d7cc9a'
---

Canary ist eine Familie von Sprachmodellen des NeMo-Teams von NVIDIA. Das Spitzenmodell Canary-1B wurde im April 2024 veröffentlicht. Anders als typische ASR-Modelle, die Audio lediglich transkribieren, unterstützt Canary sowohl Spracherkennung als auch Sprachübersetzung für Englisch, Französisch, Deutsch und Spanisch. Es wandelt gesprochene Sprache entweder in Text derselben Sprache um oder übersetzt sie in eine andere. Das Modell kombiniert einen FastConformer-Encoder mit einem Transformer-Decoder. NVIDIA optimierte diese Architektur auf hohe Genauigkeit bei vergleichsweise geringer Modellgröße. Bei der Veröffentlichung übertraf Canary-1B auf der Hugging-Face-Open-ASR-Bestenliste mehrfach Konkurrenten, die ein Vielfaches seiner Größe hatten.

NVIDIA stellt Canary-1B über Hugging Face und das NeMo-Framework zur Selbstbereitstellung sowie als gehostete API über NVIDIA NIM bereit. Die ursprüngliche Version Canary-1B steht unter CC-BY-NC 4.0 und ist damit auf nicht kommerzielle Nutzung beschränkt. NVIDIA hat inzwischen neuere Varianten veröffentlicht, darunter Canary-1B-Flash und Canary-1B-v2, die unter der freizügigeren Lizenz CC-BY-4.0 mit ausdrücklicher kommerzieller Nutzungserlaubnis und schnellerer Inferenz stehen.
