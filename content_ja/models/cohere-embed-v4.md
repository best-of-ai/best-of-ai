---
title: 'Cohere Embed v4'
name: 'Cohere Embed v4'
slug: 'cohere-embed-v4'
subtitle: 'テキスト、画像、混在した文書に対応する、Cohereの最新のマルチモーダルエンベディングモデル'
description: 'テキスト、画像、混在した文書に対応する、Cohereの最新のマルチモーダルエンベディングモデル'
company: 'cohere'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://cohere.com/blog/embed-4'
price: 'Paid'
rank: 6
release_date: '2025-04-15'
param_count: 'Undisclosed'
context_window_tokens: 128000
modality: [text, image]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.12
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Cohere API']
date: '2026-07-16'
tags: [embedding, multimodal, api]
i18n_source: 'edb96743b450'
---

Cohere Embed v4は、Cohereのマルチモーダルなエンベディングモデルで、Embed v3の後継として2025年4月に公開されました。前のモデルと違い、テキスト、画像、混在した文書を1回の呼び出しで受け取り、統一されたベクトル表現を出力します。そのため、PDFのページ、スライド、表のスクリーンショットを、先にテキストへ変換せずに、通常のテキストと並べて直接インデックスできます。128,000トークンのコンテキスト長に対応し、OpenAIやVoyageのエンベディングモデルをはるかに上回ります。256、512、1024、1536次元のMatryoshkaエンベディングを備えており、ユーザーは保存容量と精度のどちらを重視するかを選べます。Cohere APIでの料金は、テキストが100万トークンあたり0.12ドル、画像が100万トークンあたり0.47ドルで、Amazon BedrockとAzure AIでも使えます。Cohereは、プレーンテキストだけでなく、スキャンされた文書や視覚的に整形された内容を扱う必要がある、企業の文書検索とRAGシステム向けとして位置づけています。
