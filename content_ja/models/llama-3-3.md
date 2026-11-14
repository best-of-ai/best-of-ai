---
title: 'Llama 3.3'
name: 'Llama 3.3'
slug: 'llama-3-3'
subtitle: 'より大きな前世代モデルに匹敵する効率的なMetaの70Bオープンウェイトモデル'
description: 'より大きな前世代モデルに匹敵する効率的なMetaの70Bオープンウェイトモデル'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 7
release_date: '2024-12-06'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.3 Community License'
api_available: true
mmlu_score: 86.0
humaneval_score: 88.4
lmarena_score: 1270
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, foundation-model]
extra_model_types: ['Code']
i18n_source: '00af49010fb3'
---
Llama 3.3はMetaが2024年12月に公開した70Bのテキストモデルで、Llama 3.1 70Bをそのまま置き換える更新版です。パラメータ数を増やさず、新しい事後学習手法で調整しました。その結果、6倍ほど大きい同世代の405Bモデルに対し、指示追従と数学で匹敵または上回ります。HumanEvalとMMLUのスコアもLlama 3.1 70Bから向上し、独立ベンチマークでは日常的なタスクで他社の同時期のモデルに対して良好な性能を示しました。405Bより実行コストが大幅に低いため、低価格で主力級の品質を求めるチームに選ばれ、Together AIやGroqなどの推論サービスで広く使われるようになりました。
