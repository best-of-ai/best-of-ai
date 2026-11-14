---
title: 'Mistral 7B'
name: 'Mistral 7B'
slug: 'mistral-7b'
subtitle: '大規模な競合モデルを上回ったMistral初の小型オープンウェイトモデル'
description: '大規模な競合モデルを上回ったMistral初の小型オープンウェイトモデル'
company: 'mistral-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://mistral.ai/news/announcing-mistral-7b/'
price: 'Free'
rank: 6
release_date: '2023-09-27'
param_count: '7B'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 60.1
humaneval_score: 30.5
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, small-model, self-hosted]
extra_model_types: ['Code']
i18n_source: 'c7cb93d8e531'
---
Mistral 7BはMistral AIを広く知らしめたモデルで、フランスのスタートアップが2023年9月27日に初めて公開しました。70億パラメータと小さく、一般向けGPU1台で動かせる一方、Mistralが試したすべてのベンチマークでLlama 2 13Bを上回り、推論とプログラミングの複数タスクではLlama 2 34Bも超えました。MMLUで60.1％、HumanEvalで30.5％を記録しています。Grouped-query attentionとsliding-window attentionを使い、3万2,000トークンのコンテキストでも高速でメモリ効率のよい推論を実現します。

Apache 2.0ライセンスで利用制限なく公開されました。当時、この品質のモデルとしては珍しく、Hugging FaceやOllama、llama.cppなどを通じてオープンソースコミュニティに急速に広まりました。ファインチューニングやモデル統合の基盤として広く使われ、公開から数か月でMistral AIをMetaやOpenAIに対抗する企業として確立しました。
