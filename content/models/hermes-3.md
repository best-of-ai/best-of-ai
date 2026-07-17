---
title: 'Hermes 3'
name: 'Hermes 3'
slug: 'hermes-3'
subtitle: 'Nous Research''s open-weight fine-tune focused on steerability and reasoning'
description: 'Nous Research''s open-weight fine-tune focused on steerability and reasoning'
company: 'nous-research'
model_type: 'Language'
logo_url: ''
product_url: 'https://nousresearch.com/hermes3/'
price: 'Free'
rank: 4
release_date: '2024-08-27'
param_count: '405B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fine-tune, self-hosted]
---

Hermes 3 is an open-weight language model built by Nous Research on top of Meta's Llama 3.1 405B base. Nous released it in August 2024 as a full-parameter fine-tune rather than a lightweight adapter, aiming to hand more control back to the user through system-prompt steerability, agentic tool use, and long chains of reasoning. It ships in three sizes (8B, 70B, and 405B) trained mostly on synthetic data curated by Nous, and it supports structured output and function calling well enough to run as a drop-in agent backend. On public benchmarks it matches or beats Meta's own Llama 3.1 Instruct tune on tasks like ARC, HellaSwag, and IFEval, which is notable since it is a community fine-tune competing against the vendor's official release. Because weights are open under the Llama 3.1 license, developers can self-host the full 405B model or run it through third-party inference providers instead of a proprietary API.
