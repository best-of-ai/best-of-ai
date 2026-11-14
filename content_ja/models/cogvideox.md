---
title: 'CogVideoX'
name: 'CogVideoX'
slug: 'cogvideox'
subtitle: 'Zhipuのオープンウェイトの、テキストから動画を作るモデルファミリー'
description: 'Zhipuのオープンウェイトの、テキストから動画を作るモデルファミリー'
company: 'zhipu-ai'
model_type: 'Video Generation'
logo_url: ''
product_url: 'https://github.com/THUDM/CogVideo'
price: 'Free'
rank: 6
release_date: '2024-08-27'
param_count: '5B'
modality: [text, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Zhipu API']
date: '2026-07-16'
tags: [video-generation, open-weight, api]
i18n_source: '892ae410997f'
---

CogVideoXは、Zhipu AIのオープンウェイトのテキストから動画を作るモデルです。清華大学のKEGラボと共同で作られ、元のCogVideoプロジェクトの後継として2024年8月に公開されました。2Bと5Bパラメータのバリアントがあり、空間と時間の圧縮に3D因果VAEを使い、エキスパート適応型LayerNormのTransformerと組み合わせています。テキストから動画、画像から動画、1フレームまたはプロンプトからの動画の続きの生成に対応します。5Bモデルは、最大10秒、解像度は最大768p、毎秒16フレームのクリップを生成します。Zhipuは2024年11月に、より長く高解像度の出力ができるCogVideoX-1.5のアップデートも出しました。重みはApache 2.0で公開され、Hugging Faceにあります。Zhipuは自社のAPIからもモデルを提供しているため、CogVideoXは自前で動かすオープンモデルとしても、ホスト型サービスとしても使えます。Stability AIやRunwayが動画生成を位置づけるやり方と似ています。
