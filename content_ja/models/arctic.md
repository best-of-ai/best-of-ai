---
title: 'Arctic'
name: 'Arctic'
slug: 'arctic'
subtitle: 'SQLとRAGに最適化された、Snowflakeの企業向けオープンウェイトモデル'
description: 'SQLとRAGに最適化された、Snowflakeの企業向けオープンウェイトモデル'
company: 'snowflake-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.snowflake.com/en/blog/arctic-open-efficient-foundation-language-models-snowflake/'
price: 'Free'
rank: 4
release_date: '2024-04-24'
param_count: '480B (17B active)'
context_window_tokens: 4096
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: true
mmlu_score: 67.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Snowflake Cortex']
date: '2026-07-16'
tags: [llm, open-weight, enterprise, self-hosted]
i18n_source: '083cf9082048'
---

Arcticは、Snowflakeが2024年4月に公開した大規模言語モデルです。一般的なチャットではなく、SQL生成、プログラミング、指示への追従といった企業での作業向けに作られています。Mixture-of-Expertsの設計で、128のエキスパートにまたがる合計4,800億パラメータを持ちますが、1トークンあたりで動くのは約170億だけです。このため、同規模の密なモデルより推論コストを抑えられます。Snowflakeはベースとinstructの両方のチェックポイントをApache 2.0ライセンスで公開しており、重みは自前でホストすることも、Snowflake Cortex経由で動かすこともできます。テキストからSQLを生成するSpiderベンチマークでは約79%の精度で、Snowflakeは、クエリをサードパーティのAPIに送らずに、高性能なオープンモデルをデータウェアハウスに持ち込む手段として打ち出しました。コンテキスト長は4Kと短く、一般的なチャットは苦手ですが、対象とした限られた企業向けのタスクでは高い性能を出します。
