---
title: 'Gemini 2.5 Flash'
name: 'Gemini 2.5 Flash'
slug: 'gemini-2-5-flash'
subtitle: 'Googleの低遅延・低コストなGeminiモデル'
description: 'Googleの低遅延・低コストなGeminiモデル'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 7
release_date: '2025-04-17'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 84.0
humaneval_score: 82.0
lmarena_score: 1290
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, low-latency, multimodal, api]
i18n_source: 'd2ed515fd5c9'
---
Gemini 2.5 Flashは、Gemini 2.5世代の低コストモデルです。2025年4月にプレビュー版として公開され、翌月に一般提供が始まりました。思考過程を表示する機能を最初から備えた初のFlashモデルで、回答前に問題を段階的に推論できます。開発者は「思考予算」を設定し、回答の質と遅延、コストのバランスを調整できます。テキスト、画像、音声を入力でき、Proと同じ100万トークンのコンテキスト長に対応します。

料金は入力100万トークンあたり0.30ドル、出力100万トークンあたり2.50ドルで、思考トークンは出力と同じ料金です。さらに、単純な処理をより安く行うFlash-Lite版もあります。MMLU-Proで約83％を記録し、料金に対してコーディングや数学のベンチマークで良好な性能を示しています。Proほど深い推論を必要としない大量処理向けに、Googleが標準モデルとして推奨しています。
