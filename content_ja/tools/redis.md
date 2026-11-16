---
title: 'Redis'
name: 'Redis'
subtitle: 'キャッシュとベクトル検索に使われるインメモリデータベース'
slug: 'redis'
description: 'Redisは、キャッシュ、キュー、セッション、リアルタイム機能に使われるインメモリのデータストアです。ベクトル検索、JSON、セマンティックキャッシュにも対応しているため、高速な検索が必要なAIアプリケーションに使われます。'
website: 'https://redis.io'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Freemium'
featured: false
rank: 8
alternatives:
  - pinecone
  - qdrant
  - weaviate
  - mongodb-atlas
  - elasticsearch
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration, fast]
i18n_source: '294da6bd62ae'
---

Redisはデータをメモリに保存するので、読み書きが極めて高速です。開発者は、遅いデータベースの前に置くキャッシュ、ログインユーザーのセッションストア、メッセージキュー、さらにリーダーボード、レート制限、カウンターに使います。リスト、セット、ソート済みセット、ハッシュ、ストリームといったデータ型により、これらのパターンを簡単なコマンドで作れます。ウェブ上で最も広く展開されているインフラの1つです。

AI向けには、Redisがベクトル検索を加えました。アプリケーションは埋め込みを保存し、検索拡張生成、レコメンデーション、セマンティック検索のために似た項目を探せます。セマンティックキャッシュは、過去の質問への回答を保存して、似た新しい質問に返すため、言語モデルを呼び出すときのコストとレイテンシが下がります。Redisはエージェントの会話メモリも保持します。オープンソースソフトウェア、Redis Cloud、企業向けのデプロイとして動かせます。

ライセンスは議論になってきました。Redisはライセンスを変更し、クラウドプロバイダーが支援するValkeyというコミュニティのフォークが生まれました。その後、オープンソースのライセンスの選択肢が再び提供されました。メモリはディスクより高価なので、大きなデータセットは費用がかさむことがあり、永続性には設定が必要です。代替には、Valkey、シンプルなキャッシュ向けのMemcached、DragonflyDB、Amazon ElastiCacheのようなクラウドサービスがあります。Redisは、速度が重要なアプリケーションに向いています。
