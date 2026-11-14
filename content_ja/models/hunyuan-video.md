---
title: 'Hunyuan Video'
name: 'Hunyuan Video'
slug: 'hunyuan-video'
subtitle: 'Tencentのオープンウェイト・テキスト動画生成モデル'
description: 'Tencentのオープンウェイト・テキスト動画生成モデル'
company: 'tencent'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://aivideo.hunyuan.tencent.com/'
price: 'Free'
rank: 6
release_date: '2024-12-03'
param_count: '13B'
modality: [text, video]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [video-generation, open-weight, text-to-video]
i18n_source: '840cb7f4cbbc'
---
HunyuanVideoはTencentのオープンウェイト動画生成モデルです。2024年12月に約130億パラメータで公開され、当時最大のオープン動画モデルでした。テキストや画像から、最大約720p、5秒の動画を生成できます。プロンプトへの追従と動きの品質は、Runway Gen-3やKlingなどのクローズドモデルと比べても高く評価されました。Tencentは、学習・推論コード一式と事前学習済み重みをGitHubとHugging Faceで公開し、ライセンスは多くの地域で商用利用を認めています。この規模のモデルとしては珍しいことでした。重みが公開されているため、研究者やスタジオはAPIだけに頼らず、特定のスタイルや題材に合わせてファインチューニングできます。その後Tencentは、計算量を抑えながら同等の品質を目指す83億パラメータのHunyuanVideo-1.5を公開しました。
