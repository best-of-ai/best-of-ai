---
title: 'Hunyuan-A13B'
name: 'Hunyuan-A13B'
slug: 'hunyuan-a13b'
subtitle: 'Open-Weight-Mixture-of-Experts-Modell für Schlussfolgern von Tencent.'
description: 'Open-Weight-Mixture-of-Experts-Modell für Schlussfolgern von Tencent.'
company: 'tencent'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 4
release_date: '2025-06-27'
param_count: '80B (13B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, mixture-of-experts]
i18n_source: '1fc3c97bd4e4'
---

Hunyuan-A13B ist ein Sprachmodell mit offenen Gewichten von Tencent, veröffentlicht im Juni 2025. Es hat insgesamt 80 Milliarden Parameter, davon aber nur 13 Milliarden aktive pro Token. So bleiben die Inferenzkosten ähnlich wie bei einem deutlich kleineren dichten Modell. Nativ unterstützt es ein Kontextfenster von 256.000 Tokens; viele selbst gehostete Umgebungen begrenzen es jedoch, damit es in den GPU-Speicher passt. Ein dualer Modus erlaubt den Wechsel zwischen schnellen Antworten und langsamem schrittweisem Schlussfolgern für schwierige Mathematik-, Wissenschafts- und Programmieraufgaben. Tencent veröffentlichte die Gewichte unter der eigenen Hunyuan-Lizenz auf Hugging Face. Für Teams, die das Modell nicht selbst betreiben möchten, gibt es außerdem die Tencent-Cloud-API. Es konkurriert mit effizienten offenen MoE-Schlussfolgerungsmodellen wie kleineren DeepSeek-Veröffentlichungen und Alibaba Qwen und setzt eher auf Effizienz aktiver Parameter als auf maximale Gesamtparameterzahl.
