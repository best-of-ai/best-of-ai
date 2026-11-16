---
title: 'GLM-5.3'
name: 'GLM-5.3'
slug: 'glm-5-3'
subtitle: 'Auf Programmierung ausgerichtetes Update von GLM-5.2, intensiv auf Schwachstellenforschung abgestimmt'
description: 'Auf Programmierung ausgerichtetes Update von GLM-5.2, intensiv auf Schwachstellenforschung abgestimmt'
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Paid'
rank: 7
release_date: '2026-08-14'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['GLM Coding Plan', 'API']
date: '2026-08-17'
tags: [llm, coding, cybersecurity, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: '87f3720943f0'
---

Zhipu AI veröffentlichte GLM-5.3 am 14. August 2026 und bezeichnete es als stärkstes offenes Code-Modell, auch wenn die Gewichte erst zwei Wochen nach der Ankündigung bereitgestellt werden sollten. Die Basisarchitektur entspricht GLM-5.2. Der von Zhipu berichtete Leistungsanstieg beim Programmieren um etwa 50 Prozent stammt daher vollständig aus erweitertem Nachtraining und nicht aus einem größeren Modell. Besonders hob das Unternehmen Sicherheit hervor: GLM-5.3 erzielte 84,5 Prozent bei CyberGym, einem Benchmark zur Erkennung und Validierung von Schwachstellen im Quellcode. Damit lag es knapp vor Claude Mythos von Anthropic mit 83,8 Prozent und GPT-5.6 Sol von OpenAI mit 83,6 Prozent. Interne Sicherheitsteams hätten das Modell genutzt, um 2.436 Schwachstellen in 269 Projekten aufzudecken.

Derzeit erfolgt der Zugriff über Zhipus GLM Coding Plan. Das Modell funktioniert mit Programmieragenten wie Claude Code, OpenCode und Zhipus eigenem ZCode. Die gestaffelte Veröffentlichung – zuerst API-Zugriff, später offene Gewichte – hat Zhipu bei der GLM-Reihe bereits zuvor verwendet.
