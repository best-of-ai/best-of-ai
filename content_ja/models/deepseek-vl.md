---
title: 'DeepSeek-VL'
name: 'DeepSeek-VL'
slug: 'deepseek-vl'
subtitle: 'DeepSeek-VL2の前に出た、DeepSeek初の視覚言語モデル'
description: 'DeepSeek-VL2の前に出た、DeepSeek初の視覚言語モデル'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-VL'
price: 'Free'
rank: 5
release_date: '2024-03-11'
param_count: '7B'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'DeepSeek License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy]
i18n_source: '08ae210ac767'
---

DeepSeek-VLはDeepSeek初の視覚言語モデルで、2024年3月11日に、1.3Bと7Bのパラメータ数で公開されました。ハイブリッドのビジョンエンコーダと言語モデルを組み合わせています。エンコーダは、重い計算を使わずに最大1024x1024ピクセルの高解像度画像を扱えるよう調整されており、言語モデルはキャプション付きの写真だけでなく、ウェブのスクリーンショット、OCRデータ、グラフ、文書を混ぜて学習しています。この学習の混ぜ方は、一般的な画像を説明するだけでなく、グラフやスライドを読むといった実用的なタスクで役立てるためのものでした。DeepSeekは事前学習の最初から視覚言語の学習を組み入れたので、モデルは視覚的な対応づけに加えて、テキストのみの性能も高く保てました。

純粋な言語モデルの先へ進むDeepSeekの取り組みの中で、控えめながらも確かな初期の一歩でした。同じ年の後半にDeepSeekが拡張した、より大きなMixture-of-ExpertsのDeepSeek-VL2のアーキテクチャの下地にもなっています。
