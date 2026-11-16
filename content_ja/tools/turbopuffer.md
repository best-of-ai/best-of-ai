---
title: 'Turbopuffer'
name: 'Turbopuffer'
subtitle: '大規模でも低レイテンシの検索に最適化した高速ベクトルデータベース'
slug: 'turbopuffer'
description: 'Turbopufferは、数十億のベクトルに対する類似検索を、低コストで高速に行うために設計されたベクトルデータベースです。永続化にはオブジェクトストレージを、速度のためにメモリとSSDのキャッシュを使います。'
website: 'https://turbopuffer.com'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Freemium'
featured: false
rank: 5
alternatives:
  - pinecone
  - qdrant
  - weaviate
  - lancedb
  - chroma
  - milvus
date: '2025-06-15'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, fast, affordable]
i18n_source: '77d11935fb5a'
---

Turbopufferは、ベクトルデータベースのコストの考え方を見直しています。すべてのデータを高価なメモリに置く代わりに、ベクトルを安価なオブジェクトストレージに保存し、よく使うデータをキャッシュします。大きなコレクションのコストを抑えつつ、頻繁に使うデータのレイテンシも低く保てます。

フィルタ付きの全文検索とベクトル検索に対応していて、サーバーレスの料金体系なのでクラスタの管理は要りません。非常に大きなコーパスを持つAIアプリケーションの検索に、企業が使っています。

Turbopufferは従量課金です。コールドデータへのクエリのレイテンシは、キャッシュ済みのデータより高くなります。代替にはPinecone、Qdrant、Milvus、Weaviate、pgvectorがあります。Turbopufferは、非常に大きなベクトルのコレクションを保存するチームに向いています。
