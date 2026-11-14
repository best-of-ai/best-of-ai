---
title: 'MiniCPM-V'
name: 'MiniCPM-V'
slug: 'minicpm-v'
subtitle: 'スマートフォンでGPT-4V級の視覚タスクに対応するOpenBMBのマルチモーダル・エッジモデル'
description: 'スマートフォンでGPT-4V級の視覚タスクに対応するOpenBMBのマルチモーダル・エッジモデル'
company: 'openbmb'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/OpenBMB/MiniCPM-V'
price: 'Free'
rank: 5
release_date: '2024-05-20'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, small-model, on-device]
i18n_source: '83a16a62bccc'
---
MiniCPM-Vは清華大学から派生した研究所OpenBMBのオープンウェイト視覚言語モデル群です。サーバーGPUなしでスマートフォンなどの限られた端末上で画像・動画を理解できるよう設計されました。2024年5月公開のMiniCPM-Llama3-V 2.5はLlama3の80億パラメータ基盤にSigLip視覚エンコーダーを組み合わせ、OCR、複数画像推論、視覚QAで公開ベンチマーク上GPT-4Vに並ぶか上回る性能をうたい、スマートフォン上で完全オフライン動作します。

後継のMiniCPM-V 4.5や4.6では精度を上げながらパラメータ数を減らし、小型端末内モデルと大規模クラウドモデルの差を縮めています。Apache 2.0でHugging FaceとGitHubから提供され、一般向け機器でオフラインかつプライバシーを保ったマルチモーダルAIを必要とする開発者向けです。
