---
title: 'Jamba 1.5 Large'
name: 'Jamba 1.5 Large'
slug: 'jamba-1-5-large'
subtitle: '非常に長いコンテキスト向けに作られたAI21のTransformer・Mamba混合モデル'
description: '非常に長いコンテキスト向けに作られたAI21のTransformer・Mamba混合モデル'
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 5
release_date: '2024-08-22'
param_count: '398B (94B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 2
output_price_usd_per_m: 8
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: '53e8093cdb62'
---
Jamba 1.5 LargeはAI21 LabsのJambaシリーズ最上位モデルで、2024年8月22日に公開されました。TransformerのアテンションブロックとMambaの状態空間レイヤーをMoE構成で組み合わせ、総パラメータ数3,980億のうち推論時に使うのは940億です。この設計により、同等の品質を持つ密なTransformerよりメモリ使用量と推論コストを抑えながら、当時、オープンライセンスのモデルでは最長級の25万6,000トークンのコンテキストを扱えます。AI21は自社APIで入力100万トークンあたり2ドル、出力100万トークンあたり8ドルに設定しました。重みはHugging FaceとAWS BedrockでもJamba Open Model Licenseのもと配布されています。長文書の分析、要約、検索拡張生成などの企業用途を想定し、同分野ではMixtral 8x22BやCommand R+と競合します。
