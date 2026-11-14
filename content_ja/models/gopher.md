---
title: 'Gopher'
name: 'Gopher'
slug: 'gopher'
subtitle: 'Chinchillaのスケーリング則につながった、DeepMindの2800億パラメータの研究用モデル'
description: 'Chinchillaのスケーリング則につながった、DeepMindの2800億パラメータの研究用モデル'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/'
price: 'Paid'
rank: 6
release_date: '2021-12-08'
param_count: '280B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 60.0
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, research, legacy]
---

Gopherは2800億パラメータの言語モデルで、モデルの性能がサイズに応じてどう伸びるかを調べる研究の一環として、DeepMindが学習させ、2021年12月の論文で説明しました。学習には10.5テラバイトのコーパスMassiveTextを使い、4400万から70億パラメータの5つの小さいモデルと並べて評価して、規模に応じて能力がどう向上するかを見ています。MMLUベンチマークでは5-shot設定で60%を記録し、当時の既存モデルを大きく上回りました。

DeepMindはGopherを公開せず、APIでも提供しませんでした。研究のための道具にとどまっています。主な遺産は、その後の分析をまとめたChinchillaの論文です。Gopherとその兄弟モデルを使い、当時の大規模言語モデルの多くが、パラメータ数に比べて学習が足りていないことを示しました。この発見は、その後何年も、各研究機関がモデルサイズと学習データのあいだで計算資源を配分するやり方を変えました。
