---
title: 'Codex'
name: 'Codex'
slug: 'codex'
subtitle: '初期のGitHub Copilotを支えた、OpenAIの最初のコード補完モデル'
description: '初期のGitHub Copilotを支えた、OpenAIの最初のコード補完モデル'
company: 'openai'
model_type: 'Code'
logo_url: ''
product_url: 'https://openai.com/index/openai-codex/'
price: 'Paid'
rank: 6
release_date: '2021-08-10'
param_count: '12B'
context_window_tokens: 4096
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: false
humaneval_score: 28.8
access_methods: [Research]
runs_at_home: false
platforms: ['API (deprecated)']
date: '2026-07-16'
tags: [code, legacy, foundation-model]
i18n_source: '2cde22dddd75'
---

Codexは、OpenAIで最初のコード生成専用モデルで、2021年8月に発表されました。GPT-3の流れをくみ、GitHubの公開ソースコード数十億行でファインチューンされています。公開された最大のバージョンは120億パラメータで、4,096トークンのコンテキスト長を持ちます。OpenAIのHumanEvalベンチマークでは、1回目で問題の28.8%を解き、問題ごとに100回サンプリングできる場合は77.5%まで上がりました。Codexは、2021年にGitHub Copilotが技術プレビューとして始まった際、その元のバージョンを動かしていたモデルです。LLMをチャットや補完のデモではなく、コーディングアシスタントとして大規模に展開した最初の例の1つになりました。OpenAIはプライベートベータのAPIとして数年間提供し、2023年3月に単体のCodex APIを終了して、その機能を後継のGPT-3.5とGPT-4ファミリーのモデルに取り込みました。名前は今も、OpenAIの新しいエージェント型のコーディング製品のブランドとして残っていますが、元のCodexモデルそのものは、APIからは使えません。
