---
title: 'Fuyu-8B'
name: 'Fuyu-8B'
slug: 'fuyu-8b'
subtitle: 'Adept''s open-weight multimodal model built for digital-agent perception'
description: 'Adept''s open-weight multimodal model built for digital-agent perception'
company: 'adept-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.adept.ai/blog/fuyu-8b'
price: 'Free'
rank: 3
release_date: '2023-10-17'
param_count: '8B'
context_window_tokens: 16000
modality: [text, image]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, multimodal, open-weight, agentic]
---

Fuyu-8B is a multimodal model Adept AI released in October 2023, built specifically to support digital agents that need to see and act on screens rather than to serve as a general-purpose chatbot. Adept designed it around a simplified architecture: it feeds image patches directly into a standard decoder-only transformer without a separate image encoder, which lets it accept images at whatever resolution they come in instead of resizing everything to a fixed size. That matters for Adept's use case, since it needs to read UI elements, buttons, and text at native resolution to answer questions about screenshots, graphs, and diagrams, and to localize specific elements on a screen. Adept released the 8 billion parameter model on Hugging Face under a CC-BY-NC license, meaning it's free to use and modify but not for commercial purposes, positioning it as a smaller public preview of the model that powers Adept's own product rather than a fully separate offering. It supports a 16K token context window, and Adept has since been acquired, with much of its team moving to Amazon in 2024, leaving Fuyu-8B as a snapshot of its agent-focused research direction.
