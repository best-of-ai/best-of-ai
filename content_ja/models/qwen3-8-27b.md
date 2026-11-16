---
title: 'Qwen3.8-27B'
name: 'Qwen3.8-27B'
slug: 'qwen3-8-27b'
subtitle: '単体のローカルGPUで動くサイズのAlibabaオープンウェイト・マルチモーダルモデル'
description: '単体のローカルGPUで動くサイズのAlibabaオープンウェイト・マルチモーダルモデル'
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-14'
param_count: '27B'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-08-17'
tags: [llm, open-weight, multimodal, single-gpu, apache-2.0, local]
i18n_source: '1e091b27bdc3'
---
AlibabaのQwenチームは2026年8月14日、Qwen3.8-27BをApache 2.0ライセンスのオープンウェイトで公開しました。混合エキスパートではなく高密度の270億パラメータモデルで、テキスト、画像、動画を扱い、図、文書、数時間の映像にも対応します。ネイティブのコンテキスト長は262,000トークンで、YaRN拡張により100万まで伸ばせます。Alibabaによると、大型のQwen3.7-Plusをコーディングやオフィス業務で上回り、エージェント計画も改善され、監督を減らして多段階タスクを完了します。

データセンタークラスターではなく、一般向けまたはワークステーションGPU 1基に収まるモデルを求める開発者向けです。MetaやGoogleの同様にローカル運用を重視したモデルに対抗します。同時に同世代のMax級モデルQwen3.8-2.4T-A95Bもオープンウェイト化し、軽量版と重いエージェント作業向けの大規模版を選べるようにしました。
