---
title: 'Neon'
name: 'Neon'
slug: 'neon-db'
description: 'Neonは、オートスケール、ゼロスケール、即時のデータベースブランチに対応したサーバーレスPostgresサービスです。現在はDatabricksの一部で、アプリ、プレビュー環境、大量のデータベースを必要とするAIエージェントでよく使われています。'
website: 'https://neon.tech'
company: 'neon'
logo_url: ''
category: 'database-tools'
category_name: 'データベース'
price: 'Freemium'
featured: false
rank: 8
alternatives:
  - supabase-ai
  - planetscale
  - turso
  - mongodb-atlas
date: '2026-06-15'
tags: [collaboration, model_based, fast, ai_powered, intelligent, platform, tool, service]
i18n_source: 'c4e0f3856856'
---

NeonはストレージとコンピュートをPostgresから切り離し、クラウド向けに作り直しました。この設計により、負荷に応じてデータベースを拡大し、使われていないときはゼロまで縮小できます。サーバーを動かし続ける代わりに、使った分だけ支払う形です。開発者が使うのは標準のPostgresなので、既存のツール、ドライバ、拡張機能がそのまま動きます。AIアプリケーションで埋め込みを保存するpgvectorも使えます。

最大の特徴はブランチ機能です。ストレージがコピーオンライトのため、Gitのブランチのように、データベース全体のコピーを数秒で作れます。マイグレーションのテスト、プルリクエストごとのプレビュー環境、開発者ごとに分離したコピーなどに使えます。同じ仕組みのおかげで、短命なデータベースを大量に立ち上げるAIコーディングエージェントやプラットフォームにも向いています。コネクションプーリング、リードレプリカ、Vercelなどとの連携も利用できます。

Neonには小規模なプロジェクト向けの無料枠があり、有料プランは従量課金です。DatabricksはAIエージェント向けのデータベースを支えるためにNeonを買収し、サービスは継続するとしています。ゼロスケールからの起動(コールドスタート)では少し遅延が出ることがあり、費用はコンピュート時間とストレージ量で決まります。Supabaseはより幅広いバックエンドツールをそろえたPostgresを提供しており、PlanetScaleやAWS Aurora Serverlessが競合で、分散型の用途にはCockroachDBが向きます。Neonは現代的なウェブアプリでよく選ばれています。
