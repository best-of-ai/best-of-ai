---
title: 'Amazon Bedrock AgentCore'
name: 'Amazon Bedrock AgentCore'
subtitle: '本番のAIエージェントを作り、デプロイし、動かすAWSの基盤'
slug: 'amazon-bedrock-agentcore'
description: 'Amazon Bedrock AgentCoreは、本番でAIエージェントを作り、動かすためのAWSの基盤です。管理されたランタイム、アイデンティティ、メモリ、ゲートウェイのツール、ポリシー制御を備え、どのフレームワークやモデルで作ったエージェントでも使えます。'
website: 'https://aws.amazon.com/bedrock/agentcore/'
company: 'amazon'
logo_url: ''
category: 'ai-agents'
category_name: 'AIエージェント'
price: 'Paid'
featured: false
rank: 7
alternatives:
  - azure-ai-foundry
  - vertex-ai
  - databricks-agent-bricks
  - salesforce-agentforce
date: '2026-11-05'
tags: [ai, assistant, automation, productivity, enterprise, agent]
i18n_source: '27c7992a821e'
---

AgentCoreが担うのは、エージェントを試作から本番へ持っていくときのインフラの作業です。ランタイムはセッションを隔離して各ユーザーの作業を分けたままエージェントをホストし、スケーリングも扱います。アイデンティティの機能では、エージェントがユーザーに代わって他のサービスへ認証できます。ゲートウェイは既存のAPIやサービスを、エージェントが呼び出せるツールに変え、観測の機能はエージェントが何をしたかを追跡します。開発者はLangGraph、CrewAI、Strands Agents SDKなどのフレームワークと、Bedrock上のモデルや他の提供者のモデルと組み合わせて使えます。

メモリは主要な構成要素です。AgentCoreはセッション内の短期の文脈と、セッションをまたぐ長期の記憶を保存し、以前のやりとりをエージェントが思い出せるエピソード記憶も含みます。現在プレビューのポリシー機能では、チームがエージェントに許す範囲を定められます。コードインタープリタとブラウザのツールは、安全なサンドボックスの中でコードを実行し、ウェブを使う手段をエージェントに与えます。

AgentCoreの料金は各コンポーネントの使用量に基づき、事前の契約はありません。すでにAWS上で開発していて、エージェント向けの管理されたインフラが欲しいチームが対象です。代替にはAzure AI Foundryのエージェントサービス、GoogleのVertex AI Agent Engine、Kubernetes上に組んだオープンソースまたは自前で運用する構成があります。どれが合うかは、その企業がすでに使っているクラウドによることが多いです。土台になるモデルサービスについては、Amazon Bedrockの項目を参照します。
