---
title: 'BLIP-2'
name: 'BLIP-2'
slug: 'blip-2'
subtitle: 'Salesforce''s more efficient successor to BLIP, bootstrapping vision-language pretraining from frozen encoders'
description: 'Salesforce''s more efficient successor to BLIP, bootstrapping vision-language pretraining from frozen encoders'
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/LAVIS/tree/main/projects/blip2'
price: 'Free'
rank: 6
release_date: '2023-01-30'
param_count: '3.7B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
---

BLIP-2 is a vision-language model that Salesforce Research published in January 2023, and it's built around a specific efficiency trick: instead of training a large image encoder and language model together from scratch, it freezes both a pretrained image encoder and a pretrained language model and trains only a lightweight connector between them, called a Q-Former. That Q-Former has around 188 million trainable parameters, less than 2% of the total model, which made BLIP-2 far cheaper to train than comparable vision-language models of the time while still doing well on image captioning and visual question answering. Salesforce released several variants pairing the Q-Former with different frozen language models, including versions built on OPT (2.7B and 6.7B parameters) and Flan-T5 (up to 11B parameters), so users could trade off capability against compute cost. The code and weights are on GitHub and Hugging Face under the MIT license as part of Salesforce's LAVIS library, and the frozen-encoder, lightweight-connector approach it popularized influenced later multimodal models that similarly bolt vision capabilities onto existing language models rather than training everything jointly.
