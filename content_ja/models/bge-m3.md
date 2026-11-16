---
title: 'BGE-M3'
name: 'BGE-M3'
slug: 'bge-m3'
subtitle: 'BAAIのオープンウェイトの、多言語・多粒度の埋め込みモデル'
description: 'BAAIのオープンウェイトの、多言語・多粒度の埋め込みモデル'
company: 'baai'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://huggingface.co/BAAI/bge-m3'
price: 'Free'
rank: 4
release_date: '2024-02-06'
param_count: '568M'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, multilingual, retrieval]
i18n_source: 'dc0d8e73a2f9'
---

BGE-M3は、BAAIのテキスト埋め込みモデルで、2024年2月に論文が発表されました。名前は、同時に備える3つの特長を指します。100以上の言語に対応する多言語性、最大8192トークンの入力を扱える多粒度、そして1回の順伝播で密ベクトル、疎な語彙の重み、ColBERT型のトークンベクトルを出せる多機能性です。パラメータ数は5億6,800万で、大規模なLLMと比べれば小さいものの、生成ではなく検索専用に学習されています。この組み合わせにより、多言語のMIRACLベンチマークと、言語をまたぐMKQAベンチマークで、当時の最高水準の結果を出しました。従来は別々の密検索と疎検索のシステムが必要だったところを、1つのモデルで置き換えられたためです。BAAIはMITライセンスでHugging Faceに公開しており、複数言語の文書や、従来のBERTベースの埋め込みモデルに多い512トークンの上限より長い文書を検索する、検索拡張生成のパイプラインで広く使われています。
