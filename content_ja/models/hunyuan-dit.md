---
title: 'Hunyuan DiT'
name: 'Hunyuan DiT'
slug: 'hunyuan-dit'
subtitle: '中国語と英語の画像生成に対応するTencent製オープンウェイト拡散トランスフォーマー'
description: '中国語と英語の画像生成に対応するTencent製オープンウェイト拡散トランスフォーマー'
company: 'tencent'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/Tencent/HunyuanDiT'
price: 'Free'
rank: 5
release_date: '2024-05-14'
param_count: '1.5B'
modality: [text, image]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: '7a104e51d815'
---
Hunyuan-DiTは、従来の拡散モデルで多く使われたU-Netではなく、拡散トランスフォーマー構造を採用したTencentのオープンウェイト画像生成モデルです。2024年5月に公開されました。15億パラメータのノイズ除去トランスフォーマーと、中国語・英語の両方を扱うCLIPおよび多言語T5のテキストエンコーダーを組み合わせ、どちらの言語のプロンプトにも同程度に従います。この二言語対応が主な特徴です。当時の多くのオープン画像生成モデルは中国語の指示をうまく扱えず、Hunyuan-DiTはその差を埋めるために訓練されました。1024x1024画像を生成でき、内蔵のマルチモーダルチャット機能を使えば、プロンプト全体を書き直さずに複数回の対話で画像を調整できます。重みはHugging FaceとGitHubで公開され、後の1.1更新では初版にあった過飽和や透かし状の乱れが修正されました。
