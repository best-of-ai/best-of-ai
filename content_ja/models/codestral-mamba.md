---
title: 'Codestral Mamba'
name: 'Codestral Mamba'
slug: 'codestral-mamba'
subtitle: 'Transformerの代わりにMambaの状態空間アーキテクチャで作られた、Mistralのコードモデル'
description: 'Transformerの代わりにMambaの状態空間アーキテクチャで作られた、Mistralのコードモデル'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral-mamba/'
price: 'Free'
rank: 6
release_date: '2024-07-16'
param_count: '7B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.25
output_price_usd_per_m: 0.25
api_available: true
humaneval_score: 75.0
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Mistral API']
date: '2026-07-16'
tags: [code, open-weight, api]
i18n_source: '071ce3f5be62'
---

Codestral Mambaは、Mistral AIが2024年7月に公開したコード生成モデルで、特徴はおもにそのアーキテクチャです。ほとんどすべてのコードモデルが使うTransformerではなく、状態空間モデルのアーキテクチャであるMambaで作られています。状態空間モデルは、系列長に対して2乗ではなく線形にスケールして系列を処理します。そのため、コンテキストが長くなっても、推論速度の低下が緩やかです。Mistralはおよそ70億パラメータで作り、256,000トークンのコンテキスト長を持たせました。同社は、その長さでも、コンテキスト内の検索が安定して働くと報告しています。

HumanEvalでは、Codestral Mambaはpass@1で約75パーセントで、はるかに大きなTransformerベースのコードモデルと競える水準です。Apache 2.0ライセンスで公開されており、重みを自由にダウンロードし、ファインチューンし、商用で使えます。MistralのAPIでも、入力と出力の100万トークンあたり0.25ドルで使えます。Mistralは、状態空間アーキテクチャが、実際のコーディングタスクでTransformerに並べることの実証だと位置づけました。大きなリポジトリを扱った推論のような、長いコンテキストの用途で、より速く安い推論ができるという点も挙げています。
