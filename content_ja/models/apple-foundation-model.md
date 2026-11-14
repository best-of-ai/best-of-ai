---
title: 'Apple Foundation Model'
name: 'Apple Foundation Model'
slug: 'apple-foundation-model'
subtitle: 'Apple Intelligenceを支える、Appleのオンデバイス用とサーバー用の基盤モデル'
description: 'Apple Intelligenceを支える、Appleのオンデバイス用とサーバー用の基盤モデル'
company: 'apple'
model_type: 'Language'
logo_url: ''
product_url: 'https://machinelearning.apple.com/research/introducing-apple-foundation-models'
price: 'Paid'
rank: 6
release_date: '2024-06-10'
param_count: '3B (on-device)'
context_window_tokens: 32000
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['iOS', 'macOS']
date: '2026-07-16'
tags: [llm, on-device, foundation-model]
i18n_source: '7fbb8197cfde'
---

AppleのFoundation Modelsは、Apple Intelligenceの背後にある2つの言語モデルです。2024年6月のWWDCで発表されました。1つは約30億パラメータで、iPhone、iPad、Macのハードウェア上で直接動くモデルです。もう1つはより大きなモデルで、オンデバイスのモデルだけでは足りないタスク向けに、AppleのPrivate Cloud Computeサーバーで動きます。オンデバイスのモデルは、KVキャッシュの共有や2ビットの量子化対応学習といった手法で、スマートフォンのメモリと電力の範囲に収めています。サーバーのモデルは、Mixture-of-ExpertsのTransformerを採用しています。オンデバイスのモデルで使えるコンテキスト長は4,096トークンまでで、サーバーのモデルは最大3万2,000トークンを扱えます。

AppleはOpenAIやAnthropicのように、これらのモデルのAPIアクセスを販売してはいません。モデルは、文章作成ツール、通知の要約、刷新されたSiriの機能といった組み込みのシステム機能を支えています。WWDC 2025からは、Foundation Modelsフレームワーク経由でサードパーティの開発者にも公開され、アプリからオンデバイスのモデルを、無料でネットワーク接続なしに直接呼び出せます。Appleはその後WWDC 2025でラインナップを更新し、WWDC 2026では第3世代を発表しました。いずれも大きさを劇的に増やすより、品質と効率の改善が中心です。ユーザーのデータをクラウド上のフロンティアモデルに送るより、プライバシーとオンデバイスでの推論を重視するAppleの姿勢の表れです。
