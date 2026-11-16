---
title: 'Kimi Code'
name: 'Kimi Code'
subtitle: 'Moonshot AIの、Kimi K3モデルを搭載したコーディングエージェント'
slug: 'kimi-code'
description: 'Kimi Codeは、Moonshot AIが公開しているターミナル向けのオープンソースのコーディングエージェントです。コードの読み取りと編集、シェルコマンドの実行、ファイル検索を行い、サブエージェント、MCPツール、Agent Client Protocol経由のエディター連携に対応しています。'
website: 'https://kimi.ai'
company: 'moonshot-ai'
logo_url: ''
category: 'code-assistant'
category_name: 'コードアシスタント'
price: 'Freemium'
featured: false
rank: 6
alternatives:
  - claude-code
  - codex
  - gemini-cli
  - opencode
  - aider
  - cursor
date: '2026-10-23'
tags: [code_generation, developer_tools, coding, programming, debugging, refactoring, terminal, cli, agentic, open_source]
i18n_source: '0182f68425f5'
---

Kimi Codeは、Claude CodeやCodex CLIと同じ系統のコマンドラインエージェントです。プロジェクトのフォルダで起動してタスクを伝えると、ファイルを読み、コードを編集し、コマンドを実行して結果を確認し、その結果をもとに次にすることを判断します。権限設定により、危険な操作は承認制にできます。

既定ではMoonshot AIのKimiモデルを使います。Kimiモデルはコーディングと長いコンテキストに強いことで知られており、ほかの互換プロバイダーにも接続できます。機能には、コーディング、探索、計画のための組み込みサブエージェント、ツールをつなぐModel Context Protocolへの対応、自動化や安全確認のためのライフサイクルフック、ZedやJetBrainsなどのエディターから操作できるACPモードがあります。

このツールはMITライセンスのオープンソースです。モデルの利用にはアカウントかAPIキーが必要で、プランには上限があります。同じ名前の非公式プロジェクトがいくつかあるため、Moonshot AIの公式リポジトリを使ってください。代替には、Claude Code、OpenAI Codex CLI、Gemini CLI、OpenCode、Aiderがあります。Kimi Codeは、Kimiモデルを中心にしたターミナルエージェントを求める開発者に向いています。
