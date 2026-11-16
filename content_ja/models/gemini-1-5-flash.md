---
title: 'Gemini 1.5 Flash'
name: 'Gemini 1.5 Flash'
slug: 'gemini-1-5-flash'
subtitle: 'Googleの速くて低コストなGemini 1.5の階層。Gemini 1.5 Proから蒸留'
description: 'Googleの速くて低コストなGemini 1.5の階層。Gemini 1.5 Proから蒸留'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/flash/'
price: 'Paid'
rank: 7
release_date: '2024-05-14'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.075
output_price_usd_per_m: 0.3
api_available: true
mmlu_score: 78.9
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Google AI Studio', 'Vertex AI', 'Gemini app']
date: '2026-07-16'
tags: [llm, multimodal, api, low-cost]
---

Gemini 1.5 Flashは、Gemini 1.5世代でGoogleの速くて低コストな階層にあたるモデルです。Gemini 1.5 Proを蒸留したバージョンとして、2024年5月に公開されました。Googleは、小さなモデルにProの出力を真似させて作り、Proの推論能力の多くを保ちながら、遅延とコストを大きく減らしました。コンテキスト長はProと同じ100万トークンで、テキスト、画像、音声、動画を扱えます。長い文書の要約や動画のキャプション生成など、Proの価格だと費用がすぐにかさむ大量処理のタスクに実用的です。

公開時の価格は、128,000トークン未満のプロンプトで、入力が100万トークンあたり0.075ドル、出力が100万トークンあたり0.30ドルでした。当時のフロンティア級のAPIとしては最安の部類です。Google AI Studio、Vertex AI、Geminiアプリで使え、Geminiアプリの多くの無料ユーザーのデフォルトにもなりました。Googleはその後、新しい開発の大半を2.0と2.5のFlash世代に移したため、1.5 Flashは現在、主にAPIの後方互換のために残されています。
