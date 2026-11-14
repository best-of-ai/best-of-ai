---
title: 'Aquila'
name: 'Aquila'
slug: 'aquila'
subtitle: 'BAAIが初めて公開した、中国語・英語のバイリンガル基盤モデル'
description: 'BAAIが初めて公開した、中国語・英語のバイリンガル基盤モデル'
company: 'baai'
model_type: 'Language'
logo_url: ''
product_url: 'https://github.com/FlagAI-Open/Aquila2'
price: 'Free'
rank: 4
release_date: '2023-06-09'
param_count: '7B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'BAAI License'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, multilingual, legacy]
i18n_source: '3f126c492a5c'
---

Aquilaは、北京智源人工知能研究院（BAAI）が初めて公開したバイリンガルの言語モデルです。2023年に、中国語と英語のテキストで学習した70億パラメータのベースモデルとしてリリースされました。BAAIはGPT型のアーキテクチャで作り、英語中心のモデルから借りたトークナイザーより、中国語のテキストを効率よく扱えるよう独自のトークナイザーを設計しました。コンテキスト長は2,048トークンです。リリースには、事前学習済みのベースモデルに加え、指示チューニングしたAquilaChatと、コード向けのAquilaCodeが含まれています。

BAAIは重みを独自のAquilaライセンスで公開しました。いくつかの条件のもとで商用利用を認めるライセンスです。モデルはHugging Faceと自前のModelHubで入手できます。Aquilaは、LLaMAなど欧米のモデルに代わる選択肢を国内の開発者に提供する狙いで、2023年に相次いだ中国のオープンウェイトモデルの1つでした。その後、BAAI自身のラインナップでは、より大きくコンテキスト長の長いAquila2ファミリーに置き換えられています。
