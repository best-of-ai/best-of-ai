---
title: 'DeepSeek V4-Pro'
name: 'DeepSeek V4-Pro'
slug: 'deepseek-v4-pro'
subtitle: 'エージェント型のコーディングと大学院レベルの推論で首位に立った、2026年最高のオープンウェイトモデル'
description: 'エージェント型のコーディングと大学院レベルの推論で首位に立った、2026年最高のオープンウェイトモデル'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 9
release_date: '2026-04-24'
param_count: '1.6T (49B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 0.87
api_available: true
mmlu_score: 90.0
humaneval_score: 91.0
lmarena_score: 1390
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API', 'Together AI']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, coding, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: '3dcf4ddbbacd'
---

DeepSeek V4-ProはDeepSeekのフラッグシップモデルで、2026年4月24日に、小型のV4-Flashと同時に公開されました。総パラメータ数1.6兆、1トークンあたりの有効パラメータ数490億のMixture-of-Expertsモデルです。Compressed Sparse AttentionとHeavily Compressed Attentionを組み合わせたハイブリッドのアテンション設計を導入しており、V3.2と比べて推論の計算量とKVキャッシュのサイズを大きく減らします。これにより100万トークンのコンテキスト長を扱えます。段階的に推論する「thinking」モードと、素早く返す非thinkingモードの両方で動きます。DeepSeekは、数学、科学、エージェント型コーディングのベンチマークでオープンウェイトモデルの中で首位だと報告しており、SWE-bench Verifiedのスコアは80%を超えます。

DeepSeekのほかのモデルと同じく、V4-Proはオープンウェイトで、MITライセンスのもと公開されました。API料金は、OpenAI、Anthropic、Googleの同等のクローズドモデルよりはるかに低くなっています。2026年初めに欧米のラボが公開した最先端の推論モデルに対するDeepSeekの答えと位置づけられており、この公開は、オープンとクローズドの最先端モデルの差が縮まり続けている証拠として広く報じられました。
