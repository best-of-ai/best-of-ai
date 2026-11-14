---
title: 'DeepSeek Harness'
name: 'DeepSeek Harness'
subtitle: 'DeepSeekのモデルでコーディングエージェントを作る、オープンソースでプラグイン中心のフレームワーク'
slug: 'deepseek-harness'
description: 'DeepSeek Harnessは、コーディングエージェント向けのオープンソースのエージェント実行基盤です。モデル、ツール、サンドボックス、オーケストレーションは差し替えられるプラグインで、DeepSeekのモデルとほかの提供元のどちらでも動きます。'
website: 'https://deepseek.com/harness/en/'
company: 'deepseek'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Free'
featured: false
rank: 5
alternatives:
  - claude-code
  - cline
  - continue-dev
  - aider
  - opencode
  - gemini-cli
date: '2026-08-17'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, open_source, autonomous, model_based]
i18n_source: '4473743a4f49'
---

DeepSeek Harnessは、コードを扱うエージェントを動かすためのフレームワークです。モデルが計画を立て、ツールを呼び出し、ファイルを読み書きし、シェルコマンドを実行し、結果を返すまでのループを備えていて、ほかの研究所のターミナル向けエージェントと同じ役割です。特徴は、ほぼすべての部品がプラグインであることです。モデルのアダプター、ツールのレジストリ、セッションのログ、エージェントのループ自体を差し替えられます。

よくある構成のプリセットがあります。ファイルシステムとシェルのツール、ウェブ検索、サブエージェント、計画モードを備えた標準のコーディングエージェントと、独自のプリセットを作るためのモードです。サンドボックスはOS自身の仕組みを使って、エージェントが触れる範囲を制限します。DeepSeekが作ったものですが、ほかの提供元のモデルにもつなげられます。

プロジェクトはMITライセンスのオープンソースで、まだ初期のプレビューです。互換性が壊れる可能性があり、外部からの貢献は今のところ限られる、という注意があります。DeepSeekは、この実行基盤自体の評価は公表していません。代替にはClaude Code、OpenAI Codex、Gemini CLI、OpenCode、Aiderがあります。DeepSeek Harnessは、手を入れて改造できるエージェントの実行基盤が欲しい開発者に向きます。
