---
title: 'Herdr'
name: 'Herdr'
subtitle: 'コーディングエージェントをバックグラウンドで動かし続けるオープンソースのデスクトップアプリ'
slug: 'herdr'
description: 'Herdrは、ターミナルと、Claude CodeやCodexのようなコーディングエージェントを一か所で動かす、オープンソースのネイティブなデスクトップアプリです。herdr-coreというランタイムの上で動くので、アプリを閉じたり更新したりしてもセッションは動き続けます。'
website: 'https://herdr.dev/'
company: 'herdr'
logo_url: ''
category: 'devtools'
category_name: '開発者向け'
price: 'Free'
featured: false
rank: 5
alternatives:
  - warp
  - claude-code
  - cursor
  - cline
date: '2026-10-29'
tags: [developer_tools, terminal, coding_agents, open_source, desktop_app, multiplexer, agent_management, productivity, cross_platform, automation]
i18n_source: '3491a22de0f6'
---

Herdrは、開発者が増やしていくエージェントのセッションをまとめます。たくさんのターミナルウィンドウの代わりに、タブの画面でエージェントを並べ、エージェントが状態を報告するときは、作業中か、終わったか、入力待ちかを示します。ターミナルで動くエージェントならどれでも使えます。

設計の要点はherdr-coreというランタイムで、セッションを動かす、手元のマシン上の小さなサーバーです。アプリはフロントエンドにすぎないので、終了したり更新したりしてもエージェントは止まりません。もともとのターミナル版のHerdrは、独自のサーバーを持つ別のプログラムとして今もあります。

HerdrはApache 2.0ライセンスの無料のオープンソースで、macOS、Linux、Windowsで動きます。デスクトップアプリは新しいので、変更は見込まれます。マシンが再起動するかコアが止まると、動いているプログラムは終了します。代替にはtmux、Zellij、Warp、Conductor、エージェントツールに組み込まれたターミナルマルチプレクサがあります。Herdrは、コーディングエージェントを同時にたくさん動かす開発者に向いています。
