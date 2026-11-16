---
title: 'Hunyuan Large'
name: 'Hunyuan Large'
slug: 'hunyuan-large'
subtitle: 'Offenes Mixture-of-Experts-Modell von Tencent'
description: 'Offenes Mixture-of-Experts-Modell von Tencent'
company: 'tencent'
model_type: 'Language'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 5
release_date: '2024-11-05'
param_count: '389B (52B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts]
i18n_source: '12052bfcac4f'
---
Hunyuan-Large ist das Mixture-of-Experts-Sprachmodell von Tencent mit offenen Gewichten. Es erschien im November 2024 mit insgesamt 389 Milliarden Parametern, von denen 52 Milliarden pro Token aktiviert werden. Tencent bezeichnete es bei der Veröffentlichung als damals größtes offenes Transformer-basiertes MoE-Modell. Es unterstützt ein Kontextfenster von 256K Tokens und wurde mit einer Mischung aus synthetischen und realen Daten trainiert, die Schlussfolgern, Programmieren und das Erinnern bei langen Kontexten gegenüber früheren dichten Hunyuan-Modellen verbessern sollte. Zusammen mit den Gewichten veröffentlichte Tencent einen technischen Bericht zu Experten-Routing und zur Skalierung der Daten. Das Modell steht zur Selbstbereitstellung auf Hugging Face unter der Hunyuan-Lizenz und über API-Zugang bei Tencent Cloud bereit. Es konkurriert mit anderen großen offenen MoE-Modellen jener Zeit, darunter DeepSeek-V2 und die Mixtral-Familie von Mistral. Ein Vorteil ist der große Expertenpool im Verhältnis zu den tatsächlich aktivierten Parametern.
