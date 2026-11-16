---
title: 'Granite 3.0'
name: 'Granite 3.0'
slug: 'granite-3-0'
subtitle: '規制業界向けにIBMが公開したオープンウェイトの企業モデルファミリー'
description: '規制業界向けにIBMが公開したオープンウェイトの企業モデルファミリー'
company: 'ibm'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 5
release_date: '2024-10-21'
param_count: '2B, 8B (dense); 1B, 3B (MoE)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 65.5
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'IBM watsonx']
date: '2026-07-16'
tags: [llm, open-weight, enterprise, self-hosted]
i18n_source: '2ebc701cde02'
---
Granite 3.0は、IBMが2024年10月21日に公開した第3世代のオープン言語モデル群です。カスタマーサービス、サイバーセキュリティ、RAGパイプラインなどの企業用途を想定しています。12兆トークンで学習した高密度の2B・8Bモデルと、1B・3Bの混合エキスパート版があり、すべてApache 2.0ライセンスで提供されます。制限なくファインチューニングして商用展開できます。IBMはMetaやMistralの同規模モデルと競合する製品として位置づけ、一般的なGPUで低コストに動作する小型モデルを保ちながら、推論、コード、数学のベンチマークで同等以上のスコアを報告しました。初期版のコンテキスト長は4Kで、2024年12月のGranite 3.1更新で128Kに拡張されました。Hugging Face、Ollama、IBM watsonxから利用でき、Granite Guardian、Code、Vision各モデルの基盤にもなっています。
