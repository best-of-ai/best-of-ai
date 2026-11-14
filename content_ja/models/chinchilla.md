---
title: 'Chinchilla'
name: 'Chinchilla'
slug: 'chinchilla'
subtitle: 'LLM学習のスケーリング則の前提を覆した、DeepMindの2022年の研究モデル'
description: 'LLM学習のスケーリング則の前提を覆した、DeepMindの2022年の研究モデル'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/'
price: 'Paid'
rank: 4
release_date: '2022-03-29'
param_count: '70B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 67.5
access_methods: [Self-hosted]
runs_at_home: false
platforms: []
date: '2026-07-16'
tags: [llm, research, legacy]
i18n_source: '14414c05c298'
---

Chinchillaは、DeepMindが2022年3月の計算最適な学習に関する論文で発表した研究用の言語モデルです。700億パラメータで、DeepMindが以前に出した2800億パラメータのGopherよりずっと小さい一方、約4倍のデータで学習されています。そして幅広いベンチマークで、Gopher、GPT-3、当時のより大きなモデルを上回りました。MMLUの平均スコアは約67.5%です。論文の中心的な発見は、それまでの大規模言語モデルの多くが、サイズに対して学習不足だったということです。計算予算が決まっているなら、モデルサイズだけを大きくするのではなく、モデルサイズと学習データを一緒に増やすべきだという主張です。

この結果は現在Chinchillaのスケーリング則として広く知られ、その後の各研究所の学習計画を変えました。パラメータ数をただ増やすより、小さなモデルをはるかに大きなデータセットで学習する方向に、分野全体が動いたのです。DeepMindはChinchillaの重みを公開しておらず、一般向けのアクセスも提供していません。論文に記された研究成果としてのみ存在します。その影響は、LLaMAからGPT-4まで、以降に学習された主要モデルのほぼすべてに間接的に現れており、どれも学習方法の一部として計算最適なスケーリングを挙げています。
