---
title: 'InternLM2.5'
name: 'InternLM2.5'
slug: 'internlm2-5'
subtitle: 'ツール利用と推論を強化したShanghai AI LabのInternLM更新版'
description: 'ツール利用と推論を強化したShanghai AI LabのInternLM更新版'
company: 'shanghai-ai-lab'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-07-03'
param_count: '7B (1.8B and 20B variants also released)'
context_window_tokens: 1000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 72.8
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, long-context]
i18n_source: '4f1fc404afae'
---
InternLM2.5はShanghai AI LaboratoryのInternLM2後継モデルです。2024年7月3日から7B版と1.8B版を公開し、8月1日に20B版を追加しました。開発元のOpenCompass評価によると、7BチャットモデルはMMLUで72.8点を記録し、複数の推論・数学ベンチマークでLlama 3 8B InstructやGemma 2 9Bを上回りました。専用の7B-Chat-1Mチェックポイントはコンテキスト長を100万トークンに広げ、needle-in-a-haystackテストでは100万トークンの文書から特定の事実を見つけられます。一方、標準の20Bモデルは最大20万トークンです。初代InternLM2より関数呼び出しとエージェント型のツール利用も強化されました。すべての重みはApache 2.0ライセンスで、Hugging FaceとInternLMのGitHubリポジトリから公開されています。
