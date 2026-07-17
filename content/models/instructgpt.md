---
title: 'InstructGPT'
name: 'InstructGPT'
slug: 'instructgpt'
subtitle: 'OpenAI''s 2022 model that introduced RLHF instruction-tuning at scale'
description: 'OpenAI''s 2022 model that introduced RLHF instruction-tuning at scale'
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/instruction-following/'
price: 'Paid'
rank: 5
release_date: '2022-01-27'
param_count: '175B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [API]
platforms: ['API']
date: '2026-07-16'
tags: [llm, foundation-model, legacy, rlhf]
---

InstructGPT is OpenAI's fine-tuned version of GPT-3, described in the paper "Training Language Models to Follow Instructions with Human Feedback" by Ouyang et al. OpenAI announced it in January 2022 and posted the full paper to arXiv that March. The team built it in three stages: collect demonstrations of good responses written by human labelers and fine-tune GPT-3 on them, gather human rankings of multiple model outputs, and use those rankings to train a reward model that guides further fine-tuning via reinforcement learning. OpenAI trained three sizes, 1.3B, 6B, and 175B parameters, all inheriting GPT-3's 2048-token context window.

The paper's most cited result is that human evaluators preferred outputs from the 1.3B InstructGPT model over the base 175B GPT-3, despite the smaller model having a hundred times fewer parameters. That gap showed that human feedback tuning mattered more than raw scale for producing responses people actually wanted, and it reduced toxic and false outputs with little cost to general capability. The technique OpenAI developed here, reinforcement learning from human feedback, became the standard method for turning a raw language model into a usable assistant, and it led directly to ChatGPT less than a year later.
