---
title: 'Gemini 3 Pro'
name: 'Gemini 3 Pro'
slug: 'gemini-3-pro'
subtitle: '100万トークンのコンテキスト長を備えたGoogleの主力マルチモーダルモデル'
description: '100万トークンのコンテキスト長を備えたGoogleの主力マルチモーダルモデル'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 9
release_date: '2025-11-18'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 2.0
output_price_usd_per_m: 12.0
api_available: true
mmlu_score: 90.0
humaneval_score: 89.0
lmarena_score: 1501
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, multimodal, foundation-model, api, long-context]
extra_model_types: ['Code']
i18n_source: '5002a0dbde88'
---
Gemini 3 Proは、2025年11月18日にGemini 2.5 Proの後継として発表されたGoogleの主力モデルです。テキスト、画像、音声、動画を読み取り生成できます。入力コンテキスト長は100万トークン、出力上限は64,000トークンで、数学、科学、エージェント系ベンチマークで高い性能を掲げて登場しました。公開時にLMArenaで1500 Eloを超えて1501に達し、公開ランキングの首位を獲得しました。GoogleはMMMU-Proなどのマルチモーダル理解テストでも競合モデルを大きく上回ったと報告しています。

API料金は入力20万トークン以下のプロンプトで入力100万トークンあたり2ドル、出力100万トークンあたり12ドルです。この上限を超えると倍になります。Geminiアプリ、Google AI Studio、Vertex AI、Gemini APIから利用できます。Googleの新しいエージェント機能やコーディングアシスタントの基盤モデルにもなっています。2026年2月にはGemini 3.1 Proが登場し、コンテキスト長と料金をほぼ維持したまま推論性能をさらに高めました。
