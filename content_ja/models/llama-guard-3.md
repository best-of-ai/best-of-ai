---
title: 'Llama Guard 3'
name: 'Llama Guard 3'
slug: 'llama-guard-3'
subtitle: 'LLMの入出力をモデレーションするMetaのオープンウェイト安全性分類モデル'
description: 'LLMの入出力をモデレーションするMetaのオープンウェイト安全性分類モデル'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 4
release_date: '2024-07-23'
param_count: '8B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Llama 3.1 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, safety, self-hosted]
i18n_source: 'f0c740f9e81b'
---
Llama Guard 3はMetaが2024年7月にLlama 3.1と公開した安全性分類モデルで、推奨製品としてLlama Guard 2に代わりました。Llama 3.1の80億パラメータ版を基盤に、危険カテゴリを3つ増やして合計14種類とし、多言語のモデレーションも改善しました。単独アシスタントではなく、パイプライン内でプロンプトや応答を読み、安全・危険のラベルと該当カテゴリを返します。Llama 3.1 Community Licenseのオープンウェイトで、外部APIに頼らずモデレーション層を設けたい企業に広く使われています。
