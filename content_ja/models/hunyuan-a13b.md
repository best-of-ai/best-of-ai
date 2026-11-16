---
title: 'Hunyuan-A13B'
name: 'Hunyuan-A13B'
slug: 'hunyuan-a13b'
subtitle: 'TencentのオープンウェイトMoE推論モデル'
description: 'TencentのオープンウェイトMoE推論モデル'
company: 'tencent'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://llm.hunyuan.tencent.com/'
price: 'Free'
rank: 4
release_date: '2025-06-27'
param_count: '80B (13B active)'
context_window_tokens: 256000
modality: [text]
open_weight: true
license: 'Tencent Hunyuan License'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Tencent Cloud']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, mixture-of-experts]
i18n_source: '1fc3c97bd4e4'
---
Hunyuan-A13BはTencentのオープンウェイトな混合エキスパート（MoE）言語モデルです。2025年6月に公開され、総パラメータ数は800億ですが、各トークンの処理で使うのは130億です。そのため、推論コストをより小さな密モデルに近づけられます。ネイティブで256Kのコンテキスト長に対応しますが、自宅環境ではGPUメモリに合わせて上限を下げる構成も多くあります。高速応答モードと、難しい数学・科学・プログラミング問題向けの段階的な推論モードを切り替えられます。重みはHugging Faceで独自のHunyuanライセンスのもと公開され、セルフホストを望まないチームはTencent CloudのAPIも利用できます。DeepSeekの小型モデルやAlibabaのQwenなど、効率を重視したオープンMoE推論モデルと競合し、総パラメータ数よりもアクティブパラメータの効率を強みとしています。
