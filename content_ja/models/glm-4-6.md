---
title: 'GLM-4.6'
name: 'GLM-4.6'
slug: 'glm-4-6'
subtitle: 'Zhipuの、日々のプログラミング向けのバリューティアのオープンウェイトモデル'
description: 'Zhipuの、日々のプログラミング向けのバリューティアのオープンウェイトモデル'
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 7
release_date: '2025-09-30'
param_count: '355B (MoE, ~32B active)'
context_window_tokens: 200000
modality: [text, image, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.43
output_price_usd_per_m: 1.75
api_available: true
humaneval_score: 85.0
lmarena_score: 1320
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
---

GLM-4.6は、Zhipu（Z.ai）のバリューティアのオープンウェイトモデルで、GLM-4.5の強化版として2025年9月30日に公開されました。エキスパート混合の設計で、総パラメータは約3550億、トークンあたりのアクティブは約320億です。コンテキスト長は128,000から200,000トークンに伸び、より長いエージェントのセッションに対応しました。テキスト、画像、コードを扱い、Claude Code、Cline、Roo Codeなどのコーディングアシスタント内でのツール利用向けに、Zhipuが特に調整しています。

プログラミングのベンチマークではオープンウェイト勢の上位に入り、LiveCodeBench v6で首位に立ち、エージェント系のいくつかのタスクではDeepSeek-V3.1-TerminusやClaude Sonnet 4と競っています。最大の売りは価格で、入力100万トークンあたり1ドルを大きく下回り、ほとんどのプロプライエタリな主力モデルより大幅に安いまま、実際のプログラミング作業に使えます。セルフホストやAPI経由の開発者向けツールによく登場するのは、このためです。
