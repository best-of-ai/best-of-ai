---
title: 'Amazon Nova Lite'
name: 'Amazon Nova Lite'
slug: 'amazon-nova-lite'
subtitle: 'Amazonの低コストなマルチモーダルBedrockモデルのティア'
description: 'Amazonの低コストなマルチモーダルBedrockモデルのティア'
company: 'amazon'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 4
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 300000
modality: [text, image, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.06
output_price_usd_per_m: 0.24
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, multimodal, low-latency, api]
i18n_source: 'e235a3a5281e'
---

Amazon Nova Liteは、AmazonのNovaファミリーのマルチモーダルモデルです。2024年12月のAWS re:Inventで発表され、Amazon Bedrockから使えます。テキスト、画像、動画を入力でき、出力はテキストです。コンテキスト長は30万トークンで、料金は入力が100万トークンあたり0.06ドル、出力が0.24ドルです。テキスト専用のNova Microと、より高性能なNova Proの間の中位モデルとして作られました。画像や動画を扱いつつ、応答の速さと低コストも求めるアプリケーション向けです。

Nova Liteは、OpenAIやGoogleの同規模のマルチモーダルモデルと競合します。AmazonはNovaシリーズを、ベンチマークのランキング首位より、価格あたりの性能で売り込んできました。BedrockでファインチューンとディスティレーションにLite対応しているため、文書理解や視覚的な質問応答などの特定タスクに合わせて調整でき、推論時に大きなモデルの料金を払う必要がありません。
