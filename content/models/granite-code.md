---
title: 'Granite Code'
name: 'Granite Code'
slug: 'granite-code'
subtitle: 'IBM''s open-weight code generation model family'
description: 'IBM''s open-weight code generation model family'
company: 'ibm'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 4
release_date: '2024-05-06'
param_count: '3B, 8B, 20B, 34B'
context_window_tokens: 8192
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'IBM watsonx']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
---

Granite Code is IBM's family of open code models, released in May 2024 in four sizes: 3B, 8B, 20B, and 34B parameters, each available in both base and instruction-tuned versions. IBM Research trained the models on roughly 3 to 4 trillion tokens spanning 116 programming languages, mixing raw code with natural-language text about code so the models handle tasks like code generation, bug fixing, and code explanation in the same system. The models are released under Apache 2.0, letting companies fine-tune and redeploy them without licensing friction, which IBM aimed squarely at enterprises wary of closed code assistants. Benchmarks at launch showed Granite Code models matching or beating other open code models of similar size on HumanEval and related suites. The line is available on Hugging Face, through Ollama, and on AWS via Bedrock and SageMaker, and later scaling work pushed some variants to a 128K context window.
