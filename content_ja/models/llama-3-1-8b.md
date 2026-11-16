---
title: 'Llama 3.1 8B'
name: 'Llama 3.1 8B'
slug: 'llama-3-1-8b'
subtitle: 'Llama 3.1世代のコンパクトモデル'
description: 'Llama 3.1世代のコンパクトモデル'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2024-07-23'
param_count: '8B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
mmlu_score: 69.4
humaneval_score: 72.6
lmarena_score: 1180
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
extra_model_types: ['Code']
i18n_source: 'fa37d1d53ede'
---
Llama 3.1 8Bは、2024年7月の同シリーズで最小のモデルです。1基のGPU、または高性能ノートPCで実用的なモデルを動かしたい人向けに設計されています。上位モデルと同じ128,000トークンのコンテキスト長と多言語学習に対応します。学習データの増加と事後学習の改善により、MMLUとHumanEvalのスコアは元のLlama 3 8Bを上回ります。70Bや405Bでは過剰、あるいは提供コストが高すぎる用途で、開発者は端末内アシスタント、低価格のバッチ処理、ファインチューニング実験に使っています。Ollamaなどのツールで簡単に動かせ、Hugging Faceで最も多くダウンロードされるモデルの1つです。
