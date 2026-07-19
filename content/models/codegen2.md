---
title: 'CodeGen2'
name: 'CodeGen2'
slug: 'codegen2'
subtitle: 'Salesforce''s open-weight code model built for infilling and multi-turn program synthesis'
description: 'Salesforce''s open-weight code model built for infilling and multi-turn program synthesis'
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeGen2'
price: 'Free'
rank: 5
release_date: '2023-05-03'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [code, open-weight]
---

CodeGen2 is Salesforce Research's second-generation family of open code models, released in May 2023 as a follow-up to the original CodeGen. It comes in four sizes: 1B, 3.7B, 7B, and 16B parameters. The main improvement over the first CodeGen is infilling support, meaning the model can fill in a missing chunk of code given the surrounding context on both sides, rather than only generating text left to right. This makes it better suited to real editor workflows like autocomplete and code repair, where the model needs to write code in the middle of an existing file.

The models are trained on a mix of natural language and source code across many programming languages and are released under the permissive Apache 2.0 license through Hugging Face and GitHub. CodeGen2 was tested with a working context of around 2,000 tokens, modest by today's standards but typical for code models of that era. Salesforce positioned it as a research-friendly alternative to closed code models like Codex, and it was later followed by CodeGen2.5, a smaller model tuned to match the performance of larger predecessors.
