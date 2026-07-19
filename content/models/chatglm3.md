---
title: 'ChatGLM3'
name: 'ChatGLM3'
slug: 'chatglm3'
subtitle: 'Zhipu''s third-generation open-weight bilingual dialogue model'
description: 'Zhipu''s third-generation open-weight bilingual dialogue model'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 4
release_date: '2023-10-27'
param_count: '6B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
---

ChatGLM3 is the third generation of the ChatGLM dialogue model line, built jointly by Zhipu AI and Tsinghua University's KEG lab and released in late October 2023. The base ChatGLM3-6B model uses a bilingual Chinese-English design and added stronger support for function calling, code execution, and agent-style tool use compared to its predecessors, along with a more diverse pretraining mix covering more training tokens and better alignment training. At release, Zhipu reported that the 6B base model led other pretrained models under 10 billion parameters across dozens of benchmarks spanning reasoning, math, code, and general knowledge.

Zhipu released ChatGLM3 in several context-length variants, with the standard ChatGLM3-6B alongside longer-context 32K and 128K versions for handling bigger documents and conversations. The model is open-weight under Apache 2.0 and widely available through Hugging Face, making it a common choice for self-hosted Chinese-language chat applications. Zhipu has since moved on to newer GLM-4 series models with larger scale and stronger benchmark results, and now operates under the Z.ai brand, leaving ChatGLM3 as a legacy option mainly used where its smaller size and low hosting cost matter more than top-tier capability.
