---
title: 'Command R Plus'
name: 'Command R Plus'
slug: 'command-r-plus'
subtitle: 'CohereのフラッグシップモデルでCommand Rの上位にあたる、RAGとツール利用向けに最適化されたモデル'
description: 'CohereのフラッグシップモデルでCommand Rの上位にあたる、RAGとツール利用向けに最適化されたモデル'
company: 'cohere'
model_type: 'Language'
logo_url: ''
product_url: 'https://cohere.com/blog/command-r-plus-microsoft-azure'
price: 'Free'
rank: 7
release_date: '2024-04-04'
param_count: '104B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'CC-BY-NC 4.0'
input_price_usd_per_m: 2.5
output_price_usd_per_m: 10
api_available: true
mmlu_score: 75.7
lmarena_score: 1250
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Cohere API', 'Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, retrieval-augmented, api]
i18n_source: '65043857657f'
---

Command R PlusはCohereがCommand Rの世代で出したフラッグシップモデルで、2024年4月に公開されました。コンテキスト長は128,000トークン、パラメータ数は1040億です。CohereはRAG、複数ステップのツール利用、多言語タスク向けに作り、Microsoft Azureと組んで公開しました。この世代の中で、強いRAG性能とエージェント的なツール呼び出しを両立させた最初期のモデルの一つです。MMLUのスコアは75.7です。重みはCC-BY-NC 4.0ライセンスと利用規定の追補付きでHugging Faceに公開されており、研究者は非商用であれば無料でダウンロードして動かせます。商用で使うには別途ライセンスを取るか、CohereのホスティングAPIを使います。APIの料金は入力が100万トークンあたり2.50ドル、出力が10ドルです。Cohereのラインナップでは小型のCommand Rの上に位置し、2025年にCommand Aに引き継がれました。
