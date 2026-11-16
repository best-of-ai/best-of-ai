---
title: 'GPT-OSS-120B'
name: 'GPT-OSS-120B'
slug: 'gpt-oss-120b'
subtitle: 'GPT-2以来初のOpenAIオープンウェイトモデル。多くの推論ベンチマークでo4-miniに並ぶ性能'
description: 'GPT-2以来初のOpenAIオープンウェイトモデル。多くの推論ベンチマークでo4-miniに並ぶ性能'
company: 'openai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://openai.com/index/introducing-gpt-oss/'
price: 'Free'
rank: 8
release_date: '2025-08-05'
param_count: '117B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 90.0
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Together AI', 'Azure AI Foundry']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: 'caa1902f73b4'
---
GPT-OSS-120Bは、OpenAIが2025年8月5日に公開したオープンウェイト推論モデルです。2019年のGPT-2以来、同社初のオープンモデルとなりました。混合エキスパート型Transformerを採用し、総パラメータ数は1,170億ですが、トークンごとに有効になるのは約51億です。そのため、同規模の高密度モデルに必要な複数GPUクラスターではなく、ハイエンドGPU 1基で推論負荷の高い処理を実行できます。公開時にMMLUで約90点を記録し、多くの推論・コーディングベンチマークでOpenAI自身のo4-miniと同程度でした。Apache 2.0ライセンスで提供され、企業は利用制限なしに自社環境で運用し、ファインチューニングできます。OpenAIがクローズドなモデルを続ける一方、オープンウェイト分野をリードしていたMeta、Mistral、DeepSeekやAlibabaのQwenチームに対抗するために開発されました。Hugging Face、Together AI、Azure AI Foundry、OpenAI APIから利用でき、自社運用とマネージド提供を選べます。
