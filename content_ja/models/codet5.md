---
title: 'CodeT5+'
name: 'CodeT5+'
slug: 'codet5'
subtitle: 'Salesforceのオープンウェイトの、エンコーダ・デコーダ型のコードモデルファミリー'
description: 'Salesforceのオープンウェイトの、エンコーダ・デコーダ型のコードモデルファミリー'
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeT5'
price: 'Free'
rank: 3
release_date: '2023-05-13'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
humaneval_score: 30.9
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '20777365e144'
---

CodeT5+は、Salesforce Researchが作ったオープンウェイトのコードモデルのファミリーで、元のCodeT5エンコーダ・デコーダモデルの後継として2023年5月に公開されました。サイズは2億2000万から160億パラメータまであり、エンコーダのみ、デコーダのみ、完全なエンコーダ・デコーダのいずれのモードでも動かせます。1つのアーキテクチャで、欠陥検出のようなコード理解のタスクと、コード補完やテキストからコードへの合成のような生成タスクを、どちらも扱えます。学習では、スパンのノイズ除去、因果言語モデリング、対照学習、テキストとコードのマッチングという目的を組み合わせています。Salesforceによると、この手法により、同程度のサイズのデコーダのみのコードモデルより、検索拡張生成のタスクで優位に立てます。16BバリアントのHumanEvalのpass@1は約30.9%で、同じチェックポイントのインストラクションチューニング版は35%を超え、同じベンチマークでOpenAIの古いcode-cushman-001モデルを上回ります。重みはBSD-3-Clauseライセンスのもと、Hugging Faceにあります。CodeT5+は、Codex時代のプロプライエタリなコードモデルに代わる、完全にオープンな選択肢の初期の1つです。
