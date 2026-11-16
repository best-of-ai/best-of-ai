---
title: 'Llama 5'
name: 'Llama 5'
slug: 'llama-5'
subtitle: '端末上とデータセンターの双方を想定したMeta次世代の主力オープンウェイト・マルチモーダルモデル'
description: '端末上とデータセンターの双方を想定したMeta次世代の主力オープンウェイト・マルチモーダルモデル'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 9
release_date: '2026-07-14'
param_count: '520B (24B active)'
context_window_tokens: 2000000
modality: [text, image, audio]
open_weight: true
license: 'Llama 4 Community License'
api_available: true
mmlu_score: 89.5
humaneval_score: 90.0
lmarena_score: 1381
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI', 'AWS Bedrock', 'Azure AI Foundry']
date: '2026-07-19'
tags: [llm, open-weight, multimodal, self-hosted, mixture-of-experts]
i18n_source: '47cdfc96510e'
---
Llama 5はMetaのLlama 4に続くモデルです。混合エキスパート方式を継承し、総パラメータ数5,200億、トークンごとの有効数は240億です。コンテキスト長は200万トークンで、Llama 4 Maverickの2倍となり、コードベース全体や長い動画の文字起こしを一度に処理できます。テキスト、画像、音声をネイティブに入力でき、テキストモデルへ後付けエンコーダーを足す構成ではありません。Metaによると、疎なエキスパート振り分けの効率を保ちながら公開ベンチマークでGemini 3.5 ProやGPT-5.6を上回ります。

過去のLlama同様、重みはLlama 4 Community Licenseで公開され、Hugging Faceからすぐ入手できます。Together AI、AWS Bedrock、Azure AI Foundryなどもマネージド推論を提供します。一定数以上のユーザーを持つ企業には完全な商用利用権を認めず、Llama 2以降と同じ例外があります。
