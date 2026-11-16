---
title: 'BitNet b1.58'
name: 'BitNet b1.58'
slug: 'bitnet-b1-58'
subtitle: '1.58ビットの三値の重みで、LLMとして競争力のある性能を示したMicrosoftの研究モデル'
description: '1.58ビットの三値の重みで、LLMとして競争力のある性能を示したMicrosoftの研究モデル'
company: 'microsoft'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/microsoft/BitNet'
price: 'Free'
rank: 6
release_date: '2024-02-27'
param_count: '2B (2B4T release)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, research, efficiency]
i18n_source: '4d1b2822f6ff'
---

BitNet b1.58は、三値の重みで作る言語モデルを探るMicrosoftの研究の系列です。三値の重みとは、通常の16ビットや32ビットの浮動小数点ではなく、すべての重みを-1、0、1に限ったものです。2024年2月の最初の論文「The Era of 1-bit LLMs」は、後から量子化するのではなく、最初からこの形式で学習したモデルが、同程度のサイズのLlama 2などの全精度モデルに並びつつ、メモリ使用量と推論時のエネルギーを大きく減らせることを示しました。Microsoftは2025年4月に、4兆トークンで学習した20億パラメータのチェックポイントBitNet b1.58 2B4Tを公開してこれに続きました。埋め込みを除くメモリ使用量は約0.4GBで、Gemma 3 1BやMiniCPM 2Bのような同規模のモデルよりずっと小さい値です。重みと推論コードはMITライセンスでGitHubとHugging Faceにあります。このプロジェクトが注目されるのは、ほかのモデルをベンチマークで上回ることより、1ビットでの学習が大きな性能の低下なしに成り立つと示した点です。スマートフォンやエッジデバイスで高性能なモデルを動かすうえで意味があります。
