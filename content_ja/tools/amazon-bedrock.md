---
title: 'Amazon Bedrock'
name: 'Amazon Bedrock'
subtitle: 'API経由で基盤モデルを使う、AWSのマネージドサービス'
slug: 'amazon-bedrock'
description: 'Amazon Bedrockは、生成AIのアプリケーションを作るためのAWSのマネージドサービスです。一つのAPIで多くの提供者の基盤モデルを使え、検索、エージェント、ガードレール、評価の機能があります。'
website: 'https://aws.amazon.com/bedrock'
company: 'amazon'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Freemium'
featured: false
rank: 9
alternatives:
  - azure-openai
  - vertex-ai
  - together-ai
  - fireworks-ai
  - openrouter
  - groq
date: '2025-09-21'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, api_available, enterprise, secure]
i18n_source: '03ddec47ee00'
---

Bedrockは、AWSを使う多くの企業が、モデルのインフラを自分で動かさずに大規模言語モデルを使う方法です。各AIラボと別々に契約する代わりに、Anthropic、Meta、Mistral、Amazon自身などの提供者のモデル一覧から選び、一つのAPIで呼び出します。データは自分のAWSアカウントの中に留まるので、セキュリティ、プライバシー、コンプライアンスの要件があるチームにとって重要で、すでに使っているIAM、ネットワーク、ログのツールと一緒に動きます。

モデルの周りには、実際のアプリケーションを作るのに必要な部品があります。Knowledge Basesは、検索で補強した回答のために、モデルを自分の文書へつなぎます。Agentsは、モデルが計画を立ててAPIを呼び、作業を終えられるようにし、AgentCoreはどのフレームワークで作ったエージェントでも動かすためのインフラです。Guardrailsは望まない話題や機微なデータを止め、回答が事実に基づいているかを確認できます。モデル同士を評価し、ファインチューンし、プロンプトをキャッシュして費用を下げる機能もあります。

Bedrockの課金は使用量で、オンデマンドでは通常トークン単位です。負荷が安定しているときは、バッチ処理と予約した容量も選べます。扱えるモデルの範囲と、新しいモデルが現れる速さは、各提供者自身のAPIとは違うので、モデルがラボのサイトより遅れてBedrockに載ることがあります。競合はAzure AI Foundryと、Google CloudのVertex AIです。すでにAWSに寄せているチームは、便利さと請求の一本化からBedrockを選ぶことが多いです。
