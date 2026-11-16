---
title: 'Canary'
name: 'Canary'
slug: 'canary'
subtitle: 'NVIDIAの多言語音声認識・翻訳モデル'
description: 'NVIDIAの多言語音声認識・翻訳モデル'
company: 'nvidia'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://huggingface.co/nvidia/canary-1b'
price: 'Free'
rank: 5
release_date: '2024-04-18'
param_count: '1B'
modality: [audio, text]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['NVIDIA NIM', 'Hugging Face']
date: '2026-07-16'
tags: [speech-recognition, open-weight, multilingual]
i18n_source: 'ad7707d7cc9a'
---

CanaryはNVIDIAのNeMoチームによる音声モデルのファミリーで、主力のCanary-1Bは2024年4月に公開されました。音声を文字にするだけの一般的なASRモデルと違い、Canaryは英語、フランス語、ドイツ語、スペイン語の間で音声認識と音声翻訳の両方を行い、話された音声を同じ言語のテキストにすることも、別の言語に翻訳することもできます。FastConformerエンコーダとTransformerデコーダを組み合わせた構成で、比較的小さなモデルで高い精度が出るようにNVIDIAが調整したものです。公開時には、数倍の規模の競合モデルを抑えて、Hugging FaceのOpen ASR Leaderboardで首位に立ちました。

NVIDIAはCanary-1BをHugging FaceとNeMoフレームワークで配布しており、自前の環境で動かせます。ホスト型APIとしてはNVIDIA NIMからも使えます。元のCanary-1BはCC-BY-NC 4.0ライセンスで、非商用に限られます。その後NVIDIAは、Canary-1B-FlashやCanary-1B-v2などの新しいバリアントを、より緩やかなCC-BY-4.0ライセンスで公開しました。こちらは商用利用が明示的に認められ、推論も速くなっています。
