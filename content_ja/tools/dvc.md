---
title: 'DVC'
name: 'DVC'
subtitle: 'MLのデータセットと実験向け、オープンソースのバージョン管理'
slug: 'dvc'
description: 'DVCはData Version Controlの略で、データセット、モデル、実験をGitのコードと一緒にバージョン管理するオープンソースのツールです。クラウドストレージに置いた大きなファイルを、Gitに似た操作で追跡します。'
website: 'https://dvc.org'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Free'
featured: false
rank: 5
alternatives:
  - mlflow
  - zenml
  - metaflow
  - clearml
  - comet-ml
  - weights-biases
  - prefect
date: '2025-06-15'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, open_source, cloud_based, machine_learning]
i18n_source: '18847a8c544f'
---

DVCは、Gitが想定していなかった問題、つまり大きなデータファイルを扱います。データサイエンティストはDVCでデータセットとモデルファイルを追跡します。Gitには小さなポインタのファイルを置き、実データはS3やGoogle Cloud Storageなどのクラウド、またはローカルのストレージに置きます。古いコミットをチェックアウトすると、対応するデータが戻ってきます。

再現できるパイプラインにも対応しています。利用者は、データとコードを入力として出力を出すステージを定義し、DVCは変わった部分だけを再実行します。実験は追跡して比較でき、指標とプロットはリポジトリと一緒に保存されます。このプロジェクトは、現在lakeFSの下で維持されています。

DVCは無料のオープンソースです。Gitとコマンドラインに慣れている必要があります。代替にはlakeFS、より単純な場合のGit LFS、MLflow、Weights & Biases Artifacts、Pachydermがあります。DVCは、データのバージョン管理が欲しいデータサイエンティストに向いています。
