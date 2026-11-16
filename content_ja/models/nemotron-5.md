---
title: 'Nemotron 5'
name: 'Nemotron 5'
slug: 'nemotron-5'
subtitle: 'NVIDIA製ハードウェアで効率よく推論するよう調整されたオープンウェイトモデル'
description: 'NVIDIA製ハードウェアで効率よく推論するよう調整されたオープンウェイトモデル'
company: 'nvidia'
model_type: 'Language'
logo_url: ''
product_url: 'https://developer.nvidia.com/nemotron'
price: 'Free'
rank: 6
release_date: '2026-07-10'
param_count: '70B'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'NVIDIA Open Model License'
api_available: true
mmlu_score: 82.0
humaneval_score: 80.0
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'NVIDIA NIM', 'NGC']
date: '2026-07-19'
tags: [llm, open-weight, self-hosted, efficiency]
i18n_source: '528d47e90cc1'
---
Nemotron 5は、ランキング上位を狙うより、NVIDIA独自のGPUと推論基盤でモデルがどう動くかを示すことに重点を置く、同社のオープンウェイトモデルシリーズの一つです。パラメータ数700億の密なモデルで、コンテキスト長は12万8,000トークンです。NVIDIA Open Model Licenseで公開され、NVIDIA NIMマイクロサービスからワンクリックで導入できるほか、Hugging Faceからもダウンロードできます。

NemotronシリーズはNemotron-4 340B以降、品質を大きく損なわずにモデルを小さくする枝刈りや蒸留などの技術を示してきました。Nemotron 5も同じ方針です。70Bサイズは、適切な量子化を使えばH100 1台またはコンシューマーGPU2台に収まることを意図して選ばれました。NVIDIAが本当に訴求しているのはモデル単体ではなく、その下にあるハードウェアとソフトウェアの基盤です。
