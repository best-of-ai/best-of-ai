---
title: 'GPT-4o Realtime'
name: 'GPT-4o Realtime'
slug: 'gpt-4o-realtime'
subtitle: 'ライブ音声会話向けの低遅延なGPT-4o音声対音声モデル'
description: 'ライブ音声会話向けの低遅延なGPT-4o音声対音声モデル'
company: 'openai'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://openai.com/index/introducing-the-realtime-api/'
price: 'Paid'
rank: 7
release_date: '2024-10-01'
param_count: 'Undisclosed'
context_window_tokens: 32000
modality: [audio, text]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 5
output_price_usd_per_m: 20
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['API', 'ChatGPT Advanced Voice']
date: '2026-07-16'
tags: [voice, multimodal, api, real-time]
i18n_source: '507fc668616b'
---
GPT-4o Realtimeは、OpenAIが2024年10月1日にRealtime APIを通じて発表した、GPT-4oの音声対音声モデルです。音声をテキストに書き起こし、言語モデルに渡し、音声に合成し直す一般的な処理とは異なり、WebSocketまたはWebRTC接続を通じて音声を最初から最後までネイティブに処理します。これにより、従来の音声ボットにあったぎこちなさの原因となる遅延を減らします。ChatGPTの高度な音声モードを支え、1秒未満で応答する電話エージェント、音声アシスタント、リアルタイム翻訳ツールを開発者が作れます。コンテキスト長は32Kトークンで、入力テキストは100万トークンあたり5ドル、出力テキストは20ドルです。音声トークンには別途、より高い料金がかかります。Google Gemini Live APIや、Whisper級の書き起こしとLLMを組み合わせた音声系スタートアップと競合しますが、複数の工程をつなぐ方式ではなく、単一モデルによる低遅延のアーキテクチャが特徴です。
