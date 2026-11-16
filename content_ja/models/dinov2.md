---
title: 'DINOv2'
name: 'DINOv2'
slug: 'dinov2'
subtitle: 'ラベルなしで汎用的な画像特徴を作り出す、Metaの自己教師ありのビジョンモデル'
description: 'ラベルなしで汎用的な画像特徴を作り出す、Metaの自己教師ありのビジョンモデル'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/dino-v2-computer-vision-self-supervised-learning/'
price: 'Free'
rank: 6
release_date: '2023-04-17'
param_count: '1.1B'
modality: [image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [computer-vision, open-weight, self-supervised]
i18n_source: '35d54331b555'
---

DINOv2はMeta AIが2023年4月に公開したコンピュータビジョンのモデルで、LVD-142Mと呼ばれる1億4200万枚の画像を選んだデータセットで、ラベルなしで学習されています。あらかじめ決まったカテゴリに画像を分類するのではなく、自己教師ありの蒸留によって汎用的な視覚特徴を学習します。その特徴は画像分類、深度推定、セグメンテーション、検索など幅広い下流のタスクでよく働き、ファインチューンなしでも使えることが多いです。公開された最大のモデルは11億パラメータです。

特徴がそのままよく転用できるため、DINOv2はほかのコンピュータビジョンシステムの共通のバックボーンになりました。ラベル付きデータが少ない医療画像のような分野でも使われています。Metaはコードとモデルの重みをApache 2.0ライセンスで公開し、のちにDINOv3を出しましたが、DINOv2は汎用の視覚特徴の抽出器として今も広く使われています。
