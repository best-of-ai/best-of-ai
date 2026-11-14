---
title: 'LangGraph'
name: 'LangGraph'
subtitle: '状態を持つ長時間稼働のエージェント向けのグラフベースのフレームワーク'
slug: 'langgraph'
description: 'LangGraphは、LangChainチームによるオープンソースのフレームワークで、状態を持つエージェントをステップのグラフとして作ります。分岐、ループ、永続的なメモリ、人の承認ステップ、ストリーミングに対応し、デプロイと監視ではLangSmithと組み合わせます。'
website: 'https://www.langchain.com/langgraph'
logo_url: ''
category: 'ai-agents'
category_name: 'AIエージェント'
price: 'Free'
featured: false
rank: 8
alternatives:
  - langchain
  - crewai
  - autogen-ai
  - llamaindex
  - smolagents
  - mastra
date: '2026-11-05'
tags: [ai_agent, automation, autonomous, ai_assistants, agents, multi_agent, task_automation, orchestration, agentic, collaboration, model_based]
i18n_source: '50181c5f4cd8'
---

LangGraphは、エージェントをグラフとしてモデル化します。各ノードは、モデルの呼び出し、ツールの実行、条件の確認といった1つのステップで、エッジがループや分岐を含むステップ間の流れを定義します。共有の状態オブジェクトが情報を受け渡します。この明示的な構造により、開発者はエージェントが何をいつ行うかを制御でき、自由に回り続けるループよりも複雑なエージェントを把握しやすくなります。

本番での利用を意識した機能が特徴です。チェックポイントが状態を保存するので、実行を一時停止して再開したり、失敗から復旧したりできます。人が関わるステップで、エージェントは操作の前に承認を待て、タイムトラベルデバッグで、開発者は以前のステップを再生・編集できます。途中結果のストリーミング、長期のメモリ、マルチエージェント設計にも、PythonとJavaScriptで対応します。

ライブラリは無料のオープンソースです。ホスティングと監視はLangSmithで利用でき、無料枠と有料プランがあります。LangGraphは高水準のエージェントライブラリより学習の負担が大きく、その力が最も活きるのは複雑なワークフローです。CrewAIとAutoGenはより高水準のマルチエージェントの抽象化を提供し、OpenAI Agents SDKはOpenAI中心の作業ではよりシンプルで、n8nやDifyのようなビジュアルのビルダーはコードを書かない人に向いています。多くの本番のエージェントがLangGraphで作られています。
