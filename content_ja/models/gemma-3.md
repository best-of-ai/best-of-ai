---
title: 'Gemma 3'
name: 'Gemma 3'
slug: 'gemma-3'
subtitle: 'Gemini研究から作られた、Googleのオープンウェイトモデルファミリー'
description: 'Gemini研究から作られた、Googleのオープンウェイトモデルファミリー'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.google.dev/gemma'
price: 'Free'
rank: 7
release_date: '2025-03-12'
param_count: '27B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Gemma License'
api_available: true
mmlu_score: 78.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Google Vertex AI']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
---

Gemma 3は、Googleのオープンウェイトモデルの第3世代で、Gemini 2.0プロジェクトの研究と技術を使って作られています。1B、4B、12B、27Bパラメータの4サイズがあり、それぞれにベースのチェックポイントと指示チューニング版があります。4B、12B、27Bはテキストと画像の両方を受け付け、1Bはテキストのみです。全サイズが140を超える言語を扱え、そのうち35以上の言語は標準で高い対応力があります。大きい方のモデルはコンテキスト長が128,000トークンまであり、Gemma 2の8,192トークンから大きく伸びました。

Googleは、Gemma 3を単一のGPUまたはTPUホストで動かせる小ささにしつつ、標準的なベンチマークでははるかに大きいクローズドモデルと競えるものと位置づけています。27B版はいくつかの評価でGemini 1.5 Proを上回ったと伝えられ、第三者のテストでも以前のGemma 2 27Bを大きく引き離しています。重みはGemmaライセンスでダウンロードできるため、開発者はローカルへの導入、ファインチューン、ホスト型APIにデータを送れないエッジ用途に使っています。
