---
title: 'DeepSeek-V4.1-Flash'
name: 'DeepSeek-V4.1-Flash'
slug: 'deepseek-v4-1-flash'
subtitle: 'V4-Flashの後継にあたる、より安く、視覚入力に対応し、ピーク時に価格が変わるDeepSeekのモデル'
description: 'V4-Flashの後継にあたる、より安く、視覚入力に対応し、ピーク時に価格が変わるDeepSeekのモデル'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://api-docs.deepseek.com/quick_start/pricing/'
price: 'Paid'
rank: 7
release_date: '2026-09-10'
param_count: '552B (MoE)'
context_window_tokens: 1048576
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.15
output_price_usd_per_m: 0.60
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['DeepSeek API']
date: '2026-09-18'
tags: [llm, multimodal, api, cost-efficient, moe]
i18n_source: '9bfa801c726b'
---

DeepSeekは2026年9月10日にV4.1-Flashを公開しました。5520億パラメータのMixture-of-Expertsモデルで、視覚入力にネイティブ対応し、コンテキスト長は1,048,576トークン、出力は最大393,216トークンです。料金はピークとオフピークで分かれています。オフピークの料金は、入力が100万トークンあたり、キャッシュヒット時が0.003ドル、キャッシュミス時が0.15ドルで、出力は100万トークンあたり0.60ドルです。ピーク時間帯(平日の午前、UTC)の料金はちょうど2倍になります。

この段階的な料金は、DeepSeekのいつものやり方を押し進めたものです。需要の少ない時間帯には欧米のAPI価格を大きく下回る額を付けてバッチ処理や遅延を気にしない処理を呼び込み、ピーク時にはキャパシティを管理できるだけの額を取ります。
