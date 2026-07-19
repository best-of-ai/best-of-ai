---
title: 'Granite Vision'
name: 'Granite Vision'
slug: 'granite-vision'
subtitle: 'IBM''s compact vision-language model for document and chart understanding'
description: 'IBM''s compact vision-language model for document and chart understanding'
company: 'ibm'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2025-02-26'
param_count: '2B'
context_window_tokens: 16384
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, enterprise]
---

Granite Vision is IBM's compact vision-language model, released as part of the Granite 3.2 update in February 2025 and built specifically for visual document understanding rather than general image chat. At 2 billion parameters, it reads tables, charts, infographics, plots, and scanned documents and turns them into structured text, targeting benchmarks like DocVQA and ChartQA where IBM says it matches open models several times its size. The small footprint is deliberate: IBM designed it for everyday enterprise workloads, such as parsing invoices or extracting data from reports, where running a large multimodal model isn't practical or affordable. It supports a 16K token context window, is open-weighted under Apache 2.0, and is distributed through Hugging Face and IBM watsonx, with later versions (3.3 and the Granite 4.0 vision variants) building on the same document-focused design.
