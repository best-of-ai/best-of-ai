---
title: 'Jamba 1.5 Mini'
name: 'Jamba 1.5 Mini'
slug: 'jamba-1-5-mini'
subtitle: 'AI21のコンパクトなTransformer・Mamba混合モデル'
description: 'AI21のコンパクトなTransformer・Mamba混合モデル'
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 4
release_date: '2024-08-22'
param_count: '52B (12B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 0.2
output_price_usd_per_m: 0.4
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: 'e0243c637f6d'
---
Jamba 1.5 MiniはAI21 LabsのJamba 1.5シリーズの小型版で、2024年8月22日にJamba 1.5 Largeと同時に公開されました。同じTransformerとMambaを組み合わせたMoE構造を採用し、総パラメータ数を520億、アクティブ数を120億に縮小しつつ、上位版と同じ25万6,000トークンのコンテキスト長を保っています。Arena Hardベンチマークでは46.1点を記録し、Claude 3 Haiku、Mixtral 8x22B、Command R+など同規模モデルを上回りました。関数呼び出し、構造化JSON出力、根拠に基づく生成など、低遅延が重要なビジネス用途向けに開発され、API料金は入力100万トークンあたり0.20ドル、出力100万トークンあたり0.40ドルです。Jamba 1.5 Largeと同じくJamba Open Model Licenseで公開され、Hugging FaceとAWS Bedrockから利用できます。
