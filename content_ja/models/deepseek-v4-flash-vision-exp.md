---
title: 'DeepSeek-V4-Flash-Vision-Exp'
name: 'DeepSeek-V4-Flash-Vision-Exp'
slug: 'deepseek-v4-flash-vision-exp'
subtitle: '文書やグラフの理解に向けた、DeepSeekのV4-Flashの実験的なマルチモーダル版'
description: '文書やグラフの理解に向けた、DeepSeekのV4-Flashの実験的なマルチモーダル版'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/news/news260821/'
price: 'Paid'
rank: 6
release_date: '2026-08-21'
param_count: '284B (MoE, 13B active)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.22
output_price_usd_per_m: 0.66
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-08-31'
tags: [multimodal, vision, api, document-understanding, mixture-of-experts]
i18n_source: '1264f839812e'
---

DeepSeekは2026年8月21日に、DeepSeek-V4-Flash-Vision-Expを公開しました。これはDeepSeek-V4-Flashに画像入力を加えた実験的なバージョンで、元のV4-Flashは総パラメータ数2840億、1トークンあたりの有効パラメータ数130億のスパースなMixture-of-Expertsモデルです。エージェントや推論のタスクではテキストのみのV4-Flashと同等で、そこに画像の理解が加わります。想定しているのは文書やグラフの読み取り、視覚的な質問応答、テキストと画像が混在するエージェントのワークフローです。画像はインラインのbase64データ、URL、DeepSeekのFiles API経由で渡せます。画像1枚あたり384トークンでトークン化するので、GPTやClaudeのモデルが通常1枚に使う量よりずっと少なくなります。

DeepSeek独自のマルチモーダルエージェントのベンチマークでは、視覚入力についての推論が必要なタスクで、V4-Flash-Vision-ExpがAnthropicのOpus-4.8との差の多くを縮めたと同社は報告しています。テキストのみのV4-Flashからは大きな伸びです。料金は入力が100万トークンあたり0.22ドル、出力が0.66ドルで、キャッシュされた入力には別に安い料金があります。実験版でない公開に向けて同社がフィードバックを集めている間は、DeepSeek APIでのみ使えます。
