---
title: 'BLOOMZ'
name: 'BLOOMZ'
slug: 'bloomz'
subtitle: 'An instruction-tuned variant of BLOOM trained to follow cross-lingual instructions'
description: 'An instruction-tuned variant of BLOOM trained to follow cross-lingual instructions'
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://huggingface.co/bigscience/bloomz'
price: 'Free'
rank: 5
release_date: '2022-11-03'
param_count: '176B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'RAIL License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual, legacy]
---

BLOOMZ is BigScience's instruction-tuned version of BLOOM, released in late 2022 by fine-tuning the base 176 billion parameter model on xP3, a large collection of multilingual tasks phrased as natural-language instructions. The point of the project was cross-lingual generalization: BLOOMZ was tuned mostly on English instructions but showed it could follow instructions in languages it had never seen paired with instructions during fine-tuning, as long as it had encountered that language during BLOOM's original pretraining. That made it one of the earlier public demonstrations that instruction-following skills transfer across languages rather than needing separate tuning for each one.

Like BLOOM, BLOOMZ keeps the 2,048-token context window and dense transformer architecture of the base model, and it ships under the same RAIL License permitting broad use with a list of prohibited applications. It is mainly of interest today to researchers studying multilingual instruction tuning rather than as a production chat model, since newer instruction-tuned open models offer better quality and much larger context windows for similar or lower compute cost.
