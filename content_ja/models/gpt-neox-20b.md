---
title: 'GPT-NeoX-20B'
name: 'GPT-NeoX-20B'
slug: 'gpt-neox-20b'
subtitle: '当時最大級の公開チェックポイントの1つとなったEleutherAIのオープンウェイトモデル'
description: '当時最大級の公開チェックポイントの1つとなったEleutherAIのオープンウェイトモデル'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 4
release_date: '2022-04-14'
param_count: '20B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
i18n_source: '3f0cef2ef3c0'
---
GPT-NeoX-20Bは200億パラメータの言語モデルです。EleutherAIは、MegatronとDeepSpeedを基盤に独自開発した学習フレームワークGPT-NeoXを約1年かけて整備し、2022年4月に発表しました。公開時点では、重みをダウンロードできる最大の高密度自己回帰型言語モデルでした。The Pileで学習し、コンテキスト長は2,048トークンです。EleutherAI独自の評価環境では、多くの標準NLPベンチマークでOpenAIのCurieとDavinciの中間に位置し、数学文章題のワンショット評価ではGPT-3の175B版を上回りました。チームはこの結果を、学習データの質がモデル規模と同じほど重要である証拠として紹介しました。Apache 2.0ライセンスでHugging Faceから公開され、研究者はクローズドAPIへのアクセスなしに大規模モデルを調べ、ファインチューニングできました。後にさらに大きく効率的なオープンモデルが登場しましたが、オープンソースLLM研究の基盤となった学習コードの参照例として影響を残しました。
