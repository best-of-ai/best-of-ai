---
title: 'Amazon SageMaker'
name: 'Amazon SageMaker'
subtitle: '機械学習モデルの構築、学習、デプロイ向けのAWSプラットフォーム'
slug: 'amazon-sagemaker'
description: 'Amazon SageMakerは、機械学習とAIのモデルを構築、学習、デプロイするためのAWSのプラットフォームです。データとAIの作業をまとめるSageMaker AIの統合スタジオと、AWS上のデータを管理するレイクハウスも含みます。'
website: 'https://aws.amazon.com/sagemaker/'
company: 'amazon'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Paid'
featured: false
rank: 8
alternatives:
  - vertex-ai
  - azure-ai-foundry
  - databricks
  - dataiku
  - datarobot
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration, machine_learning, training]
i18n_source: 'a69e213128f4'
---

SageMakerは、サーバーを自分で管理せずにAWS上で機械学習を動かす手段として始まりました。データサイエンティストはノートブックでデータを整え、コードを書き、必要に応じて規模を広げられるマネージドコンピュートでモデルを学習します。学習が終わると、SageMakerはエンドポイントの背後にモデルを配置し、性能を監視し、バージョンを管理します。ノートブック上の実験が、本番のサービスになります。PyTorchやTensorFlowなど、広く使われるフレームワークに対応しています。

製品の範囲は広がっています。SageMaker AIは基盤モデルを含むモデルの学習とデプロイを担い、大規模クラスタでの分散学習、ファインチューン、オープンなモデルのホスティングができます。SageMaker Unified Studioは、データエンジニアリング、分析、AIの作業をひとつにまとめた環境です。SageMaker Lakehouseは、S3、Redshift、その他のソースのデータを、共通の権限とガバナンスの下に集めます。パイプライン、フィーチャーストア、実験の追跡は、同じ手順を繰り返すワークフローを組むチームを支えます。

SageMakerの料金は、計算、ストレージ、マネージド機能の利用量に応じてかかり、無料枠は最初の数か月の少量をカバーします。範囲の広さは欠点でもあります。サービス、設定、料金の項目が多く、複雑で、使いすぎになりやすいです。すでにAWSを使っているチームは、IAM、S3、セキュリティ制御との連携を評価します。直接の競合はGoogle Vertex AIとAzure Machine Learningで、データを多く扱うチームにはDatabricksがよく選ばれる代替です。学習を自分で管理せず、ホストされたモデルを呼び出すだけなら、Amazon Bedrockのほうが単純です。
