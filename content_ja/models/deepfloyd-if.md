---
title: 'DeepFloyd IF'
name: 'DeepFloyd IF'
slug: 'deepfloyd-if'
subtitle: 'Stabilityが支援するDeepFloyd研究所が開発した、潜在空間ではなくピクセル空間で動くテキストから画像へのモデル'
description: 'Stabilityが支援するDeepFloyd研究所が開発した、潜在空間ではなくピクセル空間で動くテキストから画像へのモデル'
company: 'stability-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://stability.ai/news/deepfloyd-if-text-to-image-model'
price: 'Free'
rank: 5
release_date: '2023-04-28'
param_count: '4.3B'
modality: [text, image]
open_weight: true
license: 'Stability Community License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [image-generation, open-weight, legacy]
i18n_source: 'e6c34510f10f'
---

DeepFloyd IFは、Stability AIが支援する研究所DeepFloydが2023年4月に公開したテキストから画像へのモデルです。Stable Diffusionの潜在空間での拡散とは違い、3つのモジュールを連ねたカスケードでピクセル空間を直接扱います。まず64x64の低解像度画像を作り、そこから段階的にアップサンプリングして1024x1024にします。この方式のおかげで、当時の潜在拡散モデルがよく失敗していた、画像内の読める文字の描画に定評がありました。DeepFloydはベースモジュールを3つのサイズで学習しており、最大のものは43億パラメータです。パイプライン全体は、完全なオープンライセンスではなくStability Community Licenseのもとで、非商用の研究プレビューとして公開されました。Stable Diffusionのように主流の製品になることはありませんでしたが、文字描画での成果は、同じ弱点を改善した後発の商用モデルに影響を与えました。
