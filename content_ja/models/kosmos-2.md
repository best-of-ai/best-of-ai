---
title: 'Kosmos-2'
name: 'Kosmos-2'
slug: 'kosmos-2'
subtitle: '言語表現を画像内の具体的な領域に対応付けるMicrosoftのグラウンディング対応マルチモーダルモデル'
description: '言語表現を画像内の具体的な領域に対応付けるMicrosoftのグラウンディング対応マルチモーダルモデル'
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/microsoft/unilm/tree/master/kosmos-2'
price: 'Free'
rank: 5
release_date: '2023-06-26'
param_count: '1.6B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '327b99415fef'
---
Kosmos-2はMicrosoft Researchが2023年6月に発表したマルチモーダルモデルで、約16億のパラメータを持ちます。特徴はグラウンディングです。画像を文章で説明するだけでなく、出力中のフレーズを画像内の特定のバウンディングボックスに対応付けます。「犬」や「左側の椅子」についての文を、画像内の該当ピクセルに結び付けられます。このために構築したグラウンディング付き画像テキストデータセットGrITと、一般的なマルチモーダルコーパスで学習しました。参照表現の理解、フレーズのグラウンディング、標準的な視覚言語タスクで評価されています。製品ではなく研究成果として公開され、検出器を後付けするのではなく、言語モデル内でグラウンディングをエンドツーエンドに学習できることを示しました。コードと重みはMITライセンスでGitHubとHugging Faceに公開され、FlorenceやPhiの視覚言語モデルを含むMicrosoftの後続研究にもつながりました。
