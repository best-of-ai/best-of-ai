---
title: 'BLIP-2'
name: 'BLIP-2'
slug: 'blip-2'
subtitle: 'Salesforceによる、BLIPのより効率的な後継。固定したエンコーダから視覚言語の事前学習を立ち上げる'
description: 'Salesforceによる、BLIPのより効率的な後継。固定したエンコーダから視覚言語の事前学習を立ち上げる'
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/LAVIS/tree/main/projects/blip2'
price: 'Free'
rank: 6
release_date: '2023-01-30'
param_count: '3.7B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '8456e2d29321'
---

BLIP-2は、Salesforce Researchが2023年1月に発表した視覚言語モデルで、効率を上げる工夫を中心に作られています。大きな画像エンコーダと言語モデルを一緒にゼロから学習するのではなく、事前学習済みの画像エンコーダと言語モデルの両方を固定し、その間をつなぐ軽量なコネクタ、Q-Formerだけを学習します。Q-Formerの学習可能なパラメータは約1億8,800万で、モデル全体の2%未満です。そのため、BLIP-2は当時の同等の視覚言語モデルよりはるかに安く学習でき、それでいて画像のキャプション生成や視覚的な質問応答で良い成績でした。Salesforceは、Q-Formerを異なる固定された言語モデルと組み合わせた複数の版を公開しました。OPT（2.7Bと6.7Bパラメータ）やFlan-T5（最大11Bパラメータ）をベースにしたものがあり、性能と計算コストのどちらを取るかを選べます。コードと重みはMITライセンスで、SalesforceのLAVISライブラリの一部としてGitHubとHugging Faceにあります。固定したエンコーダと軽量なコネクタという、BLIP-2が広めた手法は、すべてを同時に学習するのではなく、既存の言語モデルに視覚の機能を後付けする、その後のマルチモーダルモデルに影響を与えました。
