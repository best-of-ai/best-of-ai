---
title: 'Gemini Embedding'
name: 'Gemini Embedding'
slug: 'gemini-embedding'
subtitle: 'Geminiから作られた、Googleの統合テキスト埋め込みモデル'
description: 'Geminiから作られた、Googleの統合テキスト埋め込みモデル'
company: 'google-deepmind'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://ai.google.dev/gemini-api/docs/embeddings'
price: 'Freemium'
rank: 5
release_date: '2025-03-07'
param_count: 'Undisclosed'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Google Vertex AI']
date: '2026-07-16'
tags: [embedding, retrieval, api]
---

Gemini EmbeddingはGoogleのテキスト埋め込みモデルです。Geminiファミリーをもとに作られ、2025年3月からGemini APIで一般提供されています。テキストを1本のベクトル表現に変換し、開発者は検索、クラスタリング、分類、検索拡張生成に使います。以前は別々だったGoogleの埋め込みモデルに代わり、100を超える言語とコードで学習した1つのモデルにまとめました。Matryoshka Representation Learningに対応しているため、既定の埋め込みを768や256次元などの小さなサイズに切り詰めて、再学習なしで保存容量を減らせます。

公開時にはMTEBの多言語ランキングで、次点のモデルを大きく引き離して首位に立ちました。その後もGoogleはこの系列を拡張していて、同じベクトル空間でテキストに加えて画像、音声、動画をネイティブに扱える新しいバージョンもあります。Gemini APIとVertex AIから使え、ほかのGeminiモデルと同じく入力トークン単位で課金されます。
