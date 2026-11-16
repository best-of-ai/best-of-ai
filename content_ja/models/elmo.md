---
title: 'ELMo'
name: 'ELMo'
slug: 'elmo'
subtitle: 'トランスフォーマー以前の時代に出た、AI2の深い文脈化された単語表現モデル'
description: 'トランスフォーマー以前の時代に出た、AI2の深い文脈化された単語表現モデル'
company: 'allen-institute-for-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://allenai.org/allennlp/software/elmo'
price: 'Free'
rank: 5
release_date: '2018-02-15'
param_count: '93.6M'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['AllenNLP']
date: '2026-07-16'
tags: [llm, open-weight, legacy, foundation-model]
i18n_source: 'b789397d7327'
---

ELMoはEmbeddings from Language Modelsの略で、Allen Institute for AIとワシントン大学から2018年2月に出ました。Matthew Peters氏とMark Neumann氏らによる論文「Deep Contextualized Word Representations」で説明されています。word2vecやGloVeのような以前の埋め込みは、単語ごとに固定の1つのベクトルを割り当てていました。ELMoは、文に対して双方向LSTMを動かし、周囲の文脈に依存する表現を単語ごとに作ります。そのため、同じ単語でも使われ方によって違うベクトルになります。約10億語で学習し、既存のモデルに特徴として組み込むと、質問応答や固有表現抽出を含む6つのNLPタスクで、当時の結果を改善しました。ELMoはtransformerアーキテクチャより前のもので、公開から約1年のうちに、大半がBERTとその後継に取って代わられました。それでも、文脈を考慮した単語表現をNLPの標準的な手法として確立したモデルの一つとして、今も引用されています。
