---
title: 'IDEFICS2'
name: 'IDEFICS2'
slug: 'idefics2'
subtitle: 'Offenes Vision-Language-Modell von Hugging Face für Dokumenten- und Diagrammfragen'
description: 'Offenes Vision-Language-Modell von Hugging Face für Dokumenten- und Diagrammfragen'
company: 'hugging-face'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://huggingface.co/blog/idefics2'
price: 'Free'
rank: 5
release_date: '2024-04-15'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: 'd3fac35a3fdd'
---
IDEFICS2 ist das offene Vision-Language-Modell von Hugging Face und erschien im April 2024 als Nachfolger des ursprünglichen IDEFICS. Es hat acht Milliarden Parameter und kombiniert Mistral-7B als Sprachmodell mit einem SigLIP-Vision-Encoder. Bilder verarbeitet es in ihrer ursprünglichen Auflösung und mit ihrem ursprünglichen Seitenverhältnis, statt sie alle auf einen quadratischen Ausschnitt zuzuschneiden. Diese Entscheidung und ein effizienterer Umgang mit Bild-Tokens verschaffen ihm bei Dokumentenverständnis, Diagrammauswertung und OCR-intensiven Aufgaben einen Vorteil gegenüber Modellen, die um ein Mehrfaches größer sind, darunter LLaVA-NeXT-34B. Hugging Face veröffentlichte die Gewichte unter Apache 2.0. Damit kann das Modell ohne Lizenzbeschränkungen kommerziell genutzt und feinabgestimmt werden. Es ist für den selbst gehosteten Betrieb statt für eine gehostete API gedacht und passt damit zum Ziel von Hugging Face, Forschenden und Entwicklern leistungsfähige offene Vision-Language-Baselines bereitzustellen.
