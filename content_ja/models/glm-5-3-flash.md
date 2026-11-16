---
title: 'GLM-5.3-Flash'
name: 'GLM-5.3-Flash'
slug: 'glm-5-3-flash'
subtitle: '「Ox Alpha」の名で話題になったあとに正体が明かされた、Zhipu初のネイティブマルチモーダルなGLM-5モデル'
description: '「Ox Alpha」の名で話題になったあとに正体が明かされた、Zhipu初のネイティブマルチモーダルなGLM-5モデル'
company: 'zhipu-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Paid'
rank: 7
release_date: '2026-08-26'
param_count: '320B (MoE, 18B active)'
context_window_tokens: 1000000
modality: [text, image, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.15
output_price_usd_per_m: 0.5
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'API']
date: '2026-08-31'
tags: [llm, multimodal, coding, agentic, mixture-of-experts]
extra_model_types: ['Code']
---

Zhipu AIは2026年8月26日にGLM-5.3-Flashを正式に発表しました。テストプラットフォームに「Ox Alpha」の名前で匿名で出されていたモデルで、誰が作ったか分からない間に5日間で50兆トークンを超えるトラフィックを集めていたと、このとき明かしています。3200億パラメータのエキスパート混合モデルで、トークンあたりのアクティブは180億パラメータです。GLM-5シリーズで初のネイティブマルチモーダルで、疎な注意と線形の注意を組み合わせたハイブリッド設計を採り、コンテキスト長は100万トークンです。Zhipuは30兆トークンのマルチモーダルコーパスで事前学習させたとしています。効率とトークンあたりのコストはNvidia GPUのモデルと同等で、動かすのは中国国産のチップだと述べています。

価格はZhipu自身のGLM-5.3よりはるかに低く、定価で入力100万トークンあたり0.15ドル、出力100万トークンあたり0.50ドルです。発売記念の割引で、9月上旬までは約半額になります。GLM-5.3の公表価格の約10分の1にあたり、GLM-5.3-Flashは、Zhipuの主力プログラミングモデルの置き換えではなく、マルチモーダルやエージェントの作業向けの、安くて速い選択肢という位置づけです。
