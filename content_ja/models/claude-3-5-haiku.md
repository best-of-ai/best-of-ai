---
title: 'Claude 3.5 Haiku'
name: 'Claude 3.5 Haiku'
slug: 'claude-3-5-haiku'
subtitle: '一部のベンチマークで前世代のClaude 3 Opusに並ぶ、高速で手頃なAnthropicのモデル'
description: '一部のベンチマークで前世代のClaude 3 Opusに並ぶ、高速で手頃なAnthropicのモデル'
company: 'anthropic'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.anthropic.com/claude/haiku'
price: 'Paid'
rank: 6
release_date: '2024-11-04'
param_count: 'Undisclosed'
context_window_tokens: 200000
modality: [text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.8
output_price_usd_per_m: 4
api_available: true
humaneval_score: 88.1
lmarena_score: 1240
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'API']
date: '2026-07-16'
tags: [llm, low-latency, foundation-model, api]
extra_model_types: ['Code']
i18n_source: '43df5415f16a'
---

Claude 3.5 Haikuは、Claude 3.5ファミリーでAnthropicの高速・低価格モデルです。2024年10月に、アップグレードされたClaude 3.5 Sonnetと同時に公開されました。ラインナップでもっとも安く速い選択肢としてClaude 3 Haikuに代わるよう作られており、大きなモデルとの能力差も大きく縮めています。SWE-bench Verifiedなどのコーディング評価では、元のClaude 3.5 Sonnetと互角のスコアを出し、公開時点で使えたいくつかのより大きなモデルも上回りました。コード生成のHumanEvalでは88.1%とAnthropicは報告しています。

コンテキスト長は、Claude 3.5ラインで標準の200,000トークンのままです。料金は入力が100万トークンあたり0.80ドル、出力が100万トークンあたり4ドルで、登場時点では、最先端に近いモデルの中でも安い部類でした。カスタマーサポート、コンテンツモデレーション、データ抽出のように、大量処理で遅延に敏感な用途が想定されています。こうした用途では、推論の質を最後まで絞り出すことよりも、応答の速さと1回あたりのコストが大切です。AnthropicのAPI、claude.ai、AWS Bedrockなどのクラウドプラットフォームから使えます。
