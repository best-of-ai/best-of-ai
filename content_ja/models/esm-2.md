---
title: 'ESM-2'
name: 'ESM-2'
slug: 'esm-2'
subtitle: 'Metaのタンパク質言語モデル。配列から構造を予測するのに使われる'
description: 'Metaのタンパク質言語モデル。配列から構造を予測するのに使われる'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/protein-folding-esmfold-metagenomics/'
price: 'Free'
rank: 6
release_date: '2022-10-31'
param_count: '15B'
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [science, biology, open-weight]
---

ESM-2は、Meta AIが2022年10月に公開したタンパク質言語モデルです。約2億5000万のタンパク質配列で学習しており、多重配列アラインメントの工程は使いません。サイズは複数あり、最大は150億パラメータで、公開時点では最大のタンパク質言語モデルでした。Metaの調べでは、モデルを大きくすると、明示的に教えていなくても内部表現にタンパク質の3次元構造の情報が表れ始めます。この性質を使っているのがMetaの構造予測システムESMFoldです。ESMFoldはESM-2でタンパク質配列を読み、得られた表現をそのまま原子座標に変換します。AlphaFoldのようなツールが頼るアラインメントデータベースを使わないため、構造予測が大幅に速くなりました。Metaは重みを公開し、ESM-2を使って、これまで性質が調べられていなかった数億のタンパク質について予測構造を集めた公開データベース、ESM Metagenomic Atlasも作りました。
