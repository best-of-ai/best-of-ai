---
title: 'IDEFICS2'
name: 'IDEFICS2'
slug: 'idefics2'
subtitle: '文書や図表への質問応答向けに開発されたHugging Faceのオープン視覚言語モデル'
description: '文書や図表への質問応答向けに開発されたHugging Faceのオープン視覚言語モデル'
company: 'hugging-face'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://huggingface.co/blog/idefics2'
price: 'Free'
rank: 5
release_date: '2024-04-15'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: 'd3fac35a3fdd'
---
IDEFICS2はHugging Faceのオープン視覚言語モデルで、前作IDEFICSに続いて2024年4月に公開されました。80億パラメータで、言語処理の基盤にMistral-7B、視覚エンコーダーにSigLIPを組み合わせています。画像を固定の正方形に切り取らず、元の解像度と縦横比のまま処理します。画像トークンをより効率よく使う学習とあわせ、モデル規模が数倍大きいLLaVA-NeXT-34Bなどより、文書理解、図表の読み取り、OCRを多用するタスクで優位です。重みはApache 2.0で公開され、商用利用やファインチューニングにも制限なく使えます。ホスト型APIではなく、自分の環境で動かす設計で、研究者や開発者が使える高性能なオープン視覚言語モデルを保つというHugging Faceの方針に沿っています。
