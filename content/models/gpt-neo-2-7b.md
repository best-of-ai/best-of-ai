---
title: 'GPT-Neo 2.7B'
name: 'GPT-Neo 2.7B'
slug: 'gpt-neo-2-7b'
subtitle: 'EleutherAI''s early GPT-3-style open model, a predecessor to GPT-J and GPT-NeoX'
description: 'EleutherAI''s early GPT-3-style open model, a predecessor to GPT-J and GPT-NeoX'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/EleutherAI/gpt-neo-2.7B'
price: 'Free'
rank: 4
release_date: '2021-03-21'
param_count: '2.7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
---

GPT-Neo 2.7B is EleutherAI's 2.7 billion parameter language model, released on March 21, 2021, alongside smaller 125M and 1.3B versions as the group's first public models. It replicates the GPT-3 architecture using the mesh-tensorflow library and was trained on the Pile for roughly 420 billion tokens, giving it a 2048 token context window and general text generation ability comparable to OpenAI's smaller GPT-3 tiers at the time. EleutherAI released it under the Apache 2.0 license specifically because OpenAI had not made GPT-3 downloadable, and researchers and hobbyists used it for everything from chatbots to creative writing tools in the months before GPT-J and GPT-NeoX-20B arrived with larger parameter counts. It predates both of those later EleutherAI releases and is mostly of historical interest now, though it still runs comfortably on a single consumer GPU, which kept it in use in resource-constrained projects well after larger open models became available.
