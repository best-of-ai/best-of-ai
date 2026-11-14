---
title: 'Kolors'
name: 'Kolors'
slug: 'kolors'
subtitle: '中国語プロンプトに強いKuaishouのオープンウェイト画像生成モデル'
description: '中国語プロンプトに強いKuaishouのオープンウェイト画像生成モデル'
company: 'kuaishou'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Kwai-Kolors/Kolors'
price: 'Free'
rank: 5
release_date: '2024-07-06'
param_count: '2.6B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Kuaishou API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: 'b566c88c4748'
---
KolorsはKuaishouが2024年7月に公開したオープンウェイトのテキスト画像生成モデルです。U-Netアーキテクチャを基にした潜在拡散モデルで、約26億のパラメータを持ちます。CLIP系のエンコーダーではなくChatGLMをテキストエンコーダーとして使うため、中国語のプロンプトや画像内の中国語テキストの読み取り・描画に強みがあります。ネイティブの1024×1024解像度で画像を生成し、複数のアスペクト比に対応します。数十億組のテキストと画像で学習し、GitHubとHugging Faceで重みを公開しました。研究には無料で使えますが、商用展開には別途登録が必要です。FluxやStable Diffusion 3などと並び、ラテン文字以外の文字を適切に扱える広く使われているオープン画像モデルの1つです。
