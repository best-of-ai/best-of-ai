---
title: 'skills'
name: 'skills'
slug: 'builderio-skills'
subtitle: 'エージェントの作業監視、レビュー、リリース向けに組み合わせられるBuilder.ioの小型スキル'
description: 'Builder.ioのスキルはエージェントの監督を重視しています。別のエージェントのセッションを監視する、チェックとレビューを通じてプルリクエストを見守る、レビュー待ちの作業を処理する、または人の判断が必要な作業をダイジェストで送るスキルがあります。「factory」系スキルは実験的とされています。リポジトリには約26件のスキルがあります。'
author: 'BuilderIO'
skill_type: 'Workflow & Productivity'
source_url: 'https://github.com/BuilderIO/skills'
compatible_with: ['Claude Code', 'Codex']
install: 'Run npx @agent-native/skills@latest add to pick from the recommended skills.'
price: 'Free'
open_source: true
license: 'MIT'
stars: 4651
stars_this_week: 0
stars_updated: '2026-11-08'
rank: 5
date: '2026-11-08'
tags: [workflow, pull-requests, orchestration, code-review]
i18n_source: '0bfb058224a8'
---
このリポジトリには次のスキルが含まれます。

- **agent-watchdog**：セッションIDを指定し、別のエージェントの作業を監視、監査、修正します。
- **efficient-orchestrator**：明示的に呼び出された場合に限り、調整役のエージェントを使って大きなタスクを実行します。
- **factory-collect**：フィードバック、テレメトリ、エラー、Issueを収集してトリアージします。
- **factory-babysit-pr**：承認済みのプルリクエスト1件について、チェックとレビューを追跡します。
- **factory-review-prs**：返信、承認、マージの基準を分けて、プルリクエストのキューをレビューします。
- **factory-human-digest**：設定済みのリポジトリについて、人の判断が必要な作業を要約します。
