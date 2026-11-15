---
title: 'GLM-5'
name: 'GLM-5'
slug: 'glm-5'
subtitle: 'Offenes Frontier-Modell von Zhipu, vollständig auf heimischer Huawei-Hardware trainiert'
description: 'Offenes Frontier-Modell von Zhipu, vollständig auf heimischer Huawei-Hardware trainiert'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-02-11'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 203000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.57
output_price_usd_per_m: 1.92
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
i18n_source: 'd5e3911c0704'
---

GLM-5 ist Zhipu AIs Spitzenmodell mit offenen Gewichten und erschien am 11. Februar 2026. Gegenüber GLM-4.5 wurde es ungefähr verdoppelt: Die Gesamtzahl der Parameter stieg von 355 auf rund 744 Milliarden, während das Mixture-of-Experts-Design weiterhin etwa 40 Milliarden aktive Parameter pro Token nutzt. Das Kontextfenster umfasst 203.000 Tokens und blieb damit deutlich unter den eine Million Tokens, die der vier Monate später veröffentlichte Nachfolger GLM-5.2 bieten sollte. Zhipu trainierte das Modell vollständig auf Huawei-Ascend-Chips mit dem MindSpore-Framework statt auf Nvidia-Hardware. Die API kostet über Zhipus Plattform und WaveSpeed 0,57 US-Dollar pro Million Eingabetokens und 1,92 US-Dollar pro Million Ausgabetokens. GLM-5 wurde unter MIT-Lizenz veröffentlicht und galt damals als erstes Spitzenmodell eines chinesischen Labors, das vollständig auf heimischer Hardware entwickelt wurde.
