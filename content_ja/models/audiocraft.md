---
title: 'AudioCraft'
name: 'AudioCraft'
slug: 'audiocraft'
subtitle: '音楽と効果音の生成にまたがる、Metaのオープンソースフレームワーク'
description: '音楽と効果音の生成にまたがる、Metaのオープンソースフレームワーク'
company: 'meta-ai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://ai.meta.com/blog/audiocraft-musicgen-audiogen-encodec-generative-ai-audio/'
price: 'Free'
rank: 6
release_date: '2023-08-02'
param_count: '300M-3.3B (MusicGen), 1.5B (AudioGen)'
modality: [audio, text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['GitHub']
date: '2026-07-16'
tags: [audio, open-weight, music-generation]
i18n_source: '0ed2f655dea3'
---

AudioCraftは、Metaが2023年8月に公開したコードライブラリで、3つの音声生成モデルをまとめています。テキストから音楽を生成するMusicGen、環境音の効果音を作るAudioGen、波形をトークン化するために両者が使うニューラル音声コーデックのEnCodecです。MusicGenは複数のサイズ（3億、15億、33億パラメータ）があり、テキストのプロンプトに加えてメロディにも従える版もあります。AudioGenは、音楽ではなく効果音で学習した15億パラメータのモデルです。Metaはコードと重みをMITライセンスで公開し、Googleなどの企業のクローズドなシステムとは対照的に、AudioCraftはテキストから音声を生成する最初期の完全オープンなツールキットの1つになりました。小さいチェックポイントなら一般向けGPU1枚で動き、オープンソースの音楽生成プロジェクトや、制御可能な音声合成の研究でよく使われる土台になっています。
