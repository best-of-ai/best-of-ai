---
title: 'GLM-5.3'
name: 'GLM-5.3'
slug: 'glm-5-3'
subtitle: 'Zhipu''s coding-focused update to GLM-5.2, tuned heavily on vulnerability research'
description: 'Zhipu''s coding-focused update to GLM-5.2, tuned heavily on vulnerability research'
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
---

Zhipu AI released GLM-5.3 on August 14, 2026, calling it the strongest open-weights coding model available, though the weights themselves are not landing until two weeks after the announcement. It shares its base architecture with GLM-5.2, so the roughly 50 percent jump in coding capability Zhipu reports comes entirely from extended post-training rather than a larger model. The company points to a security angle in particular: GLM-5.3 scored 84.5 percent on CyberGym, a benchmark for finding and validating vulnerabilities from source code, edging out Anthropic's Claude Mythos at 83.8 percent and OpenAI's GPT-5.6 Sol at 83.6 percent. Zhipu says internal security teams used the model to surface 2,436 vulnerabilities across 269 projects.

For now, access runs through Zhipu's GLM Coding Plan, and the model works with coding agents including Claude Code, OpenCode, and Zhipu's own ZCode. The staggered rollout, API access first and open weights later, is a pattern Zhipu has used before with the GLM line.
