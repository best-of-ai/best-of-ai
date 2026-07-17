---
title: 'Canary'
name: 'Canary'
slug: 'canary'
subtitle: 'NVIDIA''s multilingual speech recognition and translation model'
description: 'NVIDIA''s multilingual speech recognition and translation model'
company: 'nvidia'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://huggingface.co/nvidia/canary-1b'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '1B'
modality: [audio, text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [Self-hosted, API]
platforms: ['NVIDIA NIM', 'Hugging Face']
date: '2026-07-16'
tags: [speech-recognition, open-weight, multilingual]
---

Canary is a family of speech models from NVIDIA's NeMo team, with the flagship Canary-1B released in April 2024. Unlike a typical ASR model that only transcribes audio, Canary handles both speech recognition and speech translation across English, French, German, and Spanish, converting spoken audio into text in the same language or translating it into another. It combines a FastConformer encoder with a transformer decoder, an architecture NVIDIA tuned to get strong accuracy from a comparatively small model, and it topped the Hugging Face Open ASR Leaderboard against competitors several times its size when it launched.

NVIDIA distributes Canary-1B through Hugging Face and its NeMo framework for self-hosted use, and also through NVIDIA NIM as a hosted API. The original Canary-1B ships under a CC-BY-NC 4.0 license, restricting it to non-commercial use, though NVIDIA has since released newer Canary variants, including Canary-1B-Flash and Canary-1B-v2, under the more permissive CC-BY-4.0 license with explicit commercial clearance and faster inference.
