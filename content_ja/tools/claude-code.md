---
title: 'Claude Code'
name: 'Claude Code'
subtitle: 'ターミナルで直接動く、Anthropicのエージェント型コーディングツール'
slug: 'claude-code'
description: 'Claude CodeはAnthropicのコーディングエージェントです。リポジトリを読み、ファイルを編集し、コマンドを実行して、ターミナルでタスクを進めます。IDE、デスクトップ、Webでも使えます。'
website: 'https://claude.ai/code'
company: 'anthropic'
logo_url: ''
category: 'code-assistant'
category_name: 'コードアシスタント'
price: 'Freemium'
featured: false
rank: 8
alternatives:
  - codex
  - cursor
  - gemini-cli
  - github-copilot
  - aider
  - cline
  - opencode
  - windsurf
date: '2025-09-21'
tags: [code_generation, developer_tools, productivity, coding, programming, autocomplete, debugging, refactoring, ide, extensible]
i18n_source: '012aa47ad99b'
---

Claude Codeは、エディタの中で候補を出す仕組みではなく、実際のプロジェクトの上で動くエージェントです。ターミナルからリポジトリの中で起動し、失敗しているテストの修正、エンドポイントの追加、依存関係の更新といったタスクを説明します。関係するファイルを読み、計画を立て、プロジェクト全体にわたってコードを編集し、テストやほかのコマンドを実行し、エラーを見ながらやり直します。リスクがあり得る操作は許可を求め、コミットの前に、差分として、またはgitを通して変更を確認できます。

カスタマイズの幅は広いです。プロジェクト内のCLAUDE.mdには、エージェントが毎回従う指示と規約を置き、スキルは繰り返せる手順をまとめます。フックはワークフローの途中で自前のスクリプトを実行し、サブエージェントは作業を並列のコンテキストに分け、Model Context Protocolはデータベース、issueトラッカー、ほかのツールへつなぎます。VS CodeやJetBrainsのようなエディタ、デスクトップアプリ、ブラウザでも動き、スクリプトとCIから、自動化されたタスクとして実行することもできます。

Claude Codeは有料のClaudeプランに含まれ、利用量で課金されるAPIキーでも使えます。費用は、どれだけ動かすかによります。長く自律で動くセッションは、トークンを多く消費することがあります。出力は、とくにセキュリティに関わるコードでは、まだ確認が必要です。主な代替は、OpenAIのCodex、GoogleのGemini CLI、Cursor、GitHub Copilotのエージェント、Clineです。
