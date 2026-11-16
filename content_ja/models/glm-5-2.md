---
title: 'GLM-5.2'
name: 'GLM-5.2'
slug: 'glm-5-2'
subtitle: '2026年半ばにKimi K2.7と並んで公開された、Zhipuの主力オープンウェイトモデル'
description: '2026年半ばにKimi K2.7と並んで公開された、Zhipuの主力オープンウェイトモデル'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2026-06-13'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 1.4
output_price_usd_per_m: 4.4
api_available: true
mmlu_score: 91.72
humaneval_score: 88.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, coding, self-hosted]
extra_model_types: ['Code']
---

GLM-5.2は、Zhipu AIの主力オープンウェイトモデルで、2026年6月13日にMITライセンスで公開されました。エキスパート混合のモデルで、総パラメータは約7440億、トークンあたりのアクティブは約400億です。コンテキスト長は100万トークンで、前世代のGLM-4.6の128,000トークンを大きく上回ります。Zhipuは、長期にわたるプログラミングエージェント向けに作っていて、汎用のチャットではなく、エージェントによるソフトウェアエンジニアリングの場面で数か月かけて学習させました。

ベンチマークでは、MMLUが91.72%、GPQA Diamondが80.3%、SWE-bench Proが62.1%です。SWE-bench ProはGPT-5.5の報告値58.6%を上回っています。Zhipuが設定したAPIの価格は入力100万トークンあたり1.40ドル、出力100万トークンあたり4.40ドルで、同等のプロプライエタリモデルの料金のごく一部です。同社は、オープンウェイトであることとプログラミング性能の組み合わせを、OpenAIやAnthropicのクローズドなフロンティアモデルへの正面からの挑戦として打ち出しています。
