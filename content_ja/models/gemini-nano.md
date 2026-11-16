---
title: 'Gemini Nano'
name: 'Gemini Nano'
slug: 'gemini-nano'
subtitle: 'PixelとAndroidに組み込まれた、Googleのオンデバイス向けGemini'
description: 'PixelとAndroidに組み込まれた、Googleのオンデバイス向けGemini'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 4
release_date: '2023-12-06'
param_count: '3.25B'
context_window_tokens: 8192
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Android', 'Chrome']
date: '2026-07-16'
tags: [llm, on-device, small-model]
---

Gemini NanoはGoogleのGeminiファミリーで最も小さい階層で、サーバーを呼び出さず、スマートフォンの中だけで動くように設計されています。GoogleはGemini ProおよびUltraと同じ2023年12月6日に発表し、最初にPixel 8 Proに搭載しました。そこでは、メッセージアプリのスマートリプライ、通話の要約、レコーダーアプリの要約といった端末上の機能を支えています。サイズは約18億と32.5億パラメータの2種類で、スマートフォンのメモリとNPUの制約の中で効率よく動くよう量子化されています。完全にオフラインで動き、データが端末の外に出ることはありません。

ローカルで動くため、Nanoは処理能力を抑える代わりに、速度、プライバシー、1クエリあたりの追加コストがゼロという利点があります。使えるコンテキスト長も、Googleのサーバー側モデルよりずっと小さくなっています。Googleは発売後、対応端末をPixelの他のモデルに広げ、提携を通じてSamsung Galaxyにも広げました。サードパーティのAndroid開発者には、公開クラウドAPIではなく、AICoreシステムとML Kit GenAI APIを通じてNanoを提供しています。
