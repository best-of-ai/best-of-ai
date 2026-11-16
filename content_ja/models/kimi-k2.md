---
title: 'Kimi K2'
name: 'Kimi K2'
slug: 'kimi-k2'
subtitle: 'Moonshotが最初に公開したK2世代のオープンウェイト基盤モデル'
description: 'Moonshotが最初に公開したK2世代のオープンウェイト基盤モデル'
company: 'moonshot-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 7
release_date: '2025-07-11'
param_count: '1T (32B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.2
api_available: true
humaneval_score: 85.0
lmarena_score: 1340
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: '611eb2c97d06'
---
Kimi K2はMoonshot AIが2025年7月に公開したK2世代の基盤モデルで、当時利用できる最大級のオープンウェイト言語モデルの1つでした。Mixture of Experts構成で総パラメータ数は約1兆、トークンあたりの有効パラメータは320億、コンテキスト長は128,000トークンです。純粋なチャットより、ツール呼び出しや複数段階のタスク実行などのエージェント用途を重視して設計されました。多言語版HumanEvalのMultiPL-Eなどのコーディングベンチマークでは、同年夏に利用できた最上位の非公開モデルに近いスコアでした。改変MITライセンスで重みを公開しているため、企業はMoonshot APIを使わずにダウンロード、ファインチューニング、セルフホストできます。K2.5、K2.6、K2.7 Codeを含む後続モデルの基盤にもなりました。
