---
title: 'ERNIE 4.5'
name: 'ERNIE 4.5'
slug: 'ernie-4-5'
subtitle: 'Baiduのフラッグシップのマルチモーダル基盤モデル'
description: 'Baiduのフラッグシップのマルチモーダル基盤モデル'
company: 'baidu'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://yiyan.baidu.com/'
price: 'Free'
rank: 5
release_date: '2025-06-30'
param_count: '0.3B-424B (10 variants, MoE)'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Baidu Cloud', 'Hugging Face']
date: '2026-07-16'
tags: [llm, multimodal, open-weight]
i18n_source: 'c0b7a3d6a9c8'
---

ERNIE 4.5はBaiduが2025年3月に発表し、同年6月30日にApache 2.0ライセンスでオープンソースにしたモデルファミリーで、以前のERNIEの世代のクローズドな方針からの転換になりました。ファミリーにはMixture-of-Expertsアーキテクチャのバリエーションが10種類あり、0.3Bの密結合モデルから、1トークンあたり約47Bのパラメータを動かす4240億パラメータのマルチモーダルのフラッグシップ(ERNIE-4.5-VL-424B-A47B)までそろっています。大半のバリエーションは、最大で約128,000トークンのコンテキスト長に対応します。Baiduは重みをHugging Face、GitHub、自社のPaddlePaddleプラットフォームで公開し、主要な独自のマルチモーダルモデルに匹敵するベンチマーク結果を報告しました。このオープン公開は、DeepSeekをはじめとする中国のオープンウェイトのラボとの競争で、Baiduがこれまでで最も攻めた一手だと広く受け止められました。Baiduはその後、ERNIE 5.0に移っています。
