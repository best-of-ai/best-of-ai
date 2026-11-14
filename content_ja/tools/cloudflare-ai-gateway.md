---
title: 'Cloudflare AI Gateway'
name: 'Cloudflare AI Gateway'
subtitle: 'AIアプリの観測、制御、複数プロバイダへのルーティング'
slug: 'cloudflare-ai-gateway'
description: 'Cloudflare AI Gatewayは、アプリとAIモデルのプロバイダの間に入ります。分析、ログ、キャッシュ、レート制限、再試行、モデルのフォールバックを備え、開発者が利用状況を見て費用を抑えられます。'
website: 'https://developers.cloudflare.com/ai-gateway/'
company: 'cloudflare'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Freemium'
featured: false
rank: 5
alternatives:
  - portkey
  - litellm
  - helicone
  - langfuse
  - openrouter
  - vercel-ai-platform
  - eden-ai
date: '2026-07-17'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, cloud_based, analytics, model_based]
i18n_source: '76831d31774b'
---

AI Gatewayは、言語モデルへの呼び出しのプロキシです。開発者はアプリのリクエストをプロバイダではなくCloudflareのURLへ向け、ゲートウェイは内容を記録しながら転送します。これでOpenAI、Anthropic、Googleなどのプロバイダをまたいだリクエスト、トークン、費用、エラーのダッシュボードが得られます。

制御の機能も足しています。キャッシュは同じリクエストに保存した回答を返し、費用と時間を節約します。レート制限は予算を守り、再試行とフォールバックは一つのモデルが失敗したときに別のモデルへ切り替えます。ログはプロンプトのデバッグに役立ち、ガードレールと鍵の管理はセキュリティを支えます。

中核の機能はCloudflareのプランで使え、多くは無料ですが、ログの保存には制限があります。複数のモデルを呼ぶ本番のアプリに向きます。代替にはPortkey、LiteLLM、Helicone、OpenRouter、Kong AI Gatewayがあります。Cloudflare AI Gatewayは、モデルへの通信を把握し、制御したい開発者に向いています。
