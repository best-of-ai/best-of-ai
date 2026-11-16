---
title: 'Inkling'
name: 'Inkling'
slug: 'inkling'
subtitle: 'Mira MuratiのThinking Machines Labが初めて公開したオープンウェイトモデル'
description: 'Mira MuratiのThinking Machines Labが初めて公開したオープンウェイトモデル'
company: 'thinking-machines'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://thinkingmachines.ai/model-card/inkling/'
price: 'Free'
rank: 6
release_date: '2026-07-15'
param_count: '975B (41B active)'
context_window_tokens: 1000000
modality: [text, image, audio]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Tinker']
date: '2026-07-25'
tags: [llm, open-weight, multimodal, self-hosted]
i18n_source: '010a5c004d85'
---
Inklingは、元OpenAI CTOのMira Muratiが設立したAIスタートアップThinking Machines Labが初めて公開した本番向けモデルです。2026年7月15日、テキスト、画像、音声、動画で事前学習したネイティブなマルチモーダルMoEモデルとして提供を開始しました。総パラメータ数は9,750億、トークンごとのアクティブ数は410億です。Nvidia GB300 NVL72システムを使い、45兆トークンで学習されました。重みはHugging Faceで公開され、コンテキスト長は100万トークンです。同社のTinkerファインチューニング基盤から使う場合は25万6,000トークンに制限されます。Apache 2.0ライセンスで公開され、自由にファインチューニングや再配布ができます。Artificial Analysis Intelligence Indexでは初登場時に41点を記録し、当時、米国の研究所が公開したオープンウェイトモデルとして最高のスコアでした。特定の利用者に合わせたモデルを作り、万人向けの単一システムを目指さないというThinking Machinesの方針にも沿っています。
