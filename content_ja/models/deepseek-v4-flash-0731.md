---
title: 'DeepSeek-V4-Flash-0731'
name: 'DeepSeek-V4-Flash-0731'
slug: 'deepseek-v4-flash-0731'
subtitle: 'エージェント型のコーディングを強化するために再学習した、MITライセンスの2840億パラメータのMoEモデル'
description: 'エージェント型のコーディングを強化するために再学習した、MITライセンスの2840億パラメータのMoEモデル'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 6
release_date: '2026-07-31'
param_count: '284B (13B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.14
output_price_usd_per_m: 0.28
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-08-09'
tags: [llm, open-weight, code, agentic, mixture-of-experts]
extra_model_types: ['Code']
i18n_source: '247907c6207f'
---

DeepSeek-V4-Flash-0731は、DeepSeek-V4-Flashをプレビューから公開ベータへ移したもので、後学習をやり直したチェックポイントです。2026年7月31日に、同社のAPI変更履歴で発表されました。アーキテクチャは4月のデビュー時から変わらず、2840億パラメータのMixture-of-Expertsで、1トークンあたりの有効パラメータ数は130億、共有エキスパート1つとルーティングされるエキスパート256、コンテキスト長は100万トークンです。変わったのは後学習のパイプラインで、DeepSeekはコーディング、エージェントによるツール利用、推論に特化して調整し直しました。APIはResponses形式にネイティブ対応し、Codexとそのまま使えます。ライセンスは引き続きMITでゲートもなく、商用でも制限なく自前でホストできます。必要なメモリは3ビット量子化で約110 GB、フル精度なら4xのGB300ノードです。API料金は入力が100万トークンあたり0.14ドル、出力が0.28ドルと、低いままです。
