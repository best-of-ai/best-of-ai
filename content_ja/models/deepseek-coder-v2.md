---
title: 'DeepSeek Coder V2'
name: 'DeepSeek Coder V2'
slug: 'deepseek-coder-v2'
subtitle: 'DeepSeekのオープンウェイトの、コードに特化したMixture-of-Expertsモデル'
description: 'DeepSeekのオープンウェイトの、コードに特化したMixture-of-Expertsモデル'
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2024-06-17'
param_count: '236B (21B active)'
context_window_tokens: 128000
modality: [text, code]
open_weight: true
license: 'MIT'
api_available: true
humaneval_score: 90.2
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '5e8d9823340f'
---

DeepSeek-Coder-V2はDeepSeekの第2世代のコードモデルで、2024年6月に公開されました。Mixture-of-Expertsモデルで、総パラメータ数は2360億、1トークンあたりの有効パラメータ数は210億です。コンテキスト長は初代DeepSeek-Coderの16,000トークンから128,000トークンへと大きく延び、対応するプログラミング言語も86から338に増えました。HumanEvalでは90.2%を記録し、DeepSeekは当時、コーディングタスクでGPT-4 Turboのようなクローズドモデルとの差を縮めたと説明しました。前作と比べて、一般的な推論や数学のベンチマークも向上しています。初代DeepSeek-Coderのより厳しいライセンスとは違い、DeepSeek-Coder-V2はMITライセンスで公開されており、商用プロジェクトでも自由に使えます。重みはHugging Faceにあり、DeepSeek自身のプラットフォームからAPIでも使えます。
