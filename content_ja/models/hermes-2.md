---
title: 'Hermes 2'
name: 'Hermes 2'
slug: 'hermes-2'
subtitle: 'Nous Researchが初期に公開したオープンウェイトのファインチューニングモデル群'
description: 'Nous Researchが初期に公開したオープンウェイトのファインチューニングモデル群'
company: 'nous-research'
model_type: 'Language'
logo_url: ''
product_url: 'https://nousresearch.com/'
price: 'Free'
rank: 3
release_date: '2024-02-01'
param_count: '34B'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fine-tune, self-hosted]
i18n_source: '539b85db9ee0'
---
Hermes 2は、独立系AI研究グループNous Researchが公開したオープンウェイトのファインチューニングモデル群です。同社は基盤モデルを一から作るのではなく、高性能な基盤モデルを選び、厳選した指示・会話データで再訓練することで知られています。Mistral 7B、Mixtral 8x7Bをベースにした版と、Yi-34Bをベースにした34B版があり、最大モデルのコンテキスト長は基盤モデルを引き継いだ4,096トークンです。Nousは一般的なアシスタント動作、関数呼び出し、商用チャットボットに比べた拒否の少なさを目指し、合成データと人が選別した会話で訓練しました。Apache 2.0で公開され、Hugging Faceから配布されています。llama.cppやOllamaなどを使ったローカル実行で、オープンソースLLMコミュニティに広まりました。後継のHermes 3は同じ調整手法をLlama 3.1など、より大規模で高性能な基盤モデルに適用しました。
