---
title: 'Gemma'
name: 'Gemma'
slug: 'gemma'
subtitle: 'Geminiと同じ研究から作られた、Google最初のオープンウェイトGemma'
description: 'Geminiと同じ研究から作られた、Google最初のオープンウェイトGemma'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://blog.google/technology/developers/gemma-open-models/'
price: 'Free'
rank: 7
release_date: '2024-02-21'
param_count: '7B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 64.3
humaneval_score: 32.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Google AI Studio']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
---

Gemmaは、Googleで最初のオープンウェイト言語モデルのファミリーです。2024年2月に公開され、Gemini内部で使われているのと同じ研究から作られました。2Bと7Bパラメータの2サイズで、それぞれベースと指示チューニング版のチェックポイントがあります。学習に使ったウェブテキスト、数学、コードは、順に2兆と6兆トークンです。コンテキスト長は8,192トークンと控えめで、当時のほかのモデルと同程度です。

このリリースが重要だったのは、APIに頼らず、一般的なコンシューマー向けGPU1枚やノートパソコンでも動かせる、実用的な小型モデルを開発者に渡したことです。ライセンスは商用利用を認める一方、Googleが指定する有害な用途は禁止しています。Apache 2.0のような完全にオープンなライセンスと、多くのプロプライエタリモデルのクローズドな条件との中間にあたります。Gemmaはその後Gemma 2とGemma 3に置き換わりましたが、以降Googleが続けている名称とライセンスの型はこのモデルで決まりました。
