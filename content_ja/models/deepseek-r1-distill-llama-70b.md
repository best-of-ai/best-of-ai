---
title: 'DeepSeek-R1-Distill-Llama-70B'
name: 'DeepSeek-R1-Distill-Llama-70B'
slug: 'deepseek-r1-distill-llama-70b'
subtitle: 'DeepSeek-R1の推論過程をLlamaに蒸留したモデルで、蒸留版の中で最大'
description: 'DeepSeek-R1の推論過程をLlamaに蒸留したモデルで、蒸留版の中で最大'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-R1'
price: 'Free'
rank: 6
release_date: '2025-01-20'
param_count: '70B'
context_window_tokens: 131072
modality: [text]
open_weight: true
license: 'Llama 3.3 Community License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: '875e7d1cacd9'
---

DeepSeek-R1-Distill-Llama-70Bは、DeepSeekが2025年1月にDeepSeek-R1と同時に公開した蒸留推論モデルです。推論モデルをゼロから学習する代わりに、DeepSeekはMetaのLlama 3.3 70B Instructを、完全版のR1が生成した推論過程でファインチューンしました。これでR1の連鎖的思考による問題解決の力の多くを、より小さく、動かすコストも低い構成に移しています。DeepSeekが公開したR1の蒸留バージョン6つのうち最大で、ベースはQwenとLlamaにわたり、1.5Bから70Bまでのパラメータ数があります。公開時にはAIME 2024でpass@1が70.0%、MATH-500で94.5%となり、同じ数学ベンチマークでGPT-4oやClaude 3.5 Sonnetのような汎用モデルを大きく上回りました。コンテキスト長はLlama 3.3のベースから引き継いだ128,000トークンです。ライセンスはLlama 3.3 Community Licenseで、重みはHugging Faceにあり、Together AIなどのプロバイダー経由でホスティングAPIも使えます。
