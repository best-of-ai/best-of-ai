---
title: 'ChatGLM3'
name: 'ChatGLM3'
slug: 'chatglm3'
subtitle: '智譜AIの第3世代オープンウェイト、中英バイリンガル対話モデル'
description: '智譜AIの第3世代オープンウェイト、中英バイリンガル対話モデル'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 4
release_date: '2023-10-27'
param_count: '6B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
i18n_source: '9a38147f22d8'
---

ChatGLM3は、ChatGLM対話モデルシリーズの第3世代です。Zhipu AIと清華大学のKEGラボが共同で開発し、2023年10月下旬に公開されました。ベースのChatGLM3-6Bは中英バイリンガルの設計で、前世代に比べて関数呼び出し、コード実行、エージェント型のツール利用への対応が強化されています。事前学習のデータも多様になり、学習トークン数が増え、アラインメントの学習も改善されました。公開時にZhipuは、推論、数学、コード、一般知識にまたがる数十のベンチマークで、6Bのベースモデルが100億パラメータ未満の他の事前学習モデルを上回ったと報告しています。

Zhipuはコンテキスト長の異なる複数のバリアントを公開しました。標準のChatGLM3-6Bに加え、より大きな文書や会話を扱える32Kと128Kの長コンテキスト版があります。モデルはApache 2.0のオープンウェイトで、Hugging Faceから広く入手できるため、自前で動かす中国語チャットアプリの定番になっています。Zhipuはその後、規模も大きく、ベンチマークの結果も強いGLM-4シリーズに移り、現在はZ.aiブランドで事業を行っています。ChatGLM3は旧世代の選択肢となり、最高水準の性能より、小さなサイズと低いホスティングコストが重視される場面で主に使われています。
