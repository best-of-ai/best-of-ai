---
title: 'Kosmos-2'
name: 'Kosmos-2'
slug: 'kosmos-2'
subtitle: 'Microsoft''s grounded multimodal model that links language to specific image regions'
description: 'Microsoft''s grounded multimodal model that links language to specific image regions'
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/microsoft/unilm/tree/master/kosmos-2'
price: 'Free'
rank: 5
release_date: '2023-06-26'
param_count: '1.6B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
---

Kosmos-2 is a multimodal model from Microsoft Research, published in June 2023, with about 1.6 billion parameters. Its distinguishing feature is grounding: instead of just describing an image in text, it links phrases in its output to specific bounding boxes in the image, so a sentence about "a dog" or "the chair on the left" points to the exact pixels it refers to. Microsoft trained it on GrIT, a large dataset of grounded image-text pairs they built for this purpose, combined with general multimodal corpora, and evaluated it on referring expression comprehension, phrase grounding, and standard vision-language tasks. Kosmos-2 was a research release rather than a product, aimed at showing that grounding could be learned end-to-end inside a language model rather than bolted on with a separate detector. The code and weights are open on GitHub and Hugging Face under an MIT license, and the work fed into Microsoft's later multimodal research, including parts of the Florence and Phi vision-language lines.
