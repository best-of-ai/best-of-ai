---
title: 'Arctic'
name: 'Arctic'
slug: 'arctic'
subtitle: 'Snowflake''s open-weight enterprise-focused model, optimized for SQL and RAG'
description: 'Snowflake''s open-weight enterprise-focused model, optimized for SQL and RAG'
company: 'snowflake-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.snowflake.com/en/blog/arctic-open-efficient-foundation-language-models-snowflake/'
price: 'Free'
rank: 4
release_date: '2024-04-24'
param_count: '480B (17B active)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Snowflake Cortex']
date: '2026-07-16'
tags: [llm, open-weight, enterprise, self-hosted]
---

Arctic is a large language model that Snowflake released in April 2024, built for enterprise work like SQL generation, coding, and instruction following rather than general chat. It uses a mixture-of-experts design with 480 billion total parameters spread across 128 experts, but only about 17 billion are active for any given token, which keeps inference costs down relative to dense models of similar scale. Snowflake released both the base and instruct checkpoints under an Apache 2.0 license, so the weights can be self-hosted or run through Snowflake Cortex. On the Spider text-to-SQL benchmark it scored around 79% accuracy, and Snowflake pitched it as a way to bring capable open models into data warehouses without sending queries to a third-party API. It trades off a shorter 4K context window and weaker general chat ability against strong performance on the narrow enterprise tasks it was built for.
