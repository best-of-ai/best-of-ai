---
title: 'DeepSeek-V2'
name: 'DeepSeek-V2'
slug: 'deepseek-v2'
subtitle: '2024年にAPI価格で競合を下回った、DeepSeekのMixture-of-Expertsモデル'
description: '2024年にAPI価格で競合を下回った、DeepSeekのMixture-of-Expertsモデル'
company: 'deepseek'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 5
release_date: '2024-05-06'
param_count: '236B (21B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'DeepSeek License'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
mmlu_score: 78.5
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts, legacy]
i18n_source: '988dda9730f9'
---

DeepSeek-V2はDeepSeekが2024年5月に公開したMixture-of-Expertsの言語モデルで、総パラメータ数は2360億、1トークンあたりの有効パラメータ数は210億です。技術面での主な貢献はMulti-head Latent Attentionで、これはキーと値のキャッシュを圧縮する手法です。メモリ使用量を大きく減らし、同じハードウェアで、DeepSeekのそれまでの密結合67Bモデルよりずっと多くのトークンを毎秒処理できるようになりました。8.1兆トークンで学習し、コンテキスト長は128Kです。MMLUやコーディングのベンチマークでは、当時の他のオープンモデルと競える成績でした。

V2が注目された理由はアーキテクチャだけでなく、価格にもありました。DeepSeekは、中国や欧米の競合が付けていた価格のごく一部でAPIを始めました。これをきっかけに業界全体で値下げが相次ぎ、当時の論者はそれを「価格戦争」と呼びました。ここで導入されたMLAとDeepSeekMoEの手法は、V3やR1を含むその後のすべてのDeepSeekモデルに引き継がれました。V2は、同社のその後の最先端モデルの土台になったアーキテクチャです。
