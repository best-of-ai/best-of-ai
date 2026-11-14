---
title: 'Emu3'
name: 'Emu3'
slug: 'emu3'
subtitle: 'テキスト、画像、動画の生成と理解を、次トークン予測で1つにまとめたBAAIのモデル'
description: 'テキスト、画像、動画の生成と理解を、次トークン予測で1つにまとめたBAAIのモデル'
company: 'baai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://baai-agents.github.io/Emu3/'
price: 'Free'
rank: 5
release_date: '2024-09-27'
param_count: '8B'
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, research]
extra_model_types: ['Image Generation']
i18n_source: '6fd97391d2f7'
---

Emu3は北京智源人工知能研究院(BAAI)が2024年9月に公開した、オープンウェイトのマルチモーダルモデルで、ある一つの考え方を軸にしています。テキスト、画像、動画のすべてを離散トークンの系列として扱い、3つすべてにわたって次のトークンを予測するように、1つのtransformerを学習させるというものです。拡散やCLIP型の別個の部品はありません。BAAIは80億パラメータのモデルとして、ChatとGenの2つのバリエーションで公開しました。一方は視覚と言語の理解向け、もう一方は生成向けに調整されています。目的を一つにした単純な設計にもかかわらず、BAAIは、画像生成ではSDXL、視覚と言語の理解ではLLaVA-1.6といった、当時の確立したタスク特化のオープンモデルを、Emu3が上回ったと報告しています。このプロジェクトは、2025年後半に公開されたBAAIのより大きなEmu3.5の前身にあたります。Emu3.5は同じ次トークン予測の手法を、340億パラメータまで拡大しています。
