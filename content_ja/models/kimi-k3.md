---
title: 'Kimi K3'
name: 'Kimi K3'
slug: 'kimi-k3'
subtitle: '公開済みモデルで最大とMoonshotが主張する、2.8兆パラメータのオープンウェイトモデル'
description: '公開済みモデルで最大とMoonshotが主張する、2.8兆パラメータのオープンウェイトモデル'
company: 'moonshot-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.moonshot.ai/'
price: 'Free'
rank: 8
release_date: '2026-07-16'
param_count: '2.8T (MoE)'
context_window_tokens: 1000000
modality: [text, image, video]
open_weight: true
license: 'Modified MIT'
input_price_usd_per_m: 3
output_price_usd_per_m: 15
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-08-09'
tags: [llm, open-weight, multimodal, reasoning, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: 'bf5cebe9bf5c'
---
Kimi K3はMoonshot AIがこれまでに公開した最大のモデルです。同社によると、総パラメータ数2.8兆のMixture of Expertsモデルで、公開済みのオープンウェイトモデルとして最大です。テキスト、画像、動画をネイティブに読み取り、コンテキスト長は100万トークンです。高速応答用の別モードはなく、常時思考モードで動作します。API料金は入力100万トークンあたり3ドル（キャッシュヒット時は0.30ドル）、出力100万トークンあたり15ドルです。西側企業の非公開最先端モデルより大幅に低価格です。7月16日の発表後まもなくHugging Faceに全重みが公開されました。MXFP4量子化によりダウンロードサイズは約1.4 TBとなり、専用クラスターがなくても本格的なセルフホスト環境で動かせる規模です。
