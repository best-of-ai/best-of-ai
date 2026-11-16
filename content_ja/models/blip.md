---
title: 'BLIP'
name: 'BLIP'
slug: 'blip'
subtitle: 'キャプション生成と検索のための、Salesforceの視覚言語の事前学習モデル'
description: 'キャプション生成と検索のための、Salesforceの視覚言語の事前学習モデル'
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/BLIP'
price: 'Free'
rank: 6
release_date: '2022-01-28'
param_count: '223M'
modality: [text, image]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy]
i18n_source: '0a995979513f'
---

BLIP（Bootstrapping Language-Image Pre-training）は、Salesforce Researchが2022年初めに発表した視覚言語モデルです。画像のキャプション生成や視覚的な質問応答といった理解のタスクと、画像とテキストを対応づける検索のタスクの両方を扱います。モデルは、ウェブから集めたノイズの多いキャプションを整えるブートストラップの手法で学習しました。合成のキャプションを生成し、合わない組み合わせを除くやり方で、整理されていない膨大なデータだけに頼らずに、高い成績を出せました。パラメータ数は約2億2,300万で、後のマルチモーダルシステムと比べれば小さいものの、事前学習ではキャプションの量と同じくらい質が大事だと示した点で影響力がありました。

SalesforceはBLIPの重みとコードをBSDライセンスで公開しました。視覚言語の研究で一般的なベースラインとなり、Stable Diffusionのインタロゲーター機能の初期版など、ほかのプロジェクトの部品にもなりました。後継のBLIP-2は、固定した画像エンコーダと固定した言語モデルを軽量なブリッジのモジュールでつなぐことで効率を改善しました。それでも、小さくて資料が整ったキャプション生成モデルで足りる学術研究やセルフホストのパイプラインでは、初代のBLIPが今も使われています。
