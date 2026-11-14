---
title: 'CosyVoice'
name: 'CosyVoice'
slug: 'cosyvoice'
subtitle: 'Alibabaのオープンウェイトの、ゼロショット音声クローンと音声合成に対応したモデル'
description: 'Alibabaのオープンウェイトの、ゼロショット音声クローンと音声合成に対応したモデル'
company: 'alibaba'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://github.com/FunAudioLLM/CosyVoice'
price: 'Free'
rank: 5
release_date: '2024-07-09'
param_count: 'Undisclosed'
modality: [audio, text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Alibaba Cloud']
date: '2026-07-16'
tags: [text-to-speech, open-weight, voice-cloning, api]
i18n_source: '6cc55c56d545'
---

CosyVoiceはAlibabaのFunAudioLLMチームによる音声合成と音声クローンのモデルで、2024年7月にオープンウェイトとして公開されました。短い参照音声から音声を生成するので、数秒のサンプルがあれば声をクローンし、その声で任意のテキストを読み上げられます。対応言語は中国語、英語、日本語、韓国語など複数です。教師あり学習の意味的な音声トークンと、言語モデル型の生成方式を組み合わせており、話者ごとのファインチューンなしで、言語をまたぐクローンやゼロショットのクローンができます。Alibabaはその後もシリーズを更新し、より大きなベースモデルと低いレイテンシを備えたCosyVoice 2とCosyVoice 3を公開しました。初代はApache 2.0ライセンスのもと、Hugging FaceとAlibaba CloudのModel Studio APIから引き続き使えます。
