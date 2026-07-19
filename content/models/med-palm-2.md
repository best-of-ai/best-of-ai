---
title: 'Med-PaLM 2'
name: 'Med-PaLM 2'
slug: 'med-palm-2'
subtitle: 'Google''s medical LLM that reached expert-level scores on US medical licensing exam questions'
description: 'Google''s medical LLM that reached expert-level scores on US medical licensing exam questions'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://sites.research.google/med-palm/'
price: 'Paid'
rank: 6
release_date: '2023-05-16'
param_count: 'Undisclosed'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 86.5
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, healthcare, research]
---

Med-PaLM 2 is Google's second-generation medical question-answering model, built on the PaLM 2 base and fine-tuned on medical domain data. It was the first language model to reach expert-level performance on the MedQA benchmark, a set of US Medical Licensing Examination style questions, scoring 86.5%, a jump of roughly 19 points over the original Med-PaLM. Google evaluated it across MultiMedQA, a collection of seven datasets spanning professional exams, medical research questions, and consumer health queries, and introduced a technique called ensemble refinement, where the model generates multiple reasoning paths and then combines them into a final answer.

Google shared Med-PaLM 2 with a small set of healthcare organizations for testing rather than releasing it broadly, reflecting the caution around deploying medical AI in clinical settings. It later informed MedLM, a Google Cloud product for healthcare customers, and is positioned as a research step toward AI systems that can support doctors and answer patient questions safely, rather than a general-purpose chatbot.
