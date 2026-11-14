---
title: 'Qwen3.8-Flash-Next'
name: 'Qwen3.8-Flash-Next'
slug: 'qwen3-8-flash-next'
subtitle: '次世代Qwen4アーキテクチャを先行公開するAlibabaのオープンウェイト・プレビュー'
description: '次世代Qwen4アーキテクチャを先行公開するAlibabaのオープンウェイト・プレビュー'
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-26'
param_count: '125B (6B active)'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-09-05'
tags: [llm, open-weight, multimodal, moe, apache-2.0, cost-efficient]
i18n_source: '6dac4a7632ca'
---
Alibabaは2026年8月26日、Qwen4ファミリー全体の公開に先立ち、アーキテクチャを試せるQwen3.8-Flash-Nextをオープンソース化しました。マルチモーダル混合エキスパートモデルで、基盤は1,250億パラメータ、トークンごとの有効数は60億です。さらに510億パラメータのn-gram埋め込みテーブルと40億パラメータの複数トークン予測モジュールを備えます。コンテキスト長は標準で262,144トークン、拡張時は100万です。Alibabaによると、旧Qwen3.7-Plusより特にコーディングやオフィス業務で高性能で、学習コストは約9分の1、実行コストは約12分の1です。標準版とFP8チェックポイントの両方が公開されました。
