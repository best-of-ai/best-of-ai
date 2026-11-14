---
title: 'GLM-4'
name: 'GLM-4'
slug: 'glm-4'
subtitle: 'Zhipuの2024年の汎用オープンウェイトモデル'
description: 'Zhipuの2024年の汎用オープンウェイトモデル'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 5
release_date: '2024-06-05'
param_count: '9B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.4
humaneval_score: 71.8
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted]
---

GLM-4は、Zhipu AIが2024年6月に公開したオープンウェイトモデルで、GLM-4-9Bとして、ベース、チャット、長いコンテキスト長の各バリエーションが配布されています。90億パラメータなので、高性能なGPU1枚で動かせる大きさです。それでもZhipuは、意味理解、数学、推論、コードの評価で、MetaのLlama 3 8Bを上回ったと報告しています。チャット版は、Webブラウジング、コード実行、関数呼び出しによるカスタムツールの呼び出しにも対応し、コンテキスト長は128,000トークンまで伸びます。

中国語と英語に加えて、日本語、韓国語、ドイツ語を含む26言語に対応したため、Zhipuの本拠地の外でも使われるようになりました。ライセンスはApache 2.0で、Hugging Faceでよく使われる小型オープンウェイトモデルの1つになりました。のちにZhipuがGLM-4-Plus、GLM-4.5、GLM-4.6へと拡大していく土台のアーキテクチャも、このモデルで定まりました。
