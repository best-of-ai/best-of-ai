---
title: 'BioGPT'
name: 'BioGPT'
slug: 'biogpt'
subtitle: 'Microsofts domänenspezifisches generatives Modell, vortrainiert mit biomedizinischer Literatur'
description: 'Microsofts domänenspezifisches generatives Modell, vortrainiert mit biomedizinischer Literatur'
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BioGPT'
price: 'Free'
rank: 5
release_date: '2022-09-24'
param_count: '347M (base), 1.5B (Large)'
context_window_tokens: 1024
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [healthcare, open-weight, legacy]
i18n_source: 'b08c07fb9738'
---

BioGPT ist ein Sprachmodell, das Microsoft Research im Oktober 2022 vorstellte. Es wurde gezielt für biomedizinische Texte entwickelt und nicht nachträglich aus einem Allzweckmodell abgeleitet. Die GPT-2-ähnliche Decoder-Architektur wurde von Grund auf mit rund 15 Millionen PubMed-Abstracts trainiert. Es gibt eine Basisversion mit 347 Millionen Parametern und BioGPT-Large mit 1,5 Milliarden Parametern. Da das Modell von Beginn an mit biomedizinischen Texten trainiert wurde, übertraf es frühere Allzweck-Sprachmodelle bei Aufgaben wie der Extraktion biomedizinischer Beziehungen, der Beantwortung von Fragen zu medizinischer Literatur und der Dokumentenklassifizierung. Microsoft veröffentlichte beide Checkpoints unter der MIT-Lizenz auf Hugging Face und GitHub. Sie sind damit ein verbreiteter Ausgangspunkt für Forschungsgruppen, die biomedizinische NLP-Werkzeuge entwickeln möchten, ohne ein domänenspezifisches Modell von Grund auf zu trainieren. BioGPT erschien vor dem Aufkommen allgemeiner instruction-tuned Chatmodelle und wurde nicht weiter aktualisiert. Heute dient es vor allem als leichtgewichtige, selbst hostbare Option für eng umrissene Aufgaben mit biomedizinischen Texten und weniger als allgemeiner Assistent.
