---
title: 'Gato'
name: 'Gato'
slug: 'gato'
subtitle: 'テキスト、画像、ロボット制御にまたがって学習した、DeepMindの単一の汎用エージェント'
description: 'テキスト、画像、ロボット制御にまたがって学習した、DeepMindの単一の汎用エージェント'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/a-generalist-agent/'
price: 'Paid'
rank: 5
release_date: '2022-05-12'
param_count: '1.18B'
modality: [text, image]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [multimodal, research, generalist-agent]
---

Gatoは、DeepMindが2022年5月に発表した単一のニューラルネットワークです。同じ重みのまま、600を超えるさまざまなタスクをこなせます。Atariのゲームをプレイし、画像にキャプションを付け、テキストで会話し、実際のロボットアームを操作してブロックを積むことまでできます。DeepMindはタスクごとにモデルを学習するのではなく、テキスト、画像、関節のトルク、ボタン操作といったすべての入力を、1本の平らなトークン列にシリアライズし、それらすべてで1つのtransformerを同時に学習しました。アーキテクチャは大規模言語モデルに似ていますが、トークンが単語だけでなく、動作やセンサーのデータも表します。

パラメータ数は11.8億で、GPT-3の1750億と比べるとごく小さく、個々のタスクでの性能は、そのタスク専用に作られた専門モデルに及びません。注目されたのは、1つのネットワークが、これほど異なるモダリティや制御の問題にわたって、そこそこの仕事をこなせることを示した点です。DeepMindはこれを、製品ではなく、より汎用的なエージェントへ向けた研究のステップだと説明しており、Gatoが一般公開されたり、APIで提供されたりすることはありませんでした。
