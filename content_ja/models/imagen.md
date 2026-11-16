---
title: 'Imagen'
name: 'Imagen'
slug: 'imagen'
subtitle: 'Partiとともに研究プレビューとして発表されたGoogle初のテキスト画像拡散モデル'
description: 'Partiとともに研究プレビューとして発表されたGoogle初のテキスト画像拡散モデル'
company: 'google-deepmind'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://imagen.research.google/'
price: 'Paid'
rank: 6
release_date: '2022-05-24'
param_count: 'Undisclosed'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [image-generation, research, legacy]
i18n_source: '6e5bc6e9c169'
---
ImagenはGoogle Research初のテキスト画像拡散モデルです。「Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding」という論文で説明され、2022年5月にarXivへ公開されました。大規模な凍結言語モデルT5と、段階的に解像度を上げる拡散モデルを組み合わせています。まず64x64の画像を生成し、続く2段階の超解像処理で256x256、さらに1024x1024へ拡大します。論文の中心的な発見は、画像の拡散ネットワーク自体を大きくするより、テキストエンコーダーを拡大するほうが画像品質とプロンプトとの整合性を向上させたことでした。この結果は業界の後続のテキスト画像生成システムにも影響しました。COCOのデータで訓練していないにもかかわらず、COCOベンチマークで当時最高水準のFIDスコア7.27を報告しました。

GoogleはImagenを一般向け製品として公開せず、自己回帰型のPartiとともに研究プレビューとして紹介し、数か月前に公開されたOpenAIのDALL-E 2とも比較しました。名称と系譜は後の商用モデルImagen 2、3、4へ引き継がれました。これらは同じ拡散方式を基盤としつつ、初代にはなかった本番向けの基盤設備、安全フィルタリング、APIアクセスを加えています。
