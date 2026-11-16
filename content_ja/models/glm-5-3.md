---
title: 'GLM-5.3'
name: 'GLM-5.3'
slug: 'glm-5-3'
subtitle: 'Zhipuの、脆弱性の調査を重点的に調整したGLM-5.2のプログラミング向け更新'
description: 'Zhipuの、脆弱性の調査を重点的に調整したGLM-5.2のプログラミング向け更新'
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Paid'
rank: 7
release_date: '2026-08-14'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['GLM Coding Plan', 'API']
date: '2026-08-17'
tags: [llm, coding, cybersecurity, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
---

Zhipu AIは2026年8月14日にGLM-5.3を公開し、利用できるオープンウェイトのプログラミングモデルとして最も強いと述べています。ただし重みそのものは、発表から2週間後まで入手できません。基盤のアーキテクチャはGLM-5.2と同じなので、Zhipuが報告するプログラミング能力の約50パーセントの向上は、大きなモデルにしたからではなく、ポストトレーニングを拡張しただけで得られたものです。会社が特に挙げているのはセキュリティ面で、GLM-5.3はソースコードから脆弱性を見つけて検証するベンチマークのCyberGymで84.5パーセントを記録しました。AnthropicのClaude Mythosの83.8パーセント、OpenAIのGPT-5.6 Solの83.6パーセントをわずかに上回っています。Zhipuによると、社内のセキュリティチームはこのモデルで、269のプロジェクトから2,436件の脆弱性を見つけました。

現時点の利用経路は、ZhipuのGLM Coding Plan経由です。Claude Code、OpenCode、Zhipu自身のZCodeなどのプログラミングエージェントで動きます。先にAPIを提供し、あとからオープンウェイトを出すという段階的な展開は、ZhipuがGLMシリーズで以前から使っている方式です。
