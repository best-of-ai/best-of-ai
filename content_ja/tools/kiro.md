---
title: 'Kiro'
name: 'Kiro'
subtitle: '仕様を起点にするAWSのエージェント型IDE'
slug: 'kiro'
description: 'KiroはAWSのエージェント型IDEで、チャットのプロンプトではなく、書いた仕様を作業の単位にします。エージェントが機能を計画し、要件と設計を書き、実装、テスト、文書化まで行います。'
website: 'https://kiro.dev'
company: 'amazon'
logo_url: ''
category: 'code-assistant'
category_name: 'コードアシスタント'
price: 'Freemium'
featured: false
rank: 5
alternatives:
  - cursor
  - windsurf
  - claude-code
  - codex
  - google-antigravity
  - github-copilot
  - myspec-ai
date: '2026-07-29'
tags: [code_generation, developer_tools, productivity, coding, programming, autocomplete, debugging, refactoring, ide, extensible]
i18n_source: '85f0afaed192'
---

Kiroは仕様駆動の開発を中心に作られています。開発者が機能を説明すると、Kiroは要件文書、技術設計、タスク一覧を作ります。開発者がそれらを確認して直し、そのあとエージェントがタスクを進め、コードとテストを書きます。狙いは、大きな作業ではエージェントを意図に沿わせ、チャットからその場で進めるのではないようにすることです。

エディタはCode OSSを土台にしているので、VS Codeの拡張機能と設定を引き継げます。フックはファイルの保存などの出来事でエージェントの動作を起動し、steering filesはプロジェクトについての指針を残しておき、Model Context Protocolへの対応で外部ツールをつなぎます。ClaudeのモデルをAWS経由で使います。

Kiroには無料枠と、利用量に応じた有料プランがあります。仕様は構造を足す一方で手間も増え、小さな修正より大きな機能に向きます。代替にはCursor、Claude Code、Windsurf、GitHub Copilot、GitHub Spec Kitがあります。Kiroは、エージェントに計画の規律を持たせたい開発者に向いています。
