---
title: 'Llama 3.2'
name: 'Llama 3.2'
slug: 'llama-3-2'
subtitle: '視覚対応モデルと端末内向けモデルを初めて加えたMetaのLlama世代'
description: '視覚対応モデルと端末内向けモデルを初めて加えたMetaのLlama世代'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/llama/'
price: 'Free'
rank: 6
release_date: '2024-09-25'
param_count: '90B'
context_window_tokens: 128000
modality: [text, image]
open_weight: true
license: 'Llama 3.2 Community License'
api_available: true
mmlu_score: 86.0
lmarena_score: 1250
access_methods: [Self-hosted, API]
runs_at_home: false
platforms: ['Hugging Face', 'Ollama']
date: '2026-07-16'
tags: [llm, open-weight, multimodal, self-hosted]
extra_model_types: ['Reasoning']
i18n_source: '70c7f383bbf6'
---
Llama 3.2はMetaが2024年9月に公開したシリーズで、Llamaに初めて視覚機能を加え、スマートフォンやエッジデバイス向けの小型テキストモデルも揃えました。主力の90B視覚モデルはLlama 3.1のテキスト基盤と約60億組の画像・テキストで学習した画像エンコーダーを組み合わせ、チャートの読み取り、写真のキャプション作成、画像についての質問応答を通常のテキストプロンプトとともに行えます。同じシリーズには、データセンターではなくモバイル機器上でのローカル実行を狙う軽量な1Bと3Bモデルもあります。推論ベンチマークでは90Bモデルはマルチモーダル入力に対応しながらLlama 3.1 70Bに近い性能です。Llama 3.2 Community Licenseで配布され、重みはHugging Faceにあります。
