---
title: 'Kimi K2.5'
name: 'Kimi K2.5'
slug: 'kimi-k2-5'
subtitle: 'サブエージェント群を連携させるMoonshotのK2ネイティブマルチモーダルモデル'
description: 'サブエージェント群を連携させるMoonshotのK2ネイティブマルチモーダルモデル'
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 7
release_date: '2026-01-27'
param_count: '1T (32B active)'
context_window_tokens: 262144
modality: [text, image]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.44
output_price_usd_per_m: 2.0
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, multimodal, agentic, self-hosted]
extra_model_types: ['Code']
i18n_source: '60d1d73ac216'
---
Kimi K2.5はMoonshot AIのネイティブなマルチモーダル版Kimi K2で、元のK2を基に約15兆のテキストと画像の混合トークンで継続事前学習し、2026年1月27日に公開されました。MoonshotがAgent Swarmと呼ぶ仕組みを中心に設計され、モデルが最大100の専門サブエージェントを調整しながら1つのタスクに取り組めます。視覚的なコーディング能力と、以前のKimiモデルが重視していたエージェント型のツール呼び出しを組み合わせています。コンテキスト長は262,144トークン、出力は最大98,000トークンです。MoonshotのAPI料金は入力100万トークンあたり約0.44ドル、出力100万トークンあたり2ドルで、第三者プロバイダーも同程度の料金を設定しています。Kimi K2シリーズと同様、改変MITライセンスのオープンウェイトで公開されました。元のK2と後のK2.6、K2.7 Codeの中間に位置します。
