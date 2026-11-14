---
title: 'InternLM2'
name: 'InternLM2'
slug: 'internlm2'
subtitle: '長文脈と推論能力に優れたShanghai AI Labのオープンウェイト基盤モデル'
description: '長文脈と推論能力に優れたShanghai AI Labのオープンウェイト基盤モデル'
company: 'shanghai-ai-lab'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/InternLM/InternLM'
price: 'Free'
rank: 5
release_date: '2024-01-17'
param_count: '20B'
context_window_tokens: 200000
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.7
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, long-context]
i18n_source: 'e91b498370ff'
---
InternLM2はShanghai AI Laboratoryが開発したオープンウェイト言語モデルです。2024年1月17日に7Bと20Bのサイズ、およびそれぞれに対応するチャット版が公開されました。両サイズともコンテキスト長は20万トークンで、4Kトークンの系列から始めて32K以上へ段階的に広げる学習で実現しています。この長さの長文書に対するneedle-in-a-haystackテストでも良好な結果を示しました。20Bチャット版はMMLUで67.7点を記録し、公開当時、同規模の複数のオープンモデルを上回りました。英語と中国語に特に強い大規模な多言語コーパスで訓練され、Shanghai AI Labが同年後半にInternLM2.5を公開するまでは、推論、プログラミング、長文脈タスク向けの汎用基盤モデルとして位置づけられました。Apache 2.0ライセンスで公開され、Hugging FaceとInternLMのGitHubリポジトリから入手できます。
