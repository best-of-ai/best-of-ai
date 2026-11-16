---
title: 'GLM-5'
name: 'GLM-5'
slug: 'glm-5'
subtitle: 'すべて国産のHuaweiハードウェアで学習した、Zhipuのフロンティア級オープンウェイトモデル'
description: 'すべて国産のHuaweiハードウェアで学習した、Zhipuのフロンティア級オープンウェイトモデル'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-02-11'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 203000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.57
output_price_usd_per_m: 1.92
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-25'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
---

GLM-5は、Zhipu AIのフロンティア級オープンウェイトモデルで、2026年2月11日に公開されました。GLM-4.5からおよそ2倍にスケールアップし、総パラメータは3550億から約7440億になりましたが、エキスパート混合の設計でトークンあたりのアクティブは同程度の400億のままです。コンテキスト長は203,000トークンで、4か月後に後継のGLM-5.2が加える100万トークンには遠く及びません。学習にはNvidiaのハードウェアではなく、MindSporeフレームワークを使ってHuawei Ascendチップだけを使いました。APIの料金は、Zhipu自身のプラットフォームとWaveSpeed APIで、入力100万トークンあたり0.57ドル、出力100万トークンあたり1.92ドルからです。ライセンスはMITで、当時の報道では、完全に国産のハードウェアで作られた、中国の研究機関初のフロンティア級モデルと位置づけられました。
