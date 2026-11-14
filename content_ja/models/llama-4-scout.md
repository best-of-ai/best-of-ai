---
title: 'Llama 4 Scout'
name: 'Llama 4 Scout'
slug: 'llama-4-scout'
subtitle: '1,000万トークンのコンテキスト長を備えたMeta Llama 4の小型・高速モデル'
description: '1,000万トークンのコンテキスト長を備えたMeta Llama 4の小型・高速モデル'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2025-04-05'
param_count: '109B (17B active)'
context_window_tokens: 10000000
modality: [text, image]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 80.5
lmarena_score: 1290
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, long-context, self-hosted]
i18n_source: 'a01f39772dca'
---
Llama 4 Scoutは2025年4月公開のMeta Llama 4小型版です。混合エキスパート方式で総パラメータ数1,090億、トークンごとの有効数170億、エキスパート数16です。最大1,000万トークンのコンテキスト長が特長で、コードベース全体や大量文書の一括要約に向いています。Maverick同様、テキストと画像を同時処理するマルチモーダルモデルです。Metaは公開ベンチマークでGemma 3やGemini 2.0 Flash-Liteを上回りつつ、より高速・低価格な選択肢として位置づけました。量子化すればH100 GPU 1基で動作し、自社運用でも人気を得ました。
