---
title: 'Cloudflare Kitesurf'
name: 'Cloudflare Kitesurf'
subtitle: '人ではなくAIエージェント向けに作られたクラウドブラウザ'
slug: 'cloudflare-kitesurf'
description: 'Kitesurfは、人が見るためではなく、AIエージェントが操作するためにCloudflareが作ったブラウザです。Cloudflare Workers上で動き、タブや拡張など、エージェントに不要な通常のブラウザの部分を省いています。'
website: 'https://kitesurf.cloudflare.app/'
company: 'cloudflare'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Free'
featured: false
rank: 5
alternatives:
  - browserbase
  - multion
  - e2b-ai
  - firecrawl
  - openai-operator
date: '2026-08-07'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, free_tier, cloud_based, machine_learning]
i18n_source: '8918f291d1e6'
---

Kitesurfは、ソフトウェアのためのブラウザを作り直しています。自動化ツールの多くは完全なデスクトップブラウザを操作しますが、それは重く、人の利用を前提に作られています。KitesurfはCloudflareのWorkersプラットフォームの中で動くよう書かれた軽いブラウザで、エージェントはChrome一式の負荷なしにページを開き、読み、クリックや入力ができます。

既存のツールとも動きます。Puppeteer、Playwright、Model Context Protocolを使うクライアントは、小さな変更でCloudflareのブラウザサービス経由で接続できます。設計はどのページも信用せず、セッションごとにまっさらな状態から始めるので、エージェントのセキュリティに向きます。Cloudflareは、自社のテストでChromiumよりメモリ使用が少ないとしています。

Kitesurfはベータで、制限があります。動画の再生、WebGL、長くログインしたままのセッション、本物のブラウザのフィンガープリントを確認するサイトには向きません。そうした用途にはCloudflareの標準のブラウザサービスが残ります。代替にはBrowserbase、Browserless、Steel、自分でホストするPlaywrightがあります。Kitesurfは、ウェブを大規模に読み、操作するエージェントを作る開発者に向いています。
