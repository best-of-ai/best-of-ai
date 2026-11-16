---
title: 'InternVL2'
name: 'InternVL2'
slug: 'internvl2'
subtitle: '独自のマルチモーダルモデルと競うShanghai AI Labのオープン視覚言語モデル群'
description: '独自のマルチモーダルモデルと競うShanghai AI Labのオープン視覚言語モデル群'
company: 'shanghai-ai-lab'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/OpenGVLab/InternVL'
price: 'Free'
rank: 6
release_date: '2024-07-04'
param_count: '76B (flagship; family spans 1B-108B)'
context_window_tokens: 8192
modality: [text, image, video]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: '75f0788941ee'
---
InternVL2はShanghai AI LaboratoryのOpenGVLabが開発したオープン視覚言語モデル群で、2024年7月4日に公開されました。1Bから最大108B（76B InternViTとLlama 3 70B）までのサイズがあります。InternViT視覚エンコーダーと言語モデルを組み合わせ、最上位のInternVL2-Llama3-76BはMMMUベンチマークで62.0％を記録しました。当時GPT-4oと並ぶ結果で、DocVQAやChartQAなど文書・図表理解タスクでは他のオープンマルチモーダルモデルを上回りました。静止画だけでなく、動画のフレームを抽出して内容を推論でき、文書処理や比較タスク向けに複数画像の入力にも対応します。MITライセンスで重みをHugging Faceから公開し、当時はGPT-4oやGeminiなどのクローズドシステムに対抗する有力なオープンモデルでした。2024年12月には後継のInternVL2.5を公開し、最大モデルのMMMUスコアは70％を超えました。
