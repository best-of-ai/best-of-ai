---
title: 'Galactica'
name: 'Galactica'
slug: 'galactica'
subtitle: 'Meta''s 2022 model trained on scientific literature, pulled days after launch'
description: 'Meta''s 2022 model trained on scientific literature, pulled days after launch'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://galactica.org/'
price: 'Free'
rank: 3
release_date: '2022-11-15'
param_count: '120B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Non-commercial research license'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, science, legacy]
---

Galactica is a language model Meta AI built specifically for science, trained on 48 million papers, textbooks, reference material, and encyclopedias rather than the general web text used to train most large language models. Meta released it in November 2022 in sizes ranging from 125 million up to 120 billion parameters, with the largest version trained on around 106 billion tokens of curated scientific text. It could generate citations, solve math problems, write chemistry notation, and draft Wikipedia-style articles, and Meta pitched it as a tool for researchers to summarize papers and search the scientific literature.

The public demo came down within three days of launch after users showed it producing fabricated citations and confidently wrong scientific claims stated in an authoritative tone. The episode became a widely cited early example of the risks of releasing generative models without enough guardrails, and it predates ChatGPT's launch by about two weeks. Meta kept the model weights available for researchers on Hugging Face under a noncommercial license, and Galactica is now mostly referenced as a cautionary case study rather than a tool in active use.
