---
title: 'BabyAGI'
name: 'BabyAGI'
subtitle: 'タスク駆動の、最小構成のオープンソース自律エージェント'
slug: 'babyagi'
description: 'BabyAGIは、Yohei Nakajimaによる小さなオープンソースのPythonプロジェクトです。LLMが目標に向けてタスクを作り、優先順位を付け、実行できることを示し、その後の多くの自律エージェントのフレームワークに影響しました。'
website: 'https://github.com/yoheinakajima/babyagi'
logo_url: ''
category: 'ai-agents'
category_name: 'AIエージェント'
price: 'Free'
featured: false
rank: 6
alternatives:
  - autogpt
  - agentgpt
  - superagi
  - crewai
  - manus
date: '2026-11-05'
tags: [ai_agent, automation, autonomous, ai_assistants, agents, multi_agent, task_automation, orchestration, agentic, model_based]
i18n_source: '0dec64a691c0'
---

BabyAGIは、自律エージェントの実験が広がった早い時期に出ました。最初のスクリプトは数十行だけでした。目標を渡すと、言語モデルがタスクの一覧を作り、最初のタスクを実行し、結果をベクトルデータベースに保存し、学んだことに基づいて新しいタスクを作り、優先順位を付け直します。その単純なループは広くコピーされ、手を加えられました。

このプロジェクトが意味を持ったのは、AIエージェントという考えを理解しやすく、試しやすくしたからです。多くの後継と、自律システムに何ができるかという議論を生み、開発者はその限界から学びました。たとえばループ、目的からのずれ、コストです。後の版は、関数をデータベースに置いて自己改善するエージェントを作るフレームワークへ作り直されました。

BabyAGIは無料のオープンソースで、一般の利用者ではなく、開発者と学ぶ人向けです。本番用のツールというより、参照する設計として見るのがよいです。実際の作業では、LangGraph、CrewAI、AutoGen、あるいはOpenAIとAnthropicのエージェントSDKのようなフレームワークを使うことが多いです。BabyAGIは、単純なエージェントのループがどう動くかを調べたい人に向いています。
