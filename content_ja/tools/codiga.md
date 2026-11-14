---
title: 'Codiga'
name: 'Codiga'
subtitle: 'AIによるコード解析と、安全なコーディングのアシスタント'
slug: 'codiga'
description: 'Codigaは、静的コード解析とコーディング支援の企業でした。Datadogが買収し、単体のIDEプラグインとサービスを終了して、その技術をDatadog Code Securityに取り込みました。'
website: 'https://codiga.io'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Freemium'
featured: false
rank: 7
dead: true
dead_reason: 'DatadogはCodigaを買収して単体の製品を終了しました。技術はDatadog Code Securityの中で続いています。'
dead_date: '2023-05-04'
alternatives:
  - sonarqube
  - codacy
  - snyk-ai
  - semgrep-ai
date: '2025-09-21'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, real_time, collaboration, secure]
i18n_source: '2ebc87322bd1'
---

Codigaは、エディタの中でリアルタイムのコード解析を出していました。VS Code、JetBrainsのIDE、その他のツール向けプラグインが、入力しながらセキュリティの脆弱性、バグ、コーディング規約への違反を調べ、ルールエンジンでチームは独自のチェックを書けました。コードスニペットのアシスタントと、後にはAIによる提案もあり、Gitのプラットフォームと連携してpull requestを自動でレビューしていました。

同社はDatadogに買収されました。Datadogは、コード解析を自社のオブザーバビリティとセキュリティのプラットフォームに入れたいと考えていました。Codigaの単体製品はその後まもなく終了し、有料の利用者には返金があり、チームはDatadogに加わりました。静的解析のエンジンとそのルールは今、Datadog Code Securityの土台になっており、アナライザーはオープンソースとして公開されています。

似たツールでは、SonarQube、Semgrep、Snyk Code、CodeQLが静的解析を行い、CodeRabbitやQodoのようなAIレビューのツールがpull requestを扱います。Datadogを使っているチームは、組み込みのコードセキュリティ機能を使えます。古いツール一覧やチュートリアルが今もCodigaに触れているので、この項目は参照用に残しています。
