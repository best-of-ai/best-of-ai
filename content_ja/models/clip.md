---
title: 'CLIP'
name: 'CLIP'
slug: 'clip'
subtitle: '現代のマルチモーダルAIの多くの土台となった、OpenAIの基礎的な画像とテキストの対照学習モデル'
description: '現代のマルチモーダルAIの多くの土台となった、OpenAIの基礎的な画像とテキストの対照学習モデル'
company: 'openai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://openai.com/index/clip/'
price: 'Free'
rank: 8
release_date: '2021-01-05'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy, foundation-model]
i18n_source: 'bc970f441b1f'
---

CLIP(Contrastive Language-Image Pre-training)は、OpenAIが2021年1月に公開したモデルで、画像とテキストの説明を対応づけることを学習します。インターネットから集めた4億の画像とテキストのペアで学習しており、対応する画像とテキストのエンベディングを近づけ、対応しないペアを遠ざける、対照学習の目的関数を使っています。公開された最大のバリアントは、ViT-L/14の視覚Transformerと、6300万パラメータのテキストTransformerを組み合わせたもので、合計で約4億2800万パラメータです。CLIPは特定の狭いタスクのために学習するのではなく、画像とテキストの汎用的な共同エンベディング空間を学びます。そのため、タスク固有のファインチューニングなしに、画像をテキストのラベル群と比べて、ゼロショットの画像分類ができます。

CLIPが本当に大きな影響を与えたのは、公開後のことで、目立つベンチマークの数字によるものではありません。その画像とテキストのエンコーダは、DALL-E 2の画像生成パイプライン、Stable Diffusionのテキスト条件付け、数多くの画像検索ツールなど、後に続くシステムの土台になりました。MetaやSalesforceなどの研究所は独自のCLIPバリアントやファインチューンを公開しています。それでも、GitHubとHugging FaceでMITライセンスのもとで公開されているOpenAIの元の重みは、公開から何年たっても、マルチモーダルのプロジェクトの出発点として広く使われています。
