---
title: 'Med-PaLM'
name: 'Med-PaLM'
slug: 'med-palm'
subtitle: 'Google''s first LLM tuned to answer medical exam and consumer health questions'
description: 'Google''s first LLM tuned to answer medical exam and consumer health questions'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://sites.research.google/med-palm/'
price: 'Paid'
rank: 5
release_date: '2022-12-26'
param_count: '540B'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, healthcare, research]
---

Med-PaLM is Google's first attempt at a medical question-answering model, built by fine-tuning the 540B parameter PaLM model on clinical and consumer health data. Described in a paper posted in December 2022 and later published in Nature, it was the first AI system to score a passing grade on US Medical Licensing Examination style questions, clearing the roughly 60% bar. Google evaluated it on MultiMedQA, a benchmark it introduced alongside the model that pulls together medical exam questions, research literature queries, and the kinds of questions people search for about their own health.

The project set up the comparison that Med-PaLM 2 would later improve on, and it stayed a research system rather than a public product. Clinicians who reviewed its answers found it prone to the kind of factual errors and omissions that make unsupervised use in real medical settings risky, which is part of why Google kept it restricted to research partners.
