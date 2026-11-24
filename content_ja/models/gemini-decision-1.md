---
title: 'Gemini Decision 1'
name: 'Gemini Decision 1'
slug: 'gemini-decision-1'
subtitle: '文章ではなく、選択肢のスコアと信頼度を返す、Googleの非生成モデル'
description: '文章ではなく、選択肢のスコアと信頼度を返す、Googleの非生成モデル'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/'
price: 'Paid'
rank: 6
release_date: '2026-11-11'
param_count: 'Undisclosed'
context_window_tokens: 256000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Gemini API', 'Google AI Studio']
date: '2026-11-24'
tags: [classification, decision-model, multimodal, api]
i18n_source: '1bbd28f7737a'
---

Gemini Decision 1は、2026年11月11日に始まったGoogleのDecisions APIの裏側にあるモデルで、文章は書きません。1回のフォワードパスで選択肢を採点し、それぞれの確率と信頼度を返します。はい/いいえの質問、2〜255個の選択肢がある多肢選択、順序付きのルーブリック採点に対応し、1回のリクエストで最大1,000問まで扱えます。入力はテキスト、画像、音声、動画、PDFで、最大25万6,000トークンです。

Googleはエンドツーエンドのレイテンシを150〜250ミリ秒としています。料金は入力が100万トークンあたり0.10ドルで、出力は無料です。AI Studioにはプロトタイプ用の無料枠があります。Googleによると、同じテストスイートでGemini 3.5 Flash-Liteの約5分の1のコストです。モデルIDはgemini-decision-1で、OpenRouter、LangChain、Vercel、LiteLLMとの連携が順次始まっています。
