---
title: 'AudioLM'
name: 'AudioLM'
slug: 'audiolm'
subtitle: 'リアルな音声や音の続きを生成するGoogleのフレームワーク'
description: 'リアルな音声や音の続きを生成するGoogleのフレームワーク'
company: 'google-deepmind'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://google-research.github.io/seanet/audiolm/examples/'
price: 'Paid'
rank: 5
release_date: '2022-09-07'
param_count: 'Undisclosed'
modality: [audio]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [audio, research, legacy]
i18n_source: '944df39235b8'
---

AudioLMは、Googleが2022年9月に発表した研究フレームワークです。音声の生成を、スペクトログラムや波形の回帰といった通常の手法ではなく、離散的な音声トークン上の言語モデリングの問題として扱います。2種類の表現を組み合わせています。1つは、自己教師ありの音声モデルw2v-BERTによるセマンティックトークンで、長い範囲の構造を捉えます。もう1つは、ニューラルコーデックSoundStreamによる音響トークンで、高品質な合成のために細かな音の情報を保ちます。生の音声だけで学習し、文字起こしや注釈は使いません。数秒の話し声やピアノ曲の続きを、数十秒にわたってまとまりを保ったまま生成でき、これは従来の音声生成手法が苦手としていたことです。Googleは製品として公開せず、論文とデモページにとどまりました。Google DeepMindはこのトークンベースの手法を、後のMusicLMやLyriaの一部といった研究の土台にしました。
