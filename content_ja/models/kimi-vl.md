---
title: 'Kimi-VL'
name: 'Kimi-VL'
slug: 'kimi-vl'
subtitle: 'Moonshotのオープンウェイト視覚言語モデル'
description: 'Moonshotのオープンウェイト視覚言語モデル'
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 4
release_date: '2025-04-10'
param_count: '16B (2.8B active)'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
extra_model_types: ['Reasoning']
i18n_source: 'edae211c40fc'
---
Kimi-VLはMoonshot AIが2025年4月に公開したオープンウェイト視覚言語モデルです。総パラメータ数160億のMixture of Experts構成ですが、言語デコーダーで有効化されるのは約28億に限られ、性能に対して推論コストを抑えています。言語デコーダーにMoonViTを組み合わせています。これは画像を先に縮小せず、超高解像度の画像をネイティブ解像度で読み取る視覚エンコーダーです。長文書や動画向けに128,000トークンのコンテキスト長にも対応します。画面を操作するOSWorldなどのエージェント型タスクに加え、OCR、画像を使った数学的推論、複数画像の比較を想定しています。Moonshotは、長い推論を行うよう思考過程データで強化学習したKimi-VL-Thinking版も公開しました。
