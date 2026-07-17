---
title: 'LLaMA'
name: 'LLaMA'
slug: 'llama'
subtitle: 'Meta''s original 2023 open-weight release that kicked off the open LLM boom'
description: 'Meta''s original 2023 open-weight release that kicked off the open LLM boom'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/large-language-model-llama-meta-ai/'
price: 'Free'
rank: 6
release_date: '2023-02-24'
param_count: '65B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Non-commercial research license'
api_available: false
mmlu_score: 63.4
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
---

LLaMA is Meta's original large language model, released in February 2023 in four sizes ranging from 7B to 65B parameters, with a modest 2,048-token context window by today's standards. Unlike later Llama generations, access was initially restricted: Meta granted weights to researchers on a case-by-case basis under a non-commercial license rather than publishing them freely, though the weights leaked publicly within weeks of release. Meta reported that its 13B model beat GPT-3's 175B parameter version on several benchmarks, and that the 65B model was competitive with PaLM and Chinchilla, a claim that got the open-source LLM community paying close attention to efficient training. LLaMA is the model that set off the wave of open fine-tunes and derivatives, like Alpaca and Vicuna, that defined open-source LLM research through 2023, even though it has since been fully superseded by Llama 2, 3, and 4.
