---
title: 'Amazon Nova Sonic'
name: 'Amazon Nova Sonic'
slug: 'amazon-nova-sonic'
subtitle: 'リアルタイムの会話型音声エージェント向けの、Amazonの音声対音声モデル'
description: 'リアルタイムの会話型音声エージェント向けの、Amazonの音声対音声モデル'
company: 'amazon'
model_type: 'Audio Generation'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/speech/'
price: 'Freemium'
rank: 6
release_date: '2025-04-08'
param_count: 'Undisclosed'
context_window_tokens: 300000
modality: [audio, text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [voice, audio, api, real-time]
i18n_source: '1cbaa750f79c'
---

Amazon Nova Sonicは、Amazonが2025年4月に発表した音声対音声モデルです。音声の理解と音声の生成を1つのモデルにまとめており、音声認識、言語モデル、音声合成の別々のシステムをつなぐ方式ではありません。Amazon Bedrockの双方向ストリーミングAPIから使い、コンテキスト長は30万トークンです。聞き取り、推論し、自然な音声で低レイテンシに応答する、リアルタイムの音声エージェント向けに作られています。ツール利用とナレッジのグラウンディングにも対応するため、Sonicで作った音声エージェントは、会話の途中で外部の関数を呼んだり情報を取得したりできます。

Amazonは、ASR、LLM、TTSの別々のパイプラインを組み合わせるより低コストな選択肢として、また、音声アシスタントやカスタマーサービスのボット向けに、OpenAIのRealtime APIやGoogleのネイティブ音声モデルに対抗するものとして、Sonicを売り込みました。後にAmazonは、対応言語を増やしコンテキスト長を広げたNova 2 Sonicを出しましたが、既存の音声エージェントのワークフロー向けに、元のSonicもBedrockで引き続き使えます。
