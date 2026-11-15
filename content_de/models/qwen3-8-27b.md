---
title: 'Qwen3.8-27B'
name: 'Qwen3.8-27B'
slug: 'qwen3-8-27b'
subtitle: 'Offenes multimodales Modell von Alibaba, ausgelegt für den Betrieb auf einer einzelnen lokalen GPU'
description: 'Offenes multimodales Modell von Alibaba, ausgelegt für den Betrieb auf einer einzelnen lokalen GPU'
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-14'
param_count: '27B'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-08-17'
tags: [llm, open-weight, multimodal, single-gpu, apache-2.0, local]
i18n_source: '1e091b27bdc3'
---

Alibabas Qwen-Team veröffentlichte Qwen3.8-27B am 14. August 2026. Die offenen Gewichte waren sofort unter der Apache-2.0-Lizenz verfügbar. Das Modell hat 27 Milliarden Parameter und verwendet eine dichte Architektur statt eines Mixture-of-Experts-Ansatzes. Es verarbeitet Text, Bilder und Videos, darunter Diagramme, Dokumente und mehrstündiges Filmmaterial. Das Kontextfenster umfasst nativ 262.000 Tokens und lässt sich mit der YaRN-Skalierungsmethode auf eine Million erweitern. Alibaba zufolge übertrifft es das größere Qwen3.7-Plus bei Programmier- und Büroaufgaben. Auch die agentische Planung wurde verbessert, sodass das Modell mehrstufige Aufgaben mit weniger Aufsicht erledigen kann.

Die Veröffentlichung richtete sich gezielt an Entwickler, die ein leistungsfähiges Modell auf einer einzelnen Consumer- oder Workstation-GPU statt in einem Rechenzentrumscluster betreiben möchten. Damit positioniert es sich neben ähnlichen lokal ausgerichteten Veröffentlichungen von Meta und Google. Zum Start stellte Alibaba außerdem offene Gewichte für Qwen3.8-2.4T-A95B bereit, das Modell der Max-Klasse aus derselben Generation. Entwickler können so zwischen der leichten Version und einem Modell im Spitzenbereich für anspruchsvollere agentische Arbeitslasten wählen.
