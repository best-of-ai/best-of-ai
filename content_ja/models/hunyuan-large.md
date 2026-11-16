---
title: 'Hunyuan Large'
name: 'Hunyuan Large'
slug: 'hunyuan-large'
subtitle: 'Tencentのオープンウェイト混合エキスパートモデル'
description: 'Tencentのオープンウェイト混合エキスパートモデル'
company: 'tencent'
model_type: 'Language'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 5
release_date: '2024-11-05'
param_count: '389B (52B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, mixture-of-experts]
i18n_source: '12052bfcac4f'
---
Hunyuan-LargeはTencentのオープンウェイト混合エキスパート言語モデルです。2024年11月に公開され、総パラメータ数は3,890億、各トークンで有効になるのは520億です。Tencentは公開時点で最大のオープンなTransformerベースMoEモデルと説明しました。コンテキスト長は256Kで、以前の密なHunyuanモデルと比べ、推論、プログラミング、長文脈の情報想起を向上させるため、合成データと実データを組み合わせて訓練されました。専門家の振り分けやデータ拡張の方針を記した技術レポートも重みとともに公開し、Hugging FaceでのセルフホストとTencent Cloud経由のAPI利用に対応しています。DeepSeek-V2やMistralのMixtralシリーズなど、同時期の大規模オープンMoEモデルと競合します。特に、実際に動作するパラメータ数に対して大きな専門家プールを持つ点が特徴です。
