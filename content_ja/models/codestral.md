---
title: 'Codestral'
name: 'Codestral'
slug: 'codestral'
subtitle: 'Mistralのコード生成と補完向けモデル'
description: 'Mistralのコード生成と補完向けモデル'
company: 'mistral-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://mistral.ai/news/codestral/'
price: 'Free'
rank: 6
release_date: '2024-05-29'
param_count: '22B'
context_window_tokens: 256000
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.3
output_price_usd_per_m: 0.9
api_available: true
humaneval_score: 81.1
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, code, open-weight, api]
i18n_source: '0c94b2ec4923'
---

Codestralは、Mistral AIのコード生成専用モデルで、2024年5月に220億パラメータで最初に公開されました。fill-in-the-middleの補完と、多言語のコード生成向けに作られています。公開時のHumanEvalのpass@1は81.1パーセントで、当時のCode Llama 70BやDeepSeek Coder 33Bのような、より大きなコードモデルを上回りました。最初のリリースは32,000トークンのコンテキスト長で、Mistral AI Non-Production Licenseのもとで出されました。このライセンスでは、無料で使えるのは研究とテストに限られ、本番環境への展開には別の商用ライセンスが必要でした。

Mistralはその後、Codestralのコンテキスト長を256,000トークンに広げました。2026年4月にはモデルのライセンスをApache 2.0に切り替えており、以前の商用利用の制限がなくなって、IDE、コーディングアシスタント、CIパイプラインで自由に使えるようになりました。CodestralはHugging Faceでダウンロードできる重みと、MistralのAPIの両方で使え、現在の料金は入力が100万トークンあたり0.30ドル、出力が0.90ドルです。Codestral MambaやCode Llamaなど、他の中規模のオープンなコードモデルと直接競合します。寛容なライセンスへの切り替えは、オープンソースのコーディングモデルの分野で大きな転換と広く見られました。
