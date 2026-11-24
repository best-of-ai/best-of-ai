---
title: 'GPT-6 Cyber'
name: 'GPT-6 Cyber'
slug: 'gpt-6-cyber'
subtitle: '許可を得た脆弱性調査向けの、OpenAIの利用制限付きGPT-6モデル'
description: '許可を得た脆弱性調査向けの、OpenAIの利用制限付きGPT-6モデル'
company: 'openai'
model_type: 'Code'
logo_url: ''
product_url: 'https://developers.openai.com/api/docs/models/gpt-6-cyber'
price: 'Paid'
rank: 6
release_date: '2026-11-05'
param_count: 'Undisclosed'
context_window_tokens: 1050000
modality: [text, image, code]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 20
output_price_usd_per_m: 100
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Daybreak Red']
date: '2026-11-24'
tags: [cybersecurity, code, api, restricted-access]
i18n_source: '0c450f701351'
---

GPT-6 Cyberは、OpenAIのセキュリティテスト用モデルです。脆弱性の調査、許可を得たテスト環境での再現、修正の確認に使います。呼び出すには、組織がDaybreak Redへのアクセスと承認を得る必要があり、アクセスはアカウントチームが確認します。トラッカーによると、提供開始は2026年11月5日です。

コンテキスト長は105万トークンで、出力は最大12万8,000トークンです。料金は、27万2,000トークンまでのプロンプトで入力が100万トークンあたり20ドル、出力が100万トークンあたり100ドルです。それより長いプロンプトでは40ドルと150ドルになります。Chat CompletionsとResponses APIで動き、関数呼び出し、コードインタプリタ、ホステッドシェル、コンピュータ操作、MCPに対応していますが、Batch APIはありません。
