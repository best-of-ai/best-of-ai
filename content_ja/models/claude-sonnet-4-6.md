---
title: 'Claude Sonnet 4.6'
name: 'Claude Sonnet 4.6'
slug: 'claude-sonnet-4-6'
subtitle: 'Opus級の結果に迫りながら価格は5分の1を目指して作られた、AnthropicのデフォルトのSonnetモデル'
description: 'Opus級の結果に迫りながら価格は5分の1を目指して作られた、AnthropicのデフォルトのSonnetモデル'
company: 'anthropic'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.anthropic.com/news/claude-sonnet-4-6'
price: 'Paid'
rank: 9
release_date: '2026-02-17'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 3
output_price_usd_per_m: 15
api_available: true
lmarena_score: 1380
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Claude.ai', 'AWS Bedrock', 'Google Vertex AI', 'API']
date: '2026-07-25'
tags: [llm, reasoning, frontier-model, api, agentic]
extra_model_types: ['Code']
i18n_source: '1c6e036cc247'
---

Claude Sonnet 4.6は2026年2月17日に登場し、claude.aiと、Anthropicのワークスペース製品であるClaude Coworkで標準のモデルになりました。Opus 4.6と同じ100万トークンのコンテキスト長と128,000トークンの出力上限を備え、料金は入力が100万トークンあたり3ドル、出力が15ドルです。Opus 4.6の料金の約5分の1にあたります。SWE-bench Verifiedでは79.6パーセントで、価格差があるにもかかわらず、Opusモデルと数ポイント差でした。エージェント型のターミナル操作とコンピュータ操作のタスクを測るベンチマークでは、Terminal-Bench 2.0で59.1パーセント、OSWorld-Verifiedで72.5パーセントを記録しています。最大100ステップまで続けられる拡張推論の連鎖も組み込まれており、Opusの価格は払わずに、Opus級の信頼性がほしい開発者向けです。
