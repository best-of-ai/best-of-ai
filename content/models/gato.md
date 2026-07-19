---
title: 'Gato'
name: 'Gato'
slug: 'gato'
subtitle: 'DeepMind''s single generalist agent trained across text, images, and robotic control'
description: 'DeepMind''s single generalist agent trained across text, images, and robotic control'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/a-generalist-agent/'
price: 'Paid'
rank: 5
release_date: '2022-05-12'
param_count: '1.18B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, generalist-agent]
---

Gato is a single neural network DeepMind introduced in May 2022 that the same set of weights can handle over 600 different tasks: playing Atari games, captioning images, holding a text conversation, and controlling a real robot arm to stack blocks. Instead of training separate models per task, DeepMind serialized every input, whether text, images, joint torques, or button presses, into one flat sequence of tokens and trained a single transformer on all of it at once, using an architecture similar to a large language model but with tokens standing in for actions and sensor data as well as words.

At 1.18 billion parameters, Gato is tiny next to GPT-3's 175 billion, and its performance on any one task trails specialists built just for that task. What made it notable was the demonstration that one network could do reasonable work across such different modalities and control problems at all. DeepMind described it as a research step toward more general-purpose agents rather than a product, and Gato was never released publicly or offered through an API.
