---
title: 'Kalanos Grader'
name: 'Kalanos Grader'
subtitle: 'ロボットの学習用録画データを調べるオープンソースの品質監査ツール'
slug: 'kalanos-grader'
description: 'Kalanos Graderは、ロボットやフィジカルAIの学習用録画をローカルで監査する、無料のApache-2.0ライセンスのコマンドラインツールです。タイミング、動き、整合性、ビジョン、アノテーションの問題をスコア化し、HTMLまたはJSONのレポートを出力します。'
website: 'https://kalanos.ai/grader'
logo_url: ''
category: 'robotics'
category_name: 'ロボティクス'
price: 'Free'
featured: false
rank: 5
alternatives:
  - foxglove
  - cleanlab
  - formant
date: '2026-11-24'
tags: [robotics, data_quality, dataset_audit, imitation_learning, physical_ai, open_source, cli, python, lerobot, free_tier]
i18n_source: 'cadc52e004d3'
---

Kalanos Graderは、ロボットの録画エピソードを学習に使う前にチェックします。pipでインストールし、`kalanos grade ./my_recordings --report audit.html`を実行します。タイミング、信号、動きの問題を探し、確認が必要なエピソードとその理由を示し、結果をHTMLレポートまたはJSONで書き出します。アカウントは不要で、ローカルでの監査は自分のマシン上で動きます。

各録画には、整合性、タイミング、動き、ビジョン、アノテーションの5つの項目について0から100のスコアが付きます。デフォルトの重みは、整合性が3、タイミング、動き、ビジョンがそれぞれ2、アノテーションが1です。スコアは評価した範囲での品質を表します。Kalanosは、これは合格率ではなく、学習後のモデルの挙動の予測でもないと説明しています。ページには、ALOHAの50エピソードを監査したサンプルが載っていて、39件が合格、11件が要確認でした。

Python 3.10以降が必要です。LeRobot v2.0、v2.1、v3.0のデータセットと、CSV、JSON、JSONLファイルは基本パッケージで使えます。HDF5とMCAPまたはROS 2の録画には追加パッケージが必要で、カメラのチェックにはvideo追加パッケージが必要です。任意のHDF5レイアウトはマッピングできない場合があります。1,000エピソードのフルレポートは、Kalanos自身の実行で約52分かかりました。Kalanosは、これはベンチマークではないとしています。模倣学習に取り組むチームが、データセットの品質をすばやく確認したい場合に向いています。
