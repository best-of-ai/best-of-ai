---
title: 'Cerebras-GPT'
name: 'Cerebras-GPT'
slug: 'cerebras-gpt'
subtitle: 'Cerebrasが自社のウェハスケールチップで学習させた、完全オープンのモデルファミリー'
description: 'Cerebrasが自社のウェハスケールチップで学習させた、完全オープンのモデルファミリー'
company: 'cerebras'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.cerebras.ai/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models'
price: 'Free'
rank: 3
release_date: '2023-03-28'
param_count: '13B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, fully-open, self-hosted]
i18n_source: 'ff8674011b4e'
---

Cerebras-GPTは、パラメータ数が1億1100万から130億までの言語モデルのファミリーです。Cerebrasが自社のCS-2ウェハスケールシステムで学習させ、2023年3月に公開しました。このプロジェクトの狙いはベンチマークで勝つことよりも、公開の徹底にありました。Cerebrasは、ファミリー全サイズ分の重み、学習コード、ハイパーパラメータとスケーリングの挙動を記した詳細な技術レポートを公開しています。学習はChinchillaと同様の計算最適なレシピに従っています。そのため、当時もっとも文書が整ったオープンモデルのファミリーの1つとなり、スケーリング則を調べたい研究者にとって、再現しやすい基準として役立ちました。

Cerebras-GPTのチェックポイントはすべてApache 2.0で公開され、Hugging Faceにあります。商用でも研究でも無料で使えます。モデルは標準的なGPT型のアーキテクチャで、コンテキスト長は2,048トークンです。2023年の水準では、LLaMAなどと比べて素の性能は控えめでした。Cerebrasがベンチマークの最高値を狙うより、透明で再現できる学習を優先したためです。現在は主にスケーリング則の研究で引用されるほか、AIハードウェア企業が自社チップでモデル群を丸ごと学習してオープンソースにした例として挙げられます。
