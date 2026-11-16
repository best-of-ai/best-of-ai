---
title: 'DeepSeek-VL2'
name: 'DeepSeek-VL2'
slug: 'deepseek-vl2'
subtitle: 'DeepSeekのオープンウェイトの、視覚言語向けMixture-of-Expertsモデル'
description: 'DeepSeekのオープンウェイトの、視覚言語向けMixture-of-Expertsモデル'
company: 'deepseek'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-12-13'
param_count: '27B (4.5B active)'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'DeepSeek License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, vision]
i18n_source: 'f06b4bb46852'
---

DeepSeek-VL2はDeepSeekが2024年12月13日に公開した視覚言語モデルのファミリーで、同年前半の初代DeepSeek-VLの続編です。Tiny、Small、フルのVL2という3つのサイズがあり、総パラメータ数はそれぞれ3B、16B、27B、有効パラメータ数は1B、2.8B、4.5Bです。DeepSeekの言語モデルと同じDeepSeekMoEとMulti-head Latent Attentionのアーキテクチャを使っています。動的なタイリングの手法により、さまざまなアスペクト比の高解像度画像を細部を失わずに処理できます。細かい文書、グラフ、スクリーンショットを読むタスクで役立ちます。

Mixture-of-Expertsの設計なので、入力ごとに動くエキスパートはごく一部です。そのため、総パラメータ数のわりに推論のコストが低いまま、視覚的な質問応答、OCR、視覚的グラウンディングのベンチマークで高い性能を出します。3つのサイズすべてがオープンウェイトで公開され、DeepSeek-VL2は当時入手できたオープンなマルチモーダルモデルのファミリーの中で、高性能なものの一つになりました。
