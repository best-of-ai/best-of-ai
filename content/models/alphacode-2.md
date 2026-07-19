---
title: 'AlphaCode 2'
name: 'AlphaCode 2'
slug: 'alphacode-2'
subtitle: 'DeepMind''s competitive-programming model built on Gemini, ranking among top human competitors'
description: 'DeepMind''s competitive-programming model built on Gemini, ranking among top human competitors'
company: 'google-deepmind'
model_type: 'Code'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/alphacode-2-technical-report/'
price: 'Paid'
rank: 6
release_date: '2023-12-06'
param_count: 'Undisclosed'
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [code, research]
---

AlphaCode 2 is Google DeepMind's competitive-programming system, published as a technical report in December 2023 as a follow-up to the original AlphaCode. Instead of a single model, it is a pipeline built on fine-tuned Gemini models: it samples up to a million candidate C++ solutions per problem, then filters them down through test-based checks, behavioral clustering, and a learned scoring model to pick roughly ten final submissions. On a set of recent Codeforces contests, it solved 43 percent of problems within ten attempts, nearly double the original AlphaCode's 25 percent.

DeepMind estimated that AlphaCode 2's performance would place it in the 85th percentile among human Codeforces competitors, putting it between the "Expert" and "Candidate Master" ranks on that platform. The project was research-only, never shipped as a product or API, and served mainly to demonstrate how much a strong base model plus heavy sampling and filtering can improve performance on hard, verifiable coding problems. It is a direct ancestor of the reasoning and code-generation techniques later folded into DeepMind's Gemini and AlphaProof lines of work.
