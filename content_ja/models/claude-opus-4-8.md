---
title: 'Claude Opus 4.8'
name: 'Claude Opus 4.8'
slug: 'claude-opus-4-8'
subtitle: '深い分析と長期的なタスク向けの、Anthropicで最も高性能なOpus階層のモデル'
description: '深い分析と長期的なタスク向けの、Anthropicで最も高性能なOpus階層のモデル'
company: 'anthropic'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.anthropic.com/news/claude-opus-4-8'
price: 'Paid'
rank: 9
release_date: '2026-05-28'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 5
output_price_usd_per_m: 25
api_available: true
mmlu_score: 92.4
humaneval_score: 92.5
lmarena_score: 1415
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, reasoning, frontier-model, api]
extra_model_types: ['Code']
i18n_source: '9185c0fd20db'
---

Claude Opus 4.8は、Anthropicでもっとも高性能なOpus階層のモデルで、2026年5月28日に公開されました。Opus 4.7のアップデートで、そのモデルのコメントの冗長さやツール呼び出しの癖のいくつかを直しています。SWE-bench Verifiedで約88.6パーセント、より難しいSWE-bench Proで69.2パーセントを記録し、公開時点では同じテストでGPT-5.5とGemini 3.1 Proを上回りました。Anthropicによると、根拠のない主張を自信ありげに述べるのではなく、自分の不確かさを示す傾向が強まっています。100万トークンの入力コンテキスト長と、最大128,000トークンの出力に対応しています。Claude Codeでは、リサーチプレビュー機能のDynamic Workflowsが加わりました。モデルが大きなタスクを計画し、1つのセッションで数百の並列サブエージェントを動かせる機能です。料金は前のバージョンから変わらず、入力が100万トークンあたり5ドル、出力が25ドルで、より速い「ファストモード」は10ドル/50ドルです。
