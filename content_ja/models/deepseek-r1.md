---
title: 'DeepSeek R1'
name: 'DeepSeek R1'
slug: 'deepseek-r1'
subtitle: '数学とコードでクローズドな最先端モデルに並んだ、DeepSeekの推論モデル'
description: '数学とコードでクローズドな最先端モデルに並んだ、DeepSeekの推論モデル'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-01-20'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.19
api_available: true
mmlu_score: 90.8
humaneval_score: 92.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, chain-of-thought]
i18n_source: 'fa3b02ee20e3'
---

DeepSeek R1は、中国のラボDeepSeekが2025年1月20日に公開した推論モデルです。6710億パラメータのMixture-of-Expertsアーキテクチャで、1トークンあたりの有効パラメータ数は370億です。教師ありファインチューンだけに頼らず、大規模な強化学習を一部取り入れて学習しており、これによって回答の前に問題を段階的に考え抜くようになりました。公開時には、数学、コーディング、科学のベンチマークでOpenAIのo1に並びました。MMLUのスコアは90.8で、AIMEやCodeforces形式の問題でも当時のモデルの最上位付近でした。それでいて重みはMITライセンスのオープンウェイトで公開され、APIの料金もo1よりはるかに低く設定されました。

この公開は、通常のAI研究の世界をはるかに越えて騒ぎになりました。DeepSeekのアプリが一時期、米国のApp Storeのランキング首位になりました。比較的小さな中国のラボが、通常よりずっと少ないコストで最先端クラスの推論モデルを学習したという話は、AI関連株を揺らしました。R1はDeepSeek自身のAPIとチャットから使えます。オープンウェイトなので自前でホストでき、Hugging Faceで広くミラーされ、サードパーティの推論プロバイダーからも提供されています。
