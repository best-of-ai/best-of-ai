---
title: 'Chameleon'
name: 'Chameleon'
slug: 'chameleon'
subtitle: 'テキストと画像のトークンをそのまま混ぜて扱う、Metaのアーリーフュージョンモデル'
description: 'テキストと画像のトークンをそのまま混ぜて扱う、Metaのアーリーフュージョンモデル'
company: 'meta-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://ai.meta.com/blog/meta-fair-research-new-releases/'
price: 'Free'
rank: 6
release_date: '2024-05-16'
param_count: '34B'
context_window_tokens: 4096
modality: [text, image]
open_weight: true
license: 'Research-only'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, open-weight]
extra_model_types: ['Image Generation']
i18n_source: '6e820e7a5edb'
---

ChameleonはMeta FAIRのマルチモーダルモデルで、2024年5月の論文で発表されました。言語モデルに視覚エンコーダを後から付け足すのではなく、最初からテキストと画像を混ぜて学習します。多くのマルチモーダルシステムは「レイトフュージョン」を採っており、テキストだけで事前学習した言語モデルに、別の画像エンコーダが視覚特徴を渡します。Chameleonは画像を離散トークンに量子化し、テキストと画像のトークンが交互に並ぶ列を最初から学習します。そのため同じTransformerが両方のモダリティを扱って推論でき、画像を説明するだけでなく、画像を出力として生成することもできます。

Metaは2つのサイズ、Chameleon-7BとChameleon-34Bを公開しました。34B版は画像キャプションと視覚的な質問応答でFlamingoやIDEFICSを上回り、混合モダリティの生成タスクの一対比較による人間の選好テストでは、GPT-4VやGemini Proと並ぶ結果だったと報告しています。重みはGitHubで研究用限定のライセンスのもとで公開されており、商用では使えません。Metaは製品というより、アーリーフュージョン型の学習の実証として位置づけました。Chameleonの考え方は、その後のMetaのマルチモーダルLlamaモデルに引き継がれ、アーリーフュージョン型の学習が、商用ライセンスのより幅広いモデルラインに広がりました。
