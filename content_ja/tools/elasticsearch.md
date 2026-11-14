---
title: 'Elasticsearch'
name: 'Elasticsearch'
subtitle: '分散型の検索とベクトルデータベースのエンジン'
slug: 'elasticsearch'
description: 'Elasticsearchは、オープンソースの検索と分析のエンジンです。大量のデータに対する全文検索、ベクトル検索、ハイブリッド検索を扱い、サイト内検索、ログ分析、AIアプリケーションでの取得に広く使われています。'
website: 'https://www.elastic.co/elasticsearch'
company: 'elastic-nv'
logo_url: ''
category: 'search-engines'
category_name: '検索エンジン'
price: 'Freemium'
featured: false
rank: 9
alternatives:
  - algolia-ai-search
  - typesense
  - meilisearch
  - vectara
  - weaviate
date: '2026-11-05'
tags: [search, ai_assistant, discovery, information, query, web_search, answers, knowledge, retrieval, analytics]
i18n_source: '9de9525c0d39'
---

Elasticsearchは文書をJSONで保存してインデックスし、数十億件のレコードでも検索をミリ秒で返します。全文検索エンジンとして始まり、商品カタログやウェブサイトの検索に使われてきました。ログ、メトリクス、セキュリティデータにも、よく使われています。Elastic Stackの中核で、ダッシュボードのKibanaと、データを取り込むツールが付きます。企業は、テキストの多い大量のデータをすばやく検索したり集計したりするときに使います。

AIでは、ベクトルデータベースとしても、取得の層としても働きます。埋め込みを保存し、キーワード一致とベクトルの類似度を混ぜたセマンティック検索とハイブリッド検索を実行し、言語モデルへ渡す前に結果の順位を付け直せます。そのため、検索拡張生成のシステムの部品としてよく使われます。ES|QLなどのクエリ言語は分析に対応します。LLMへ接続し、企業データの上にエージェントを作るツールもあります。

自社のサーバーで自分で運用することも、ホスティング型またはサーバーレスのElastic Cloudを使うこともできます。ソフトウェアはオープンソースのライセンスの選択肢で使え、一部の機能は有料のサブスクリプションに限られます。うまく動かすには、クラスタのサイズ、インデックス、アップグレードの技能が要るので、多くのチームはマネージドサービスを選びます。代替には、主にAmazonが保守するフォークのOpenSearch、Algolia、Meilisearchがあります。Pineconeなどの専用ベクトルデータベースは、AI用途で競います。
