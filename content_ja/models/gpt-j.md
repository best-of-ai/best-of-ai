---
title: 'GPT-J'
name: 'GPT-J'
slug: 'gpt-j'
subtitle: 'GPT-3型アーキテクチャを採用したEleutherAI初期のオープンウェイトモデル'
description: 'GPT-3型アーキテクチャを採用したEleutherAI初期のオープンウェイトモデル'
company: 'eleuther-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.eleuther.ai/'
price: 'Free'
rank: 3
release_date: '2021-06-04'
param_count: '6B'
context_window_tokens: 2048
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
extra_model_types: ['Code']
i18n_source: '3c03d602f92a'
---
GPT-Jは60億パラメータの言語モデルです。EleutherAIは2021年6月9日、有料APIの背後にGPT-3を置いていたOpenAIに対する初期の有力なオープンな再実装の1つとして公開しました。独自の825GBのテキストデータセット「The Pile」で学習し、Mesh Transformer JAXライブラリを使ってGPUではなくTPUポッド上に学習を並列化しました。28層、コンテキスト長2,048トークンで、GPT-3最大構成よりかなり小型ながら、一般的な文章生成、質問応答、コード補完を十分にこなしたため、オープンソースNLP研究の標準的な比較対象になりました。Apache 2.0ライセンスで公開され、誰でもダウンロード、ファインチューニング、展開ができ、OpenAIの利用制限もありませんでした。その後GPT-NeoX-20Bなどに置き換えられましたが、クローズドな研究機関にオープンソースコミュニティが追いついたGPT-3時代を示す参照点として、今もよく挙げられます。
