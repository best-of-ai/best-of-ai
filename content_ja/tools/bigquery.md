---
title: 'BigQuery'
name: 'BigQuery'
subtitle: 'Google Cloudのサーバーレスなデータウェアハウス'
slug: 'bigquery'
description: 'BigQueryは、Google Cloudのサーバーレスなデータウェアハウスです。非常に大きなデータセットをSQLで問い合わせ、BigQuery MLでSQLのまま機械学習モデルを作り、クエリの作成はGeminiが助けます。'
website: 'https://cloud.google.com/bigquery'
company: 'google'
logo_url: ''
category: 'data'
category_name: 'データ'
price: 'Paid'
featured: false
rank: 8
alternatives:
  - snowflake
  - databricks
  - motherduck
  - dbt-cloud
date: '2026-11-05'
tags: [data_analysis, analytics, business, insights, visualization, data_science, reporting, dashboards, sql, cloud_based, machine_learning, training]
i18n_source: '902eae4f55c8'
---

BigQueryを使うと、サーバーを管理せずに膨大な量のデータを分析できます。ファイル、データベース、ストリーム、他のGoogleサービスからデータを読み込み、SQLを書くと、BigQueryは処理を多くのマシンに分散し、テーブルが数百万行でも数兆行でも結果を速く返します。ストレージとコンピュートは分離されて管理されるので、規模を決めたり調整したりするクラスタはありません。分析チームがこれを好む大きな理由です。

データとAIのいまの仕事向けに、多くの機能が加わっています。BigQuery MLでは、予測や分類を含むモデルの学習と実行をSQL文で行い、クエリの中からGeminiや他のモデルにつないで、テキストや埋め込みを生成できます。ベクトル検索は、類似度と取得のワークロードを支えます。Gemini in BigQueryは、SQLを書いて説明し、コードを生成し、データの変換を提案するのを助けます。Looker、Connected Sheets、他社のBIツールともつながります。

料金の形は二つです。クエリが走査したデータ量に基づくオンデマンド課金と、確保したコンピュートへのキャパシティ料金で、これにストレージ料金が加わります。毎月の無料枠があります。テーブルが大きく、パーティションもなければ、高いクエリをうっかり実行しやすいので、費用の管理が要ります。主な競合はSnowflakeとDatabricksで、Amazon RedshiftはAWSにおける同等のサービス、DuckDBはより小さなローカル分析をカバーします。BigQueryは、すでにGoogle Cloudを使っているチームに合います。
