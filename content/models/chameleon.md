---
title: 'Chameleon'
name: 'Chameleon'
slug: 'chameleon'
subtitle: 'Meta''s early-fusion model that natively mixes text and image tokens'
description: 'Meta''s early-fusion model that natively mixes text and image tokens'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-fair-research-new-releases/'
price: 'Free'
rank: 6
release_date: '2024-05-16'
param_count: '34B'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'Research-only'
api_available: false
access_methods: [Self-hosted]
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, open-weight]
---

Chameleon is a multimodal model from Meta FAIR, described in a May 2024 paper, that mixes text and images from the ground up rather than bolting a vision encoder onto a language model. Most multimodal systems use "late fusion," where a separate image encoder feeds visual features into a language model that was pretrained on text alone. Chameleon instead quantizes images into discrete tokens and trains on sequences of interleaved text and image tokens from scratch, so the same transformer learns to reason over both modalities and can also generate images as output, not just describe them.

Meta released two sizes, Chameleon-7B and Chameleon-34B, and reported that the 34B version outperformed models like Flamingo and IDEFICS on image captioning and visual question answering, while holding its own against GPT-4V and Gemini Pro in pairwise human preference tests on mixed-modal generation tasks. The weights are available on GitHub under a research-only license, so Chameleon cannot be used commercially, and Meta positioned it mainly as a demonstration of early-fusion training rather than a product. Ideas from Chameleon fed into Meta's later multimodal Llama models, which extended early-fusion-style training to a broader, commercially licensed model line.
