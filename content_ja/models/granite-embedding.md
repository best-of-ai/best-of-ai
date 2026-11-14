---
title: 'Granite Embedding'
name: 'Granite Embedding'
slug: 'granite-embedding'
subtitle: '検索用のIBMエンタープライズ向けテキスト埋め込みモデルファミリー'
description: '検索用のIBMエンタープライズ向けテキスト埋め込みモデルファミリー'
company: 'ibm'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 4
release_date: '2024-12-18'
param_count: '278M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['IBM watsonx', 'Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, enterprise]
i18n_source: '623d675b4ebd'
---
Granite Embeddingは、watsonxや自社運用環境の企業向けRAGシステムに組み込める、IBMのテキスト埋め込みモデル群です。2億7,800万パラメータの多言語版は、日本語、英語、ドイツ語、アラビア語、中国語など12言語を扱い、最大512トークンの入力から768次元のベクトルを生成します。IBMは、オープンな関連性ペアのデータセットと自社で整備したデータを組み合わせ、コントラスト学習、知識蒸留、モデルマージを用いて学習しました。企業利用に適した、許諾条件の明確なデータを重視しています。Graniteシリーズと同様、Apache 2.0ライセンスでHugging Face、Ollama、IBM watsonxから提供されます。検索ベンチマークではBGEやGTEなどのオープン埋め込みモデルと競合し、規制業界の顧客に向けてコンプライアンスと追跡可能な学習データを重視しています。
