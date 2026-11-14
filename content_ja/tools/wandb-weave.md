---
title: 'W&B Weave'
name: 'W&B Weave'
subtitle: 'Weights & BiasesのLLM評価・オブザーバビリティ'
slug: 'wandb-weave'
description: 'WeaveはWeights & BiasesのLLMアプリ開発用ツールキットです。モデル呼び出しをすべてトレースし、データセットを使った評価を実行し、本番のアプリを監視します。PythonとTypeScriptに対応しています。'
website: 'https://weave.wandb.ai'
company: 'weights-biases'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Freemium'
featured: false
rank: 7
alternatives:
  - langsmith
  - langfuse
  - braintrust
  - arize
  - helicone
  - mlflow
  - comet-ml
date: '2025-09-21'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration, integrations, model_based]
i18n_source: '749108f2e1fc'
---

Weaveが扱うのは、LLMアプリでよくある「中で何が起きているのかわからない」という問題です。数行のコードを足すだけで、呼び出しごとに入力、出力、レイテンシ、コスト、前後の関数呼び出しが記録されます。開発者は失敗した応答を推測に頼らず、一歩ずつ調べられます。トレースは入れ子の呼び出しにも及ぶので、複数のモデルやツールをつなぐエージェントで役に立ちます。

評価も扱えます。チームはテストケースのデータセットを作り、スコアラー（LLMによる判定も含む）を定義し、実験を回して、出荷前にプロンプト、モデル、アプリのバージョンを比べます。結果は時系列で追えるので、変更が本当に効いたのか判断しやすくなります。オンライン評価では実際のトラフィックを採点し、本番での性能低下を知らせます。

WeaveはWeights & Biasesの一部で、現在はCoreWeaveが所有しています。学習実験を扱うW&Bのプラットフォームとも連携します。個人向けの無料枠とチーム向けの有料プランがあり、企業向けにはセルフホストも選べます。代替にはLangSmith、Langfuse、Arize Phoenix、Braintrust、Heliconeがあります。WeaveはすでにW&Bを使っている開発者や、トレースと評価を一か所にまとめたい開発者に向いています。
