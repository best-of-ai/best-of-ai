---
title: 'CogView3'
name: 'CogView3'
slug: 'cogview3'
subtitle: 'Zhipuのリレーディフュージョン方式の、テキストから画像を作るモデル'
description: 'Zhipuのリレーディフュージョン方式の、テキストから画像を作るモデル'
company: 'zhipu-ai'
model_type: 'Image Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogView3'
price: 'Free'
rank: 5
release_date: '2024-09-29'
param_count: '3B'
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [image-generation, open-weight, api]
i18n_source: 'e06af9d7cbba'
---

CogView3は、Zhipu AIと清華大学によるテキストから画像を作るモデルで、2024年3月の研究論文で発表され、2024年9月にHugging Faceでオープンソース化されました。リレーディフュージョンを軸にしています。これは段階を重ねる方式で、30億パラメータのベース段階が、解像度の低い512x512の画像を生成します。次の段階でその画像にノイズを戻し、その上で、より短い超解像のディフュージョンを行います。従来のカスケード型のモデルのように、低解像度の出力に第2段階を直接条件づけることはしません。Zhipuによると、CogView3は人間による評価でStable Diffusion XLを大きく上回り、必要な推論時間は約半分です。蒸留版は、SDXLの約10分の1の推論ステップで、同じ品質に並びます。モデルとコードはApache 2.0で公開されました。Zhipuはその後、同じファミリーのより大きなディフュージョンTransformerのバリアントであるCogView-3Plusを出しています。自分で動かしたくない開発者向けに、ZhipuのAPIからホスト版も使えます。
