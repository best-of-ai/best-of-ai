---
title: 'Temporal'
name: 'Temporal'
slug: 'temporal'
subtitle: '長時間のワークフローを支える耐久実行プラットフォーム'
description: 'Temporalはオープンソースのプラットフォームで、ワークフローをコードとして耐久実行できます。サーバーが落ちても状態を保つので、長時間のジョブは途中から再開します。決済、オンボーディング、データパイプライン、AIエージェントなどに使われています。'
website: 'https://temporal.io'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Freemium'
featured: false
rank: 7
alternatives:
  - inngest
  - trigger-dev
  - prefect
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration]
i18n_source: 'db4f201d9543'
---

Temporalが扱うのは、信頼できるソフトウェアを作るうえで難しい部分、つまり長く続く複数ステップの処理を障害から守ることです。開発者はGo、Java、Python、TypeScriptなどふつうのプログラミング言語でワークフローを書きます。Temporalが各ステップとその状態を記録するので、サーバーが落ちたりネットワーク呼び出しが失敗したりしても、ワークフローは止まった場所から進み、それまでの進捗は失われません。リトライ、タイムアウト、タイマーは組み込みです。

そのため、数分から数か月かかる処理に向いています。決済フロー、注文処理、顧客のオンボーディング、インフラのプロビジョニング、データ処理などです。最近は、AIエージェントのオーケストレーションに使うチームも増えています。タスクがモデルやツールを長時間呼び出し、信頼性と可観測性が必要になるためです。Temporal Cloudはマネージドサービスで、オープンソースのサーバーは自前でホストできます。

TemporalはMITライセンスの無料のオープンソースで、Temporal Cloudは使用量に応じた料金です。考え方に慣れるまで時間がかかり、サービスは自分で運用するか、料金を払って使う必要があります。代替にはAWS Step Functions、データワークフロー向けのApache Airflow、Inngest、Restate、Camunda、Celeryのようなキューがあります。重要で長く続く処理を作るエンジニアリングチームに向いています。
