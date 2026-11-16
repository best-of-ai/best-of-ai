---
title: 'CodeGen2'
name: 'CodeGen2'
slug: 'codegen2'
subtitle: 'インフィリングと複数ターンのプログラム合成向けの、Salesforceのオープンウェイトのコードモデル'
description: 'インフィリングと複数ターンのプログラム合成向けの、Salesforceのオープンウェイトのコードモデル'
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeGen2'
price: 'Free'
rank: 5
release_date: '2023-05-03'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [code, open-weight]
i18n_source: '19442e527069'
---

CodeGen2は、Salesforce Researchの第2世代のオープンなコードモデルのファミリーで、元のCodeGenの後継として2023年5月に公開されました。サイズは1B、3.7B、7B、16Bパラメータの4種類です。最初のCodeGenからの主な改良点は、インフィリングに対応したことです。左から右へテキストを生成するだけでなく、前後の文脈をもとに、抜けているコードの一部を埋められます。そのため、既存のファイルの途中にコードを書く必要があるオートコンプリートやコード修復のような、実際のエディタのワークフローに向いています。

モデルは、自然言語と多くのプログラミング言語のソースコードを混ぜて学習しており、寛容なApache 2.0ライセンスで、Hugging FaceとGitHubから公開されています。CodeGen2は約2,000トークンの作業コンテキストでテストされました。今の基準では控えめですが、当時のコードモデルとしては標準的でした。SalesforceはCodexのようなクローズドなコードモデルに代わる、研究者が使いやすい選択肢として位置づけています。その後、より大きな前身モデルの性能に合わせて調整された、小型のCodeGen2.5が続きました。
