---
title: 'DeepSeek-R1-Distill-Qwen-32B'
name: 'DeepSeek-R1-Distill-Qwen-32B'
slug: 'deepseek-r1-distill-qwen-32b'
subtitle: 'DeepSeek-R1の推論過程をQwenベースの小さなオープンモデルに蒸留したモデル'
description: 'DeepSeek-R1の推論過程をQwenベースの小さなオープンモデルに蒸留したモデル'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-R1'
price: 'Free'
rank: 6
release_date: '2025-01-20'
param_count: '32B'
context_window_tokens: 131072
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: '3cf96c55115c'
---

DeepSeek-R1-Distill-Qwen-32Bは、Qwen2.5-32Bを完全版のDeepSeek-R1が生成した推論過程でファインチューンして作った、320億パラメータの密結合モデルです。小さなモデルをゼロから学習する代わりに、DeepSeekはR1の連鎖的思考の出力を複数のベースモデルに蒸留しました。その中で32BのQwen版が、グループで最も強い結果になりました。規模は比較的控えめなのに、数学、コーディング、科学のベンチマークでOpenAIのo1-miniを上回りました。そのため、単体のハイエンドGPUで動かせるほど小さく、しかも本物の推論力を示した、最初期のオープンモデルの一つになりました。重みはR1ファミリーの他のモデルと同じくMITライセンスで公開されており、Hugging Faceで広くミラーされ、Together AIやGroqなどの推論プロバイダーからも使えます。

R1のような段階的な推論がほしいが、671Bの完全版に料金を払ったり自前でホストしたりはしたくない、というチームに向いています。標準的な密結合のtransformerでMixture-of-Expertsではないため、DeepSeekのフラッグシップモデルよりファインチューンも運用も簡単です。
