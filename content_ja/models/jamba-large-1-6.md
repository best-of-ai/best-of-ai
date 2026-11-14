---
title: 'Jamba Large 1.6'
name: 'Jamba Large 1.6'
slug: 'jamba-large-1-6'
subtitle: 'AI21のTransformer・Mamba混合最上位モデルの更新版'
description: 'AI21のTransformer・Mamba混合最上位モデルの更新版'
company: 'ai21-labs'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.ai21.com/jamba/'
price: 'Free'
rank: 4
release_date: '2025-03-06'
param_count: '398B (94B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Jamba Open Model License'
input_price_usd_per_m: 2
output_price_usd_per_m: 8
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'AWS Bedrock']
date: '2026-07-16'
tags: [llm, open-weight, long-context, hybrid-architecture]
i18n_source: '7f46269a09c0'
---
Jamba Large 1.6はTransformerのアテンション層とMambaの状態空間モデル層を組み合わせた、AI21 Labsの最上位言語モデルです。2025年3月、Jamba Mini 1.6とともにJamba 1.6シリーズの一部として公開されました。総パラメータ数は3,980億ですが、MoE設計により推論時に使うのは940億で、計算コストを抑えながら25万6,000トークンのコンテキストに対応します。長文書、契約書、コードベースを外部へ送信せず処理したい企業向けに提供され、自社環境への導入とAPI利用の両方が可能です。AI21のベンチマークでは、Meta、Mistral、Cohereのオープンモデルを複数のタスクで上回りました。また、Mamba層が長い系列を効率よく扱うため、同規模の密なTransformerより大幅に高速に動作します。
