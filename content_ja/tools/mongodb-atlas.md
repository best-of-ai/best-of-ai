---
title: 'MongoDB Atlas'
name: 'MongoDB Atlas'
subtitle: 'ベクトル検索を内蔵したマネージドのMongoDB'
slug: 'mongodb-atlas'
description: 'MongoDB Atlasは、ドキュメントデータベースであるMongoDBの完全マネージドのクラウドサービスです。AWS、Azure、Google Cloudで動き、Atlas Vector Searchを含むため、チームはAI機能向けにエンベディングをアプリケーションのデータの隣に保存できます。'
website: 'https://www.mongodb.com/atlas'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Freemium'
featured: false
rank: 8
alternatives:
  - pinecone
  - weaviate
  - qdrant
  - datastax
  - supabase-ai
  - elasticsearch
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration]
i18n_source: '38c8f7841c9e'
---

MongoDBは、データを行と列ではなく、柔軟なJSONのようなドキュメントとして保存するので、データの形が頻繁に変わるアプリケーションに向いています。Atlasはそれをマネージドサービスとして動かします。プロビジョニング、バックアップ、スケーリング、セキュリティを担い、主要なクラウドをまたいで動きます。開発者はほとんどの言語のドライバーで接続し、レプリケーションとシャーディングの機能が高可用性と大規模なデータセットを支えます。無料枠で小さなプロジェクトや学習ができます。

AI向けに、Atlasは通常のデータベースと並んでベクトル検索を提供するため、アプリケーションはデータを別のベクトルデータベースに移さずに、エンベディングを保存して類似検索を実行できます。検索拡張生成、レコメンデーション、セマンティック検索を支えます。MongoDBはエンベディングとリランキングのモデルを作る会社も買収しており、LangChainやLlamaIndexなどの一般的なAIフレームワークと連携します。全文検索、時系列、分析の機能も同じプラットフォームにあります。

Atlasは使用量で課金されます。コンピュートのティア、ストレージ、データ転送が対象で、無料枠と本番向けの専用プランがあります。大規模なクラスターでは費用がかさむことがあります。ドキュメントモデルは、向いているアプリケーションとそうでないものがあり、リレーショナルな性質の強いデータを扱うチームはPostgresを好むことが多いです。代替には、NeonやSupabaseなどのサービスでpgvectorを使うPostgreSQL、Amazon DynamoDBとDocumentDB、Couchbase、Pineconeなどの専用のベクトルデータベースがあります。Atlasは、スキーマが変化していくアプリでよく選ばれます。
