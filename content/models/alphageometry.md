---
title: 'AlphaGeometry'
name: 'AlphaGeometry'
slug: 'alphageometry'
subtitle: 'DeepMind''s neuro-symbolic system that solves olympiad geometry problems'
description: 'DeepMind''s neuro-symbolic system that solves olympiad geometry problems'
company: 'google-deepmind'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/'
price: 'Paid'
rank: 6
release_date: '2024-01-17'
param_count: 'Undisclosed'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [reasoning, math, research]
---

AlphaGeometry is a neuro-symbolic system from Google DeepMind, published in Nature in January 2024, built to solve geometry problems at the level of International Mathematical Olympiad competitors. It pairs a language model trained on synthetically generated geometry proofs with a traditional symbolic deduction engine: the neural half proposes useful auxiliary constructions, such as new points or lines, and the symbolic half runs formal logical deduction to complete the proof. On a benchmark of 30 IMO geometry problems from 2000 to 2022, it solved 25, close to the average gold medalist's score and far ahead of prior automated theorem provers.

DeepMind trained the language model on a hundred million synthetic theorems and proofs generated without any human demonstrations, since labeled olympiad-geometry data is scarce. The project was research-only and never became a product, but it showed that combining a neural model with a symbolic solver could beat approaches relying on either technique alone. DeepMind followed it a year later with AlphaGeometry2, which raised the solve rate to 84 percent of all geometry problems from the last 25 years of IMOs, surpassing the average gold medalist for the first time.
