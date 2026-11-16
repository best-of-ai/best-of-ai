---
title: 'Dolly 2.0'
name: 'Dolly 2.0'
slug: 'dolly-2-0'
subtitle: 'Databricksが初めて出した、完全にオープンで商用利用できる指示追従モデル'
description: 'Databricksが初めて出した、完全にオープンで商用利用できる指示追従モデル'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm'
price: 'Free'
rank: 5
release_date: '2023-04-12'
param_count: '12B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: '24b60e23db79'
---

Dolly 2.0は、Databricksが2023年4月12日に公開した120億パラメータの指示追従型の言語モデルで、EleutherAIのPythiaモデルの上に作られています。注目された点は性能そのものではありません。性能は当時のGPT-3.5にかなり及びませんでした。注目されたのはライセンスです。Databricksはモデルの重み、学習コード、databricks-dolly-15kという新しい指示データセットをオープンソースにし、すべて商用利用が認められました。この1万5000件のデータセットは、約5000人のDatabricks社員がゼロから書いたものです。それ以前のオープンな指示チューニング済みモデルが頼っていた、OpenAIの出力から作ったデータセットに付くライセンス上の制限を避けるためでした。

Databricksは、同程度の性能のオープンモデルの大半が研究用のみのライセンスだった時期に、Dolly 2.0を、制限の厳しい条件なしで有用な指示追従モデルを作って共有できることの証明と位置づけました。今の指示チューニング済みモデルと比べると競争力はありませんが、クローズドな商用チャットボットに代わる完全にオープンな選択肢として、早い時期に影響を与えた例です。
