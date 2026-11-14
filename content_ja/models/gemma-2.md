---
title: 'Gemma 2'
name: 'Gemma 2'
slug: 'gemma-2'
subtitle: 'Googleのオープンウェイトモデルファミリーの前世代'
description: 'Googleのオープンウェイトモデルファミリーの前世代'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 6
release_date: '2024-06-27'
param_count: '27B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 75.2
humaneval_score: 51.8
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted]
extra_model_types: ['Code']
---

Gemma 2は、Googleのオープンウェイトモデルファミリーの第2世代です。Geminiと同じ研究から作られていて、誰でもダウンロードして自分で動かせます。Googleは2024年6月27日に90億と270億パラメータの版を公開し、その後、ノートパソコンやスマートフォンで動かすことを想定した20億パラメータの小型版が続きました。27Bモデルは2倍以上大きいモデルと渡り合うよう調整されています。9B版も、公開時にいくつかのベンチマークでLlama 3 8Bや同サイズのオープンモデルを上回り、MMLUは75.2、HumanEvalは51.8でした。

GoogleはGemma 2の重みをHugging FaceとKaggleで配布していて、自分で動かしたくない人向けにはGoogle AI StudioとVertex AIでも提供しています。ライセンスはGoogle独自のGemmaライセンスで、商用利用はできますが、Apache 2.0のような完全に寛容なライセンスではなく、利用にいくつかの制限があります。その後Googleは新しい世代としてGemma 3を出したため、Gemma 2はラインアップの中で前世代の選択肢にあたります。互換性のため、またすでにこれを土台にしているチーム向けに残されています。
