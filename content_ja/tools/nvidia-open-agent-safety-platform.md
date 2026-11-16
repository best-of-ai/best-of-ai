---
title: 'NVIDIA Open Agent Safety Platform'
name: 'NVIDIA Open Agent Safety Platform'
subtitle: '問題を起こしたAIエージェントを数ミリ秒で隔離できる、オープンソースのセキュリティ層'
slug: 'nvidia-open-agent-safety-platform'
description: 'NVIDIAのOpen Agent Safety Platformは、エージェントをサンドボックスに入れるオープンなランタイムOpenShellと、BlueField DPU上でエージェントのコンピューターとは別に動き、エージェントを隔離できる監視層Sentryを組み合わせています。'
website: 'https://developer.nvidia.com/'
company: 'nvidia'
logo_url: ''
category: 'cybersecurity'
category_name: 'サイバーセキュリティ'
price: 'Free'
featured: false
rank: 5
alternatives:
  - lakera
  - patronus-ai
  - giskard
  - nightfall
date: '2026-09-28'
tags: [ai_powered, intelligent, platform, tool, service, solution, saas, online]
i18n_source: '9264e993765c'
---

このプラットフォームは、セキュリティ上の懸念に応えるものです。コマンドを実行しデータにアクセスできる自律型エージェントには、乗っ取られたエージェントが無効にできない制限が必要です。OpenShellはオープンソースのランタイムで、各エージェントをポリシーに基づく権限を持つ専用のサンドボックスに置きます。プローバーが、与えた権限同士が組み合わさって運用者の意図しない結果にならないかを確認します。

Sentryは、エージェントのマシンの外側で強制力を加えます。ホストから切り離されたBlueFieldのデータ処理ユニット上で動くので、ホストが乗っ取られても、挙動を監視してエージェントをすばやく隔離できます。NVIDIAはこれをリファレンス設計と説明しており、多くのパートナーが各部分を組み込んでいます。

ソフトウェアはオープンソースで、ハードウェアの部分にはNVIDIAのインフラが必要です。アナリストは、権限の整合性を証明しても、あらゆる意味でエージェントが安全だと証明したことにはならず、エージェントの行動のレビューは引き続き重要だと指摘しています。代替には、E2BやDaytonaなどのサンドボックスツール、AnthropicとOpenAIのサンドボックス、エージェントに特化したセキュリティのスタートアップがあります。NVIDIAのプラットフォームは、強い分離が必要な形でエージェントを展開する組織に向いています。
