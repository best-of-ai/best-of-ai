---
title: 'FLUX.1 dev'
name: 'FLUX.1 dev'
slug: 'flux-1-dev'
subtitle: 'Black Forest LabsのFLUXのオープンウェイト版。非商用向け'
description: 'Black Forest LabsのFLUXのオープンウェイト版。非商用向け'
company: 'black-forest-labs'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://blackforestlabs.ai/'
price: 'Free'
rank: 7
release_date: '2024-08-01'
param_count: '12B'
modality: [text, image]
open_weight: true
license: 'FLUX.1 dev Non-Commercial License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Replicate']
date: '2026-07-16'
tags: [image-generation, open-weight, text-to-image, diffusion]
---

FLUX.1 devは、Black Forest Labsの画像生成ファミリーFLUXのオープンウェイト版で、クローズドなFLUX.1 Proと並んで2024年8月に公開されました。Black Forest Labsは、Stability AIの元研究者が設立した会社で、メンバーにはオリジナルのStable Diffusionに関わった人もいます。FLUXは、それ以前のテキストから画像を作るモデルで一般的だったU-Net型の拡散モデルではなく、120億パラメータのrectified flow transformerを使っています。devは、フル版のProをguidance蒸留したバージョンです。そのため動かすのが速く、クローズドな兄弟モデルの画質とプロンプトへの忠実さの大部分を保っています。Black Forest Labsは非商用に限ってライセンスし、重みをHugging Faceで配布しています。商用で使いたい企業は、BFL経由で別のライセンスを購入する必要があります。公開後すぐに、ファインチューニングや派生が最も盛んなオープン画像モデルの1つになりました。Replicateなどのプラットフォームや、ComfyUIといったStable Diffusionコミュニティのツールでも、よく使われています。
