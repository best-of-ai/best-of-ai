---
title: 'DeepSeek-Coder-33B'
name: 'DeepSeek-Coder-33B'
slug: 'deepseek-coder-33b'
subtitle: 'DeepSeek-Coder-V2の前に出た、DeepSeekのかつてのフラッグシップのコードモデル'
description: 'DeepSeek-Coder-V2の前に出た、DeepSeekのかつてのフラッグシップのコードモデル'
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-Coder'
price: 'Free'
rank: 6
release_date: '2023-11-02'
param_count: '33B'
context_window_tokens: 16384
modality: [text, code]
open_weight: true
license: 'DeepSeek License'
api_available: true
humaneval_score: 79.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-07-16'
tags: [code, open-weight, api, legacy]
i18n_source: 'e1d443d0e69c'
---

DeepSeek-Coder-33Bは、DeepSeekが2023年11月に公開したコード特化の言語モデルです。のちの推論モデルで同社が広く知られるようになる前のものです。コードと自然言語を主な内訳とする2兆トークンでゼロから学習しました。コンテキスト長は16,000トークンで、プロジェクト単位の学習により、断片的なスニペットだけでなく複数のファイルにまたがって推論できます。指示チューニング版は公開時にHumanEvalでpass@1が79.3%となり、当時のほとんどのオープンなコードモデルを上回り、コーディングのベンチマークではGPT-3.5に迫りました。コードエディタ向けのfill-in-the-middle補完に対応し、幅広いプログラミング言語を扱えます。その後DeepSeekは、より大きなMixture-of-Expertsモデルでコンテキスト長も長いDeepSeek-Coder-V2に置き換えましたが、33B版は自前でホストするためにHugging Faceで引き続き入手できます。
