---
title: 'Florence-2'
name: 'Florence-2'
slug: 'florence-2'
subtitle: 'Microsoft''s compact vision foundation model for captioning, detection, and segmentation in one model'
description: 'Microsoft''s compact vision foundation model for captioning, detection, and segmentation in one model'
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.microsoft.com/en-us/research/publication/florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks/'
price: 'Free'
rank: 6
release_date: '2024-06-15'
param_count: '0.77B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['Hugging Face', 'Azure AI Foundry']
date: '2026-07-16'
tags: [computer-vision, open-weight, multimodal]
---

Florence-2 is a vision foundation model Microsoft Research released in June 2024, built to handle captioning, object detection, segmentation, and visual grounding within a single model instead of requiring a separate model per task. It takes a prompt-based approach: the same network can produce a caption, a set of bounding boxes, or a segmentation mask depending on the text instruction it's given, using a unified sequence-to-sequence architecture. Microsoft released it in two sizes, a 230 million parameter base and a 770 million parameter large version, both tiny by comparison with typical vision-language models. It was trained on FLD-5B, an internal Microsoft dataset of about 126 million images with 5.4 billion annotations, which is what lets a model this small match or beat larger specialized models on tasks like COCO captioning and referring expression comprehension. Microsoft released the weights under the MIT license on Hugging Face and also offers it through Azure AI Foundry, making it a popular choice for teams that want vision capabilities without running a large multimodal LLM.
