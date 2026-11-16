---
title: 'Llama 2'
name: 'Llama 2'
slug: 'llama-2'
subtitle: 'オープンなLLMエコシステムを大きく前進させたMetaの2023年オープンウェイトモデル'
description: 'オープンなLLMエコシステムを大きく前進させたMetaの2023年オープンウェイトモデル'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2023-07-18'
param_count: '70B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
mmlu_score: 68.9
humaneval_score: 29.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '69c51717a945'
---
Llama 2はMetaの第2世代オープンウェイト言語モデルシリーズで、2023年7月18日に7B、13B、70Bの各サイズと、それぞれをチャット向けに調整した版が公開されました。2兆トークンで学習し、後の基準では短めの4,096トークンのコンテキスト長に対応しますが、公開当時は競争力がありました。70BモデルはMMLUで68.9を記録しGPT-3.5に近づきましたが、コード生成では差があり、HumanEvalはGPT-3.5の48.1に対して29.9でした。スコア以上に重要だったのはライセンスです。大半の企業に商用利用を認めたため、Llama 2は製品開発に使える初の本格的なオープンウェイトモデルとなり、Hugging Faceに並ぶファインチューニング版、量子化版、派生モデルの流れを生みました。Metaはその後Llama 3やLlama 4を公開しましたが、重みは数年後の現在も無料でダウンロードできます。
