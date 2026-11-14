---
title: 'Florence-2'
name: 'Florence-2'
slug: 'florence-2'
subtitle: 'Microsoftのコンパクトな視覚基盤モデル。キャプション生成、検出、セグメンテーションを1つで扱う'
description: 'Microsoftのコンパクトな視覚基盤モデル。キャプション生成、検出、セグメンテーションを1つで扱う'
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.microsoft.com/en-us/research/publication/florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks/'
price: 'Free'
rank: 6
release_date: '2024-06-15'
param_count: '0.77B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Azure AI Foundry']
date: '2026-07-16'
tags: [computer-vision, open-weight, multimodal]
---

Florence-2は、Microsoft Researchが2024年6月に公開した視覚基盤モデルです。キャプション生成、物体検出、セグメンテーション、視覚的グラウンディングを、タスクごとに別のモデルを用意せず、1つのモデルでこなせるように作られています。プロンプトベースの方式を取り、統一されたsequence-to-sequenceアーキテクチャのもと、同じネットワークが、与えられたテキストの指示に応じてキャプション、バウンディングボックスの集合、セグメンテーションマスクのどれかを出力します。Microsoftは2つのサイズで公開しました。2億3000万パラメータのベース版と、7億7000万パラメータのラージ版で、どちらも一般的な視覚言語モデルと比べるとごく小さい規模です。学習にはFLD-5Bを使いました。Microsoftの社内データセットで、約1億2600万枚の画像と54億のアノテーションを含みます。これのおかげで、この小ささのモデルでも、COCOのキャプション生成や参照表現の理解といったタスクで、より大きな専用モデルに並ぶか、それを上回れます。Microsoftは重みをMITライセンスでHugging Faceに公開し、Azure AI Foundry経由でも提供しています。大きなマルチモーダルLLMを動かさずに視覚の機能がほしいチームに、よく選ばれています。
