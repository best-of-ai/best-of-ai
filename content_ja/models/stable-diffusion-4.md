---
title: 'Stable Diffusion 4'
name: 'Stable Diffusion 4'
slug: 'stable-diffusion-4'
subtitle: 'Stability AI次世代のオープンウェイト・テキスト画像拡散モデル'
description: 'Stability AI次世代のオープンウェイト・テキスト画像拡散モデル'
company: 'stability-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://stability.ai/'
price: 'Free'
rank: 7
release_date: '2026-07-15'
param_count: '12B'
modality: [text, image]
open_weight: true
license: 'Stability AI Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Stability API']
date: '2026-07-19'
tags: [image-generation, open-weight, text-to-image, diffusion, self-hosted]
i18n_source: '14d55cb2be7c'
---
Stable Diffusion 4は、2024年後半のSD 3.5以来となるStability AIの大型更新です。モデルは120億パラメータに拡大し、クローズドなMidjourneyやImagenに対する長年の弱点だったプロンプト追従と画像内文字の描画を改善しました。SD 3.5と同じStability AI Community Licenseで公開され、個人と小規模企業は無料で利用できますが、一定の売上基準を超える場合は有料ライセンスが必要です。

重みは従来どおりHugging Faceで公開され、量子化版は一般向けGPU 1基で動作します。インフラ管理を望まないチーム向けに、自社APIによるホスト推論も提供されます。FLUXなどのオープン画像モデルが先行を脅かす中で登場したSD4は、Stable Diffusionをオープンウェイト画像生成の標準に保ってきたコミュニティの追加学習環境（LoRA、ControlNet、カスタムチェックポイント）を大きく取り入れています。競争は一段と激しくなっています。
