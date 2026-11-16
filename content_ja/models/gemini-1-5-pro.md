---
title: 'Gemini 1.5 Pro'
name: 'Gemini 1.5 Pro'
slug: 'gemini-1-5-pro'
subtitle: '100万トークンのコンテキスト長を打ち出した、Googleの2024年のモデル'
description: '100万トークンのコンテキスト長を打ち出した、Googleの2024年のモデル'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 6
release_date: '2024-02-15'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.25
output_price_usd_per_m: 5
api_available: true
mmlu_score: 85.9
humaneval_score: 71.9
lmarena_score: 1260
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, multimodal, long-context, api, legacy]
extra_model_types: ['Code']
---

Gemini 1.5 Proは、100万トークンのコンテキスト長を、主流のAPIに初めて持ち込んだモデルです。Googleが2024年2月に公開し、同年5月に一般提供になりました。テキスト、画像、音声、動画を1つのプロンプトで読み込めます。Googleは、1時間分の動画や数百ページの文書をコンテキストに丸ごと保持させるデモを行いました。当時のGPT-4やClaudeが扱える範囲を、はるかに超えています。アーキテクチャはMixture-of-Expertsで、Googleによれば、より大きなGemini 1.0 Ultraにほとんどのベンチマークで並ぶか上回りつつ、動かすコストは安くなりました。

Googleは2024年中に1.5 Proの価格を2度引き下げ、最終的に、128,000トークン未満のプロンプトで、入力が100万トークンあたり約1.25ドル、出力が約5ドルに落ち着きました。スコアはMMLUが約85.9、HumanEvalが71.9で、2024年の大半を通じて、Geminiアプリ、Vertex AI、Gemini API経由で、Googleの本番用デフォルトモデルになりました。2025年にGoogleはフラッグシップをGemini 2.5 Proに替えましたが、1.5 Proは、既存の連携向けにAPIで引き続き使えます。
