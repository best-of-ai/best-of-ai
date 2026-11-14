---
title: 'MiniCPM'
name: 'MiniCPM'
slug: 'minicpm'
subtitle: 'スマートフォンやエッジ端末での動作に適したOpenBMBの効率的な小型モデル'
description: 'スマートフォンやエッジ端末での動作に適したOpenBMBの効率的な小型モデル'
company: 'openbmb'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM'
price: 'Free'
rank: 5
release_date: '2024-02-01'
param_count: '2.4B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, small-model, on-device]
i18n_source: '0dcdb45ddc3c'
---
MiniCPMは24億パラメータの言語モデルで、70億・130億モデルでは重いスマートフォンやエッジ端末向けにOpenBMBが2024年2月に公開しました。一般ベンチマークでMistral 7Bに近く、中国語理解、数学、コードなどではLlama 2 13BやFalcon 40Bを上回ると報告されています。長文脈版MiniCPM-2B-128kは文書用途向けに12万8,000トークンに対応します。

Apache 2.0のオープンウェイトでHugging Faceから提供されます。メモリや計算資源が限られたオフライン・低コストアプリの開発者向けです。後のMiniCPM-Vマルチモーダルモデルの基盤となり、規模拡大に頼らない端末内AIという研究所の方針を示しました。
