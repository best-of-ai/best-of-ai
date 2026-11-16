---
title: 'DeepSeek V3'
name: 'DeepSeek V3'
slug: 'deepseek-v3'
subtitle: '競合の何分の一かのコストで学習した、DeepSeekの効率的なMixture-of-Expertsモデル'
description: '競合の何分の一かのコストで学習した、DeepSeekの効率的なMixture-of-Expertsモデル'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2024-12-26'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.27
output_price_usd_per_m: 1.1
api_available: true
mmlu_score: 88.5
humaneval_score: 82.6
lmarena_score: 1330
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, self-hosted]
extra_model_types: ['Code']
i18n_source: '3c9c049bbd9a'
---

DeepSeek V3は、DeepSeekが2024年12月26日に公開した、6710億パラメータのMixture-of-Expertsモデルで、1トークンあたりの有効パラメータ数は370億です。推論を行わないベースモデルで、V2と同じMulti-head Latent AttentionとDeepSeekMoEのアーキテクチャで作られています。DeepSeekはGPU時間で約560万ドルかけて学習したと報告しており、これは欧米のラボが同等のモデルに使っていた額よりはるかに低い数字です。MMLUは88.5、HumanEvalは82.6で、学習コストが低いにもかかわらず、多くのベンチマークでGPT-4oやClaude 3.5 Sonnetとほぼ同等でした。

V3はオープンウェイトでMITライセンスのもと公開され、DeepSeekはAPIの価格を競合の最先端モデルよりずっと低く設定しました。のちにR1の推論向け強化学習を積み上げるベースモデルとなっています。コスト効率の高さは、最先端レベルの性能に届くまでに実際どれだけの計算量が必要なのかをめぐって、業界全体の話題になりました。
