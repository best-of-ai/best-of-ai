---
title: 'Llama Guard 2'
name: 'Llama Guard 2'
slug: 'llama-guard-2'
subtitle: 'Llama Guard 3に先行するMetaのコンテンツ安全性分類モデル'
description: 'Llama Guard 3に先行するMetaのコンテンツ安全性分類モデル'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-llama-3/'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [safety, open-weight, legacy]
i18n_source: '1ec3f0456e4e'
---
Llama Guard 2はMetaが2024年4月にLlama 3とともに公開した安全性分類モデルです。汎用チャットではなく、Llama 3の80億パラメータ版を基盤としています。LLMに入力するプロンプトと出力応答を確認し、MLCommonsの分類体系に基づく暴力、ヘイトスピーチ、性的コンテンツなど11種の危険カテゴリを検出します。回答生成ではなく別のLLMの前後に置くガードレールとして使います。MetaはLlama Guard 3に置き換えましたが、既存利用者向けにLlama 3 Community LicenseでHugging Faceから入手できます。
