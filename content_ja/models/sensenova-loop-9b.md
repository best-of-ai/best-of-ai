---
title: 'SenseNova Loop-9B'
name: 'SenseNova Loop-9B'
slug: 'sensenova-loop-9b'
subtitle: '層をループで再利用する、SenseTimeのオープンウェイト9Bマルチモーダルモデル'
description: '層をループで再利用する、SenseTimeのオープンウェイト9Bマルチモーダルモデル'
company: 'sensetime'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.sensetime.com/en/news/sensenova-loop-9b-release-20261118-1435'
price: 'Free'
rank: 5
release_date: '2026-11-17'
param_count: '9B (about 14.6B inference-equivalent)'
context_window_tokens: 512000
modality: [text, image]
open_weight: true
license: 'Open weights'
api_available: true
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-11-24'
tags: [llm, open-weight, multimodal, small-model, self-hosted]
i18n_source: '842af8c2e04b'
---

SenseNova Loop-9Bは、SenseTimeのオープンウェイトのマルチモーダルモデルの正式版で、プレビューを経て2026年11月17日に公開されました。パラメータは約9Bで、32個の異なるデコーダ層があり、1回のパスで56回の層の計算として実行されるため、推論時には約14.6B相当のパラメータになります。テキストと画像を入力でき、テキストを出力し、最大51万2,000トークンのコンテキストを扱えます。

4ビットの重みは約4.9 GBで、一般向けのハードウェアに収まり、公式のAWQ版が公開初日に出ました。SenseTimeはQwen3.8-27Bと同等としていて、NL2Repoでは41.36に対して44.60、AIDABenchでは65.31に対して65.01です。重みはHugging Faceにsensenova/sensenova-loopとして置かれ、コードはGitHubにあります。
