---
title: 'Kimi K2.6'
name: 'Kimi K2.6'
slug: 'kimi-k2-6'
subtitle: '長時間のエージェント処理とツール利用向けに設計されたMoonshotのオープンウェイトモデル'
description: '長時間のエージェント処理とツール利用向けに設計されたMoonshotのオープンウェイトモデル'
company: 'moonshot-ai'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-04-20'
param_count: '1T (32B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 0.6
output_price_usd_per_m: 2.5
api_available: true
mmlu_score: 88.0
humaneval_score: 87.0
lmarena_score: 1355
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, agentic, reasoning, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: 'f4220c32edb6'
---
Kimi K2.6はMoonshot AIのオープンウェイト主力モデルで、初代Kimi K2の後継として2026年4月に公開されました。総パラメータ数1兆、トークンあたり約320億を有効化するMixture of Expertsモデルです。低コストで推論できるようINT4形式でネイティブに提供され、コンテキスト長は262,144トークンです。長時間のエージェント処理を想定し、複数エージェントのオーケストレーション、人の介入なしで何時間も続くコーディング、後付けではないネイティブなマルチモーダル入力を中心に設計されています。Artificial Analysisの独立評価では、利用可能なオープンウェイトモデルの最上位に位置し、SWE-Bench ProやHumanity's Last ExamなどでOpenAIやAnthropicの非公開最先端モデルとの差は数ポイントでしたが、トークン単価はその一部です。改変MITライセンスで重みを公開しており、MoonshotのAPIを使わずダウンロードしてセルフホストできます。
