---
title: 'Code Llama'
name: 'Code Llama'
slug: 'code-llama'
subtitle: 'Metaのオープンウェイトの、コード向けに特化したLlamaバリアント'
description: 'Metaのオープンウェイトの、コード向けに特化したLlamaバリアント'
company: 'meta-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://ai.meta.com/blog/code-llama-large-language-model-coding/'
price: 'Free'
rank: 6
release_date: '2023-08-24'
param_count: '34B'
context_window_tokens: 100000
modality: [text, code]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
humaneval_score: 53.7
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: 'f77a90c92a53'
---

Code Llamaは、Metaが2023年8月に公開した、Llama 2のコード向けバージョンです。ベースのLlama 2の重みの上に、コードの多いデータで追加学習しています。基盤となる3つのサイズ(7B、13B、34Bパラメータ)で提供され、それぞれにベース版、Python特化版、チャット形式のコーディング支援向けのインストラクションチューニング版があります。Metaはその後、70Bのバリアントも追加しました。ベースのLlama 2からの重要な変更は、RoPEの位置エンベディングを調整して、コンテキスト長を4,096トークンから100,000トークンまで広げたことです。これにより、長いファイルやコードベース全体を、1回で読んで編集するのにずっと使いやすくなりました。

HumanEvalベンチマークでは、34Bモデルがpass@1で53.7パーセントを記録しました。公開時点のGPT-3.5とほぼ同等ですが、GPT-4にははるかに及びません。Code Llamaは、元のモデルと同じLlama 2 Community Licenseで公開されており、ほとんどの企業は商用で使えます。重みはHugging Faceから自由にダウンロードできます。広く採用された最初期のオープンウェイトのコーディングモデルの1つで、CodestralやDeepSeek Coderなど、後のオープンなコードモデルが競い合うことになる手本を作りました。
